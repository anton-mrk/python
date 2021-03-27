nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(nat.replace('Fast', 'Gigabit'))

mac = "AAAA:BBBB:CCCC"
print(mac.replace(':', '.'))

config = "switchport trunk allowed vlan 1,3,10,20,30,100"
result = config.split(' ')[-1].split(',')
print(result)

vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
result = sorted(set(vlans))
print(result)

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
result = sorted(set(command1.split(' ')[-1].split(',')) & set(command2.split(' ')[-1].split(',')))
print(result)

ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
temp = ospf_route.strip().split(' ') 
options = ('Prefix', 'AD/Metric', 'Next-Hot', 'Last update', 'Outbound Interface')
template = f'''
    {options[0]:<20} {temp[0]:<15}
    {options[1]:<20} {temp[1]:<15}
    {options[2]:<20} {temp[2]:<15}
    {options[3]:<20} {temp[3].rstrip(','):<15}
    {options[4]:<20} {temp[4].rstrip(','):<15}
    '''
print(template)

mac = "AAAA:BBBB:CCCC"
print(bin(int(mac.replace(':', '') ,16))[2:])

ip = "192.168.3.1"
temp = ip.split('.')
template = '''
    {0:<8}  {1:<8}  {2:<8} {3:<8}
    {0:08b}  {1:08b}  {2:08b} {3:08b}
    '''
print(template.format(int(temp[0]), int(temp[1]), int(temp[2]),int(temp[3])))