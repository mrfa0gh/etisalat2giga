#اتصالات2جيجا اوبن سورس م ش مشفر

#@mrfa0gh
import webbrowser
import requests
import base64
from datetime import datetime,timedelta 


def x4lwash():
    number = input("Enter Your Number : ")
    print("-"*69)
    password = input("ENTER Your Password : ")
    print("\033[1;33m" + "-"*69 + "\033[0m")
    email = input("mENTER Your Email :")
    print("\033[1;33m" + "-"*44 + "\033[0m")

    if "011" in number:
        num = number[+1:]
    else:
        num = number
    
    code = email + ":" + password
    ccode = code.encode("ascii")
    base64_bytes = base64.b64encode(ccode)
    auth = base64_bytes.decode("ascii")
    xauth = "Basic" + " " + auth

    urllog = "https://mab.etisalat.com.eg:11003/Saytar/rest/authentication/loginWithPlan"

    headerslog = {
        "applicationVersion": "2",
        "applicationName": "MAB",
        "Accept": "text/xml",
        "Authorization": xauth,
        "APP-BuildNumber": "964",
        "APP-Version": "27.0.0",
        "OS-Type": "Android",
        "OS-Version": "12",
        "APP-STORE": "GOOGLE",
        "Is-Corporate": "false",
        "Content-Type": "text/xml; charset=UTF-8",
        "Content-Length": "1375",
        "Host": "mab.etisalat.com.eg:11003",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/5.0.0-alpha.11",
        "ADRUM_1": "isMobile:true",
        "ADRUM": "isAjax:true"
    }

    datalog = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><loginRequest><deviceId></deviceId><firstLoginAttempt>true</firstLoginAttempt><modelType></modelType><osVersion></osVersion><platform>Android</platform><udid></udid></loginRequest>"
    log = requests.post(urllog, headers=headerslog, data=datalog)

    
    if "true" in log.text:
        st = log.headers["Set-Cookie"]
        ck = st.split(";")[0]
        br = log.headers["auth"]

        url22 = 'https://mab.etisalat.com.eg:11003/Saytar/rest/General/submitOrder'

        headers22 = {
            'applicationVersion': '2',
            'applicationName': 'MAB',
            'Accept': 'text/xml',
            'Cookie': ck,
            'Language': 'ar',
            'APP-BuildNumber': '10493',
            'APP-Version': '30.1.0',
            'OS-Type': 'Android',
            'OS-Version': '7.1.1',
            'APP-STORE': 'GOOGLE',
            'auth': "Bearer " + br,
            'Is-Corporate': 'false',
            'Content-Type': 'text/xml; charset=UTF-8',
            'Content-Length': '316',
            'Host': 'mab.etisalat.com.eg:11003',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/5.0.0-alpha.11',
            'ADRUM_1': 'isMobile:true',
            'ADRUM': 'isAjax:true'
        }

        data22 = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><generalSubmitOrderRequest><category></category><contactDial></contactDial><msisdn>%s</msisdn><operation>ACTIVATE</operation><passParameters /><productName>SNAPCHAT_APP_OFFER</productName><requestId></requestId><type></type></generalSubmitOrderRequest>"%(num)

        response = requests.post(url22, headers=headers22, data=data22).text
        
        if "true" in response:
            trx = "2Giga Added "
            print("\033[1;31m" + trx.center(49) + "\033[0m")
        else:
            print("Check Your Data")    


x4lwash()

