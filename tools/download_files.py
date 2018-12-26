import requests
response = requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(response.status_code)
try:
    response.raise_for_status()
except Exception as exc:
    print("There was a problem %s" % (exc))
if response.status_code == requests.codes.ok:
    print("ok")
print(len(response.text))
print(response.text[:50])
play_file = open("save.txt", 'wb')
for chunk in response.iter_content(5000):
    play_file.write(chunk)

play_file.close()
