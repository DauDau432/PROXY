try:
    import requests
    import threading
    import random
    import os
except ImportError:
    try:
        import os
        os.system('pip install requests')
        exit('Hay bat lai tools')
    except ImportError:
        exit('Khong the cai dat goi requests')

os.system("color 0")
os.system("cls" if os.name == "nt" else "clear")

with open('day_ip_vietnam.txt') as f:
    proxy_list = f.read().splitlines()


def random_ip_vietnam(proxy_list):
    q1 = random.choice(proxy_list).split('|')[0].split('.0')[0]
    return '{}.{}'.format(q1, random.randint(1, 255))


def random_port():
    list_port = ['80', '80', '80', '80', '80', '80', '80', '80', '443', '443', '443', '443', '443', '8888', '8888', '8080', '8080']
    return random.choice(list_port)


def check_proxy():
    class ProxyCheckerThread(threading.Thread):
        def run(self):
            while True:
                proxy = '{}:{}'.format(random_ip_vietnam(proxy_list), random_port())
                if loai == "1":
                    ok = {'http': proxy}
                elif loai == "2":
                    ok = {'http': 'socks4://{}'.format(proxy), 'https': 'socks4://{}'.format(proxy)}
                elif loai == "3":
                    ok = {'http': 'socks5://{}'.format(proxy), 'https': 'socks5://{}'.format(proxy)}
                try:
                    aa = requests.get('http://103.195.236.167/a.html', proxies=ok, timeout=out)
                except:
                    print('[DIE] {}'.format(proxy))
                    continue
                if aa.status_code == 200:
                    print('[LIVE] {}'.format(proxy))
                    with open('{}.txt'.format(luu), "a+") as f:
                        f.write('{}\n'.format(proxy))
                else:
                    print('[DIE] {}'.format(proxy))

    num_threads = luong
    for i in range(num_threads):
        thread = ProxyCheckerThread()
        thread.start()


loai = raw_input("[1] HTTP(s)\n[2] SOCKS4\n[3] SOCKS5\nChon: ")
if loai == "1" or loai == "2" or loai == "3":
    pass
else:
    exit("Vui long chon 1 trong 3")
try:
    luong = int(raw_input("Nhap so luong: "))
except ValueError:
    exit("Loi tham so dau vao")
if luong == "":
    exit("khong the de trong")
try:
    out = int(raw_input("Nhap time out (1 - 10), khuyen khich 5: "))
except ValueError:
    exit("Loi tham so dau vao")
luu = raw_input("Ten file luu proxy live (.txt): ")
if luu == "":
    exit("khong the de trong")
print("\nRun...\n")
check_proxy()
