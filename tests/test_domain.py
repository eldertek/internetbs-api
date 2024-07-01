import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../internetbs')))
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
                'dotfrcontactentitytype': 'individual',
                'street': '123 PyBS Street',
                'street2': 'Suite 100',
                'street3': '',
                'city': 'PyCity',
                'countryCode': 'FR',
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
                'countryCode': 'FR',
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
                'countryCode': 'FR',
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
                'countryCode': 'FR',
                'postalCode': '12345'
            }
        }
        response = domain.create_domain('pyb1562s.fr', contacts)        
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
    elif test_number == 6:
        print("(6) Testing Domain/InitiateTransfer")
        contacts = {
            'registrant': {'firstName': 'John', 'lastName': 'Doe', 'email': 'john.doe@pybs.com'}
        }
        response = domain.initiate_transfer('pybs.com', 'authcode123', contacts)
        print("Status:", response['status'])
        print("Message:", response.get('message', ''))
    elif test_number == 7:
        print("(7) Testing Domain/RetryTransfer")
        response = domain.retry_transfer('pybs.com')
    elif test_number == 8:
        print("(8) Testing Domain/CancelTransfer")
        response = domain.cancel_transfer('pybs.com')
        print("Status:", response['status'])
        print("Message:", response.get('message', ''))
    elif test_number == 9:
        print("(9) Testing Domain/ResendTransferAuthEmail")
        response = domain.resend_transfer_auth_email('pybs.com')
        print("Status:", response['status'])
        print("Message:", response.get('message', ''))
    elif test_number == 10:
        print("(10) Testing Domain/GetTransferHistory")
        response = domain.get_transfer_history('pybs.com')
        print("Status:", response['status'])
        print("History:", response.get('history', ''))
    elif test_number == 11:
        print("(11) Testing Domain/ApproveTransferAway")
        response = domain.approve_transfer_away('pybs.com')
        print("Status:", response['status'])
        print("Message:", response.get('message', ''))
    elif test_number == 12:
        print("(12) Testing Domain/RejectTransferAway")
        response = domain.reject_transfer_away('pybs.com')
        print("Status:", response['status'])
        print("Message:", response.get('message', ''))
    elif test_number == 13:
        print("(13) Testing Domain/Trade")
        contacts = {
            'registrant': {'firstName': 'John', 'lastName': 'Doe', 'email': 'john.doe@pybs.com'}
        }
        response = domain.trade_domain('pybs.com', contacts)
        print("Status:", response['status'])
        print("Message:", response.get('message', ''))
    elif test_number == 14:
        print("(14) Testing Domain/EnableRegistrarLock")
        response = domain.enable_registrar_lock('pybs.com')
        print("Status:", response['status'])
        print("Message:", response.get('message', ''))
    elif test_number == 15:
        print("(15) Testing Domain/DisableRegistrarLock")
        response = domain.disable_registrar_lock('pybs.com')
        print("Status:", response['status'])
        print("Message:", response.get('message', ''))
    elif test_number == 16:
        print("(16) Testing Domain/GetRegistrarLockStatus")
        response = domain.get_registrar_lock_status('pybs.com')
        print("Status:", response['status'])
        print("Registrar Lock Status:", response.get('registrarlockstatus', ''))
    elif test_number == 17:
        print("(17) Testing Domain/EnablePrivateWhois")
        response = domain.enable_private_whois('pybs.com')
        print("Status:", response['status'])
        print("Message:", response.get('message', ''))
    elif test_number == 18:
        print("(18) Testing Domain/DisablePrivateWhois")
        response = domain.disable_private_whois('pybs.com')
        print("Status:", response['status'])
        print("Message:", response.get('message', ''))
    elif test_number == 19:
        print("(19) Testing Domain/GetPrivateWhoisStatus")
        response = domain.get_private_whois_status('pybs.com')
        print("Status:", response['status'])
        print("Private WHOIS Status:", response.get('privatewhoisstatus', ''))
    elif test_number == 20:
        print("(20) Testing Domain/Push")
        response = domain.push_domain('pybs.com', 'target_account')
        print("Status:", response['status'])
        print("Message:", response.get('message', ''))
    elif test_number == 21:
        print("(21) Testing Domain/ChangeTagUK")
        response = domain.change_tag_uk('pybs.com', 'new_tag')
        print("Status:", response['status'])
        print("Message:", response.get('message', ''))
    elif test_number == 22:
        print("(22) Testing Domain/List")
        domains = domain.list_domains()
        for domain_item in domains:
            print("Domain:", domain_item.domain_name)
    elif test_number == 23:
        print("(23) Testing Domain/Renew")
        response = domain.renew_domain('pybs.com')
        print("Status:", response['status'])
        print("Message:", response.get('message', ''))
    elif test_number == 24:
        print("(24) Testing Domain/Restore")
        response = domain.restore_domain('pybs.com')
        print("Status:", response['status'])
        print("Message:", response.get('message', ''))
    elif test_number == 25:
        print("(25) Testing Domain/Count")
        response = domain.count_domains()
        print("Status:", response['status'])
        print("Count:", response.get('count', ''))
    elif test_number == 26:
        print("(26) Testing Domain/GetRegistrantVerificationInfo")
        response = domain.get_registrant_verification_info('pybs.com')
        print("Status:", response['status'])
        print("Verification Info:", response.get('verificationinfo', ''))
    elif test_number == 27:
        print("(27) Testing Domain/StartRegistrantVerification")
        response = domain.start_registrant_verification('pybs.com')
        print("Status:", response['status'])
        print("Message:", response.get('message', ''))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_number = int(sys.argv[1])
    else:
        test_number = 1 
    run_test(test_number)
