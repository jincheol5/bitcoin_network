import requests
import json

# url=f"https://blockchain.info/q/getblockcount"

# response=requests.get(url)

# print(response.status_code)
# print(int(response.text))


block_height=0
url=f"https://blockchain.info/block-height/{block_height}"
params={
    "format":"json"
}
response=requests.get(url,params=params)
print(response.status_code)
print(
        json.dumps(
            response.text.model_dump(),
            indent=2,
            ensure_ascii=False
            )
    )

# genesis hash=000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f