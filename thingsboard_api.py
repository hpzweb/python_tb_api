import requests

class api:
    def __init__(self, host, usr, pwd):
        self.host = 'http://' + host
        payload = {"username": usr, "password": pwd}
        resp = requests.post(self.host + '/api/auth/login', json=payload)
        resp.raise_for_status()
        self.auth_header = {'X-Authorization': 'Bearer ' + resp.json()['token']}

    def get_request(self, path, parameters=None):
        resp = requests.get(self.host + path, headers=self.auth_header, params=parameters)
        return resp.text

    def post_request(self, path, body, parameters=None):
        resp = requests.post(self.host + path, headers=self.auth_header, params=parameters, json=body)
        return resp.text

    def delete_request(self, path, parameters=None):
        resp = requests.delete(self.host + path, headers=self.auth_header, params=parameters)
        return resp.text


if __name__ == "__main__":

    a = api('localhost:8080', 'sysadmin@thingsboard.org', 'sysadmin')

    print(a.get_request('/api/admin/updates'))
    print(a.post_request('/api/devices', {'deviceTypes': ['string']}))
