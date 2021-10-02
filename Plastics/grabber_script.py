import requests
import bs4
import time
import os


url = requests.get("https://www.google.co.in/search?q=plastics&tbm=isch&hl=en&chips=q:plastics,g_1:waste:a-CkCJLh5Ik%3D,g_1:non+biodegradable:MovCgN2EqIA%3D&authuser=0&sa=X&ved=2ahUKEwiwnKTf65_zAhWKsksFHaccDVkQ4lYoBXoECAEQHQ&biw=1903&bih=969").text
soup = bs4.BeautifulSoup(url, "html.parser")
a=len(os.listdir())
for tag in soup.find_all("img"): 
##    print(tag['src'])
    a+=1
    string = tag['src']
    print(string)
    try:
        if string.split(":")[0] == "https":
            image = requests.get(string)
            with open(f"some{a}.png", "wb") as file:
                file.write(image.content)
    except Exception as e:
##        print(e)
        pass
##    if a == 50:
##        break
print(a)
