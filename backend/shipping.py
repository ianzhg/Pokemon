import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import zipcodes
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
import logging
import re
import time

chrome_driver_path = ChromeDriverManager().install()
def function_runner(function, cards, jp_zipcode, us_zipcode, attempts = 2):
    for _ in range(attempts):
        try:
            return function(cards, jp_zipcode, us_zipcode)
        except Exception as err:
            pass
    return {"error":"timeout, try another time"}

def get_japan_prefecture(postal_code):
    base_url = "https://zipcloud.ibsnet.co.jp/api/search"
    response = requests.get(base_url, params={"zipcode": postal_code})
    data = response.json()

    if data["status"] == 200 and data["results"]:
        return data["results"][0]["address1"]
    else:
        return None

def translate_prefecture_to_english(prefecture):
    prefecture_map = {
        "北海道": "Hokkaido",
        "青森県": "Aomori",
        "岩手県": "Iwate",
        "宮城県": "Miyagi",
        "秋田県": "Akita",
        "山形県": "Yamagata",
        "福島県": "Fukushima",
        "茨城県": "Ibaraki",
        "栃木県": "Tochigi",
        "群馬県": "Gunma",
        "埼玉県": "Saitama",
        "千葉県": "Chiba",
        "東京都": "Tokyo",
        "神奈川県": "Kanagawa",
        "新潟県": "Niigata",
        "富山県": "Toyama",
        "石川県": "Ishikawa",
        "福井県": "Fukui",
        "山梨県": "Yamanashi",
        "長野県": "Nagano",
        "岐阜県": "Gifu",
        "静岡県": "Shizuoka",
        "愛知県": "Aichi",
        "三重県": "Mie",
        "滋賀県": "Shiga",
        "京都府": "Kyoto",
        "大阪府": "Osaka",
        "兵庫県": "Hyogo",
        "奈良県": "Nara",
        "和歌山県": "Wakayama",
        "鳥取県": "Tottori",
        "島根県": "Shimane",
        "岡山県": "Okayama",
        "広島県": "Hiroshima",
        "山口県": "Yamaguchi",
        "徳島県": "Tokushima",
        "香川県": "Kagawa",
        "愛媛県": "Ehime",
        "高知県": "Kochi",
        "福岡県": "Fukuoka",
        "佐賀県": "Saga",
        "長崎県": "Nagasaki",
        "熊本県": "Kumamoto",
        "大分県": "Oita",
        "宮崎県": "Miyazaki",
        "鹿児島県": "Kagoshima",
        "沖縄県": "Okinawa"
    }
    return prefecture_map.get(prefecture, None)

def find_jp_state(postal_code):
    return translate_prefecture_to_english(get_japan_prefecture(postal_code))

def get_us_state(postal_code):
    state_abbrev_to_name = {
        'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California', 'CO': 'Colorado',
        'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho',
        'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana',
        'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi',
        'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
        'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma',
        'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota',
        'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington',
        'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'
    }

    zipcode_info = zipcodes.matching(postal_code)
    if zipcode_info:
        state_abbrev = zipcode_info[0]["state"]
        return state_abbrev_to_name.get(state_abbrev, None)
    else:
        return None

def find_element_text(driver, xpath):
    try:
        element = driver.find_element("xpath", xpath)
        return element.text.strip()
    except Exception as err:
        return ""

    
def japan_post(cards, jp_zipcode = "120-0011", us_zipcode = "90001"):
    chrome_driver_path = ChromeDriverManager().install()
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path = chrome_driver_path, options = chrome_options)

    #     # Open the Japan Post website
    url = "https://www.post.japanpost.jp/cgi-charge/index.php?lang=_en"
    driver.get(url)

    type_element = driver.find_element("xpath", "/html/body/div[1]/div[3]/div/div[1]/div/div[2]/form/dl[1]/dd/ul/li[1]/label")
    type_element.click()

    weight_element = driver.find_element("xpath", "/html/body/div[1]/div[3]/div/div[1]/div/div[2]/form/dl[2]/dd/div/input")
    #each card weight 1.7 grams; with the case about 5 grams
    weight = int(cards) * 5
    weight_element.send_keys(str(weight))

    weight_button = driver.find_element("xpath", "/html/body/div[1]/div[3]/div/div[1]/div/div[2]/form/dl[2]/dd/ul[1]/li[1]/label")
    weight_button.click()

    shipping_from_element = driver.find_element("xpath", "/html/body/div[1]/div[3]/div/div[1]/div/div[2]/form/dl[3]/dd/div/select")
    shipping_select = Select(shipping_from_element)
    jp_prefecture = find_jp_state(jp_zipcode)
    shipping_select.select_by_visible_text(jp_prefecture)

    destination_country_element = driver.find_element("xpath", "/html/body/div/div[3]/div/div[1]/div/div[2]/form/dl[4]/dd/div[1]/select")
    dest_country_select = Select(destination_country_element)
    dest_country_select.select_by_visible_text("United States")
    # wait the state selection come out
    sleep(0.5)
    destination_state_element = driver.find_element("xpath", "/html/body/div/div[3]/div/div[1]/div/div[2]/form/dl[4]/dd/div[2]/select")
    dest_state_select = Select(destination_state_element)
    us_state = get_us_state(us_zipcode)
    dest_state_select.select_by_visible_text(us_state)

    weight_button = driver.find_element("xpath", "/html/body/div[1]/div[3]/div/div[1]/div/div[2]/form/div/input")
    weight_button.click()

    #start scraping all the shipping info
    info = {}
    shipping_info = driver.find_element("xpath", "/html/body/div[1]/div[3]/div/div[1]/div/div[1]/ul").text.strip()
    # shipping_info = shipping_info.text.strip().split("\n")

    fastest_way = driver.find_element("xpath", "/html/body/div[1]/div[3]/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/a")
    fastest_info = driver.find_element("xpath", "/html/body/div[1]/div[3]/div/div[1]/div/div[2]/div[2]/div[1]/div[2]/span")
    fastest_link = driver.find_element("xpath", "/html/body/div[1]/div[3]/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/a").get_attribute("href")

    info["shipping_info"] = shipping_info
    info["fastest_way"] = fastest_way.text.strip()
    info["fastest_way_cost_and_time"] = fastest_info.text.strip()
    info["fatstest_link"] = fastest_link
    
    method1 = find_element_text(driver, "/html/body/div/div[3]/div/div[1]/div/div[3]/div[1]/span")
    method1_cost = find_element_text(driver, "/html/body/div/div[3]/div/div[1]/div/div[3]/div[2]/div[1]/div[2]/table/tbody/tr/td[1]/span")
    method1_time = find_element_text(driver, "/html/body/div/div[3]/div/div[1]/div/div[3]/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/ul").split("\n")[0]

    method2 = find_element_text(driver, "/html/body/div/div[3]/div/div[1]/div/div[4]/div[1]/span")
    method2_cost = find_element_text(driver, "/html/body/div/div[3]/div/div[1]/div/div[4]/div[2]/div[1]/div[2]/table/tbody/tr/td[1]/span")
    method2_time = find_element_text(driver, "/html/body/div/div[3]/div/div[1]/div/div[4]/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/ul").split("\n")[0]

    method3 = find_element_text(driver, "/html/body/div/div[3]/div/div[1]/div/div[5]/div[1]/span")
    method3_cost = find_element_text(driver, "/html/body/div/div[3]/div/div[1]/div/div[5]/div[2]/div[1]/div[2]/table/tbody/tr/td[1]/span")
    method3_time = find_element_text(driver, "/html/body/div/div[3]/div/div[1]/div/div[5]/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/ul").split("\n")[0]


    info[method1] = (method1_cost + method1_time).replace("\n", "")
    info[method2] = (method2_cost + method2_time).replace("\n", "")
    info[method3] = (method3_cost + method3_time).replace("\n", "")
    driver.quit()
    return info

def DHL(cards, jp_zipcode = "120-0011", us_zipcode = "90001"):
    def accept_cookies(driver, accept_button_locator):
        wait = WebDriverWait(driver, 2)
        accept_button = wait.until(EC.element_to_be_clickable(accept_button_locator))
        accept_button.click()

    def wait_to_pop(driver, location):
        input_locator = (By.XPATH, location)
        accept_button = WebDriverWait(driver, 2).until(EC.visibility_of_element_located(input_locator))

    def click_on_empty_space(driver, x, y):
        action_chains = ActionChains(driver)
        action_chains.move_by_offset(x, y).click().perform()


    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path = chrome_driver_path, options=chrome_options)

    url = "https://www.dhl.com/jp-en/home/get-a-quote.html"
    driver.get(url)
    sleep(1.5)
    
    accept_button_locator = (By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
    accept_cookies(driver, accept_button_locator)

    # sleep(1)
    wait_to_pop(driver, '//*[@id="originZip"]')
    japan_postcode = driver.find_element("xpath", '//*[@id="originZip"]')
    japan_postcode.send_keys(jp_zipcode)

    dest = driver.find_element("xpath", "/html/body/div[7]/main/div[4]/div/div[2]/div/form/div[2]/fieldset[2]/div[2]/div[1]/div/div/div/div[2]/input")
    dest.click()
    dest.send_keys("United States of America")

    # sleep(1)
    dest_postcode = driver.find_element(By.ID, 'destinationZip')
    dest_postcode.send_keys(us_zipcode)

    wait_to_pop(driver, '//*[@id="tradelane-panel"]/form/div[3]/button')
    next_page = driver.find_element("xpath", '//*[@id="tradelane-panel"]/form/div[3]/button')
    next_page.click()

    click_on_empty_space(driver, 0, 0)
    sleep(1)
    next_page = driver.find_element("xpath", '//*[@id="tradelane-panel"]/form/div[3]/button')
    next_page.click()


    wait_to_pop(driver, '/html/body/div[7]/main/div[4]/div/form/div/div/div[1]/div[1]/div/div/div/input')
    weight_enter = driver.find_element("xpath",'/html/body/div[7]/main/div[4]/div/form/div/div/div[1]/div[1]/div/div/div/input')
    cards = int(cards)
    if cards <= 2:
        weight_enter.send_keys("0.01")
    else:
        weight = str(0.005 * cards)
        weight_enter.send_keys(weight)


    length_size = driver.find_element("xpath",'//*[@id="length-0"]')
    length_size.send_keys("15")
    width_size = driver.find_element("xpath",'//*[@id="width-0"]')
    width_size.send_keys("10")
    height_size = driver.find_element("xpath",'//*[@id="height-0"]')
    height_size.send_keys("5")
    get_quote = driver.find_element("xpath",'//*[@id="wcag-main-content"]/div[4]/div/form/div/div/div[4]/button')
    get_quote.click()
    sleep(2)

    info = {}
    shipment_date = driver.find_element("xpath",'//*[@id="date-picker"]').get_attribute("value")
    info['shipment_date'] = shipment_date

    delivery_date = find_element_text(driver, '//*[@id="EXP_INTERNATIONAL_PRE_12PM_NONDOC-headline"]/p')
    info['delivery_date'] = delivery_date

    price = find_element_text(driver, '//*[@id="EXP_INTERNATIONAL_PRE_12PM_NONDOC-price"]/p[2]')
    info['price'] = price
    driver.quit()
    return info

def fedex(cards, jp_zipcode = "120-0011", us_zipcode = "90001"):
    def click_on_empty_space(driver, x, y):
        action_chains = ActionChains(driver)
        action_chains.move_by_offset(x, y).click().perform()

    def wait_to_pop(driver, location):
        input_locator = (By.XPATH, location)
        accept_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(input_locator))
        accept_button.click()
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path = chrome_driver_path, options=chrome_options)

    url = "https://www.fedex.com/en-us/home.html#"
    driver.get(url)

    check_rate = driver.find_element("xpath", '//*[@id="cubeOnePar"]/button')
    check_rate.click()
    wait_to_pop(driver, '/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/div/div/div/div/magr-root/div/div/fdx-purple-engine/fdx-loading-indicator/div[2]/div/div/div/magr-error/magr-locations-container/magr-error/fieldset/div[1]/div/magr-location/magr-autocomplete/magr-floating-label/div/div/span/input')

    shipping_from = driver.find_element("xpath", '/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/div/div/div/div/magr-root/div/div/fdx-purple-engine/fdx-loading-indicator/div[2]/div/div/div/magr-error/magr-locations-container/magr-error/fieldset/div[1]/div/magr-location/magr-autocomplete/magr-floating-label/div/div/span/input')
    shipping_from.send_keys("Japan")
    sleep(1)
    click_on_empty_space(driver, 0, 0)

    enter_own_add =  driver.find_element("xpath", '//*[@id="fromLocationMessages"]/div/button') 
    enter_own_add.click()
    shipping_from = driver.find_element("xpath", '//*[@id="null"]')
    shipping_from.send_keys("Japan")

    shipping_postal = driver.find_element("xpath", '//*[@id="fromPostcode"]')
    shipping_postal.click()
    #fake the detection from google
    shipping_postal.send_keys("1")
    sleep(1)
    click_on_empty_space(driver, 0, 0)
    shipping_postal = driver.find_element("xpath", '//*[@id="fromPostcode"]')
    shipping_postal.send_keys(jp_zipcode)

    shipping_to = driver.find_element("xpath", '//*[@id="toGoogleAddress"]')
    shipping_to.send_keys("United States")
    sleep(1)
    click_on_empty_space(driver, 0, 0)

    enter_own_add = driver.find_element("xpath", '//*[@id="toLocationMessages"]/div/button')
    enter_own_add.click()

    shippingto_postal = driver.find_element("xpath", '//*[@id="toPostcode"]')
    shippingto_postal.send_keys(us_zipcode)
    click_on_empty_space(driver, 0, 0)
    sleep(0.5)
    shippingto_postal = driver.find_element("xpath", '//*[@id="toPostcode"]')
    shippingto_postal.click()
    sleep(1)
    continue_button = driver.find_element("xpath", '//*[@id="main-container"]/div/fdx-purple-engine/fdx-loading-indicator/div[2]/div/div/div/magr-error/magr-locations-container/magr-error/fieldset/magr-error/div/button')
    continue_button.click()

    wait_to_pop(driver, '//*[@id="package-details__weight-0"]')
    weight = driver.find_element("xpath", '//*[@id="package-details__weight-0"]')
    cards = int(cards)
    if cards <= 4:
        weight.send_keys("0.02")
    else:
        new_key = str(0.005 * cards)
        weight.send_keys(new_key)

    length = driver.find_element("xpath", '//*[@id="package-details__dimensions-0"]/input[1]')
    length.send_keys("15")
    width = driver.find_element("xpath", '//*[@id="package-details__dimensions-0"]/input[2]')
    width.send_keys("10")
    height = driver.find_element("xpath", '//*[@id="package-details__dimensions-0"]/input[3]')
    height.send_keys("5")

    rate_button = driver.find_element("xpath", '//*[@id="e2ePackageDetailsSubmitButtonRates"]')
    rate_button.click()

    wait_to_pop(driver, '/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/div/div/div/div/magr-root/div/div/fdx-purple-engine/fdx-loading-indicator/div[2]/magr-rate-container/div/div/div/div/magr-rate-list/ul/li[1]/magr-rate/section/div/header/dl/dd')
    sleep(1)
    info = {}
    shipment_date = driver.find_element("xpath", '//*[@id="packageShipDate"]').text.strip().split("\n")[0]
    info['shipment_date'] = shipment_date

    arrive_date = find_element_text(driver, '/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/div/div/div/div/magr-root/div/div/fdx-purple-engine/fdx-loading-indicator/div[2]/magr-rate-container/div/div/div/div/magr-rate-list/ul/li[1]/magr-rate/section/div/header/dl/dd')
    time1 = find_element_text(driver, '/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/div/div/div/div/magr-root/div/div/fdx-purple-engine/fdx-loading-indicator/div[2]/magr-rate-container/div/div/div/div/magr-rate-list/ul/li[1]/magr-rate/section/div/ul/li[1]/div/dl/dd[1]')
    money1 = find_element_text(driver, '/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/div/div/div/div/magr-root/div/div/fdx-purple-engine/fdx-loading-indicator/div[2]/magr-rate-container/div/div/div/div/magr-rate-list/ul/li[1]/magr-rate/section/div/ul/li[1]/div/button[1]')
    info[arrive_date + " "+ time1] = money1

    time2 = find_element_text(driver, '/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/div/div/div/div/magr-root/div/div/fdx-purple-engine/fdx-loading-indicator/div[2]/magr-rate-container/div/div/div/div/magr-rate-list/ul/li[1]/magr-rate/section/div/ul/li[2]/div/dl/dd[1]')
    money2 = find_element_text(driver, '/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/div/div/div/div/magr-root/div/div/fdx-purple-engine/fdx-loading-indicator/div[2]/magr-rate-container/div/div/div/div/magr-rate-list/ul/li[1]/magr-rate/section/div/ul/li[2]/div/button[1]')
    info[arrive_date + " "+ time2] = money2

    time3 = find_element_text(driver, '/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/div/div/div/div/magr-root/div/div/fdx-purple-engine/fdx-loading-indicator/div[2]/magr-rate-container/div/div/div/div/magr-rate-list/ul/li[1]/magr-rate/section/div/ul/li[3]/div/dl/dd[1]')
    money3 = find_element_text(driver, '/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/div/div/div/div/magr-root/div/div/fdx-purple-engine/fdx-loading-indicator/div[2]/magr-rate-container/div/div/div/div/magr-rate-list/ul/li[1]/magr-rate/section/div/ul/li[3]/div/button[1]')
    info[arrive_date + " "+ time3] = money3

    arrive_date2 = find_element_text(driver, '/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/div/div/div/div/magr-root/div/div/fdx-purple-engine/fdx-loading-indicator/div[2]/magr-rate-container/div/div/div/div/magr-rate-list/ul/li[2]/magr-rate/section/div/header/dl/dd')
    time4 = find_element_text(driver, '/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/div/div/div/div/magr-root/div/div/fdx-purple-engine/fdx-loading-indicator/div[2]/magr-rate-container/div/div/div/div/magr-rate-list/ul/li[2]/magr-rate/section/div/header/dl/dd')
    money4 = find_element_text(driver, '/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/div/div/div/div/magr-root/div/div/fdx-purple-engine/fdx-loading-indicator/div[2]/magr-rate-container/div/div/div/div/magr-rate-list/ul/li[2]/magr-rate/section/div/ul/li/div/button[1]')
    info[arrive_date2 + " "+ time4] = money4

    driver.quit()
    return info

def is_valid_us_zipcode(zipcode: str) -> bool:
    pattern = re.compile(r'^\s{5}$')
    return bool(pattern.match(zipcode))

def is_valid_jp_zipcode(zipcode: str) -> bool:
    pattern = re.compile(r'^\s{3}-\s{4}$')
    return bool(pattern.match(zipcode))

def run_all(cards, jp_zipcode, us_zipcode):
    if is_valid_us_zipcode(us_zipcode):
        print("wrong us zipcode")
        return
    if is_valid_jp_zipcode(jp_zipcode):
        print("wrong japan zipcode")
        return


    print('japan_post')
    print('--------------------------------')
    res1 = function_runner(japan_post, cards, jp_zipcode, us_zipcode)
#     print(res1)
#     print('--------------------------------')
#     print('--------------------------------')
#     print('DHL')
#     print('--------------------------------')
    res2 = function_runner(DHL, cards, jp_zipcode, us_zipcode)
#     print(res2)
#     print('--------------------------------')
#     print('--------------------------------')
    print('fedex')
    print('--------------------------------')
    res3 = function_runner(fedex, cards, jp_zipcode, us_zipcode)
#     print(res3)
#     print('--------------------------------')
#     print('--------------------------------')
    return [res1, res2, res3]

