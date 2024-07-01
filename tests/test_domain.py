import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from domain import Domain

domain = Domain('testapi', 'testpass', test_mode=True)

def run_test(test_number):
    if test_number == 1:
        print("(1) Testing Domain/Check")
        response = domain.check_availability('pybs.com')
        print("Domain Check Status:", response.status)
        print("Domain Check Domain:", response.domain)
        print("Domain Check Minimum Registration Period:", response.minregperiod)
        print("Domain Check Maximum Registration Period:", response.maxregperiod)
        print("Domain Check Registrar Lock Allowed:", response.registrarlockallowed)
        print("Domain Check Private WHOIS Allowed:", response.privatewhoisallowed)
        print("Domain Check Real-Time Registration:", response.realtimeregistration)
    elif test_number == 2:
        print("(2) Testing Domain/Create")
        contacts = {
            'registrant': {
                'firstName': 'John', 
                'lastName': 'Doe', 
                'organization': 'PyBS Inc.',
                'email': 'john.doe@pybs.com',
                'phoneNumber': '+33.765151515',
                'street': '123 PyBS Street',
                'street2': 'Suite 100',
                'street3': '',
                'city': 'PyCity',
                'countryCode': 'US',
                'postalCode': '12345'
            },
            'admin': {
                'firstName': 'Jane', 
                'lastName': 'Doe', 
                'email': 'jane.doe@pybs.com',
                'phoneNumber': '+33.765151515',
                'street': '123 PyBS Street',
                'street2': 'Suite 100',
                'street3': '',
                'city': 'PyCity',
                'countryCode': 'US',
                'postalCode': '12345'
            },
            'technical': {
                'firstName': 'Tech', 
                'lastName': 'Support', 
                'email': 'tech.support@pybs.com',
                'phoneNumber': '+33.765151515',
                'street': '123 PyBS Street',
                'street2': 'Suite 100',
                'street3': '',
                'city': 'PyCity',
                'countryCode': 'US',
                'postalCode': '12345'
            },
            'billing': {
                'firstName': 'Bill', 
                'lastName': 'Pay', 
                'email': 'bill.pay@pybs.com',
                'phoneNumber': '+33.765151515',
                'street': '123 PyBS Street',
                'street2': 'Suite 100',
                'street3': '',
                'city': 'PyCity',
                'countryCode': 'US',
                'postalCode': '12345'
            }
        }
        response = domain.create_domain('pybs.com', contacts)        
        print("Transaction ID:", response.transactid)
        print("Status:", response.status)
        print("Currency:", response.currency)
        print("Price:", response.price)
        print("Product:", response.product)
    elif test_number == 3:
        print("(3) Testing Domain/Update")
        contacts = {
            'registrant': {'firstName': 'John', 'lastName': 'Does', 'email': 'john.doe@pybs.com'}
        }
        response = domain.update_domain('pybs.com', contacts)
        print("Status:", response.status)
        print("Message:", response.message)
    elif test_number == 4:
        print("(4) Testing Domain/GetInfo")
        response = domain.get_domain_info('pybs.com')
        print("Transaction ID:", response.transactid)
        print("Status:", response.status)
        print("Domain:", response.domain)
        print("Expiration Date:", response.expirationdate)
        print("Registration Date:", response.registrationdate)
        print("Paid Until:", response.paiduntil)
        print("Registrar Lock:", response.registrarlock)
        print("Auto Renew:", response.autorenew)
        print("Private WHOIS:", response.privatewhois)
        print("WHOIS Privacy:", response.whoisprivacy)
        print("Domain Status:", response.domainstatus)
        print("Contacts:", response.contacts)
        print("Transfer Auth Info:", response.transferauthinfo)
        print("DNSSEC:", response.dnssec)
        print("Price:", response.price)
    elif test_number == 5:
        print("(5) Testing Domain/GetRegistryStatus")
        response = domain.get_registry_status('pybs.com')
        print("Transaction ID:", response.transactid)
        print("Domain:", response.domain)
        print("Registry Status:", response.registrystatus)
        print("Status:", response.status)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_number = int(sys.argv[1])
    else:
        test_number = 1 
    run_test(test_number)
