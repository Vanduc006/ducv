'''import requests

cookie_gl = '_ga=GA1.2.80771609.1679159480; _gid=GA1.2.417871531.1679816243; fblo_901999673240219=y'
headers = {
    'authority': 'gomlua.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
    'cache-control': 'max-age=0',
    'cookie': f'{cookie_gl}',
    'if-modified-since': 'Fri, 10 Feb 2023 02:23:51 GMT',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

list_job = requests.get('https://gomlua.com/cpi/listCampaignFacebook?os=web&type=like_post',headers=headers)
print(list_job.text)'''
import requests
cookie_gl = '_ga=GA1.2.80771609.1679159480; _gid=GA1.2.417871531.1679816243; fblo_901999673240219=y'
cookie_fb = 'sb=Ia95Ywt-JWwosiJYc8EjUNem; datr=Ia95Y7xxHSYbqSjk04-Jz4bU; c_user=100030029031374; m_page_voice=100030029031374; xs=45:w-21eo8Hz6lpUQ:2:1670039278:-1:6282::AcXW4WpNjBd1PA4VzkAysPUmEYCgyyzDBvMl2NclXQ; fr=0ufwkWF0yKuSFj1z1.AWVNn6q-mrseburxJaiZ8-wEHXw.BkHbbk.NA.AAA.0.0.BkHbbk.AWXx9CofPsg; presence=C{"t3":[],"utc3":1679668983173,"v":1}; wd=550x664; sb=q7wdZJAGwnqQ9FXof-7gojTn; datr=q7wdZFGP7F_F7lUEqAO2HJpj; m_pixel_ratio=1; x-referer=eyJyIjoiL2hvbWUucGhwP3RidWE9MSIsImgiOiIvaG9tZS5waHA/dGJ1YT0xIiwicyI6Im0ifQ==; usida=eyJ2ZXIiOjEsImlkIjoiQXJzMTgyMjFjczFoaW4iLCJ0aW1lIjoxNjc5NjczMTIyfQ==; c_user=100030029031374; xs=45:w-21eo8Hz6lpUQ:2:1670039278:-1:6282::AcVeg37dsRkTq0QGR5QWAZp14IIgw6vxGcr225SDKy4; fr=0ufwkWF0yKuSFj1z1.AWW5W5gHtHxNvBoQyepRn9wdhIE.BkHbbk.NA.AAA.0.0.BkIHkx.AWUzeSauOXw; presence=C{"t3":[],"utc3":1679849788895,"v":1}; wd=529x636'
def GetToken():
    headers = {
        "authority": "mbasic.facebook.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,",
        "accept-language": "vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
        "cookie": cookie_fb,
        "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        "sec-ch-ua-mobile": '?0',
        "sec-ch-ua-platform": '"Windows"',
        'sec-fetch-dest': "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        
    }
    # data này kệ đi, có lúc nó cần phải login kiểu này thôi
    # data = {
    #     "fb_dtsg": "NAcMqnAp8MoNuHm9oYsmbYoD5GdbkTNBC4wjX1MS2rW0UjAXgnMnpnA:7:1658162250",
    #     "jazoest": "25501",
    #     "from_post": "1",
    #     "read": "baseline,public_profile",
    #     "seen_scopes": "baseline,public_profile",
    #     "response_type": "token,signed_request,graph_domain",
    #     "dialog_type": "gdp_v4",
    #     "return_format": "return_scopes,denied_scopes,signed_request,graph_domain,access_token,base_domain",
    #     "logger_id": "fea77a3774bdc8",
    #     "sheet_name": "initial",
    #     "sdk": "joey",
    #     "encrypted_post_body": "AeBMBqHBPI_sgCe20UP3XEBT2lSabOCqWYf_tqKLuNL21befjwq9cwhHr3dHkwI7heZ3eJDL5NADVumWLES3hNu_IJ3R1t_9YMaSqAiR2WwGr8yEaJbv8UH8_zNrIplRcryfxydDI1fPgw5CdNe7VRCdPv5FbnTq3GLTqAVtdYwKGlq55sP8MvYxUo19AWnCCfZ0sAKB-5P_Q5uyg9HtcSiuLlFQ6nRwq0wsfb4UgOPUHX9gkm2G47ZpihwCAQQiBPVWb5n323df5ZzR4QuuKHZjx0r3HgizqK4FMV25B9N8OW4xKTH7mm6moZiwO0DeMitxNdH2ZcfEirKy12UHKPMH9-Bpnlpa6jTIuOdD8gZ8yz85_3Jw-waJos8y2KGMYkbkhchv1IjJoeO5FGO6VSlgVKW0MXn2SDHn27o2DmhHiCewqZuH-9N9JQ9EtSXQTywk2gj28Vy-4Vq-Sna7R2R4ftmlqfVDkog--woQAAmxNDB4lrXsaT80ZMlzw6Z8mAkvtRLdfQS_pCKvbK1z24DAKcLrGnwsEcFDPDJambc",
    #     "cbt": "1658330200591",
    # }
    login = requests.get("https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=901999673240219&kid_directed_site=0&app_id=901999673240219&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fapp_id%3D901999673240219%26cbt%3D1679851676979%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1b1ee1b5d95fe8%2526domain%253Dgomlua.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fgomlua.com%25252Ff33ab4b7d5afbc4%2526relation%253Dopener%26client_id%3D901999673240219%26display%3Dpopup%26domain%3Dgomlua.com%26e2e%3D%257B%257D%26enable_profile_selector%3Dtrue%26fallback_redirect_uri%3Dhttps%253A%252F%252Fgomlua.com%252F%2523%252Fauth%252Flogin%26locale%3Den_US%26logger_id%3Df28bb000dd7dfc4%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3ab933e4120f6c%2526domain%253Dgomlua.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fgomlua.com%25252Ff33ab4b7d5afbc4%2526relation%253Dopener%2526frame%253Dfe5bc8c38e3d6%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%26sdk%3Djoey%26version%3Dv2.9%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3ab933e4120f6c%26domain%3Dgomlua.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fgomlua.com%252Ff33ab4b7d5afbc4%26relation%3Dopener%26frame%3Dfe5bc8c38e3d6%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=vi_VN&pl_dbl=0", headers=headers).text
    if "access_token=" in login:
        return login.split('access_token=')[1].split('&')[0]
    else:
        return ""

def LoginGomlua(self):
    token = self.GetToken()
    print(token)