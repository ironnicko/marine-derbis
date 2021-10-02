import time
import os
import requests
import bs4
main = "https://www.google.com/search?q=fishing+nets&tbm=isch&hl=en&chips=q:fishing+nets,g_1:ocean:RNohVc-WDiY%3D,g_1:full:Yc-5IqTBFyI%3D&sa=X&ved=2ahUKEwjkjK6S7KvzAhXEtksFHYArCHoQ4lYoBnoECAEQHw&biw=1349&bih=657"

url = requests.get(main).text
soup = bs4.BeautifulSoup(url, "html.parser")
a=len(os.listdir())-1
for tag in soup.find_all("img"): 
    a+=1
    string = tag['src']
    print(string)
    try:
        if string.split(":")[0] == "https":
            image = requests.get(string)
            with open(f"some{a}.png", "wb") as file:
                file.write(image.content)
    except Exception as e:
        pass

print(a)
