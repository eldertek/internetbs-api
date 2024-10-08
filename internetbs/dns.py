import requests
import urllib3
from .results import DNSAddRecordResult, DNSRemoveRecordResult, DNSUpdateRecordResult, DNSListRecordsResult

class DNS:
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
        
        # Error handling
        if response.status_code != 200 or (response_data.get('status') != 'SUCCESS' and response_data.get('status') != 'FAILURE'):
            error_message = response_data.get('message', response.content)
            raise Exception(f"API request failed: {error_message}")
        
        return response_data, requested_url

    def add_record(self, domain_name, record_type, value):
        params = {'FullRecordName': domain_name, 'Type': record_type, 'Value': value}
        response_data, requested_url = self._make_request('/Domain/DnsRecord/Add', params)
        return DNSAddRecordResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
        ), requested_url

    def remove_record(self, domain_name, record_type, value=None):
        params = {'FullRecordName': domain_name, 'Type': record_type}
        if value:
            params['Value'] = value
        response_data, requested_url = self._make_request('/Domain/DnsRecord/Remove', params)
        return DNSRemoveRecordResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
        ), requested_url

    def update_record(self, domain_name, old_record_type, old_value, new_value):
        params = {
            'FullRecordName': domain_name,
            'Type': old_record_type,
            'CurrentValue': old_value,
            'NewValue': new_value
        }
        response_data, requested_url = self._make_request('/Domain/DnsRecord/Update', params)
        return DNSUpdateRecordResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
        ), requested_url

    def list_records(self, domain_name):
        params = {'Domain': domain_name}
        response_data, requested_url = self._make_request('/Domain/DnsRecord/List', params)
        return DNSListRecordsResult(
            transactid=response_data['transactid'],
            status=response_data['status'],
            records=response_data['records'],
        ), requested_url

