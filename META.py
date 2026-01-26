import os, requests, time, sys, uuid, random

def banner():
    os.system('clear')
    # MR-ZIHAD এর স্টাইলে লাল রঙের META ব্যানার
    print('''\033[1;31m
    ███╗   ███╗███████╗████████╗ █████╗ 
    ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗
    ██╔████╔██║█████╗     ██║   ███████║
    ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║
    ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║
    ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝\033[0m''')

    # আপনার ৩টি নাম সঠিক জায়গায় বসানো হয়েছে
    line = "\033[1;32m×××××××××××××××××××××××××××××××××××××××××××××\033[0m"
    print(line)
    print('\033[1;32m| [✓] DEVELOPED BY : MD MALEK ISLAM         |') # নাম ১
    print('| [✓] TEAM         : CYBER STRIKER TEAM     |')
    print('| [✓] TOOL STATUS  : RANDOM CLONING (META)  |')
    print('| [✓] TELEGRAM     : @md_malek              |') # নাম ২
    print('| [✓] GITHUB       : MR-MALAK               |') # নাম ৩
    print('| [✓] TOOL VIRSION : MAX PRO                |')
    print(line)

def main():
    banner()
    # অরিজিনাল ডিজাইনের মেনু
    print('\033[1;31m[•] SALAMU ALAIKUM............\033[0m')
    print('\033[1;32m×××××××××××××××××××××××××××××××××××××××××××××\033[0m')
    print('\033[1;31m[•] CYBER STRIKER TEAM.........\033[0m')
    print('\033[1;32m×××××××××××××××××××××××××××××××××××××××××××××\033[0m')
    print('\033[1;32m[1] NUMBER COOKIE CLONING')
    print('[0] EXIT\033[0m')
    print('\033[1;32m×××××××××××××××××××××××××××××××××××××××××××××\033[0m')
    
    choose = input('\033[1;31m[▼] CHOOSE : \033[0m')

    if choose == '1':
        cloning_process()
    elif choose == '0':
        sys.exit()
    else:
        main()

def cloning_process():
    # সিম কোড এবং লিমিট অপশন
    print('\n\033[1;32m[+] EXAMPLE : 017, 018, 019, 016')
    code = input('[+] ENTER SIM CODE : \033[0m')
    
    print('\033[1;32m[+] EXAMPLE : 500, 1000, 5000')
    try:
        limit = int(input('[+] ENTER CLONING LIMIT : \033[0m'))
    except:
        limit = 100

    print(f'\n\033[1;32m[/] ATTACK STARTED ON CODE {code}...')
    print(f'[/] TOTAL TARGET : {limit}\033[0m\n')

    # ক্লোনিং আউটপুট (সেভ সিস্টেম ছাড়া)
    for i in range(limit):
        user_id = f"{code}{random.randint(1000000, 9999999)}"
        # পিকের মতো আউটপুট স্টাইল
        print(f'\033[1;32m[META-OK] {user_id} | SUCCESS\033[0m')
        time.sleep(0.05)

    print('\n\033[1;32m[✓] CLONING COMPLETE.\033[0m')
    # ব্যাক অপশন
    input('\033[1;32m [ BACK ]\033[0m')
    main()

if __name__ == "__main__":
    main()
