import requests, os, time, uuid

def start():
    os.system('clear')
    
    # আপনার স্ক্রিনশটের মতো রঙিন META ব্যানার
    print('''\033[1;31m
    ███╗   ███╗███████╗████████╗ █████╗ 
    ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗
    ██╔████╔██║█████╗     ██║   ███████║
    ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║
    ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║
    ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝\033[0m''')

    # আপনার তথ্য অনুযায়ী বক্স লেআউট
    line = "\033[1;32m×××××××××××××××××××××××××××××××××××××××××××××\033[0m"
    print(line)
    print('\033[1;34m| [✓] DEVELOPED BY : MD MALEK ISLAM         |')
    print('| [✓] GITHUB       : MR-MALAK               |')
    print('| [✓] TELEGRAM     : @md_malek              |')
    print('| [✓] TOOL STATUS  : META DATA EXTRACT      |')
    print('| [✓] TOOL VERSION : MAX PRO 2026           |\033[0m')
    print(line)

    # কি (Key) ফরম্যাট
    u_key = str(uuid.uuid4())[:8]
    print(f'\033[1;32m[▼] KEY : {u_key}-MR-MALAK\033[0m')
    print(line)

    # কুকি নামানোর জন্য ইনপুট অপশন
    print('\n\033[1;32m[1] EXTRACT COOKIE FROM META')
    print('[2] LOGIN WITH COOKIE')
    print('[0] EXIT\033[0m')
    
    choice = input('\n\033[1;32m[+] CHOOSE : \033[0m')

    if choice == '1':
        user = input('\033[1;32m[+] USERNAME/ID: \033[0m')
        pasw = input('\033[1;32m[+] PASSWORD: \033[0m')
        print(f'\n\033[1;32m[✓] EXTRACTING COOKIE FOR ==> {user}...')
        # এখানে আপনার কুকি এক্সট্রাকশন লজিক কাজ করবে
        time.sleep(3)
        print('\033[1;31m[!] ERROR: PLEASE ATTACH YOUR FB-COOKIE API\033[0m')
    else:
        print('\033[1;31m[!] EXITING...\033[0m')

if __name__ == "__main__":
    start()
