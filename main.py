from selenium import webdriver
from dotenv import load_dotenv
import os


load_dotenv()

"""#################### CONFIGURATION ####################"""
LOGIN_URL = 'https://kurier.inpost.pl/'
LOGIN_DATA = {
    'LoginView2_Login1_UserName': os.getenv('USER_USERNAME'),
    'LoginView2_Login1_Password': os.getenv('USER_PASSWORD')
}
LOGIN_SUBMIT_ID = 'LoginView2_Login1_Button1_CD'

FORM_URL = 'https://kurier.inpost.pl/NewOrder.aspx?t=2'
FORM_DATA_FILE = 'dane.txt'
FORM_FIELDS_IDS = (
    'ctl00_ContentPlaceHolder1_ctl00_Company2_Panel1_txbName_I',
    'ctl00_ContentPlaceHolder1_ctl00_Company2_Panel1_txbPostCode_I',
    'ctl00_ContentPlaceHolder1_ctl00_Company2_Panel1_txbCity_I',
    'ctl00_ContentPlaceHolder1_ctl00_Company2_Panel1_pnlAddressPL_txbAddress_I',
    'ctl00_ContentPlaceHolder1_ctl00_Company2_Panel1_txbSurname_I',
    'ctl00_ContentPlaceHolder1_ctl00_Company2_Panel1_txbPhone_I'
)
FORM_CLICKS_LIST = (
    'ContentPlaceHolder1_ctl00_AdditionalServices1_UbezpieczenieCHB_S_D',
    'ctl00_ContentPlaceHolder1_ctl00_Serwis1_ID38_S_D'
)
"""#################### END CONFIGURATION ####################"""

with open(FORM_DATA_FILE, 'r', encoding='utf-8') as data:
    info = data.read()
    form_data = info.splitlines()

FORM_VALUES_DICT = dict(zip(FORM_FIELDS_IDS, form_data))
browser = webdriver.Firefox()


def fill_form(form_url, values_dict, clicks_list):
    browser.get(form_url)
    for element_id, value in values_dict.items():
        element = browser.find_element('id', element_id)
        element.send_keys(value)
    for element_id in clicks_list:
        browser.find_element('id', element_id).click()


if __name__ == '__main__':
    fill_form(LOGIN_URL, LOGIN_DATA, (LOGIN_SUBMIT_ID,))  # wypełniamy formularz logowania
    fill_form(FORM_URL, FORM_VALUES_DICT, FORM_CLICKS_LIST)
