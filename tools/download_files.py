import requests
import bs4
response = requests.get("https://www.baidu.com/")
#  response = requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(response.status_code)
try:
    response.raise_for_status()
except Exception as exc:
    print("There was a problem %s" % (exc))
if response.status_code == requests.codes.ok:
    print("ok")
print(len(response.text))
print(response.text[:50])

soup = bs4.BeautifulSoup(response.text, features='html.parser')
#  print(type(soup))
#  play_file = open("save.txt", 'wb')
#  for chunk in response.iter_content(5000):
    #  play_file.write(chunk)

#  play_file.close()

elems = soup.select('body')
#  print(type(elems[0].getText()))
print(elems[0].getText())
print(elems[0].attrs)
