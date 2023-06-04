from undetected_chromedriver.v2 import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import time

# Khởi tạo undetected-chromedriver
options = ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = Chrome(options=options)

driver.get("https://www.tiktok.com/@phungdatdzvl0_0/")

# Lưu trữ các liên kết đã truy cập
visited_links = set()
while True:
    previous_height = driver.execute_script("return document.body.scrollHeight")
    time.sleep(3)
    #print('Scrolling...')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # Quét và in ra các đường liên kết duy nhất
    elements = driver.find_elements(By.CSS_SELECTOR, ".tiktok-yz6ijl-DivWrapper > a")
    if len(elements) == 0:
        #print("No more elements found")

        break

    for element in elements:
        href = element.get_attribute("href")
        if href not in visited_links:
            visited_links.add(href)
            print(href)

    # In tổng số các phần tử duy nhất
    total_elements = len(visited_links)
    #print("Total unique elements:", total_elements)

    # Kiểm tra chiều cao trước và sau khi kéo trang
    current_height = driver.execute_script("return document.body.scrollHeight")
    
    if current_height == previous_height:
        #print("Reached end of page")
        break
    previous_height = current_height