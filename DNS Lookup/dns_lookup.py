import dns.resolver as dnsres

# Finding 'A' record, CNAME record and MX record
a_result=dnsres.resolve('carata.co.ke','A')
cname_result=dnsres.resolve('carata.co.ke','CNAME')
mx_result=dnsres.resolve('carata.co.ke','MX')

# Iterating through the results and displaying them
for ip_val in a_result:
    print('IP : ', ip_val.to_text())
for domain_name in cname_result:
    print('Domain name : ', domain_name.target)
for email_address in mx_result:
    print('Email address : ',email_address.exchange.text())

