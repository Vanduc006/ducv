import requests

statics = requests.get('https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/feed/?aweme_id=7231122618995297542')
data = statics.json()
cmts = data['aweme_list'][0]['statistics']['comment_count']
hearts = data['aweme_list'][0]['statistics']['digg_count']
views = data['aweme_list'][0]['statistics']['play_count']
share = data['aweme_list'][0]['statistics']['share_count']
collects = data['aweme_list'][0]['statistics']['collect_count']
ban_yet = data['aweme_list'][0]['status']['is_prohibited']
video_times = data['aweme_list'][0]['music_end_time_in_ms']

import re

def check_tiktok_url(url):
    pattern = r"^https?://(?:www\.)?tiktok\.([\w-]+)$"
    match = re.match(pattern, url)
    if match:
        return True
    else:
        return False

url = "https://www.tiktok.com/@iamphuong90"
if check_tiktok_url(url):
    print("Định dạng đường dẫn TikTok đúng.")
else:
    print("Định dạng đường dẫn TikTok sai.")


