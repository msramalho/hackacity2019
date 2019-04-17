from ipdb import set_trace, launch_ipdb_on_exception
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import json
import selenium


def scrape_accomodation_data(driver, url):
    driver.get(url)
    time.sleep(5)

    acco_fields = dict()
    acco_fields['name'] = driver.find_element_by_class_name('hp__hotel-name').text.strip('Hotel')
    acco_fields['address'] = driver.find_element_by_class_name('hp_address_subtitle').get_attribute('data-bbox')

    # WebDriverWait(driver, 1, poll_frequency=0.1)\
    # .until(ExpectedConditions.presenceOfElementLocated(drv.find_element_by_class_name('bui-review-score__badge')) > 0)

    acco_fields['score'] = dict()
    if driver.find_elements_by_css_selector('.bui-review-score__badge'):
        acco_fields['score']['global'] = driver.find_element_by_class_name('bui-review-score__badge').text

        driver.find_element_by_class_name('big_review_score_detailed').click()

        WebDriverWait(driver, 1, poll_frequency=0.1). \
            until(lambda drv: len(drv.find_elements_by_css_selector('.v2_review-scores__wrapper')) > 0)
        # if driver.find_elements_by_css_selector('v2_review-scores__wrapper'):
        for name in driver.find_elements_by_css_selector('.c-score-bar__title'):
            print(name)
            acco_fields['score'][name.text] = 'ola'

    else:
        acco_fields['score']['global'] = -1

    print(acco_fields)


driver = webdriver.Firefox()
# driver.get('http://booking.com')
# driver.find_element_by_css_selector("#ss").send_keys("Porto")
# WebDriverWait(driver, 1, poll_frequency=0.1).\
#    until(lambda drv: len(drv.find_elements_by_css_selector(".sb-searchbox__button")) > 0)
# driver.find_element_by_css_selector(".sb-searchbox__button").click()

# driver.get(
#     'https://www.booking.com/searchresults.pt-pt.html?label=gen173nr-1DCBkoggI46AdIM1gEaLsBiAEBmAEfuAEHyAEM2AED6AEB-AEDiAIBqAIDuAKExZHlBcACAQ&sid=2a3e6938484fee9b46b1f05570830152&tmpl=searchresults&class_interval=1&dest_id=-2173088&dest_type=city&dtdisc=0&from_sf=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&shw_aparth=1&slp_r_match=0&src=index&srpvid=d868358750e901e2&ss=Porto&ss_all=0&ssb=empty&sshis=0&ssne=Porto&ssne_untouched=Porto&nflt=ht_id%3D201%3Bht_id%3D216%3Bht_id%3D220%3Bht_id%3D203%3Bht_id%3D208%3Bht_id%3D222%3B&percent_htype_apt=1&rsf=&rows=8000')

driver.get('https://www.booking.com/searchresults.pt-pt.html?aid=304142&label=gen173nr-1DCBkoggI46AdIM1gEaLsBiAEBmAEfuAEHyAEM2AED6AEB-AEDiAIBqAIDuAKExZHlBcACAQ&sid=281ee05b273f22e353263ae744fe0913&tmpl=searchresults&class_interval=1&dest_id=-2173088&dest_type=city&from_sf=1&group_adults=2&group_children=0&label_click=undef&nflt=ht_id%3D201%3Bht_id%3D216%3Bht_id%3D220%3Bht_id%3D203%3Bht_id%3D208%3Bht_id%3D222%3B&no_rooms=1&percent_htype_apt=1&raw_dest_type=city&room1=A%2CA&sb_price_type=total&shw_aparth=1&slp_r_match=0&srpvid=7f5c444c6a3600ae&ss=Porto&ssb=empty&ssne=Porto&ssne_untouched=Porto&order=distance_from_search')

WebDriverWait(driver, 1, poll_frequency=0.1). \
    until(lambda drv: len(drv.find_elements_by_css_selector("div.sr_item")) > 0)

i = 0
urls = list()
while True:

    data = list()

    # get the url
    for link in driver.find_elements_by_css_selector("div.sr_item"):
        hotel_title = link.find_element_by_class_name("sr-hotel__title")
        urls.append(hotel_title.find_element_by_class_name("hotel_name_link").get_attribute("href"))

    # get the data
    # for url in urls:
    # scrape_accomodation_data(driver, url)

    # going to the next page

    # driver.execute_script("window.scrollTo(0, 4500);")
    next_page = None
    try:
        next_page = driver.find_element_by_css_selector(".paging-next")
    except:
        json.dump(urls, open("json_data.json", "a"))
        break

    url = next_page.get_attribute("href")

    driver.get(url)

    WebDriverWait(driver, 1, poll_frequency=1). \
        until(lambda drv: len(drv.find_elements_by_css_selector("div.sr_item")) > 0)

    print(i)
    i += 1

# json.dump(urls, open("json_data.json", "w"))
# json.load(open())