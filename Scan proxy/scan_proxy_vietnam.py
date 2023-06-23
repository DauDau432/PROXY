try:import  requests, threading, random, os
except:
    import os
os.system("color 0")
os.system("cls" if os.name == "nt" else "clear")
with open('day_ip_vietnam.txt') as f:
    proxy_list = f.read().splitlines()
def random_ip_vietnam(proxy_list):
    q1 = random.choice(proxy_list).split('|')[0].split('.0')[0]
    return f'{q1}.{random.randint(1, 255)}'
def random_port():
    list_port=['80','32650','53281','1433','4015','1337','41477','1911','50003','3128','41401','41497','443','8888','11218','8080','19132'
    ]
    # for ok in range(5000, 7001):
    #     list_port.append(ok)
    return random.choice(list_port)


def check_proxy():
    class ProxyCheckerThread(threading.Thread):
        def run(self):
            while True:
                proxy  = f'{random_ip_vietnam(proxy_list)}:{random_port()}'
                if loai=="1":ok= {'http': proxy}
                elif loai == "2":ok = {'http': f'socks4://{proxy}', 'https': f'socks4://{proxy}'}
                elif loai == "3":ok = {'http': f'socks5://{proxy}', 'https': f'socks5://{proxy}'}
                try:
                    aa = requests.get('http://103.195.236.167/a.html', proxies=ok,timeout=out)
                except:
                    print(f'[DIE] {proxy}')
                    continue
                if aa.status_code == 200:
                    print(f'[LIVE] {proxy}')
                    with open(f"{luu}.txt","a+") as f:f.write(f'{proxy}\n')
                else:print(f'[DIE] {proxy}')
                
    
    num_threads = luong
    for i in range(num_threads):
        thread = ProxyCheckerThread()
        thread.start()


loai=input("[1] HTTP(s)\n[2] SOCKS4\n[3] SOCKS5\nChọn: ")
if loai=="1" or loai =="2" or loai=="3":pass
else:exit("Vui lòng chọn 1 trong 3")
try:luong=int(input("Nhập số luồng: "))
except:exit("Lỗi tham số đầu vào")
if luong=="":exit("Không thể để trống")
try:out=int(input("Nhập time out(1 - 10), khuyến khích 5: "))
except:exit("Lỗi tham số đầu vào")
luu = input("Tên tệp lưu proxy sống (.txt): ")
if luu=="":exit("Không thể để trống")
print("\nRun...\n")
check_proxy()




