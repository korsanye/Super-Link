try:
    import urllib
    from selenium import webdriver
    from termcolor import colored as cl
    import time
    try:
        print(cl("\n\t\tplease wait\n\n","red"))
        time.sleep(1)
        print(cl("===================================================","blue"))
        time.sleep(0.5)
        print(cl("===================================================","red"))
        time.sleep(0.5)
        print(cl("===================================================","blue"))
        time.sleep(0.5)
        print(cl(""" ____  _            _            ___   ___  _ ""","red"))
        time.sleep(0.5)
        print(cl("""| __ )| | __ _  ___| | __  _ __ / _ \ / _ \| |_ ""","blue"))
        time.sleep(0.5)
        print(cl("""|  _ \| |/ _` |/ __| |/ / | '__| | | | | | | __|""","red"))
        time.sleep(0.5)
        print(cl("""| |_) | | (_| | (__|   <  | |  | |_| | |_| | |_ ""","blue"))
        time.sleep(0.5)
        print(cl("""|____/|_|\__,_|\___|_|\_\ |_|   \___/ \___/ \__|""","red"))
        time.sleep(0.5)
        print(cl("===================================================","blue"))
        time.sleep(0.5)
        print(cl("===================================================","red"))
        time.sleep(0.5)
        print(cl("===================================================","blue"))
        time.sleep(0.5)
        print(cl("""
            \t\tSuper Link\n
            [1] get source codes
            [2] Open the link in your browser
            ""","blue"))
        number = input(cl("Enter the number >>: ","blue"))
    #######################################################################################################################################################################
        if number == 1:
            link = raw_input(cl("Enter the link + http or https >>: ","blue"))
            url = urllib
            golink = url.urlopen(link)
            print(cl(golink.geturl(),"red"))
            if "demos/basic.html" in golink.geturl():
                print (cl("This is a tool beef to hack your browser","red"))
            codePage = golink.read()
            page = (open("page.html","w"))
            page.write(codePage)
            page.close()
            print(cl("[+]Finished saving page.html","blue"))
    #######################################################################################################################################################################
        elif number == 2:
            link = raw_input(cl("Enter the link + http or https >>: ","blue"))
            profile = webdriver.FirefoxProfile()
            system = input(cl("""
                            [1]ios
                            [2]android
                            [3]windows
                            [4]linux
                            [5]mac
                            [6]BlackBerry
                            [7]Windows Phone
                            You want to open a link across any system >>: ""","red"))
            if system == 1:
                profile.set_preference("general.useragent.override","Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1")
                web = webdriver.Firefox(profile)
                web.get(link)
            elif system == 2:
                profile.set_preference("general.useragent.override","Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko; googleweblight) Chrome/38.0.1025.166 Mobile Safari/535.19")
                web = webdriver.Firefox(profile)
                web.get(link)
            elif system == 3:
                profile.set_preference("general.useragent.override","Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)")
                web = webdriver.Firefox(profile)
                web.get(link)
            elif system == 4:
                profile.set_preference("general.useragent.override","Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.3.0")
                web = webdriver.Firefox(profile)
                web.get(link)
            elif system == 5:
                profile.set_preference("general.useragent.override","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7")
                web = webdriver.Firefox(profile)
                web.get(link)
            elif system == 6:
                profile.set_preference("general.useragent.override","BlackBerry8520/5.0.0.592 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/168")
                web = webdriver.Firefox(profile)
                web.get(link)
            elif system == 7:
                profile.set_preference("general.useragent.override","Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; NOKIA; Lumia 710)")
                web = webdriver.Firefox(profile)
                web.get(link)
    #######################################################################################################################################################################
    except KeyboardInterrupt:
        print(cl("Bye","red"))
except ImportError:
        print("install selenium v2.53.6 , termcolor \n\tpip install selenium==2.53.6\n\tpip install termcolor")
