ip_adress = input('入力＞ ').split('.')

for ip in range(len(ip_adress)):
    hoge = hex(int(ip_adress[ip]))[2:].upper()
    if hoge == '0':
        hoge = '00'
    ip_adress[ip] = hoge

print(':'.join(ip_adress))
