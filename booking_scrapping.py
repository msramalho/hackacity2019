from ipdb import set_trace, launch_ipdb_on_exception
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import json


# url from manually searching Porto in Booking.com and adjusting search parameters (we ran with different params)
URL_FIRST_PAGE = 'https://www.booking.com/searchresults.pt-pt.html?aid=304142&label=gen173nr-1DCBkoggI46AdIM1gEaLsBiAEBmAEfuAEHyAEM2AED6AEB-AEDiAIBqAIDuAKExZHlBcACAQ&sid=281ee05b273f22e353263ae744fe0913&tmpl=searchresults&class_interval=1&dest_id=-2173088&dest_type=city&from_sf=1&group_adults=2&group_children=0&label_click=undef&nflt=ht_id%3D201%3Bht_id%3D216%3Bht_id%3D220%3Bht_id%3D203%3Bht_id%3D208%3Bht_id%3D222%3B&no_rooms=1&percent_htype_apt=1&raw_dest_type=city&room1=A%2CA&sb_price_type=total&shw_aparth=1&slp_r_match=0&srpvid=7f5c444c6a3600ae&ss=Porto&ssb=empty&ssne=Porto&ssne_untouched=Porto&order=distance_from_search'


# initiate driver and get the first result page
ff_driver = webdriver.Firefox()
ff_driver.get(URL_FIRST_PAGE)

# wait for page to load
WebDriverWait(ff_driver, 1, poll_frequency=0.1). \
    until(lambda drv: len(drv.find_elements_by_css_selector("div.sr_item")) > 0)


i = 0
urls = list()
while True:

    # get the urls in this page and store them
    for link in ff_driver.find_elements_by_css_selector("div.sr_item"):
        hotel_title = link.find_element_by_class_name("sr-hotel__title")
        urls.append(hotel_title.find_element_by_class_name("hotel_name_link").get_attribute("href"))

    # going to the next page, when that fails, store urls collected
    next_page = None
    try:
        next_page = ff_driver.find_element_by_css_selector(".paging-next")
    except:
        json.dump(urls, open("json_data.json", "a"))
        break

    # repeat for next page
    url = next_page.get_attribute("href")
    ff_driver.get(url)
    WebDriverWait(ff_driver, 1, poll_frequency=1). \
        until(lambda drv: len(drv.find_elements_by_css_selector("div.sr_item")) > 0)

    print(i)
    i += 1
