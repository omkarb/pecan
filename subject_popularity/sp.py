import requests

url = 'http://www.google.com/trends/fetchComponent?hl=en-US&q=basketball&cid=TIMESERIES_GRAPH_0&export=5&w=500&h=300'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
# with urllib.request.urlopen(url) as f:
#     split = f.read().decode().split("table")
#     print(split)
r = requests.get(url, headers=headers)
print(r.text)