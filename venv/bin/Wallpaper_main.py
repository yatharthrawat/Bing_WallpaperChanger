#This Python Program pulls the Bing Daily Wallpaper and makes it the wallpaper of your mac.

#Created By Yatharth Rawat


from bs4 import BeautifulSoup
import urllib.request
from appscript import app, mactypes
from pathlib import Path
import os

home = str(Path.home())

newpath=home+'/Documents/Bing_photos/'
if not os.path.exists(newpath):
    os.makedirs(newpath)

base_url="http://bing.com"

bing=urllib.request.urlopen("http://bing.com")
soup = BeautifulSoup(bing,"html.parser")
script = soup.find_all('script')

script_img=str(script)

x=script_img.find("g_img={url:")
y=script_img.find(".jpg",x)
img_url=script_img[x+len("g_img={url:")+2:y+len(".jpg")]
r=img_url.find(".")
q=len(img_url)-img_url[::-1].find("/")
img_name=img_url[q:r]

print("URL Located Preparing to Download...")

f=open(newpath+img_name+".jpg",'wb')
f.write(urllib.request.urlopen(base_url+img_url).read())
f.close()
print("Download Complete Preparing to Change Wallpaper...")
app('Finder').desktop_picture.set(mactypes.File(newpath+img_name+'.jpg'))
print("Wallpaper Changed Successfully!\nWallpaper Name:"+img_name)


