import requests

def get_github_security_overall_count(cookie_string):
    url = 'https://github.com/kestra-io/kestra/security/overall-count'
    headers = {
        'priority': 'u=1, i',
        'x-requested-with': 'XMLHttpRequest',
        'cookie': cookie_string
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return {
            'content-type': response.headers.get('Content-Type'),
            'content-length': response.headers.get('Content-Length'),
            'status-code': response.status_code,
            'response-body': response.text
        }
    else:
        return {
            'error': f'HTTP {response.status_code}',
            'status-code': response.status_code
        }

def convert_cookie_string_to_dict(cookie_string):
    cookies = {}
    items = cookie_string.split(';')
    for item in items:
        key, value = item.strip().split('=', 1)
        cookies[key] = value
    return cookies

cookie_string = 'key1=value1;key2=value2'
cookies = convert_cookie_string_to_dict(cookie_string)
result = get_github_security_overall_count(cookie_string)
print(result)