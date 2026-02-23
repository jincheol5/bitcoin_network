import requests

url=f"https://blockchain.info/q/getblockcount"

response=requests.get(url)

print(response.status_code)
print(int(response.text))