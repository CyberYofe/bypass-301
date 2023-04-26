import requests

url = 'https://example.com'
response = requests.get(url, allow_redirects=True)
final_url = response.url
print('Final URL: ', final_url)
