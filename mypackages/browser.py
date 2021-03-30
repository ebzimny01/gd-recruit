import logging

logger = logging.getLogger(__name__)

from os import stat
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import datetime
import re
from random import uniform
import sys
from PySide2.QtWidgets import *
from PySide2.QtSql import *
from pathlib import Path
import inspect
from main import logQueryError


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


def get_recruitIDs(page_content):
    recruitIDs = []
    recruitpage_soup = BeautifulSoup(page_content, "lxml")
    select_Main_divGeneral = recruitpage_soup.find(id="ctl00_ctl00_ctl00_Main_Main_Main_divGeneral")
    recruitRows = select_Main_divGeneral.find_all("tr", id=False)
    logger.info("Scraping recruit info from Recruiting Search page...")
    for each in recruitRows:
        recruit_link_tag = each.find(class_="recruitProfileLink")
        href_tag = recruit_link_tag.attrs['href']
        href_tag_re = re.search(r'(\d{8})', href_tag)
        recruit = href_tag_re.group(1)
        rid = int(recruit)
        td_tags = each.find_all("td")
        considering = ""
        if td_tags[9].text.strip() == "undecided":
            considering = "undecided"
        else:
            considering_list = td_tags[9].find_all("a")
            for a in considering_list:
                considering += f"{a.text}\n"
            considering = considering[:-1] # removes newline at end
        recruitIDs.append({
            'id': rid,
            'name': td_tags[2].text,
            'pos': td_tags[1].text,
            'height': td_tags[3].text,
            'weight': int(td_tags[4].text),
            'rating': int(td_tags[5].text),
            'rank': td_tags[6].text,
            'hometown': td_tags[7].text,
            'miles': int(td_tags[8].text),
            'considering': considering
        })
    next_link_tag = recruitpage_soup.find(id="ctl00_ctl00_ctl00_Main_Main_Main_lnkNextPage")
    logger.info(f"Number of recruits found on page = {len(recruitIDs)}")
    if next_link_tag is not None:
        return recruitIDs, True
    else:
        return recruitIDs, False


def randsleep():
    s = uniform(0.1, 0.5)
    return s


def wis_browser(config, user, pwd, f, d, progress = None):
    headless = True # default setting
    if config.has_section('Browser'):
        logger.info("Config.ini contains Browser section")
        if config.has_option('Browser', 'headless'):
            logger.info("Browser section contains headless option")
            headless = config.getboolean('Browser', 'headless')
            logger.info(f"Setting headless = {headless}")
    else:
        logger.info("Config.ini does not contain Browser section")
        logger.info(f"Setting headless = {headless}")

    with sync_playwright() as p:
        browser_path = Path(sys.modules['playwright'].__file__).parent / 'driver' / 'package' / '.local-browsers' / 'firefox-1234' / 'firefox' / 'firefox.exe'
        logger.info(f"Browser path = {browser_path}")
        logger.info(f"Browser path is valid? = {browser_path.exists()}")
        browser = p.firefox.launch(
            headless=headless,
            executable_path=browser_path)
        context = browser.new_context()
        page = context.new_page()

        page.set_viewport_size({"width": 1900, "height": 1200})
        page.goto("https://www.whatifsports.com/locker/")
        logger.info(page.title())
        # Click text=Login
        page.click("text=Login")
        # assert page.url == "https://idsrv.fanball.com/login?signin=2c7ce157635ba9eab815f3cb2bdb83ce"
        # Go to https://idsrv.fanball.com/login?signin=2c7ce157635ba9eab815f3cb2bdb83ce&__cf_chl_jschl_tk__=748937e860f9dfc589364946f2e8af8c1eefbe7e-1614806310-0-AYX5rk621iTj_xPBtx5a9cubtsH4r7FR5uoSr4UmdL_BcUZKav9FAu1Wzybc7YI4a9N5Q7g_QAJzNzcOluUW-o99hqqOQQP1VkLwiP7W5DSaQYNqJBydxXiojR1tdAdzfnP6vQtkY42I0K7ngy-2AlArSUUiVG41fr4Y9rwHHatCLYPVhB3sTGZ17ZH8TCiXaNVC7pGYWav1fmxuY8lJ-iLb-ktGqxbLn8vV2EcrCNyZUzkeMk3ruMsoq0w-P_OTtzCltc-5vzq5SOKxnZyY84RvXRJai02utdOsiceCgMHsEWfVX0tNdHhq7tEW0lb4ABOTPwOkMuXX8WeczHUJHH35Lpxp0QzQ2QMuddSwXjS0vCfJTswNn8f8mAS_bP0GLcXHvOzXMVdD31TNyZvOUtKxmyYIoIHeKIDNZW3mvHtb
        # page.goto("https://idsrv.fanball.com/login?signin=2c7ce157635ba9eab815f3cb2bdb83ce&__cf_chl_jschl_tk__=748937e860f9dfc589364946f2e8af8c1eefbe7e-1614806310-0-AYX5rk621iTj_xPBtx5a9cubtsH4r7FR5uoSr4UmdL_BcUZKav9FAu1Wzybc7YI4a9N5Q7g_QAJzNzcOluUW-o99hqqOQQP1VkLwiP7W5DSaQYNqJBydxXiojR1tdAdzfnP6vQtkY42I0K7ngy-2AlArSUUiVG41fr4Y9rwHHatCLYPVhB3sTGZ17ZH8TCiXaNVC7pGYWav1fmxuY8lJ-iLb-ktGqxbLn8vV2EcrCNyZUzkeMk3ruMsoq0w-P_OTtzCltc-5vzq5SOKxnZyY84RvXRJai02utdOsiceCgMHsEWfVX0tNdHhq7tEW0lb4ABOTPwOkMuXX8WeczHUJHH35Lpxp0QzQ2QMuddSwXjS0vCfJTswNn8f8mAS_bP0GLcXHvOzXMVdD31TNyZvOUtKxmyYIoIHeKIDNZW3mvHtb")
    
        logger.info("Authenticating to WIS...")
        
        # Click input[name="username"]
        logger.info("Clicking on WIS username field...")
        page.click("input[name=\"username\"]")
        s = randsleep()
        logger.debug(f"Sleeping for {s} seconds...")
        time.sleep(s)
        # Fill input[name="username"]
        logger.info("Entering WIS username...")
        page.fill("input[name=\"username\"]", user)
        s = randsleep()
        logger.debug(f"Sleeping for {s} seconds...")
        time.sleep(s)
        # Click input[name="password"]
        logger.info("Clicking on WIS password field...")
        page.click("input[name=\"password\"]")
        s = randsleep()
        logger.debug(f"Sleeping for {s} seconds...")
        time.sleep(s)
        # Fill input[name="password"]
        logger.info("Entering WIS password...")
        page.fill("input[name=\"password\"]", pwd)
        s = randsleep()
        logger.debug(f"Sleeping for {s} seconds...")
        time.sleep(s)
        # Click button:has-text("Sign in")
        # with page.expect_navigation(url="https://idsrv.fanball.com/connect/authorize?acr_values=ConfirmEmailRedirectUrl%3Ahttps%3A%2F%2Fwww.whatifsports.com%2Faccount%2F&client_id=what-if-sports&nonce=637505041935753100.ZGYzYzIzNDktZTZkZC00YmUxLTg2MjQtZGY2N2JjOTY4OTNhNzJhYWM3OGEtNjkzNS00NzEwLTk3MmMtMTFhMTkwNzJhODQ0&redirect_uri=https%3A%2F%2Fwww.whatifsports.com%2Faccount%2F&response_mode=form_post&response_type=id_token%20token&scope=openid%20profile%20social%20email%20wallet-readonly%20whatifsports-readonly%20connect-notifications-publish&state=OpenIdConnect.AuthenticationProperties%3D6wZySDpgbMTUvbl_WFJuybvrjFTor6ugKdSOvE-ILuNp3RT9OJPhi4DsybXR2lf9IeJYO7-6fo2paUWlFOSXk2ssF_8LTyeAUPaG7s6RPo8Zc_3rRZN63naxd2PLtIwYxCHsOg3u3yC9xANaxu6Odg-F3W3uE3agKx6-azhTl3E6KCX4PnB1EVcq5Ej09b3xGIfzR93OQ9WhT0PppfB4yeu1z2GzzKJs3Cl-p2tG5mXOTiMb3kwcCuzHjWb0JlOqy3jkjQ&x-client-SKU=ID_NET461&x-client-ver=5.4.0.0"):
        logger.info("Clicking on WIS login button...")
        with page.expect_navigation(url='https://www.whatifsports.com/locker/lockerroom.asp', wait_until='networkidle'):
            page.click("button:has-text(\"Sign in\")")
        # assert page.url == "https://idsrv.fanball.com/localregistration/silentlogin"
        # Go to https://www.whatifsports.com/locker/lockerroom.asp
        # page.goto("https://www.whatifsports.com/locker/lockerroom.asp")
        
                
        if "scrape_recruit_IDs" in f:
            # Thread progress emit signal indicating WIS Auth is complete
            progress.emit(2, 1)    
            openDB(d)            
            dbname = d.databaseName()
            logger.info(f"Before scaping recruits:\n \
                    Database name = {d.databaseName()}\n \
                    Connection name = {d.connectionName()}\n \
                    Tables = {d.tables()}")
            logger.info(f"DB is valid: {d.isValid()}")
            logger.info(f"DB is open: {d.isOpen()}")
            logger.info(f"DB is open error: {d.isOpenError()}")
            
            teamID = re.search(r"\d{5}", dbname)
            recruitIDs = []
            position_dropdown = {
                1 : "QB",
                2 : "RB",
                3 : "WR",
                4 : "TE",
                5 : "OL",
                6 : "DL",
                7 : "LB",
                8 : "DB",
                9 : "K",
                10 : "P"
                }
            
            #s = 10
            #print(f"Sleeping for {s} seconds...")
            #time.sleep(s)
            logger.info("Post auth, waiting for network state to be idle . . . ")
            page.wait_for_load_state(state='networkidle')

            logger.info("Scraping recruit IDs...")
            
            cookie_teamID = {'domain': 'www.whatifsports.com', 'expires': 1646455554, 'httpOnly': False, 'name': 'wispersisted', 'path': '/', 'sameSite': 'None', 'secure': False, 'value': f'gd_teamid={teamID.group()}'}
            context.add_cookies([cookie_teamID])
            page.goto("https://www.whatifsports.com/gd/recruiting/Search.aspx")
            # assert page.url == "https://www.whatifsports.com/gd/recruiting/Search.aspx"
            
            # This section covers unsigned recruits
            logger.info("Scraping unsigned recruit IDs...")
            # Thread progress signaling Scraping Unsigned recruits is beginning
            progress.emit(100, 1)
            
            # Range is 1 to 11 to cover the 10 player positions
            for i in range(1,11):
                
                logger.info(f"Selecting position {position_dropdown[i]}")           
                # Select 1
                page.select_option("text=Position: All Quarterback Running Back Wide Receiver Tight End Offensive Line De >> select", f"{i}")
                
                # Click text=Recruit Search Options
                page.click("text=Recruit Search Options")
                
                # Select 300
                page.select_option("#ctl00_ctl00_ctl00_Main_Main_Main_MaxRecords", "300")
                
                # Click #ctl00_ctl00_ctl00_Main_Main_Main_btnSearch
                with page.expect_navigation():
                    page.click("#ctl00_ctl00_ctl00_Main_Main_Main_btnSearch")
                
                createRecruitQuery = get_create_recruit_query_object(d)

                next = True
                while next == True:
                    div = page.query_selector('id=ctl00_ctl00_ctl00_Main_Main_Main_cbResults')
                    div.wait_for_element_state(state="stable")
                    contents = page.content()
                    temp, next = get_recruitIDs(contents)
                    for t in temp:
                        bindRecruitQuery(createRecruitQuery, t, 0)
                    recruitIDs += temp
                    if next == True:
                        # Click text=/.*Next \>\>.*/
                        with page.expect_navigation():
                            page.click("text=/.*Next \>\>.*/")
                logger.info(f"Length of recruitIDs = {len(recruitIDs)}")
                
                createRecruitQuery.finish()
                
                # Thread signaling progress with grabbing unsigned recruits
                progress.emit(100 + i, 1)

            # This section covers signed recruits
            logger.info("Scraping signed recruit IDs...")
            # Thread progress signaling Scraping Unsigned recruits is beginning
            progress.emit(200, 1)

            # First need to check if there are any signings at all.
            # If no signings then skip.

            # Select All
            page.select_option("text=Position: All Quarterback Running Back Wide Receiver Tight End Offensive Line De >> select", "")
            
            # Select 1 = Signed
            page.select_option("#ctl00_ctl00_ctl00_Main_Main_Main_DecisionStatus", "1")

            # Click #ctl00_ctl00_ctl00_Main_Main_Main_btnSearch
            with page.expect_navigation():
                page.click("#ctl00_ctl00_ctl00_Main_Main_Main_btnSearch")


            no_recruit_check = BeautifulSoup(page.content(), "lxml")
            results_table = no_recruit_check.find(id="ctl00_ctl00_ctl00_Main_Main_Main_h3ResultsText")
            if results_table.text == "No recruits found":
                logger.info("No signings found so skipping signed recruits section...")
                # Thread progress signaling Scraping Signed recruits is done
                progress.emit(210, 1)
            else:
                for i in range(1,11):
                    
                    logger.info(f"Selecting position {position_dropdown[i]}")           
                    # Select 1
                    page.select_option("text=Position: All Quarterback Running Back Wide Receiver Tight End Offensive Line De >> select", f"{i}")
                    
                    # Click text=Recruit Search Options
                    page.click("text=Recruit Search Options")
                    
                    # Select 300 = number of search results
                    page.select_option("#ctl00_ctl00_ctl00_Main_Main_Main_MaxRecords", "300")

                    # Select 1 = Signed
                    page.select_option("#ctl00_ctl00_ctl00_Main_Main_Main_DecisionStatus", "1")
                    
                    # Click #ctl00_ctl00_ctl00_Main_Main_Main_btnSearch
                    with page.expect_navigation():
                        page.click("#ctl00_ctl00_ctl00_Main_Main_Main_btnSearch")
                    
                    createRecruitQuery = get_create_recruit_query_object(d)

                    next = True
                    while next == True:
                        div = page.query_selector('id=ctl00_ctl00_ctl00_Main_Main_Main_cbResults')
                        div.wait_for_element_state(state="stable")
                        contents = page.content()
                        temp, next = get_recruitIDs(contents)
                        for t in temp:
                            bindRecruitQuery(createRecruitQuery, t, 1)
                        recruitIDs += temp
                        if next == True:
                            # Click text=/.*Next \>\>.*/
                            with page.expect_navigation():
                                page.click("text=/.*Next \>\>.*/")
                    logger.info(f"Length of recruitIDs = {len(recruitIDs)}")

                    createRecruitQuery.finish()

                    # Thread signaling progress with grabbing signed recruits
                    progress.emit(200 + i, 1)

                
            d.close()
            context.close()
            browser.close()
            logger.info("Playwright browser closed.")


        if "grab_watched_recruits" in f:
            logger.info("In grab_watched_recruits section of WISBrowser")
            # Thread progress emit signal indicating WIS Auth is complete
            progress.emit(1)
            openDB(d)
            dbname = d.databaseName()
            d.close()
            teamID = re.search(r"\d{5}", dbname)
            logger.info("Post auth, waiting for network state to be idle . . . ")

            # Setting cookie for team id
            cookie_teamID = {'domain': 'www.whatifsports.com', 'expires': 1646455554, 'httpOnly': False, 'name': 'wispersisted', 'path': '/', 'sameSite': 'None', 'secure': False, 'value': f'gd_teamid={teamID.group()}'}
            logger.info(f"cookie_teamID = {cookie_teamID}")
            context.add_cookies([cookie_teamID])
            
            logger.info("Loading Recruiting Summary page ...")
            with page.expect_navigation():
                page.goto("https://www.whatifsports.com/gd/recruiting")
            # assert page.url == "https://www.whatifsports.com/gd/recruiting"
            progress.emit(2)
            page.wait_for_load_state(state='networkidle')
            
            # Click h3:has-text("Recruiting Summary")
            page.click("h3:has-text(\"Recruiting Summary\")")
            
            # Grab page contents to parse and return
            recruit_summary = BeautifulSoup(page.content(), "lxml")
            logger.info("Grabbed Recruiting Summary page content")
            print(recruit_summary)
            context.close()
            browser.close()
            logger.info("Playwright browser closed.")
            return recruit_summary
           

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
                                                        "gpa,"
                                                        "pot,"
                                                        "signed,"
                                                        "watched) "
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
                                                    ":gpa, "
                                                    ":pot, "
                                                    ":signed,"
                                                    ":watched)"):
        logger.info(f"Last query error = {createRecruitQuery.lastError()}")
        logQueryError(createRecruitQuery)
    return createRecruitQuery


def bindRecruitQuery(query, i, signed = int()):
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
    query.bindValue(":ath", 0)
    query.bindValue(":spd", 0)
    query.bindValue(":dur", 0)
    query.bindValue(":we", 0)
    query.bindValue(":sta", 0)
    query.bindValue(":str", 0)
    query.bindValue(":blk", 0)
    query.bindValue(":tkl", 0)
    query.bindValue(":han", 0)
    query.bindValue(":gi", 0)
    query.bindValue(":elu", 0)
    query.bindValue(":tec", 0)
    query.bindValue(":gpa", 0.0)
    query.bindValue(":pot", '')
    query.bindValue(":signed", signed)
    query.bindValue(":watched", 0)
    if not query.exec_():
        logger.info(f"Last query error = {query.lastError()}")
        logQueryError(query)
