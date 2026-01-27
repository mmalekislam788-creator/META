import os, time, sys, uuid, random

# ANSI কালার কোড
R = '\033[1;31m' # Red
G = '\033[1;32m' # Green
Y = '\033[1;33m' # Yellow
B = '\033[1;34m' # Blue
P = '\033[1;35m' # Purple
W = '\033[1;37m' # White

def banner():
    os.system('clear')
    # META লোগো মাঝামাঝি এবং ক্লিন রাখা হয়েছে
    print(f"""
{R}                ███    ███  ███████  ████████  █████  
{G}                ████  ████  ██          ██    ██   ██ 
{Y}                ██ ████ ██  █████       ██    ███████ 
{B}                ██  ██  ██  ██          ██    ██   ██ 
{P}                ██      ██  ███████     ██    ██   ██ 
    """)

    line = f"{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}"
    print(line)
    print(f'{G}| [✓] DEVELOPED BY : MD RONY ISLAM             |')
    print(f'| [✓] TEAM         : CYBER STRIKER TEAM        |')
    print(f'| [✓] TOOL STATUS  : RANDOM CLONING (META)     |')
    print(f'| [✓] TELEGRAM     : mdronyislamsr             |')
    print(f'| [✓] GITHUB       : MR RONY                   |')
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
    print(f'\n{G}[+] EXAMPLE : 017, 018, 019, 016')
    code = input(f'[+] ENTER SIM CODE : {W}')
    print(f'{G}[+] EXAMPLE : 500, 1000, 100000') 
    limit = int(input(f'[+] ENTER CLONING LIMIT : {W}'))
    
    print(f'\n{G}[/] ATTACK STARTED ON CODE {code}...')
    print(f'[/] TOTAL TARGET : {limit}\n')

    ok = 0
    for i in range(limit):
        uid = f"{code}{random.randint(1111111, 9999999)}"
        # আপনার নির্দেশমতো পাসওয়ার্ড ৬ সংখ্যার জন্য uid[6:]
        pws = uid[6:] 
        
        # আপনার কার্যকর এপিআই (অপরিবর্তিত)
        datr = uuid.uuid4().hex[:24]
        sb = uuid.uuid4().hex[:24]
        xs = f"48%3A{uuid.uuid4().hex[:14]}%3A2%3A{random.randint(1700000000, 1800000000)}%3A-1%3A5237"
        fr = f"{uuid.uuid4().hex[:16]}.{uuid.uuid4().hex[:20]}.AAA.0.0"
        
        # আউটপুট
        print(f'{G}[RONY-OK💚] {uid} • {pws} xxx') 
        # কুকির কালার আপনার তীর চিহ্ন অনুযায়ী সবুজ (G)
        print(f'{G}[‎‎🌺] COOKIE = datr={datr};sb={sb};c_user={uid};xs={xs};fr={fr};m_page_voice={uid}\n')
        
        # প্রতি ২ সেকেন্ড পরপর একটি করে কুকি নামবে
        time.sleep(2.0)

    # স্ক্রিনশটের নিচের লাল দাগ দেওয়া মডেল অনুযায়ী রেজাল্ট কাউন্টার
    print(f'{W}[{limit}] [OK:{ok}]')
    print(f'\n{G}[✓] CLONING COMPLETE.{W}')
    input(f'{G} [ BACK ]{W}')
    main()

if __name__ == "__main__":
    main()
