import ipaddress

# Validating an IP address (both ipv4 and ipv6)
try:
    print(ipaddress.ip_address(u'192.168.0.255'))
    print(ipaddress.ip_address(u'FFFF:9999:2:FDE:257:0:2FAE:112D'))
    print(ipaddress.ip_address(u'192.168.0.256'))
except ValueError as ve:
    print(f'An error of type "{ve}"')
except:
    print('Some other error occurred')

# Checking IP type
print(type(ipaddress.ip_address(u'192.168.0.255')))
print(ipaddress.ip_address(u'192.168.0.255').reverse_pointer)
print(ipaddress.ip_network(u'192.168.0.0/28'))

# Comparing IP addresses
print(ipaddress.ip_address(u'192.168.10.2') > ipaddress.ip_address(u'192.168.10.1'))
print(ipaddress.ip_address(u'192.168.100.1') == ipaddress.ip_address(u'192.168.100.0'))

# Performing some arithmetic
print(ipaddress.ip_address(u'192.168.0.0')+8)


