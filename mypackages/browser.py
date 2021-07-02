from platform import version
from PySide2.QtCore import QSettings
import debugpy
debugpy.debug_this_thread()
from configparser import Error
from loguru import logger
import pandas as pd
from os import stat
from playwright.sync_api import sync_playwright
from playwright._impl._api_types import Error, TimeoutError
from bs4 import BeautifulSoup
import time
import datetime
import re
import json
import os
from os import path
from random import uniform
import sys
from PySide2.QtWidgets import *
from PySide2.QtSql import *
from pathlib import Path
import inspect
from main import logQueryError, load_config, calculate_role_rating
from mypackages.two_factor_auth import Ui_DialogTwoFactorAuth
import mypackages.config as myconfig


storage_state = ""

def get_file_dirname() -> Path:
    """Returns the callee (`__file__`) directory name"""
    module_name = inspect.currentframe().f_back.f_globals["__name__"]
    module = sys.modules[module_name]
    assert module
    return Path(module.__file__).parent.absolute()


def openDB(database):
    if not database.open():
        QMessageBox.critical(
            None,
            "GD Recruiting App - Error!",
            "Database Error: %s" % database.lastError().databaseText()
            )
        logger.error(f"{datetime.datetime.now()}: Failed to open {database.databaseName()} using connection {database.connectionName()}")
        sys.exit(1)
    else:
        logger.info(f"Opened database {database.databaseName()} using connection {database.connectionName()}")


def parse_considering(content):
    considering = ""
    for each in content:
        each_td_tags = each.find_all("td")
        schoolid = int(each_td_tags[0].text)
        school_short = myconfig.wis_gd_df.school_short[schoolid]
        coachid = "coach?"
        school_division = myconfig.wis_gd_df.division[schoolid]
        miles_span = each_td_tags[2].find("span", class_="considering-miles")
        miles = round(float(miles_span.text))
        total_scholarships = each_td_tags[5].text
        open_scholarships = each_td_tags[6].text                
        considering += f"{school_short} ({coachid}) {school_division} {miles}mi {total_scholarships} | {open_scholarships}\n"
    considering = considering[:-1]
    return considering


def potential_mapping(p):
    mapping = {'?': '?', 'VL': '4-VL', 'L': '3-L', 'A': '2-A', 'H':'1-H', 'VH': '0-VH'}
    return mapping[p]


def update_considering(page_content, d, q, progress):
    recruitIDs = []
    recruitpage_soup = BeautifulSoup(page_content, "lxml")
    table_tbody = recruitpage_soup.find("tbody", class_="advanced-recruit-body")
    recruitRows = table_tbody.find_all("tr", class_="recruit", recursive=False)
    progress.emit(1000, myconfig.rids_unsigned_length)
    i = 0
    signed_state = {'Not Signed': 0, 'Signed': 1}
    for each in recruitRows:
        if int(each['recruitid']) in myconfig.rids_unsigned:
            td_tags = each.find_all("td")
        
            considering = ""
            recruit = {
                'id': int(td_tags[0].text),
                'signed': signed_state[td_tags[14].text],
            }
            if td_tags[42].text == "":
                recruit['considering'] = "undecided"
            else:
                consideringRows = td_tags[42].find_all("tr")
                recruit['considering'] = parse_considering(consideringRows)
            recruitIDs.append(recruit)
            i += 1
        
            bindUpdateQuery(q, recruit)
        
            progress.emit(1000 + i, myconfig.rids_unsigned_length)

    return recruitIDs

def get_recruitIDs(page_content, d, q, progress):
    recruitIDs = []
    recruitpage_soup = BeautifulSoup(page_content, "lxml")
    table_tbody = recruitpage_soup.find("tbody", class_="advanced-recruit-body")
    recruitRows = table_tbody.find_all("tr", class_="recruit", recursive=False)
    signed_state = {'Not Signed': 0, 'Signed': 1}
    logger.info("Scraping recruit info from Recruiting Search page...")
    i = 0
    recruitRows_length = len(recruitRows)
    progress.emit(100,1)
    progress.emit(110,1)
    progress.emit(200,1)
    progress.emit(210,1)
    progress.emit(1000, recruitRows_length)
    for each in recruitRows:
        td_tags = each.find_all("td")
        
        considering = ""
        if td_tags[9].text == "0":
            rank = 999
        else:
            rank = int(td_tags[9].text)
        recruit = {
            'id': int(td_tags[0].text),
            'watched': int(td_tags[1].text),
            'priority': int(td_tags[2].text),
            'name': td_tags[3].text,
            'pos': td_tags[4].text,
            'height': td_tags[6].text,
            'weight': int(td_tags[7].text),
            'rating': int(td_tags[8].text),
            'rank': rank,
            'hometown': td_tags[10].text,
            'division': td_tags[12].text,
            'miles': round(float(td_tags[13].text), None),
            'signed': signed_state[td_tags[14].text],
            'gpa': float(td_tags[15].text),
            'potential': potential_mapping(td_tags[16].text),
            'ath': int(td_tags[17].text),
            'spd': int(td_tags[18].text),
            'dur': int(td_tags[19].text),
            'we': int(td_tags[20].text),
            'sta': int(td_tags[21].text),
            'str': int(td_tags[22].text),
            'blk': int(td_tags[23].text),
            'tkl': int(td_tags[24].text),
            'han': int(td_tags[25].text),
            'gi': int(td_tags[26].text),
            'elu': int(td_tags[27].text),
            'tec': int(td_tags[28].text),
            '3_4': int(td_tags[29].text),
            '4_3': int(td_tags[30].text),
            '4_4': int(td_tags[31].text),
            '5_2': int(td_tags[32].text),
            'Nickel': int(td_tags[33].text),
            'Dime': int(td_tags[34].text),
            'IForm': int(td_tags[35].text),
            'NDB': int(td_tags[36].text),
            'Pro': int(td_tags[37].text),
            'Shot': int(td_tags[38].text),
            'Trips': int(td_tags[39].text),
            'WB': int(td_tags[40].text),
            'ST': int(td_tags[41].text)
        }
        role_ratings = calculate_role_rating(recruit)
        recruit['r1'] = float(role_ratings['r1'])
        recruit['r2'] = float(role_ratings['r2'])
        recruit['r3'] = float(role_ratings['r3'])
        recruit['r4'] = float(role_ratings['r4'])
        recruit['r5'] = float(role_ratings['r5'])
        recruit['r6'] = float(role_ratings['r6'])
        if td_tags[42].text == "":
            recruit['considering'] = "undecided"
        else:
            consideringRows = td_tags[42].find_all("tr")
            recruit['considering'] = parse_considering(consideringRows)
        recruitIDs.append(recruit)            
        bindRecruitQuery(q, recruit, 0)
        i += 1
        progress.emit(1000 + i, recruitRows_length)

    myconfig.rids_all_length = len(recruitIDs)
    logger.info(f"Number of recruits added to database = {myconfig.rids_all_length}")
    return recruitIDs


def randsleep():
    s = uniform(0.1, 0.5)
    return s


def check_for_stored_cookies(coachid):
    global storage_state
    file = os.path.join(myconfig.cookies_directory_path, f"browser_cookie_{coachid}.json")
    if path.exists(file):
        logger.info(f"{file} file path found.")
        try:
            with open(file, "r") as read_file:
                storage_state = json.load(read_file)
        except Exception as e:
            logger.error(f"Exception ({e}) reading {file} file.")
    else:
        logger.info(f"{file} file path NOT found.")

    if storage_state == "":
        logger.info("storage_state is empty")
    else:
        logger.info("storage_state is not empty")
    return storage_state


def wis_browser(f, d, progress = None):
    # Default settings #
    headless = True
    browser_pause = False
    timer_expect_navigation = 10000
    timer_incorrect_creds = 2000
    timer_mylocker = 60000
    c = load_config()
    coachid = c['coachid']
    config = c['config']
    if config.has_section('Browser'):
        logger.info("Config 'Browser' section found")
        if config.has_option('Browser','headless'):
            logger.info("'Browser' section has 'headless' option")
            try:
                headless = config.getboolean('Browser', 'headless')
            except Exception as err:
                logger.error("Error trying to get boolean value from Browser headless option.")

    logger.info(f"Setting headless = {headless}")
    logger.info(f"Setting timer_expect_navigation = {timer_expect_navigation}")
    logger.info(f"Setting timer_incorrect_creds = {timer_incorrect_creds}")
    logger.info(f"Setting timer_mylocker = {timer_mylocker}")
    logger.info(f"Setting browser_pause = {browser_pause}")


    global storage_state
    storage_state = check_for_stored_cookies(coachid)
    if storage_state == "" or "auth_to_store_cookies" in f:
        file = os.path.join(myconfig.cookies_directory_path, f"browser_cookie_{coachid}.json") 
        if path.exists(file):
            logger.info(f"Deleting current cookie file {file}")
            os.remove(file)
        headless = False
        logger.info("Session requires interactive login.")
        logger.info(f"Setting headless = {headless}")
    with sync_playwright() as p:
        if myconfig.os_platform == "Windows":
            logger.debug(f"Configuring Playwright Browser Path for {myconfig.os_platform}")
            browser_path = Path(sys.modules['playwright'].__file__).parent / 'driver' / 'package' / '.local-browsers' / 'firefox-1250' / 'firefox' / 'firefox.exe'
        elif myconfig.os_platform == "Linux":
            logger.debug(f"Configuring Playwright Browser Path for {myconfig.os_platform}")
            browser_path = Path(sys.modules['playwright'].__file__).parent / 'driver' / 'package' / '.local-browsers' / 'firefox-1250' / 'firefox' / 'firefox'
        else:
            logger.error(f"{myconfig.os_platform} is not supported!")
            return False
        logger.info(f"Browser path = {browser_path}")
        logger.info(f"Browser path is valid? = {browser_path.exists()}")
        if not browser_path.exists():
            logger.error("Browser path is not valid!!!")
            return False
        browser = p.firefox.launch(
            headless=headless,
            executable_path=browser_path)
        custom_headers = {'User-Agent': 'gdrecruit', 'Application-Name': f'{myconfig.application_name} ({myconfig.version})'}

        

        if "auth_to_store_cookies" in f or storage_state == "":
            logger.info(f"Opening non-headless browser in order to have user complete auth process and store cookies.")
            context = browser.new_context()
            page = context.new_page()
            page.set_extra_http_headers(custom_headers)
            page.set_viewport_size({"width": 1900, "height": 1200})
            
            try:
                page.goto(f"https://{myconfig.main_url}/locker/", timeout=timer_expect_navigation)
                
            except TimeoutError as err:
                logger.error(f"Exception during authentication section: {err.__class__}")
                logger.error(f"Exception = {err}")
                return False
            except Exception as err:
                logger.error(f"e.message = {err.message}")
                if err.message == "NS_BINDING_ABORTED":
                    logger.error(f"Ignoring {err} exception")
                    pass
                else:
                    logger.error(f"Exception following WIS Authentication attempt: {err.__class__}")
                    logger.error(f"Exception = {err}")
                    return False
            # Click text=Login
            page.click("text=Login")
            # Click input[name="username"]
            logger.info("Clicking on WIS username field...")
            page.click("input[name=\"username\"]")
            try:
                logger.info(f"Waiting for My Locker...")
                page.wait_for_selector("h1:has-text(\"My Locker\")", timeout=timer_mylocker)
            except TimeoutError as err:
                logger.error(f"Timeout waiting for My Locker: {err.__class__}")
                logger.error(f"Exception = {err}")
                logger.debug("progress.emit(999999)")
                progress.emit(999999)
                return False
            except Exception as err:
                if err.message == "NS_BINDING_ABORTED":
                    logger.error(f"Ignoring {err} exception")
                    cookiefile = f"browser_cookie_{coachid}.json"
                    logger.info(f"Store cookie state in {cookiefile}")
                    storage_state = context.storage_state()
                    with open(cookiefile, "w") as write_file:
                        json.dump(storage_state, write_file)
                    logger.debug("progress.emit(1)")
                    progress.emit(1)
                else:
                    logger.error(f"Exception during select text 'My Locker' section: {err.__class__}")
                    logger.error(f"Exception = {err}")
                    logger.debug("progress.emit(999999)")
                    progress.emit(999999)
                    return False
            else:
                logger.info("Found 'My Locker' so authentication was successful.")
                time.sleep(10)
                cookiefile = os.path.join(myconfig.cookies_directory_path, f"browser_cookie_{coachid}.json")
                logger.info(f"Store cookie state in {cookiefile}")
                storage_state = context.storage_state()
                with open(cookiefile, "w") as write_file:
                    json.dump(storage_state, write_file)
                logger.debug("progress.emit(1)")
                progress.emit(1)
                return True
            finally:
                
                context.close()
                browser.close()
                logger.info("Playwright browser closed.")
            
        else:
            context = browser.new_context(storage_state=storage_state)
            page = context.new_page()
            page.set_extra_http_headers(custom_headers)
            page.set_viewport_size({"width": 1900, "height": 1200})
            #page.pause()
            logger.info("Going to page https://www.whatifsports.com/locker/ ...")
            page.goto(f"https://{myconfig.main_url}/locker/")
            #with page.expect_navigation():
            #    page.click("text=Login")

            try:
                logger.info(f"Waiting for My Locker...")
                page.wait_for_selector("h1:has-text(\"My Locker\")", timeout=timer_mylocker)
            except TimeoutError as err:
                logger.error(f"Timeout waiting for My Locker: {err.__class__}")
                logger.error(f"Exception = {err}")
                return False
            except Exception as err:
                if err.message == "NS_BINDING_ABORTED":
                    logger.error(f"Ignoring {err} exception")
                else:
                    logger.error(f"Exception during select text 'My Locker' section: {err.__class__}")
                    logger.error(f"Exception = {err}")
                    context.close()
                    browser.close()
                    logger.info("Playwright browser closed.")
                    return False
            else:
                logger.info("Found 'My Locker' so authentication was successful.")

            openDB(d)            
            dbname = d.databaseName()
            
            logger.info(f"Before scraping recruits: Database name = {d.databaseName()} Connection name = {d.connectionName()} Tables = {d.tables()}")
            logger.info(f"DB is valid: {d.isValid()}")
            logger.info(f"DB is open: {d.isOpen()}")
            logger.info(f"DB is open error: {d.isOpenError()}")
            
            teamID = re.search(r"(\d{5})", dbname)

            cookie_teamID = {'domain': f'{myconfig.main_url}', 'expires': 1646455554, 'httpOnly': False, 'name': 'wispersisted', 'path': '/', 'sameSite': 'None', 'secure': False, 'value': f'gd_teamid={teamID.group()}'}
            logger.info(f"Setting cookie for teamid = {teamID}")
            context.add_cookies([cookie_teamID])

            if "grab_watched_recruits" in f:
                logger.info("In grab_watched_recruits section of WISBrowser")
                # Thread progress emit signal indicating WIS Auth is complete
                progress.emit(1)
                
                logger.info("Loading Recruiting Summary page ...")
                try:
                    with page.expect_navigation():
                        page.goto(f"https://{myconfig.main_url}/gd/recruiting")
                        # assert page.url == "https://www.whatifsports.com/gd/recruiting"
                    progress.emit(2)
                    page.wait_for_load_state(state='networkidle')
                    # Click h3:has-text("Recruiting Summary")
                    page.click("h3:has-text(\"Recruiting Summary\")")
                except Exception as e:
                    logger.error(f"Exception loading Recruiting Summary Page: {e.__class__}")
                    recruit_summary = ""
                else:
                    # Grab page contents to parse and return
                    recruit_summary = BeautifulSoup(page.content(), "lxml")
                    logger.info("Grabbed Recruiting Summary page content")
                finally:
                    context.close()
                    browser.close()
                    logger.info("Playwright browser closed.")
                    if d.isOpen():
                        d.close()
                    return recruit_summary
            else:
                team_division = myconfig.wis_gd_df.division[int(teamID.group())]
                # Dictionary lookup based on division and whether or not 'grab higher division' was enabled
                division_to_page_mapping = {'D-IA': {False: f'https://{myconfig.main_url}/gd/recruiting/Advanced.aspx?divisions=1&positions=1,2,3,4,5,6,7,8,9,10', 
                                                    True: f'https://{myconfig.main_url}/gd/recruiting/Advanced.aspx?divisions=1,2&positions=1,2,3,4,5,6,7,8,9,10'},
                                            'D-IAA': {False: f'https://{myconfig.main_url}/gd/recruiting/Advanced.aspx?divisions=2&positions=1,2,3,4,5,6,7,8,9,10', 
                                                    True: f'https://{myconfig.main_url}/gd/recruiting/Advanced.aspx?divisions=1,2&positions=1,2,3,4,5,6,7,8,9,10'},
                                            'D-II':  {False: f'https://{myconfig.main_url}/gd/recruiting/Advanced.aspx?divisions=3&positions=1,2,3,4,5,6,7,8,9,10', 
                                                    True: f'https://{myconfig.main_url}/gd/recruiting/Advanced.aspx?divisions=2,3&positions=1,2,3,4,5,6,7,8,9,10'},
                                            'D-III': {False: f'https://{myconfig.main_url}/gd/recruiting/Advanced.aspx?divisions=4&positions=1,2,3,4,5,6,7,8,9,10', 
                                                    True: f'https://{myconfig.main_url}/gd/recruiting/Advanced.aspx?divisions=3,4&positions=1,2,3,4,5,6,7,8,9,10'}
                }
                division_emit_progress_mapping = {'D-IA': {False: 1, True: 2},
                                                  'D-IAA': {False: 3, True: 4},
                                                  'D-II':  {False: 5, True: 6},
                                                  'D-III': {False: 7, True: 8}
                }
                settings = QSettings()
                dbname_short = dbname.split('\\')[-1]

                if "scrape_recruit_IDs" in f:
                    recruit_search_url = division_to_page_mapping[team_division][myconfig.higher_division_recruits]
                    
                    saved_url = settings.setValue(f"{dbname_short}/searchpage", recruit_search_url)

                if "update_considering" in f:
                    recruit_search_url = settings.value(f"{dbname_short}/searchpage", division_to_page_mapping[team_division][True])

                logger.debug(f"Going to advanced recruit search URL = {recruit_search_url}")
                page.goto(recruit_search_url)
                #page.goto("https://www.whatifsports.com/gd/recruiting/advanced.aspx")
                # assert page.url == "https://www.whatifsports.com/gd/recruiting/Search.aspx"

                div = page.query_selector('id=advanced-recruiting-table')
                logger.debug("Waiting for advanced recruit search table to stabilize...")
                div.wait_for_element_state(state="stable")
                logger.debug("Advanced recruit search table has stabilized.")
                logger.debug("Grabbing page content from Advanced Search page...")
                contents = page.content()
                #page.pause()
                context.close()
                browser.close()
                logger.info("Playwright browser closed.")

                if "scrape_recruit_IDs" in f:             
                    # Thread progress emit signal indicating WIS Auth is complete
                    progress.emit(2, division_emit_progress_mapping[team_division][myconfig.higher_division_recruits])

                    logger.info("Begin scraping recruit IDs...")
                        
                    createRecruitQuery = get_create_recruit_query_object(d)

                    recruitIDs = get_recruitIDs(contents, d, createRecruitQuery, progress)
                    
                    createRecruitQuery.finish()
                    d.close()
                    logger.info(f"Length of recruitIDs = {len(recruitIDs)}")
                    logger.info("Recruit initialization in database is complete.")
                    logger.debug("Saving hash of role ratings used for calculation to registry...")
                    role_ratings_hash = settings.setValue(f"{dbname_short}/role_ratings_hash", myconfig.role_ratings_df_hash)
                    return True

                if "update_considering" in f:             
                    # Thread progress emit signal indicating WIS Auth is complete
                    progress.emit(2, 1)    
                                    
                    # This section covers unsigned recruits
                    logger.info("Begin update considering for unsigned recruit IDs...")                
                    
                    createUpdateQuery = get_update_considering_query_object(d)

                    recruitIDs = update_considering(contents, d,createUpdateQuery, progress)

                    createUpdateQuery.finish()
                    d.close()
                    logger.info(f"Number of recruits updated from page = {len(recruitIDs)}")
                    logger.info("Recruit update considering in database is complete.")            
                    
                    return True
                
    # This 'return False' should only be reached if there was some coding error above
    return False

def get_create_recruit_query_object(d):
    logger.info(f"get_create_recruit_query_object:\nDatabase name = {d.databaseName()}\nConnection name = {d.connectionName()}")
    createRecruitQuery = QSqlQuery(d)
    if not createRecruitQuery.prepare("INSERT INTO recruits(id,"
                                                        "name,"
                                                        "pos,"
                                                        "height,"
                                                        "weight,"
                                                        "rating,"
                                                        "rank,"
                                                        "hometown,"
                                                        "miles,"
                                                        "considering,"
                                                        "ath,"
                                                        "spd,"
                                                        "dur,"
                                                        "we,"
                                                        "sta,"
                                                        "str,"
                                                        "blk,"
                                                        "tkl,"
                                                        "han,"
                                                        "gi,"
                                                        "elu,"
                                                        "tec,"
                                                        "r1,"
                                                        "r2,"
                                                        "r3,"
                                                        "r4,"
                                                        "r5,"
                                                        "r6,"
                                                        "gpa,"
                                                        "pot,"
                                                        "signed,"
                                                        "watched,"
                                                        "division) "
                                            "VALUES (:id, "
                                                    ":name, "
                                                    ":pos, "
                                                    ":height, "
                                                    ":weight, "
                                                    ":rating, "
                                                    ":rank, "
                                                    ":hometown, "
                                                    ":miles, "
                                                    ":considering, "
                                                    ":ath, "
                                                    ":spd, "
                                                    ":dur, "
                                                    ":we, "
                                                    ":sta, "
                                                    ":str, "
                                                    ":blk, "
                                                    ":tkl, "
                                                    ":han, "
                                                    ":gi, "
                                                    ":elu, "
                                                    ":tec, "
                                                    ":r1, "
                                                    ":r2, "
                                                    ":r3, "
                                                    ":r4, "
                                                    ":r5, "
                                                    ":r6, "
                                                    ":gpa, "
                                                    ":pot, "
                                                    ":signed, "
                                                    ":watched, "
                                                    ":division)"):
        logger.error(f"Last query error = {createRecruitQuery.lastError()}")
        logQueryError(createRecruitQuery)
    return createRecruitQuery


def bindRecruitQuery(query, i, signed=int()):
    query.bindValue(":id", i['id'])
    query.bindValue(":name", i['name'])
    query.bindValue(":pos", i['pos'])
    query.bindValue(":height", i['height'])
    query.bindValue(":weight", i['weight'])
    query.bindValue(":rating", i['rating'])
    query.bindValue(":rank", i['rank'])
    query.bindValue(":hometown", i['hometown'])
    query.bindValue(":miles", i['miles'])
    query.bindValue(":considering", i['considering'])
    query.bindValue(":ath", i['ath'])
    query.bindValue(":spd", i['spd'])
    query.bindValue(":dur", i['dur'])
    query.bindValue(":we", i['we'])
    query.bindValue(":sta", i['sta'])
    query.bindValue(":str", i['str'])
    query.bindValue(":blk", i['blk'])
    query.bindValue(":tkl", i['tkl'])
    query.bindValue(":han", i['han'])
    query.bindValue(":gi", i['gi'])
    query.bindValue(":elu", i['elu'])
    query.bindValue(":tec", i['tec'])
    query.bindValue(":r1", i['r1'])
    query.bindValue(":r2", i['r2'])
    query.bindValue(":r3", i['r3'])
    query.bindValue(":r4", i['r4'])
    query.bindValue(":r5", i['r5'])
    query.bindValue(":r6", i['r6'])
    query.bindValue(":gpa", i['gpa'])
    query.bindValue(":pot", i['potential'])
    query.bindValue(":signed", i['signed'])
    query.bindValue(":watched", i['watched'])
    query.bindValue(":division", i['division'])
    if not query.exec_():
        logger.error(f"Last bindRecruitQuery error = {query.lastError()}")
        logQueryError(query)
    else:
        logger.debug(f"bindRecruitQuery bound values = {query.boundValues()}")


def get_update_considering_query_object(d):
    logger.info(f"get_update_considering_query_object:\nDatabase name = {d.databaseName()}\nConnection name = {d.connectionName()}")
    createUpdateQuery = QSqlQuery(d)
    if not createUpdateQuery.prepare("UPDATE recruits "
                            "SET signed = :signed, "
                            "considering = :considering "
                            "WHERE id = :id"):
        logger.error(f"Last query error = {createUpdateQuery.lastError()}")
        logQueryError(createUpdateQuery)
    return createUpdateQuery
    

def bindUpdateQuery(query, i):
    query.bindValue(":id", i['id'])
    query.bindValue(":considering", i['considering'])
    query.bindValue(":signed", i['signed'])
    if not query.exec_():
        logger.error(f"Last bindUpdateQuery error = {query.lastError()}")
        logQueryError(query)
    else:
        logger.debug(f"bindUpdateQuery bound values = {query.boundValues()}")
