import requests
import urllib.parse

class Host:
    def __init__(self, api_key, password, test_mode=False):
        self.api_key = api_key
        self.password = password
        self.test_mode = test_mode
        self.base_url = "https://testapi.internet.bs" if test_mode else "https://api.internet.bs"
        self.last_request_url = None
        self.last_request_params = None

    def _make_request(self, resource_path, params):
        url = f"{self.base_url}{resource_path}"
        self.last_request_url = url
        params.update({
            'ApiKey': 'testapi' if self.test_mode else self.api_key,
            'Password': 'testpass' if self.test_mode else self.password,
            'ResponseFormat': 'JSON'
        })
        self.last_request_params = params
        response = requests.get(url, params=params, verify=not self.test_mode)
        return response.json()

    def get_last_request_url(self, reveal=False):
        if self.last_request_url and self.last_request_params:
            params = {k: v for k, v in self.last_request_params.items() if not reveal and k in ['ApiKey', 'Password']}
            return f"{self.last_request_url}?{urllib.parse.urlencode(params)}"
        return None

    def create_host(self, host_name, ip_addresses):
        params = {'host': host_name, 'IP_List': ip_addresses}
        return self._make_request('/Domain/Host/Create', params)

    def get_host_info(self, host_name):
        params = {'Host': host_name}
        return self._make_request('/Domain/Host/Info', params)

    def update_host(self, host_name, ip_addresses):
        params = {'host': host_name, 'IP_list': ip_addresses}
        return self._make_request('/Domain/Host/Update', params)

    def delete_host(self, host_name):
        params = {'host': host_name}
        return self._make_request('/Domain/Host/Delete', params)

    def list_hosts(self, domain_name):
        params = {'domain': domain_name}
        return self._make_request('/Domain/Host/List', params)