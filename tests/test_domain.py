import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../internetbs')))
from domain import Domain

domain = Domain('testapi', 'testpass', test_mode=True)

def run_test(test_number):
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
    
    test_cases = [
        (1, "Domain/Check", lambda: domain.check_availability('pybs.fr')),
        (2, "Domain/Create", lambda: domain.create_domain('pyb1562s.fr', contacts)),
        (3, "Domain/Update", lambda: domain.update_domain('pybs.com', contacts)),
        (4, "Domain/GetInfo", lambda: domain.get_domain_info('pybs.com')),
        (5, "Domain/GetRegistryStatus", lambda: domain.get_registry_status('pybs.com')),
        (6, "Domain/InitiateTransfer", lambda: domain.initiate_transfer('pybs.com', 'authcode123', contacts)),
        (7, "Domain/RetryTransfer", lambda: domain.retry_transfer('pybs.com')),
        (8, "Domain/CancelTransfer", lambda: domain.cancel_transfer('pybs.com')),
        (9, "Domain/ResendTransferAuthEmail", lambda: domain.resend_transfer_auth_email('pybs.com')),
        (10, "Domain/GetTransferHistory", lambda: domain.get_transfer_history('pybs.com')),
        (11, "Domain/ApproveTransferAway", lambda: domain.approve_transfer_away('pybs.com')),
        (12, "Domain/RejectTransferAway", lambda: domain.reject_transfer_away('pybs.com')),
        (13, "Domain/Trade", lambda: domain.trade_domain('pybs.com', contacts)),
        (14, "Domain/EnableRegistrarLock", lambda: domain.enable_registrar_lock('pybs.com')),
        (15, "Domain/DisableRegistrarLock", lambda: domain.disable_registrar_lock('pybs.com')),
        (16, "Domain/GetRegistrarLockStatus", lambda: domain.get_registrar_lock_status('pybs.com')),
        (17, "Domain/EnablePrivateWhois", lambda: domain.enable_private_whois('pybs.com')),
        (18, "Domain/DisablePrivateWhois", lambda: domain.disable_private_whois('pybs.com')),
        (19, "Domain/GetPrivateWhoisStatus", lambda: domain.get_private_whois_status('pybs.com')),
        (20, "Domain/Push", lambda: domain.push_domain('pybs.com', 'target_account')),
        (21, "Domain/ChangeTagUK", lambda: domain.change_tag_uk('pybs.com', 'new_tag')),
        (22, "Domain/List", lambda: domain.list_domains()),
        (23, "Domain/Renew", lambda: domain.renew_domain('pybs.com')),
        (24, "Domain/Restore", lambda: domain.restore_domain('pybs.com')),
        (25, "Domain/Count", lambda: domain.count_domains()),
        (26, "Domain/GetRegistrantVerificationInfo", lambda: domain.get_registrant_verification_info('pybs.com')),
        (27, "Domain/StartRegistrantVerification", lambda: domain.start_registrant_verification('pybs.com')),
    ]

    if test_number == 0:
        for case in test_cases:
            test_num, test_name, test_func = case
            print(f"({test_num}) Testing {test_name}")
            try:
                response, url = test_func()
                print("Transaction ID:", response.transactid)
                print("Status:", response.status)
                if test_num == 4:
                    print("Domain:", response.domain)
                print("API URL:", url)
            except Exception as e:
                print("Exception occurred:", str(e))
            input("Press Enter to continue to the next test...")
    elif 1 <= test_number <= len(test_cases):
        test_num, test_name, test_func = test_cases[test_number - 1]
        print(f"({test_num}) Testing {test_name}")
        try:
            response, url = test_func()
            print("Transaction ID:", response.transactid)
            print("Status:", response.status)
            if test_num == 4:
                print("Domain:", response.domain)
            print("API URL:", url)
        except Exception as e:
            print("Exception occurred:", str(e))
    else:
        print("Invalid test number")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_number = int(sys.argv[1])
    else:
        test_number = 0
    run_test(test_number)