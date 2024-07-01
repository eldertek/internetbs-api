import requests

class Host:
    def __init__(self, api_key, password, test_mode=False):
        self.api_key = api_key
        self.password = password
        self.test_mode = test_mode
        self.base_url = "https://testapi.internet.bs" if test_mode else "https://api.internet.bs"

    def _make_request(self, resource_path, params):
        url = f"{self.base_url}{resource_path}"
        params.update({
            'ApiKey': 'testapi' if self.test_mode else self.api_key,
            'Password': 'testpass' if self.test_mode else self.password,
            'ResponseFormat': 'JSON'
        })
        response = requests.get(url, params=params, verify=not self.test_mode)
        return response.json()

    def create_host(self, host_name, ip_address):
        params = {'HostName': host_name, 'IPAddress': ip_address}
        return self._make_request('/Domain/Host/Create', params)

    def get_host_info(self, host_name):
        params = {'HostName': host_name}
        return self._make_request('/Domain/Host/Info', params)

    def update_host(self, host_name, ip_address):
        params = {'HostName': host_name, 'IPAddress': ip_address}
        return self._make_request('/Domain/Host/Update', params)

    def delete_host(self, host_name):
        params = {'HostName': host_name}
        return self._make_request('/Domain/Host/Delete', params)

    def list_hosts(self):
        return self._make_request('/Domain/Host/List', {})
