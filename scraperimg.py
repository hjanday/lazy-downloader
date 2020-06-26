from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests
import os
# packages


# let user enter search term
def beginSearching():
    kw = input("Enter something you want to search: ")
    userags = {"q":kw}

    imgpath = kw.replace(" ", "_" ).lower()


    if not os.path.isdir(imgpath):
        os.makedirs(imgpath)
#save in user search term folder


    # i dont know how to do this on google images so bing is next option
    link = requests.get("https://bing.com/images/search", params=userags)

 #parse data
    soupLink  = BeautifulSoup(link.text, "html.parser")
     
    #find all image links
    links = soupLink.findAll("a", {"class":"thumb"})


    #parse url to image then add to folder
    for item in links:
        try:
            img_obj = requests.get(item.attrs["href"])

            print("current url is ", item.attrs["href"])

            title = item.attrs["href"].split("/")[-1]
            try:

                img = Image.open(BytesIO(img_obj.content))

                img.save("./" + imgpath + "/" + title, img.format)
            except:
                print("Image cannot be saved.")
        except:
            print("No image request available")



    beginSearching()
beginSearching()