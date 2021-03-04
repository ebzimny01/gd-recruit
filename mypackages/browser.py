from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import re
import requests
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
        page.goto("https://idsrv.fanball.com/login?signin=2c7ce157635ba9eab815f3cb2bdb83ce&__cf_chl_jschl_tk__=748937e860f9dfc589364946f2e8af8c1eefbe7e-1614806310-0-AYX5rk621iTj_xPBtx5a9cubtsH4r7FR5uoSr4UmdL_BcUZKav9FAu1Wzybc7YI4a9N5Q7g_QAJzNzcOluUW-o99hqqOQQP1VkLwiP7W5DSaQYNqJBydxXiojR1tdAdzfnP6vQtkY42I0K7ngy-2AlArSUUiVG41fr4Y9rwHHatCLYPVhB3sTGZ17ZH8TCiXaNVC7pGYWav1fmxuY8lJ-iLb-ktGqxbLn8vV2EcrCNyZUzkeMk3ruMsoq0w-P_OTtzCltc-5vzq5SOKxnZyY84RvXRJai02utdOsiceCgMHsEWfVX0tNdHhq7tEW0lb4ABOTPwOkMuXX8WeczHUJHH35Lpxp0QzQ2QMuddSwXjS0vCfJTswNn8f8mAS_bP0GLcXHvOzXMVdD31TNyZvOUtKxmyYIoIHeKIDNZW3mvHtb")
    
        print("Authenticating to WIS...")
        
        # Click input[name="username"]
        page.click("input[name=\"username\"]")
        s = 0.50
        print(f"Sleeping for {s} seconds...")
        time.sleep(s)
        # Fill input[name="username"]
        page.fill("input[name=\"username\"]", user)
        s = 0.65
        print(f"Sleeping for {s} seconds...")
        time.sleep(s)
        # Click input[name="password"]
        page.click("input[name=\"password\"]")
        s = 0.75
        print(f"Sleeping for {s} seconds...")
        time.sleep(s)
        # Fill input[name="password"]
        page.fill("input[name=\"password\"]", pwd)
        s = 0.85
        print(f"Sleeping for {s} seconds...")
        time.sleep(s)
        # Click button:has-text("Sign in")
        page.click("button:has-text(\"Sign in\")")

        # assert page.url == "https://idsrv.fanball.com/localregistration/silentlogin"
        # Go to https://idsrv.fanball.com/connect/authorize?acr_values=ConfirmEmailRedirectUrl%3Ahttps%3A%2F%2Fwww.whatifsports.com%2Faccount%2F&client_id=what-if-sports&nonce=637504031099333772.MDgxYWM3M2ItN2FkYS00ZjdmLWJmNjctNTlmYjZjMmZiNTFmMTUxNjkwM2UtMzcyOC00NDQyLTgzN2QtMTc0NTkzMjlhOTIy&redirect_uri=https%3A%2F%2Fwww.whatifsports.com%2Faccount%2F&response_mode=form_post&response_type=id_token%20token&scope=openid%20profile%20social%20email%20wallet-readonly%20whatifsports-readonly%20connect-notifications-publish&state=OpenIdConnect.AuthenticationProperties%3DS-1Qk-uKkfLVgpGPcL7yB-qOVViBx8fSkGL7Z45PIM7qxFQ8hnUs9nxV0jVW2PaOGGLS7m8ACLhiygen6m72BjLQENcZU-F4LJPVQ4QhhO52NOkRA8b2wJRq-DCL8pmkb15Pdc6cX-L0X1Ij2WzzqSYsZNCaE2y--tRR7O1qVoVqIk7d34s6wbOA_D_jxH6lmTD_dQ7tVNHDL4lE7mXSYfJZQOsGG9zMBhctiqj8MxNpLAWQlBTDuaV0NrE--rx17vBEJg&x-client-SKU=ID_NET461&x-client-ver=5.4.0.0
        page.goto("https://idsrv.fanball.com/connect/authorize?acr_values=ConfirmEmailRedirectUrl%3Ahttps%3A%2F%2Fwww.whatifsports.com%2Faccount%2F&client_id=what-if-sports&nonce=637504031099333772.MDgxYWM3M2ItN2FkYS00ZjdmLWJmNjctNTlmYjZjMmZiNTFmMTUxNjkwM2UtMzcyOC00NDQyLTgzN2QtMTc0NTkzMjlhOTIy&redirect_uri=https%3A%2F%2Fwww.whatifsports.com%2Faccount%2F&response_mode=form_post&response_type=id_token%20token&scope=openid%20profile%20social%20email%20wallet-readonly%20whatifsports-readonly%20connect-notifications-publish&state=OpenIdConnect.AuthenticationProperties%3DS-1Qk-uKkfLVgpGPcL7yB-qOVViBx8fSkGL7Z45PIM7qxFQ8hnUs9nxV0jVW2PaOGGLS7m8ACLhiygen6m72BjLQENcZU-F4LJPVQ4QhhO52NOkRA8b2wJRq-DCL8pmkb15Pdc6cX-L0X1Ij2WzzqSYsZNCaE2y--tRR7O1qVoVqIk7d34s6wbOA_D_jxH6lmTD_dQ7tVNHDL4lE7mXSYfJZQOsGG9zMBhctiqj8MxNpLAWQlBTDuaV0NrE--rx17vBEJg&x-client-SKU=ID_NET461&x-client-ver=5.4.0.0")
        # Go to https://www.whatifsports.com/locker/lockerroom.asp
        print("Going to Lockerroom page...")
        page.goto("https://www.whatifsports.com/locker/lockerroom.asp")
        
        if "updateteams" in f:
            # page.goto("https://www.whatifsports.com/locker/lockerroom.asp")
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
                    createRecruitQuery.exec_(
                        f"""
                        INSERT INTO recruits(id,name,pos,height,weight,rating,
                            rank,hometown,miles,considering,ath,spd,dur,we,sta,str,
                            blk,tkl,han,gi,elu,tec,tot,gpa,pot)
                            VALUES('{temp['id']}','{temp['name']}','{temp['pos']}',
                                '{temp['height']}','{temp['weight']}','{temp['rating']}',
                                '{temp['rank']}','{temp['hometown']}','{temp['miles']}',
                                '{temp['considering']}',0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,''
                            )
                        """
                    )
                    recruitIDs += temp
                    if next == True:
                        # Click text=/.*Next \>\>.*/
                        page.click("text=/.*Next \>\>.*/")
                print(len(recruitIDs))
            db.close()
            