import requests
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('LINKPREVIEW')

url = 'http://api.linkpreview.net/?key='+str(key)+'&q='

def linkPreview(link):
    response = requests.get(url+link)
    data = response.json()
    title = data['title']
    image = data['image']
    link = data['url']
    description = data['description']
    return (title, image, link, description)

r,s,t,u = linkPreview('https://towardsdatascience.com/mapping-with-matplotlib-pandas-geopandas-and-basemap-in-python-d11b57ab5dac')
print(f' title: {r} \n image: {s} \n link: {t} \n description: {u} ')
