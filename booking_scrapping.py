from ipdb import set_trace, launch_ipdb_on_exception
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def scrape_accomodation_data(driver, url):

    driver.get(url)
    acco_fields = dict()



    print("ola")



driver = webdriver.Firefox()
driver.get('http://booking.com')
driver.find_element_by_css_selector("#ss").send_keys("Porto")
WebDriverWait(driver, 1, poll_frequency=0.1).\
    until(lambda drv: len(drv.find_elements_by_css_selector(".sb-searchbox__button")) > 0)
driver.find_element_by_css_selector(".sb-searchbox__button").click()

WebDriverWait(driver, 1, poll_frequency=0.1).\
    until(lambda drv: len(drv.find_elements_by_css_selector("div.sr_item")) > 0)


urls = list()
data = list()

# get the url
for link in driver.find_elements_by_css_selector("div.sr_item"):
    hotel_title = link.find_element_by_class_name("sr-hotel__title")
    urls.append(hotel_title.find_element_by_class_name("hotel_name_link").get_attribute("href"))

# get the data
for url in urls:
    scrape_accomodation_data(driver, url)


set_trace()




# String selectLinkOpeninNewTab = Keys.chord(Keys.CONTROL,Keys.RETURN);
# driver.findElement(By.linkText("urlLink")).sendKeys(selectLinkOpeninNewTab);






set_trace()

driver.execute_script("window.scrollTo(0, 3750);")


driver.find_element_by_css_selector(".paging-next").click()



WebDriverWait(driver, 1, poll_frequency=1).\
    until(lambda drv: len(drv.find_elements_by_css_selector("div.sr_item")) > 0)


for link in driver.find_elements_by_css_selector("div.sr_item"):
    # arr.append(link.text)
    # print(link.text)
    print("BAMUS22222")



set_trace()

# driver.find_element_by_css_selector("#availcheck").click()
# driver.find_element_by_css_selector("#searchbox_btn").submit()


set_trace()


# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Firefox()
# driver.get('http://booking.com')
# driver.find_element_by_css_selector("#destination").send_keys("Berlin")
# WebDriverWait(driver, 1, poll_frequency=0.1).\
#     until(lambda drv: len(drv.find_elements_by_css_selector("ul.ui-autocomplete li")) > 0)
# driver.find_element_by_css_selector("ul.ui-autocomplete li").click()
# driver.find_element_by_css_selector("#availcheck").click()
# driver.find_element_by_css_selector("#searchbox_btn").submit()
# for link in driver.find_elements_by_css_selector("a.hotel_name_link"):
#     print(link.text)