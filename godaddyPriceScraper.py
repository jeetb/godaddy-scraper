from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

def scrapePrice(url):
    driver = webdriver.Chrome() 
    driver.get(url)
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "spin-results-wrap"))
        ) 
    except TimeoutException:
        raise

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser") # Also note I use the html.parser instead of lxml.
    price = soup.find('span', class_="main-price m-b-0 text-primary-o dpp-price dpp-price")
    return price

url = 'https://in.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck=bjmtuc.club'
print(scrapePrice(url))