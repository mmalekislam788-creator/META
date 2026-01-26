import os, requests, time, sys, uuid

def banner():
    os.system('clear')
    # পিকের মতো বড় রঙিন META ব্যানার
    print('''\033[1;31m
    ███╗   ███╗███████╗████████╗ █████╗ 
    ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗
    ██╔████╔██║█████╗     ██║   ███████║
    ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║
    ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║
    ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝\033[0m''')

    # আপনার তথ্য অনুযায়ী ইনফরমেশন বক্স
    line = "\033[1;32m×××××××××××××××××××××××××××××××××××××××××××××\033[0m"
    print(line)
    print('\033[1;32m| [✓] DEVELOPED BY : MD MALEK ISLAM         |')
    print('| [✓] TEAM         : CYBER STRIKER TEAM     |')
    print('| [✓] TOOL STATUS  : RANDOM CLONING (META)  |')
    print('| [✓] TELEGRAM     : @md_malek              |')
    print('| [✓] GITHUB       : MR-MALAK               |')
    print('| [✓] TOOL VIRSION : MAX PRO                |')
    print(line)

def main():
    banner()
    # পিকের মতো মেনু ডিজাইন
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
    # আপনার চাহিদা অনুযায়ী সিম কোড এবং সংখ্যা ইনপুট
    print('\n\033[1;32m[+] EXAMPLE : 017, 018, 019, 016')
    code = input('[+] ENTER SIM CODE : \033[0m')
    
    print('\033[1;32m[+] EXAMPLE : 500, 1000, 5000')
    limit = int(input('[+] ENTER CLONING LIMIT : \033[0m'))
    
    print(f'\n\033[1;32m[✓] ATTACK STARTED ON CODE {code}...')
    print(f'[✓] TOTAL TARGET : {limit}\033[0m\n')
    
    # কুকি ক্লোনিং সিমুলেশন
    for i in range(limit):
        # এখানে আপনার এপিআই লজিক কাজ করবে
        time.sleep(0.1) 
        print(f'\033[1;32m[META-OK] {code}{uuid.uuid4().hex[:8]} | SUCCESS\033[0m')
        
        # কুকি টেক্সট ফাইলে সেভ করা
        with open("meta_cookies.txt", "a") as f:
            f.write(f"Code: {code} | ID: {i} | Status: Success\n")

    print('\n\033[1;32m[✓] CLONING COMPLETE. COOKIES SAVED.\033[0m')
    input('\033[1;32m[ BACK ]\033[0m')
    main()

if __name__ == "__main__":
    main()
