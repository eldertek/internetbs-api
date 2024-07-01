import requests

class Forwarding:
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

    def add_url_forward(self, domain_name, destination_url):
        params = {'Domain': domain_name, 'Destination': destination_url}
        return self._make_request('/Domain/UrlForward/Add', params)

    def update_url_forward(self, domain_name, destination_url):
        params = {'Domain': domain_name, 'Destination': destination_url}
        return self._make_request('/Domain/UrlForward/Update', params)

    def remove_url_forward(self, domain_name):
        params = {'Domain': domain_name}
        return self._make_request('/Domain/UrlForward/Remove', params)

    def list_url_forwards(self):
        return self._make_request('/Domain/UrlForward/List', {})

    def add_email_forward(self, domain_name, source_email, destination_email):
        params = {'Domain': domain_name, 'SourceEmail': source_email, 'DestinationEmail': destination_email}
        return self._make_request('/Domain/EmailForward/Add', params)

    def update_email_forward(self, domain_name, source_email, destination_email):
        params = {'Domain': domain_name, 'SourceEmail': source_email, 'DestinationEmail': destination_email}
        return self._make_request('/Domain/EmailForward/Update', params)

    def remove_email_forward(self, domain_name, source_email):
        params = {'Domain': domain_name, 'SourceEmail': source_email}
        return self._make_request('/Domain/EmailForward/Remove', params)

    def list_email_forwards(self):
        return self._make_request('/Domain/EmailForward/List', {})
