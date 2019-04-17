from ipdb import set_trace, launch_ipdb_on_exception
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import json
import sys
import copy


# from manually checking the Booking.com website
SCORE_TYPES = ['staff', 'commodities', 'cleanliness', 'confort', 'price/quality', 'location', 'free-wifi']


def scrape_listing(driver, url):
    """From a driver and url fetch important that and save it in a json file."""
    driver.get(url)
    time.sleep(2)   # should be better than this but for now it serves its purpose

    # get main fields
    acco_fields = dict()
    acco_fields['name'] = driver.find_element_by_class_name('hp__hotel-name').text.lower()
    acco_fields['address'] = driver.find_element_by_class_name('hp_address_subtitle').text

    # try to get different score metrics
    if driver.find_elements_by_css_selector('.bui-review-score__badge'):
        acco_fields['score_global'] = driver.find_element_by_class_name('bui-review-score__badge').text
        driver.find_element_by_class_name('big_review_score_detailed').click()
        # wait for score page to appear
        WebDriverWait(driver, 1, poll_frequency=0.1).\
            until(lambda drv: len(drv.find_elements_by_css_selector('.v2_review-scores__wrapper')) > 0)
        for index_score, name in enumerate(driver.find_elements_by_css_selector('.c-score-bar__score')):
            acco_fields['score_' + SCORE_TYPES[index_score]] = name.get_attribute('innerHTML')

    # read licenses and insert each one of them as a unique listing
    licenses = driver.find_element_by_id("hp_important_info_box").find_element_by_tag_name("strong").text.split(",")
    for lic in licenses:
        obj = copy.deepcopy(acco_fields)
        obj['license'] = lic
        # print(obj)
        json.dump(obj, open('booking_new/json_data_%d_%d.json' % (index_start, size), 'a+'))


if __name__ == '__main__':

    # gather which indexes to read and load all urls
    index_start, size = list(map(int, sys.argv[1:]))
    urls = json.load(open('json_data.json', 'r'))

    ff_driver = webdriver.Firefox()
    for index, url_to_fetch in enumerate(urls):
        if not (index_start <= index <= index_start + size):
            continue
        # try to scrape listing, failing should only warn the user
        try:
            print('Listing :' + str(index))
            scrape_listing(ff_driver, url_to_fetch)
        except Exception:
            print("Error parsing %d from json_data_%d_%d" % (index, index_start, size))

