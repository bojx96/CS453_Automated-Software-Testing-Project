import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

search_list = ["input", "button"]
parser = argparse.ArgumentParser("Input")

# add the arguments
parser.add_argument('-p', '--path', type=str, required=True)
parser.add_argument('-u', '--url', type=str, required=True)

# get the inputs
args = parser.parse_args()

def get_elements(soup, name):
    return soup.find_all(name)

def parsing_elements(filename):
    with open(filename) as file:
        html_data = file.read()
    soup = BeautifulSoup(html_data, 'html.parser')
    resulted_list = []
    for el in search_list:
        objects = get_elements(soup, el)
        for obj in objects:
            resulted_list.append((el, obj['id']))
    return resulted_list

# do sth to the inputs
if args.path and args.url:
    elements = parsing_elements(args.path)
    driver = webdriver.Chrome()
    print(args.url)
    driver.get(args.url)
    test_cases = []
    for element in elements:
        test_cases.append('F')

    test_counter = 0
    for tup in elements:
        tag_type, id = tup[0], tup[1]
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.ID, id)))  # Making sure website is loaded first
            elem = driver.find_element(By.ID, id)
            # if elem.tag_name != tag_type:
            #     raise Exception("tag_name of element is not the same as defined element!")
            # else:
            #     test_cases[test_counter] = 'T'
            test_cases[test_counter] = 'T'
            test_counter += 1
        except Exception as e:
            print(f"Exception Occured: {e}")

    for bool1 in test_cases:
        if bool1 == 'T':
            print("\033[92mP", end="")
        else:
            print("\033[91mF", end="")
    print("\033[0m")
