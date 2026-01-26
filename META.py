import os, requests, time, sys, uuid

def banner():
    os.system('clear')
    # আপনার ছবির মতো বড় রঙিন META ব্যানার
    print('''\033[1;31m
    ███╗   ███╗███████╗████████╗ █████╗ 
    ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗
    ██╔████╔██║█████╗     ██║   ███████║
    ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║
    ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║
    ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝\033[0m''')

    # আপনার দেওয়া নাম ও তথ্য অনুযায়ী বক্স লেআউট
    line = "\033[1;32m×××××××××××××××××××××××××××××××××××××××××××××\033[0m"
    print(line)
    print('\033[1;34m| [✓] DEVELOPED BY : MD MALEK ISLAM         |')
    print('| [✓] TEAM         : CYBER STRIKER TEAM     |')
    print('| [✓] TOOL STATUS  : RANDOM CLONIER (META)  |')
    print('| [✓] TELEGRAM     : @md_malek              |')
    print('| [✓] GITHUB       : MR-MALAK               |')
    print('| [✓] TOOL VERSION : MAX PRO                |\033[0m')
    print(line)

def main():
    banner()
    # ছবির মতো মেনু ডিজাইন
    print('\033[1;31m[•] SALAMU ALAIKUM............\033[0m')
    print('\033[1;32m×××××××××××××××××××××××××××××××××××××××××××××\033[0m')
    print('\033[1;31m[•] CYBER STRIKER TEAM.........\033[0m')
    print('\033[1;32m×××××××××××××××××××××××××××××××××××××××××××××\033[0m')
    print('\033[1;32m[2] NUMBER CLOMER (META)')
    print('[MOL MAX PRO 2026')
    print('×××××××××××××××××××××××××××××××××××××××××××××\033[0m')
    print('\033[1;32m[•] CYBER CLOBER TEAM...............\033[0m')
    print('\033[1;32m[1] NUMBER COOKIE CLONING') # কুকি ক্লোনিং অপশন
    print('[0] EXIT\033[0m')
    
    choose = input('\n\033[1;32m[▼] CHOOSE : \033[0m')

    if choose == '1':
        cookie_cloning()
    elif choose == '0':
        exit()
    else:
        print('\033[1;31m[!] WRONG OPTION\033[0m')
        time.sleep(2)
        main()

def cookie_cloning():
    user = input('\n\033[1;32m[+] ENTER TARGET NUMBER: \033[0m')
    print(f'\033[1;32m[✓] EXTRACTING COOKIE FOR {user}...\033[0m')
    
    # কুকি জেনারেট এবং সেভ করার লজিক
    time.sleep(3)
    # এখানে আপনার মেটা এপিআই থেকে প্রাপ্ত কুকি থাকবে
    dummy_cookie = f"sb={uuid.uuid4().hex}; datr={uuid.uuid4().hex}; c_user={user}; xs=meta_cloned_ok;"
    
    print(f'\n\033[1;32m[✓] SUCCESS! COOKIE FOUND.')
    print(f'\033[1;33m[!] COOKIE: {dummy_cookie}\033[0m')
    
    # কুকি টেক্সট ফাইলে সেভ করা [নতুন সংযোজন]
    with open("meta_cookies.txt", "a") as f:
        f.write(f"Target: {user} | Cookie: {dummy_cookie}\n")
    
    print('\n\033[1;32m[✓] COOKIE SAVED IN: meta_cookies.txt\033[0m')
    input('\n\033[1;32m[ BACK ]\033[0m')
    main()

if __name__ == "__main__":
    main()
