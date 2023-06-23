try:import  requests, threading, random, os
except:
    import os
os.system("color 0")
os.system("cls" if os.name == "nt" else "clear")
def check_proxy():
    class ProxyCheckerThread(threading.Thread):
        def run(self):
            while True:
                ip  = f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'
                url="http://103.195.236.167/a.html"
                if loai=="1":ok= {'http': f'{ip}:{port}'}#, 'https': f'{ip}:{port}'}
                elif loai == "2":ok = {'http': f'socks4://{ip}:{port}', 'https': f'socks4://{ip}:{port}'}
                elif loai == "3":ok = {'http': f'socks5://{ip}:{port}', 'https': f'socks5://{ip}:{port}'}
                try:
                    aa = requests.get(url, proxies=ok,timeout=out)
                except:
                    #print(f'[DIE] {ip}:{port}')
                    continue
                if aa.status_code == 200:
                    print(f'[LIVE] {ip}:{port}')
                    with open(f"{luu}.txt","a+") as f:f.write(f'{ip}:{port}\n')
                else:pass#print(f'[DIE] {ip}:{port}')
                
    
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
port = input("Cổng: ")
if port =="":exit("Không thể để trống")
try:out=int(input("Nhập time out (1 - 10), khuyến khích 5: "))
except:exit("Lỗi tham số đầu vào")
luu = input("Tên tệp lưu proxy LIVE (không cần nhập .txt): ")
if luu=="":exit("Không thể để trống")
print("\nRun...\n")
check_proxy()