# Quiz) 부동산 매물(검단 호반 써밋1차) 정보를 스크래핑 하는 프로그램을 만드시오

# [조희 조건]
# 1. http://daum.net 접속
# 2. 검단 호빈 써밋 검색
# 3. 다음 부동산 부분에 나오는 결과 정보

# [출력 결과]
# =========== 매물 1 ================
# 거래: 매매
# 면적 : 84/59 (공급/전용)
# 가격: 165,000 (만원)
# 동 : 214동
# 층 : 고/23
# =========== 매물 2 ================
# ...

# [주의 사항]
# - 실습하는 시점에 위 매물이 없다면 다른 곳으로 대체 가능




# from email import header
# from selenium import webdriver
# # from bs4 import BeautifulSoup
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# browser = webdriver.Chrome()

# browser.get("https://www.naver.com/")

# browser.find_element_by_class_name("input_text").send_keys("검단 호반써밋")
# browser.find_element_by_class_name("btn_submit").click()


# browser.execute_script("window.scrollTo(0, 1900);")
# browser.find_element_by_class_name("api_more_theme").click()
# browser.find_element_by_class_name("list_filter_btn").click()
# browser.find_element_by_link_text
# try:
#     elem = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='articleListArea']/div[1]/div")))    
#     print(elem.text)
# finally:
#     browser.quit()



import requests
from bs4 import BeautifulSoup

url = "https://new.land.naver.com/complexes/124847?ms=37.595666,126.709328,17&a=APT:JGC:ABYG&e=RETAIL"
headers = {"user-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

c = soup.find("div", attrs={"class": "item_area"})
print(c)

# with open("quiz.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())