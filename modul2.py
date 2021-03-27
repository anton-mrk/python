london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}

device = input('Введите имя устройства: ')
temp = str(london_co[device].keys())
option = input('Введите имя параметра ' + temp.strip('([])')[11:] + ': ')
print(london_co[device].get(option.lower(), 'Такого параметра нет'))

ip_net = input('Введите IP-сеть в формате 10.1.1.1/24: ')
ip, subnet = ip_net.split('/')
bit_mask = "1" * int(subnet) + "0" * (32 - int(subnet)) 
temp = ip.split('.')
template = '''
    Network:
    {0:<8}  {1:<8}  {2:<8} {3:<8}
    {0:08b}  {1:08b}  {2:08b} {3:08b}

    Mask:
    /{4}
    {5:<8}  {6:<8}  {7:<8} {8:<8}
    {5:<08b}  {6:<08b}  {7:<08b} {8:<08b}
    '''
print(template.format(int(temp[0]), int(temp[1]), int(temp[2]), int(temp[3]), subnet, int(bit_mask[0:8], 2), int(bit_mask[8:16], 2), int(bit_mask[16:24], 2), int(bit_mask[24:32], 2)))

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

trunk_template = [
    "switchport trunk encapsulation dot1q", 
    "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]

template = {'access' : access_template, 'trunk' : trunk_template}
template2 = {'access' : 'Введите номер VLAN: ', 'trunk': 'Введите разрешенные VLANы: '}

switchport = input('Введите режим работы интерфейса (access/trunk): ')
interface = input('Введите тип и номер интерфейса: ')
vlan = input(template2[switchport])

print('interface {}'.format(interface))
print('switchport {}'.format(switchport))
print('\n'.join(template[switchport]).format(vlan))
