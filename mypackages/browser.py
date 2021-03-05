from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import re
import requests
from random import uniform
import sys
from PySide2.QtWidgets import *
from PySide2.QtSql import *


def get_recruitIDs(page_content):
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
            'weight' : int(td_tags[4].text),
            'rating' : int(td_tags[5].text),
            'rank' : int(td_tags[6].text),
            'hometown' : td_tags[7].text,
            'miles' : int(td_tags[8].text),
            'considering' : considering
        })
    next_link_tag = recruitpage_soup.find(id="ctl00_ctl00_ctl00_Main_Main_Main_lnkNextPage")
    print(f"Number of recruits found on page = {len(recruitIDs)}")
    if next_link_tag is not None:
        return recruitIDs, True
    else:
        return recruitIDs, False


def randsleep():
    s = uniform(0.5, 1.25)
    return s

def wis_browser(config, user, pwd, f, db):

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()

        page.set_viewport_size({"width": 1900, "height": 1200})
        page.goto("https://www.whatifsports.com/locker/")
        print(page.title())
        # Click text=Login
        page.click("text=Login")
        # assert page.url == "https://idsrv.fanball.com/login?signin=2c7ce157635ba9eab815f3cb2bdb83ce"
        # Go to https://idsrv.fanball.com/login?signin=2c7ce157635ba9eab815f3cb2bdb83ce&__cf_chl_jschl_tk__=748937e860f9dfc589364946f2e8af8c1eefbe7e-1614806310-0-AYX5rk621iTj_xPBtx5a9cubtsH4r7FR5uoSr4UmdL_BcUZKav9FAu1Wzybc7YI4a9N5Q7g_QAJzNzcOluUW-o99hqqOQQP1VkLwiP7W5DSaQYNqJBydxXiojR1tdAdzfnP6vQtkY42I0K7ngy-2AlArSUUiVG41fr4Y9rwHHatCLYPVhB3sTGZ17ZH8TCiXaNVC7pGYWav1fmxuY8lJ-iLb-ktGqxbLn8vV2EcrCNyZUzkeMk3ruMsoq0w-P_OTtzCltc-5vzq5SOKxnZyY84RvXRJai02utdOsiceCgMHsEWfVX0tNdHhq7tEW0lb4ABOTPwOkMuXX8WeczHUJHH35Lpxp0QzQ2QMuddSwXjS0vCfJTswNn8f8mAS_bP0GLcXHvOzXMVdD31TNyZvOUtKxmyYIoIHeKIDNZW3mvHtb
        # page.goto("https://idsrv.fanball.com/login?signin=2c7ce157635ba9eab815f3cb2bdb83ce&__cf_chl_jschl_tk__=748937e860f9dfc589364946f2e8af8c1eefbe7e-1614806310-0-AYX5rk621iTj_xPBtx5a9cubtsH4r7FR5uoSr4UmdL_BcUZKav9FAu1Wzybc7YI4a9N5Q7g_QAJzNzcOluUW-o99hqqOQQP1VkLwiP7W5DSaQYNqJBydxXiojR1tdAdzfnP6vQtkY42I0K7ngy-2AlArSUUiVG41fr4Y9rwHHatCLYPVhB3sTGZ17ZH8TCiXaNVC7pGYWav1fmxuY8lJ-iLb-ktGqxbLn8vV2EcrCNyZUzkeMk3ruMsoq0w-P_OTtzCltc-5vzq5SOKxnZyY84RvXRJai02utdOsiceCgMHsEWfVX0tNdHhq7tEW0lb4ABOTPwOkMuXX8WeczHUJHH35Lpxp0QzQ2QMuddSwXjS0vCfJTswNn8f8mAS_bP0GLcXHvOzXMVdD31TNyZvOUtKxmyYIoIHeKIDNZW3mvHtb")
    
        print("Authenticating to WIS...")
        
        # Click input[name="username"]
        page.click("input[name=\"username\"]")
        s = randsleep()
        print(f"Sleeping for {s} seconds...")
        time.sleep(s)
        # Fill input[name="username"]
        page.fill("input[name=\"username\"]", user)
        s = randsleep()
        print(f"Sleeping for {s} seconds...")
        time.sleep(s)
        # Click input[name="password"]
        page.click("input[name=\"password\"]")
        s = randsleep()
        print(f"Sleeping for {s} seconds...")
        time.sleep(s)
        # Fill input[name="password"]
        page.fill("input[name=\"password\"]", pwd)
        s = randsleep()
        print(f"Sleeping for {s} seconds...")
        time.sleep(s)
        # Click button:has-text("Sign in")
        # with page.expect_navigation(url="https://idsrv.fanball.com/connect/authorize?acr_values=ConfirmEmailRedirectUrl%3Ahttps%3A%2F%2Fwww.whatifsports.com%2Faccount%2F&client_id=what-if-sports&nonce=637505041935753100.ZGYzYzIzNDktZTZkZC00YmUxLTg2MjQtZGY2N2JjOTY4OTNhNzJhYWM3OGEtNjkzNS00NzEwLTk3MmMtMTFhMTkwNzJhODQ0&redirect_uri=https%3A%2F%2Fwww.whatifsports.com%2Faccount%2F&response_mode=form_post&response_type=id_token%20token&scope=openid%20profile%20social%20email%20wallet-readonly%20whatifsports-readonly%20connect-notifications-publish&state=OpenIdConnect.AuthenticationProperties%3D6wZySDpgbMTUvbl_WFJuybvrjFTor6ugKdSOvE-ILuNp3RT9OJPhi4DsybXR2lf9IeJYO7-6fo2paUWlFOSXk2ssF_8LTyeAUPaG7s6RPo8Zc_3rRZN63naxd2PLtIwYxCHsOg3u3yC9xANaxu6Odg-F3W3uE3agKx6-azhTl3E6KCX4PnB1EVcq5Ej09b3xGIfzR93OQ9WhT0PppfB4yeu1z2GzzKJs3Cl-p2tG5mXOTiMb3kwcCuzHjWb0JlOqy3jkjQ&x-client-SKU=ID_NET461&x-client-ver=5.4.0.0"):
        with page.expect_navigation():
            page.click("button:has-text(\"Sign in\")")
        # assert page.url == "https://idsrv.fanball.com/localregistration/silentlogin"
        # Go to https://www.whatifsports.com/locker/lockerroom.asp
        # page.goto("https://www.whatifsports.com/locker/lockerroom.asp")
        

        if "updateteams" in f:
            s = 10
            print(f"Sleeping for {s} seconds...")
            time.sleep(s)
            contents = page.content()
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
        
        if "scrape_recruit_IDs" in f:
            dbname = db.databaseName()
            if not db.open():
                QMessageBox.critical(
                    None,
                    "GD Recruiting App - Error!",
                    "Database Error: %s" % db.lastError().databaseText()
                    )
                sys.exit(1)
            createRecruitQuery = QSqlQuery()
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
            
            s = 10
            print(f"Sleeping for {s} seconds...")
            time.sleep(s)
            
            print("Scraping recruit IDs...")
            
            page.goto(f"https://www.whatifsports.com/gd/TeamRedirect.aspx?tid={teamID.group()}")
                
            page.goto("https://www.whatifsports.com/gd/recruiting/Search.aspx")
            # assert page.url == "https://www.whatifsports.com/gd/recruiting/Search.aspx"
            
            for i in range(1,11):
                
                print(f"Selecting position {position_dropdown[i]}")           
                # Select 1
                page.select_option("text=Position: All Quarterback Running Back Wide Receiver Tight End Offensive Line De >> select", f"{i}")
                
                # Click text=Recruit Search Options
                page.click("text=Recruit Search Options")
                
                # Select 300
                page.select_option("#ctl00_ctl00_ctl00_Main_Main_Main_MaxRecords", "300")
                
                # Click #ctl00_ctl00_ctl00_Main_Main_Main_btnSearch
                page.click("#ctl00_ctl00_ctl00_Main_Main_Main_btnSearch")
                
                next = True
                while next == True:
                    # Click .ContentBoxContent .resultswrapper
                    page.click(".ContentBoxContent .resultswrapper")
                    # Need to replace this sleep statement with something that is event driven
                    # time3 = 3
                    # print(f"Sleeping {time3} seconds.")
                    # time.sleep(time3)

                    contents = page.content()
                    # print(contents)
                    # Need to replace this sleep statement with something that is event driven
                    # time4 = 3
                    # print(f"Sleeping {time3} seconds.")
                    # time.sleep(time4)

                    temp, next = get_recruitIDs(contents)
                    for i in temp:
                        createRecruitQuery.exec_(
                            f"""
                            INSERT INTO recruits(id,name,pos,height,weight,rating,
                                rank,hometown,miles,considering,ath,spd,dur,we,sta,str,
                                blk,tkl,han,gi,elu,tec,tot,gpa,pot)
                                VALUES('{i['id']}','{i['name']}','{i['pos']}',
                                    '{i['height']}','{i['weight']}','{i['rating']}',
                                    '{i['rank']}','{i['hometown']}','{i['miles']}',
                                    '{i['considering']}',0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,''
                                )
                            """
                        )
                    recruitIDs += temp
                    if next == True:
                        # Click text=/.*Next \>\>.*/
                        page.click("text=/.*Next \>\>.*/")
                print(len(recruitIDs))
            db.close()
            