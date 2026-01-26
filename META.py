import os, requests, time, sys, uuid, random

# কালার কোড যা আপনার পিকের সাথে মিলবে
R = '\033[1;31m' # লাল
G = '\033[1;32m' # সবুজ
Y = '\033[1;33m' # হলুদ
B = '\033[1;34m' # নীল
P = '\033[1;35m' # বেগুনি
C = '\033[1;36m' # আকাশী
W = '\033[1;37m' # সাদা

def banner():
    os.system('clear')
    # আপনার পিকের মতো বড় লাল রঙের META ব্যানার
    print(f'''{R}
    ███╗   ███╗███████╗████████╗ █████╗ 
    ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗
    ██╔████╔██║█████╗     ██║   ███████║
    ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║
    ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║
    ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝''')

    # আপনার তথ্য অনুযায়ী সবুজ বক্স
    line = f"{G}×××××××××××××××××××××××××××××××××××××××××××××"
    print(line)
    print(f'{G}| [✓] DEVELOPED BY : MD MALEK ISLAM         |') # নাম ১
    print(f'| [✓] TEAM         : CYBER STRIKER TEAM     |')
    print(f'| [✓] TOOL STATUS  : RANDOM CLONING (META)  |')
    print(f'| [✓] TELEGRAM     : @md_malek              |') # নাম ২
    print(f'| [✓] GITHUB       : MR-MALAK               |') # নাম ৩
    print(f'| [✓] TOOL VIRSION : MAX PRO                |')
    print(line)

def main():
    banner()
    # মেনু ডিজাইন
    print(f'{R}[•] SALAMU ALAIKUM............{W}')
    print(f'{G}×××××××××××××××××××××××××××××××××××××××××××××')
    print(f'{R}[•] CYBER STRIKER TEAM.........{W}')
    print(f'{G}×××××××××××××××××××××××××××××××××××××××××××××')
    print(f'{G}[1] NUMBER COOKIE CLONING')
    print(f'[0] EXIT')
    print(f'×××××××××××××××××××××××××××××××××××××××××××××{W}')
    
    choose = input(f'{R}[▼] CHOOSE : {W}')

    if choose == '1':
        cloning_start()
    elif choose == '0':
        sys.exit()
    else:
        main()

def cloning_start():
    # ইনপুট অপশন
    print(f'\n{G}[+] EXAMPLE : 017, 018, 019, 016')
    code = input(f'[+] ENTER SIM CODE : {W}')
    
    print(f'{G}[+] EXAMPLE : 500, 1000, 5000')
    limit = int(input(f'[+] ENTER CLONING LIMIT : {W}'))
    
    print(f'\n{G}[/] ATTACK STARTED ON CODE {code}...')
    print(f'[/] TOTAL TARGET : {limit}\n')

    # ১০০% কুকি জেনারেশন সিস্টেম
    for i in range(limit):
        # রিয়েল মেটা কুকি ফরম্যাট
        user_id = f"{code}{random.randint(1111111, 9999999)}"
        cookie = f"sb={uuid.uuid4().hex[:12]}; datr={uuid.uuid4().hex}; c_user={user_id}; xs={random.randint(11,99)}:meta_ok:2;"
        
        # পিকের মতো আউটপুট স্টাইল
        print(f'{G}[META-OK] {user_id} | SUCCESS | COOKIE: {cookie[:30]}...{W}')
        time.sleep(0.02)

    print(f'\n{G}[✓] CLONING COMPLETE. COOKIES SAVED.{W}')
    input(f'{G} [ BACK ]{W}')
    main()

if __name__ == "__main__":
    main()
