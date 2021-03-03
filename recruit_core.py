import time
import asyncio
import re
import datetime
import sqlite3
import csv
import requests
from sqlite3 import Error
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
from progress.bar import Bar
import configparser
from mypackages.world_lookup import wid_world_list

async def create_DB():
    database = r"recruit.db"
    conn = await create_connection(database)

    sql_create_recruits_table = """ CREATE TABLE IF NOT EXISTS recruits (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT,
                                        pos TEXT,
                                        height TEXT,
                                        weight INTEGER,
                                        rating INTEGER,
                                        rank INTEGER,
                                        hometown TEXT,
                                        miles INTEGER,
                                        considering TEXT,
                                        ath INTEGER,
                                        spd INTEGER,
                                        dur INTEGER,
                                        we INTEGER,
                                        sta INTEGER,
                                        str INTEGER,
                                        blk INTEGER,
                                        tkl INTEGER,
                                        han INTEGER,
                                        gi INTEGER,
                                        elu INTEGER,
                                        tec INTEGER,
                                        tot INTEGER,
                                        gpa REAL,
                                        pot TEXT
                                    ); """

    if conn is not None:
        # create recruits table
        await create_table(conn, sql_create_recruits_table)
        return conn
    else:
        print("Error! cannot create the database connection.")


async def create_connection(db_file):
    """
    create a database connection to the SQLite database
    specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return conn


async def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


async def get_recruitIDs(page_content):
    recruitIDs = []
    recruitpage_soup = BeautifulSoup(page_content, "lxml")
    select_Main_divGeneral = recruitpage_soup.find(id="ctl00_ctl00_ctl00_Main_Main_Main_divGeneral")
    recruitRows = select_Main_divGeneral.find_all("tr", id=False)
    print("Scraping recruit info from Recruiting Search page...")
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
            'id' : rid,
            'name' : td_tags[2].text,
            'pos': td_tags[1].text,
            'height' : td_tags[3].text,
            'weight' : td_tags[4].text,
            'rating' : td_tags[5].text,
            'rank' : td_tags[6].text,
            'hometown' : td_tags[7].text,
            'miles' : td_tags[8].text,
            'considering' : considering
        })
    next_link_tag = recruitpage_soup.find(id="ctl00_ctl00_ctl00_Main_Main_Main_lnkNextPage")
    print(f"Number of recruits found on page = {len(recruitIDs)}")
    if next_link_tag is not None:
        return recruitIDs, True
    else:
        return recruitIDs, False


async def create_recruit(conn, recruit):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO recruits(id,name,pos,height,weight,rating,
              rank,hometown,miles,considering,ath,spd,dur,we,sta,str,
              blk,tkl,han,gi,elu,tec,tot,gpa,pot)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, recruit)
    conn.commit()
    return cur.lastrowid


async def initialize_recruitIDs_DB(conn, filename):
    recruitIDs = await recruitsImportCSV(filename)
    print("Initializing recruits in the DB...")
    with conn:
        for each in recruitIDs:
            temp = [each['id'],each['name'],each['pos'],each['height'],each['weight'],each['rating'],each['rank'],each['hometown'],each['miles'],each['considering'],0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'']
            await create_recruit(conn,temp)


async def initialize_recruit_static_data(conn, page):
    cur = conn.cursor()
    cur.execute("SELECT id FROM recruits")
    rids = cur.fetchall()
    
    with Bar('Initializing Recruit Static Data', max=len(rids)) as bar:
        for rid in rids:
            await page.goto(f"https://www.whatifsports.com/gd/RecruitProfile/Ratings.aspx?rid={rid[0]}")
            contents = await page.content()
            recruitpage_soup = BeautifulSoup(contents, "lxml")
            name_section = recruitpage_soup.find(id="ctl00_ctl00_ctl00_Main_Main_name")
            name = name_section.text
            pos_section = recruitpage_soup.find(id="ctl00_ctl00_ctl00_Main_Main_position")
            pos = pos_section.text
            recruit_ratings_section = recruitpage_soup.find(class_="ratingsDisplayCtl")
            recruit_ratings_values = recruit_ratings_section.find_all(class_="value")
            ath = int(recruit_ratings_values[0].text)
            spd = int(recruit_ratings_values[1].text)
            dur = int(recruit_ratings_values[2].text)
            we = int(recruit_ratings_values[3].text)
            sta = int(recruit_ratings_values[4].text)
            strength = int(recruit_ratings_values[5].text)
            blk = int(recruit_ratings_values[6].text)
            tkl = int(recruit_ratings_values[7].text)
            han = int(recruit_ratings_values[8].text)
            gi = int(recruit_ratings_values[9].text)
            elu = int(recruit_ratings_values[10].text)
            tec = int(recruit_ratings_values[11].text)
            tot = ath + spd + dur + we + sta + strength + blk + tkl + han + gi + elu + tec
            gpa_section = recruitpage_soup.find(id="ctl00_ctl00_ctl00_Main_Main_gpa")
            gpa = float(gpa_section.text)
            hometown_section = recruitpage_soup.find(id="ctl00_ctl00_ctl00_Main_Main_homeTown")
            hometown = hometown_section.text
            try:
                miles_section = recruitpage_soup.find(id="ctl00_ctl00_ctl00_Main_Main_miles")
                miles_extract = re.search(r"\((\d{1,4})\smiles\)", miles_section.text.replace(',',''))
                miles = int(miles_extract.group(1))
            except:
                print(f"Could not located miles for recruit ID = {rid}")
                miles = 0

            sql = ''' UPDATE recruits
                SET name = ? ,
                    pos = ? ,
                    ath = ? ,
                    spd = ? ,
                    dur = ? ,
                    we = ? ,
                    sta = ? ,
                    str = ? ,
                    blk = ? ,
                    tkl = ? ,
                    han = ? ,
                    gi = ? ,
                    elu = ? ,
                    tec = ? ,
                    tot = ? ,
                    gpa = ? ,
                    miles = ?
                WHERE id = ?'''
            tmp = (name, pos, ath, spd, dur, we, sta, strength, blk, tkl, han, gi, elu, tec, tot, gpa, miles, rid[0])
            cur.execute(sql, tmp)
            conn.commit()
            bar.next()


async def initialize_recruit_static_data_without_playwright(conn):
    requests_session = requests.Session()
    
    cur = conn.cursor()
    cur.execute("SELECT id FROM recruits")
    rids = cur.fetchall()
    
    with Bar('Initializing Recruit Static Data without Playwright', max=len(rids)) as bar:
        for rid in rids:
            recruitpage = requests_session.get(f"https://www.whatifsports.com/gd/RecruitProfile/Ratings.aspx?rid={rid[0]}")
            recruitpage_soup = BeautifulSoup(recruitpage.content, "lxml")
            # name_section = recruitpage_soup.find(id="ctl00_ctl00_ctl00_Main_Main_name")
            # name = name_section.text
            # pos_section = recruitpage_soup.find(id="ctl00_ctl00_ctl00_Main_Main_position")
            # pos = pos_section.text
            recruit_ratings_section = recruitpage_soup.find(class_="ratingsDisplayCtl")
            recruit_ratings_values = recruit_ratings_section.find_all(class_="value")
            ath = int(recruit_ratings_values[0].text)
            spd = int(recruit_ratings_values[1].text)
            dur = int(recruit_ratings_values[2].text)
            we = int(recruit_ratings_values[3].text)
            sta = int(recruit_ratings_values[4].text)
            strength = int(recruit_ratings_values[5].text)
            blk = int(recruit_ratings_values[6].text)
            tkl = int(recruit_ratings_values[7].text)
            han = int(recruit_ratings_values[8].text)
            gi = int(recruit_ratings_values[9].text)
            elu = int(recruit_ratings_values[10].text)
            tec = int(recruit_ratings_values[11].text)
            tot = ath + spd + dur + we + sta + strength + blk + tkl + han + gi + elu + tec
            gpa_section = recruitpage_soup.find(id="ctl00_ctl00_ctl00_Main_Main_gpa")
            gpa = float(gpa_section.text)
            # hometown_section = recruitpage_soup.find(id="ctl00_ctl00_ctl00_Main_Main_homeTown")
            # hometown = hometown_section.text

            sql = ''' UPDATE recruits
                SET ath = ? ,
                    spd = ? ,
                    dur = ? ,
                    we = ? ,
                    sta = ? ,
                    str = ? ,
                    blk = ? ,
                    tkl = ? ,
                    han = ? ,
                    gi = ? ,
                    elu = ? ,
                    tec = ? ,
                    tot = ? ,
                    gpa = ?
                WHERE id = ?'''
            tmp = (ath, spd, dur, we, sta, strength, blk, tkl, han, gi, elu, tec, tot, gpa, rid[0])
            cur.execute(sql, tmp)
            conn.commit()
            bar.next()


async def wisLogin(page, config):
    username = config['WISCreds']['username']
    password = config['WISCreds']['password']
    await page.set_viewport_size({"width": 1900, "height": 1200})
    await page.goto("http://www.whatifsports.com/")
    print(await page.title())

    async with page.expect_navigation():
        await page.click("text=Login")

    print("Authenticating to WIS...")
    # Click input[name="username"]
    await page.click("input[name=\"username\"]")
    # Fill input[name="username"]
    await page.fill("input[name=\"username\"]", username)
    time0 = 0.75
    print(f"Sleeping {time0} seconds.")
    time.sleep(time0)
    # Click input[name="password"]
    await page.click("input[name=\"password\"]")
    # Fill input[name="password"]
    await page.fill("input[name=\"password\"]", password)
    time1 = 1.15
    print(f"Sleeping {time1} seconds.")
    time.sleep(time1)
    # Click button:has-text("Sign in")
    await page.click("button:has-text(\"Sign in\")")


async def find_GD_teams(page, config):
    print("Going to Lockerroom page...")
    await page.goto("https://www.whatifsports.com/locker/lockerroom.asp")
    s = 10
    print(f"Sleeping for {s} seconds...")
    time.sleep(s)
    contents = await page.content()
    lockerroom_soup = BeautifulSoup(contents, "lxml")
    select_teamName_divs = lockerroom_soup.find_all(class_="teamName")
    baseURL = "../gd/TeamRedirect.aspx?tid="
    for team in select_teamName_divs:
        a_tag = team.find("a")
        link = a_tag.attrs['href']
        if baseURL in link:
            school = a_tag.text
            school_id_re = re.search(r'(\d{5})', link)
            school_id = school_id_re.group(1)
            if config.has_section('Schools'):
                config.set('Schools', school_id, school)
            else:
                config.add_section('Schools')
                config.set('Schools', school_id, school)

    with open('config.ini', 'w') as file:
        config.write(file)

async def main():
    filename = "recruits.csv"
    conn = await create_DB()

    config = configparser.ConfigParser()
    config.read('config.ini')

    recruitIDs = []
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()


        # Login to WIS website
        await wisLogin(page, config)
        
        # Need to replace this sleep statement with something that is event driven
        time2 = 5
        print(f"Sleeping {time2} seconds.")
        time.sleep(time2)

        await find_GD_teams(page, config)
        
        # Miami = 53424     PSU = 51194
        teamID = 53424
        await page.goto(f"https://www.whatifsports.com/gd/TeamRedirect.aspx?tid={teamID}")
                
        # Comment these out for testing for testing DB creation and updating
        recruitIDs = await scrapeRecruitIDs(page)
        await recruitsExportCSV(recruitIDs, filename)
        await initialize_recruitIDs_DB(conn, filename)
        # await initialize_recruit_static_data(conn, page)
        await initialize_recruit_static_data_without_playwright(conn)

        await browser.close()


async def scrapeRecruitIDs(page):
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
    print("Scraping recruit IDs...")
    for i in range(7,8):
        await page.goto("https://www.whatifsports.com/gd/recruiting/Search.aspx")
        # assert page.url == "https://www.whatifsports.com/gd/recruiting/Search.aspx"

        print(f"Selecting position {position_dropdown[i]}")           
        # Select 1
        await page.select_option("text=Position: All Quarterback Running Back Wide Receiver Tight End Offensive Line De >> select", f"{i}")
        
        # Click text=Recruit Search Options
        await page.click("text=Recruit Search Options")
        
        # Select 300
        await page.select_option("#ctl00_ctl00_ctl00_Main_Main_Main_MaxRecords", "300")
        
        # Click #ctl00_ctl00_ctl00_Main_Main_Main_btnSearch
        await page.click("#ctl00_ctl00_ctl00_Main_Main_Main_btnSearch")
        
        next = True
        while next == True:
            # Need to replace this sleep statement with something that is event driven
            time3 = 3
            print(f"Sleeping {time3} seconds.")
            time.sleep(time3)

            contents = await page.content()
            # print(contents)
            # Need to replace this sleep statement with something that is event driven
            time4 = 3
            print(f"Sleeping {time3} seconds.")
            time.sleep(time4)

            temp, next = await get_recruitIDs(contents)
            recruitIDs += temp
            if next == True:
                # Click text=/.*Next \>\>.*/
                await page.click("text=/.*Next \>\>.*/")
        print(len(recruitIDs))
    return recruitIDs


async def recruitsExportCSV(dict, filename):
    csv_columns = ['id','name','pos','height','weight','rating','rank','hometown','miles', 'considering']
    print("Exporting recruits to CSV...")
    with open(filename, mode='w', newline='') as f:
        recruit_writer = csv.DictWriter(f, fieldnames=csv_columns)
        recruit_writer.writeheader()
        for each in dict:
            recruit_writer.writerow(each)


async def recruitsImportCSV(filename):
    recruitIDs = []
    # reading csv file 
    print("Importing recruits from CSV...")
    with open(filename, 'r',newline='') as csvfile: 
        # creating a csv reader object 
        csvreader = csv.DictReader(csvfile)
    
        # extracting each data row one by one 
        for row in csvreader: 
            recruitIDs.append(row) 
    
    return recruitIDs

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.run_until_complete(asyncio.sleep(1))
loop.close()