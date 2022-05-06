from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() #창 최대화

url = "https://flight.naver.com/"
browser.get(url)  #url로 이ㅗㅇ

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((BY.XPATH, "")))
    #성공했을 때 동작 수행
    print(elem.text) # 첫번째 결과 출력

finally:
    browser.quit()
