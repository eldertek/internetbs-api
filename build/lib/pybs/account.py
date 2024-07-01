import requests
import urllib3

class Account:
    def __init__(self, api_key, password, test_mode=False):
        self.api_key = api_key
        self.password = password
        self.test_mode = test_mode
        self.base_url = "https://testapi.internet.bs" if test_mode else "https://api.internet.bs"
        if self.test_mode:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def _make_request(self, resource_path, params):
        url = f"{self.base_url}{resource_path}"
        params.update({
            'ApiKey': 'testapi' if self.test_mode else self.api_key,
            'Password': 'testpass' if self.test_mode else self.password,
            'ResponseFormat': 'JSON'
        })
        response = requests.get(url, params=params, verify=not self.test_mode)
        response_data = response.json()
        
        # Error handling
        if response.status_code != 200 or response_data.get('status') != 'SUCCESS':
            error_message = response_data.get('message', 'Unknown error')
            raise Exception(f"API request failed: {error_message}")
        
        return response_data

    def get_balance(self):
        response_data = self._make_request('/Account/Balance/Get', {})
        balance_info = response_data.get('balance', [{}])[0]
        return Balance(balance_info.get('currency'), balance_info.get('amount'))

    def set_default_currency(self, currency_code):
        params = {'Currency': currency_code}
        response_data = self._make_request('/Account/DefaultCurrency/Set', params)
        return response_data.get('status')

    def get_default_currency(self):
        response_data = self._make_request('/Account/DefaultCurrency/Get', {})
        return response_data.get('currency')

    def get_price_list(self):
        response_data = self._make_request('/Account/PriceList/Get', {})
        products_data = response_data.get('product', [])
        products = [Product(p['name'], p['price'], p['currency']) for p in products_data]
        return products

    def get_configuration(self):
        response_data = self._make_request('/Account/Configuration/Get', {})
        return Configuration(response_data)

    def set_configuration(self, transfer_approval_css, reseller_name, reseller_sender_email, reseller_support_email, reseller_whois_header, reseller_whois_footer, low_balance_limit):
        params = {
            'TransferApprovalCss': transfer_approval_css,
            'resellerName': reseller_name,
            'resellerSenderEmail': reseller_sender_email,
            'resellerSupportEmail': reseller_support_email,
            'resellerWhoisHeader': reseller_whois_header,
            'resellerWhoisFooter': reseller_whois_footer,
            'lowBalanceLimit': low_balance_limit
        }
        response_data = self._make_request('/Account/Configuration/Set', params)
        return response_data.get('status')

class Balance:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        return f"Balance(currency={self.currency}, amount={self.amount})"

class Product:
    def __init__(self, name, price, currency):
        self.name = name
        self.price = price
        self.currency = currency

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, currency={self.currency})"

class Configuration:
    def __init__(self, data):
        self.transactid = data.get('transactid')
        self.transferapprovalcss = data.get('transferapprovalcss')
        self.resellername = data.get('resellername')
        self.resellersenderemail = data.get('resellersenderemail')
        self.resellerwhoisheader = data.get('resellerwhoisheader')
        self.resellerwhoisfooter = data.get('resellerwhoisfooter')
        self.lowbalancelimit = data.get('lowbalancelimit')
        self.billableinterval = data.get('billableinterval')
        self.premiumdomainsoperations = data.get('premiumdomainsoperations')

    def __repr__(self):
        return (f"Configuration(transactid={self.transactid}, transferapprovalcss={self.transferapprovalcss}, "
                f"resellername={self.resellername}, resellersenderemail={self.resellersenderemail}, "
                f"resellerwhoisheader={self.resellerwhoisheader}, resellerwhoisfooter={self.resellerwhoisfooter}, "
                f"lowbalancelimit={self.lowbalancelimit}, billableinterval={self.billableinterval}, "
                f"premiumdomainsoperations={self.premiumdomainsoperations})")

