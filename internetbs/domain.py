import requests
import urllib3
from results import GenericResult, DomainCheckResult, DomainCreateResult, DomainUpdateResult, DomainInfoResult, DomainRegistryStatusResult, DomainItem
    
class Domain:
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
        requested_url = response.url
        response_data = response.json()
        
        if response.status_code != 200:
            error_message = response_data.get('message', 'Unknown error occurred while processing the request')
            raise Exception(f"API request failed: {error_message}")
        
        if resource_path == '/Domain/Check':
            if response_data.get('status') not in ['AVAILABLE', 'UNAVAILABLE']:
                error_message = response_data.get('message', 'Unknown error occurred while processing the request')
                raise Exception(f"API request failed: {error_message}")
        else:
            if response_data.get('status') != 'SUCCESS':
                error_message = response_data.get('message', 'Unknown error occurred while processing the request')
                raise Exception(f"API request failed: {error_message}")
        
        return response_data, requested_url

    def check_availability(self, domain_name):
        response_data, requested_url = self._make_request('/Domain/Check', {'Domain': domain_name})
        return DomainCheckResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            domain=response_data['domain'],
            minregperiod=response_data['minregperiod'],
            maxregperiod=response_data['maxregperiod'],
            registrarlockallowed=response_data['registrarlockallowed'],
            privatewhoisallowed=response_data['privatewhoisallowed'],
            realtimeregistration=response_data['realtimeregistration'],
        ), requested_url
    
    def create_domain(self, domain_name, contacts, period="1Y", ns_list=None, transfer_auth_info=None, registrar_lock="ENABLED", auto_renew="NO", discount_code=None):
        params = {
            'Domain': domain_name,
            'Period': period,
            'registrarLock': registrar_lock,
            'AutoRenew': auto_renew
        }
        if ns_list:
            params['Ns_list'] = ns_list
        if transfer_auth_info:
            params['transferAuthInfo'] = transfer_auth_info
        if discount_code:
            params['discountCode'] = discount_code
        
        if domain_name.endswith('.com'):
            # Only include the specified parameters for .com domains
            allowed_contact_fields = ['firstName', 'lastName', 'organization', 'email', 'phoneNumber', 'street', 'street2', 'street3', 'city', 'countryCode', 'postalCode']
            allowed_contact_types = ['registrant', 'admin', 'technical', 'billing']
            for contact_type, contact_fields in contacts.items():
                if contact_type in allowed_contact_types:
                    for field, value in contact_fields.items():
                        if field in allowed_contact_fields:
                            params[f"{contact_type}_{field}"] = value
        elif any(domain_name.endswith(tld) for tld in ['.fr', '.re', '.pm', '.tf', '.wf', '.yt']): 
            # Only include the specified parameters for .fr domains
            allowed_contact_fields = ['firstName', 'lastName', 'organization', 'email', 'phoneNumber', 'street', 'street2', 'street3', 'city', 'countryCode', 'postalCode', 'dotfrcontactentitytype']
            allowed_contact_types = ['registrant', 'admin']
            for contact_type, contact_fields in contacts.items():
                if contact_type in allowed_contact_types:
                    for field, value in contact_fields.items():
                        if field in allowed_contact_fields:
                            params[f"{contact_type}_{field}"] = value

        else:
            for contact_type, contact_fields in contacts.items():
                for field, value in contact_fields.items():
                    params[f"{contact_type}_{field}"] = value
        
        response_data, requested_url = self._make_request('/Domain/Create', params)

        return DomainCreateResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            currency=response_data['currency'],
            price=response_data['price'],
            product=response_data['product'],
        ), requested_url
    
    def update_domain(self, domain_name, contacts=None, ns_list=None, transfer_auth_info=None, registrar_lock=None, auto_renew=None):
        params = {'Domain': domain_name}
        if ns_list:
            params['Ns_list'] = ns_list
        if transfer_auth_info:
            params['transferAuthInfo'] = transfer_auth_info
        if registrar_lock:
            params['registrarLock'] = registrar_lock
        if auto_renew:
            params['AutoRenew'] = auto_renew
        
        if contacts:
            for contact_type, contact_fields in contacts.items():
                for field, value in contact_fields.items():
                    params[f"{contact_type}_{field}"] = value
        
        response_data, requested_url = self._make_request('/Domain/Update', params)
        return DomainUpdateResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            message=response_data.get('message', ''),
        ), requested_url
    
    def get_domain_info(self, domain_name):
        response_data, requested_url = self._make_request('/Domain/Info', {'Domain': domain_name})
        return DomainInfoResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            domain=response_data['domain'],
            expirationdate=response_data['expirationdate'],
            registrationdate=response_data['registrationdate'],
            paiduntil=response_data['paiduntil'],
            registrarlock=response_data['registrarlock'],
            autorenew=response_data['autorenew'],
            privatewhois=response_data['privatewhois'],
            whoisprivacy=response_data['whoisprivacy'],
            domainstatus=response_data['domainstatus'],
            contacts=response_data['contacts'],
            transferauthinfo=response_data['transferauthinfo'],
            dnssec=response_data['dnssec'],
            price=response_data['price'],
        ), requested_url
    
    def get_registry_status(self, domain_name):
        response_data, requested_url = self._make_request('/Domain/RegistryStatus', {'Domain': domain_name})
        return DomainRegistryStatusResult(
            transactid=response_data['transactid'],
            domain=response_data['domain'],
            registrystatus=response_data['registrystatus'],
            status=response_data['status'],
        ), requested_url
    
    def initiate_transfer(self, domain_name, auth_code, contacts):
        params = {
            'Domain': domain_name,
            'AuthCode': auth_code
        }
        for contact_type, contact_fields in contacts.items():
            for field, value in contact_fields.items():
                params[f"{contact_type}_{field}"] = value
        
        response_data, requested_url = self._make_request('/Domain/Transfer/Initiate', params)
        return GenericResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            message=response_data.get('message', ''),
        ), requested_url
    
    def retry_transfer(self, domain_name):
        response_data, requested_url = self._make_request('/Domain/Transfer/Retry', {'Domain': domain_name})
        return GenericResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            message=response_data.get('message', ''),
        ), requested_url
    
    def cancel_transfer(self, domain_name):
        response_data, requested_url = self._make_request('/Domain/Transfer/Cancel', {'Domain': domain_name})
        return GenericResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            message=response_data.get('message', ''),
        ), requested_url
    
    def resend_transfer_auth_email(self, domain_name):
        response_data, requested_url = self._make_request('/Domain/Transfer/ResendAuthEmail', {'Domain': domain_name})
        return GenericResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            message=response_data.get('message', ''),
        ), requested_url
    
    def get_transfer_history(self, domain_name):
        response_data, requested_url = self._make_request('/Domain/Transfer/History', {'Domain': domain_name})
        return GenericResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            message=response_data.get('message', ''),
        ), requested_url
    
    def approve_transfer_away(self, domain_name):
        response_data, requested_url = self._make_request('/Domain/TransferAway/Approve', {'Domain': domain_name})
        return GenericResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            message=response_data.get('message', ''),
        ), requested_url
    
    def reject_transfer_away(self, domain_name):
        response_data, requested_url = self._make_request('/Domain/TransferAway/Reject', {'Domain': domain_name})
        return GenericResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            message=response_data.get('message', ''),
        ), requested_url
    
    def trade_domain(self, domain_name, contacts):
        params = {'Domain': domain_name}
        for contact_type, contact_fields in contacts.items():
            for field, value in contact_fields.items():
                params[f"{contact_type}_{field}"] = value
        
        response_data, requested_url = self._make_request('/Domain/Trade', params)
        return GenericResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            message=response_data.get('message', ''),
        ), requested_url
    
    def enable_registrar_lock(self, domain_name):
        response_data, requested_url = self._make_request('/Domain/RegistrarLock/Enable', {'Domain': domain_name})
        return GenericResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            message=response_data.get('message', ''),
        ), requested_url
    
    def disable_registrar_lock(self, domain_name):
        response_data, requested_url = self._make_request('/Domain/RegistrarLock/Disable', {'Domain': domain_name})
        return GenericResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            message=response_data.get('message', ''),
        ), requested_url
    
    def get_registrar_lock_status(self, domain_name):
        response_data, requested_url = self._make_request('/Domain/RegistrarLock/Status', {'Domain': domain_name})
        return GenericResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            message=response_data.get('message', ''),
        ), requested_url
    
    def enable_private_whois(self, domain_name):
        response_data, requested_url = self._make_request('/Domain/PrivateWhois/Enable', {'Domain': domain_name})
        return GenericResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            message=response_data.get('message', ''),
        ), requested_url
    
    def disable_private_whois(self, domain_name):
        response_data, requested_url = self._make_request('/Domain/PrivateWhois/Disable', {'Domain': domain_name})
        return GenericResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            message=response_data.get('message', ''),
        ), requested_url
    
    def get_private_whois_status(self, domain_name):
        response_data, requested_url = self._make_request('/Domain/PrivateWhois/Status', {'Domain': domain_name})
        return GenericResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            message=response_data.get('message', ''),
        ), requested_url
    
    def push_domain(self, domain_name, target_account):
        response_data, requested_url = self._make_request('/Domain/Push', {'Domain': domain_name, 'TargetAccount': target_account})
        return GenericResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            message=response_data.get('message', ''),
        ), requested_url
    
    def change_tag_uk(self, domain_name, new_tag):
        response_data, requested_url = self._make_request('/Domain/ChangeTag/DotUK', {'Domain': domain_name, 'NewTag': new_tag})
        return GenericResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            message=response_data.get('message', ''),
        ), requested_url
    
    def list_domains(self, return_url=False):
        response_data, requested_url = self._make_request('/Domain/List', {})
        domain_names = response_data.get('domain', [])
        return [DomainItem(domain_name) for domain_name in domain_names], requested_url
    
    def renew_domain(self, domain_name, period="1Y"):
        response_data, requested_url = self._make_request('/Domain/Renew', {'Domain': domain_name, 'Period': period})
        return GenericResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            message=response_data.get('message', ''),
        ), requested_url
    
    def restore_domain(self, domain_name):
        response_data, requested_url = self._make_request('/Domain/Restore', {'Domain': domain_name})
        return GenericResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            message=response_data.get('message', ''),
        ), requested_url
    
    def count_domains(self):
        response_data, requested_url = self._make_request('/Domain/Count', {})
        return GenericResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            message=response_data.get('message', ''),
        ), requested_url
    
    def get_registrant_verification_info(self, domain_name):
        response_data, requested_url = self._make_request('/Domain/RegistrantVerification/Info', {'Domain': domain_name})
        return GenericResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            message=response_data.get('message', ''),
        ), requested_url
    
    def start_registrant_verification(self, domain_name):
        response_data, requested_url = self._make_request('/Domain/RegistrantVerification/Send', {'Domain': domain_name})
        return GenericResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            message=response_data.get('message', ''),
        ), requested_url


