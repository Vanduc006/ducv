
'''import requests,json
import webbrowser

url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"
video = input('url video:')
querystring = {"url":f"{video}"}

headers = {
	"X-RapidAPI-Key": "2bdc1f0810mshfc6e44c69c98822p1bdb0bjsn85b73f91c2d1",
	"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
res = response.json()

url_no_watermark = res['video']
user_name_orginal = res['author']
video_id_orginal = res['videoid']
final = ''.join(url_no_watermark)
username = ''.join(user_name_orginal)
videoID = ''.join(video_id_orginal)
print(response.json())
print(url_no_watermark)

webbrowser.open(final)
name_file = username + '-' + videoID + '.mp4'
name_file =  str(name_file)
response = requests.get(final)

with open(name_file, 'wb') as f:
    f.write(response.content)'''



import requests
import re
from fake_headers import Headers

header = Headers(
        browser="chrome",  # Generate only Chrome UA
        os="win",  # Generate ony Windows platform
        headers=True  # generate misc headers
    )

fake_head = header.generate()

url = "https://www.tiktok.com/@nhaconaofficial/video/7227673882012945670?is_from_webapp=1&sender_device=pc&web_id=7155705309725296130"
video_id = re.search(r'/video/(\d+)\?', url).group(1)
username = re.search(r'@(\w+)', url).group(1)
url = f'https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/feed/?aweme_id={video_id}' 
res = requests.get(url)
r = res.json()
link = r['aweme_list'][0]['video']['play_addr']['url_list'][0]
#username = r['aweme_list'][0]['author']['nickname']
print(link)
files_name = str(username) + '-' + str(video_id) + '.mp4'
files_name = str(files_name)
response = requests.get(link)

with open(files_name, 'wb') as f:
    f.write(response.content)


