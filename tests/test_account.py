import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../internetbs')))

from account import Account

account = Account('testapi', 'testpass', test_mode=True)

def run_test(test_number):
    if test_number == 1:
        print("(1) Testing Account/Balance/Get")
        print("Currency: ", account.get_balance().currency)
        print("Amount: ", account.get_balance().amount)
    elif test_number == 2:
        print("(2) Testing Account/DefaultCurrency/Set")
        print("Status of the request: ", account.set_default_currency('EUR'))
    elif test_number == 3:
        print("(3) Testing Account/DefaultCurrency/Get")
        print("Default Currency: ", account.get_default_currency())
    elif test_number == 4:
        print("(4) Testing Account/PriceList/Get")
        price_list = account.get_price_list()
        print("Product 1 Name: ", price_list[0].name)
        print("Product 1 Price: ", price_list[0].price)
        print("Product 1 Currency: ", price_list[0].currency)
        print("Product 2 Name: ", price_list[1].name)
        print("Product 2 Price: ", price_list[1].price)
        print("Product 2 Currency: ", price_list[1].currency)
        print("Product 3 Name: ", price_list[2].name)
        print("Product 3 Price: ", price_list[2].price)
        print("Product 3 Currency: ", price_list[2].currency)
    elif test_number == 5:
        print("(5) Testing Account/Configuration/Get")
        config = account.get_configuration()
        print("Transact ID: ", config.transactid)
        print("Transfer Approval CSS: ", config.transferapprovalcss)
        print("Reseller Name: ", config.resellername)
        print("Reseller Sender Email: ", config.resellersenderemail)
        print("Reseller WHOIS Header: ", config.resellerwhoisheader)
        print("Reseller WHOIS Footer: ", config.resellerwhoisfooter)
        print("Low Balance Limit: ", config.lowbalancelimit)
        print("Billable Interval: ", config.billableinterval)
        print("Premium Domains Operations: ", config.premiumdomainsoperations)
    elif test_number == 6:
        print("(6) Testing Account/Configuration/Set")
        config_params = {
            'TransferApprovalCss': 'h1{color:red}',
            'reseller_name': 'testName',
            'reseller_sender_email': 'test@sender.com',
            'reseller_support_email': 'support@sender.com',
            'reseller_whois_header': 'customwhoisheader',
            'reseller_whois_footer': 'customfooter',
            'low_balance_limit': 'USD:10,JPY:20'
        }
        print("Status of the request: ", account.set_configuration(
            config_params['TransferApprovalCss'],
            config_params['reseller_name'],
            config_params['reseller_sender_email'],
            config_params['reseller_support_email'],
            config_params['reseller_whois_header'],
            config_params['reseller_whois_footer'],
            config_params['low_balance_limit']
        ))
    else:
        print("Invalid test number")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_number = int(sys.argv[1])
    else:
        test_number = 1 
    run_test(test_number)
