from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://naver.com")

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem= browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_class_name("id").send_keys("bom1215")
browser.find_element_by_class_name("pw").send_keys("john1402!")


# 4. 로그인 버튼 클릭 
browser.find_element_by_class_id("log.login")
browser.click()