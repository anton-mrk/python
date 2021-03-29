mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
result = []
for m in mac:
    result.append(m.replace(':', '.'))
print(result)

while True:
    ip = input('Введите IP-адрес в формате 10.0.1.1: ').split('.')
    correctly_ip = len(ip) == 4

    for a in ip:
        correctly_ip = a.isdigit() and 0 <= int(a) <= 255 and correctly_ip

    if correctly_ip:
        break
    print('Неправильный IP-адрес')

if int(ip[0]) in range(1, 224):
    print('unucast')
elif int(ip[0]) in range(224, 240):
    print('multicast')
elif int(ip[0]) and int(ip[1]) and int(ip[2]) and int(ip[3]) == 255:
    print('local broadcast')
elif int(ip[0]) and int(ip[1]) and int(ip[2]) and int(ip[3]) == 0:
    print('unassigned')
else:
    print('unused')
