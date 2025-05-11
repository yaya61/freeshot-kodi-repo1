import re
import requests
import xbmcaddon

BASE_URL = "https://www.freeshot.live"

def get_categories():
    html = requests.get(f"{BASE_URL}/live-tv").text
    return re.findall(r'href="(/live-tv/[^"]+)"', html)

def get_streams(category_url):
    full_url = f"{BASE_URL}{category_url}"
    html = requests.get(full_url).text
    return re.findall(r"source:\s*'([^']+)'", html)

def router(paramstring):
    if not paramstring:
        categories = get_categories()
        for idx, cat in enumerate(categories):
            name = cat.split('/')[-1].replace('-', ' ').title()
            url = f"{BASE_URL}{cat}"
            xbmc.log(f"Adding category: {name}", xbmc.LOGINFO)
            xbmcaddon.Addon().addDirectoryItem(name, url, isFolder=True)
        xbmcaddon.Addon().endOfDirectory()
