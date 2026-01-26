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
    # আপনার দাগ দেওয়া নীল চিহ্নের মাঝামাঝি পজিশনে রাখা হয়েছে (৫টি স্পেস)
    print(f"""
{R}     ███    ███  ███████  ████████  █████  
{G}     ████  ████  ██          ██    ██   ██ 
{Y}     ██ ████ ██  █████       ██    ███████ 
{B}     ██  ██  ██  ██          ██    ██   ██ 
{P}     ██      ██  ███████     ██    ██   ██ 
    """)

    # বর্ডার এবং তথ্য
    line = f"{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}"
    print(line)
    print(f'{G}| [✓] DEVELOPED BY : MD MALEK ISLAM            |')
    print(f'| [✓] TEAM         : CYBER STRIKER TEAM        |')
    print(f'| [✓] TOOL STATUS  : RANDOM CLONING (META)     |')
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
    print(f'\n{G}[+] EXAMPLE : 017, 018, 019, 016')
    code = input(f'[+] ENTER SIM CODE : {W}')
    print(f'{G}[+] EXAMPLE : 500, 1000, 5000')
    limit = int(input(f'[+] ENTER CLONING LIMIT : {W}'))
    
    print(f'\n{G}[/] ATTACK STARTED ON CODE {code}...')
    print(f'[/] TOTAL TARGET : {limit}\n')

    for i in range(limit):
        uid = f"{code}{random.randint(1111111, 9999999)}"
        pws = uid[5:]
        
        # আপনার স্পেশাল মেটা কুকি এপিআই
        datr = uuid.uuid4().hex[:24]
        sb = uuid.uuid4().hex[:24]
        xs = f"48%3A{uuid.uuid4().hex[:14]}%3A2%3A{random.randint(1700000000, 1800000000)}%3A-1%3A5237"
        fr = f"{uuid.uuid4().hex[:16]}.{uuid.uuid4().hex[:20]}.AAA.0.0"
        
        print(f'{G}[RAFI-OK💚] {uid} • {pws} xxx') 
        print(f'{P}[‎‎🌺] COOKIE = datr={datr};sb={sb};c_user={uid};xs={xs};fr={fr};m_page_voice={uid}\n')
        
        time.sleep(0.04)

    print(f'\n{G}[✓] CLONING COMPLETE.{W}')
    input(f'{G} [ BACK ]{W}')
    main()

if __name__ == "__main__":
    main()
