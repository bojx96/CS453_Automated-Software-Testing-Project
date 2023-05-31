import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import os


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

def startDriver():
    return webdriver.Chrome()

def check_elements(driver, url, elements):
    driver.get(url)
    test_cases = []
    for _ in elements:
        test_cases.append('F')

    test_counter = 0
    for tup in elements:
        tag_type, id = tup[0], tup[1]
        try:
            element = WebDriverWait(driver, 2).until(EC.presence_of_element_located(
                (By.ID, id)))  # Making sure website is loaded first
            elem = driver.find_element(By.ID, id)
            # if elem.tag_name != tag_type:
            #     raise Exception("tag_name of element is not the same as defined element!")
            # else:
            #     test_cases[test_counter] = 'T'
            test_cases[test_counter] = 'T'

        except Exception as e:
            test_cases[test_counter] = (e, tag_type, id)

        test_counter += 1
    return test_cases

def output_results(test_cases, url):
    no_of_true = test_cases.count('T')
    test_counter = len(test_cases)
    print(f"--------Test cases in {url}--------", end="\n\n")
    print(
        f"\033[92m{no_of_true}\u001b[37m/{test_counter} tests passed", end="\n\n")
    print(
        f"\033[91m{test_counter - no_of_true}\u001b[37m tests failed", end="\n\n")
    if no_of_true < test_counter:
        print(f"--------Failed tests in {url}--------", end="\n\n")
    for result in test_cases:
        if isinstance(result[0], Exception):
            if isinstance(result[0], TimeoutException):
                print(
                    f"TimeoutException occured, no such element of type {result[1]} with id {result[2]} was found", end="\n\n")
            else:
                print(f"Exception Occured: {result[0]}")
                print(type(result[0]), end="\n\n")
    print("---------------------------", end="\n\n")
        
    
# do sth to the inputs

if __name__ == "__main__":
    # MVP2
    search_list = ["input", "button"]
    parser = argparse.ArgumentParser("Input")

    # add the arguments
    parser.add_argument('-p', '--path', type=str, required=False)
    parser.add_argument('-u', '--url', type=str, required=True)
    parser.add_argument('-f', '--folder', type = str, required= False)
    
    # get the inputs
    args = parser.parse_args()
    driver = startDriver()
    if args.folder and args.url:
        for filename in os.listdir(args.folder):
            file_path = os.path.join(args.folder, filename)
            if os.path.isfile(file_path): 
                # Check if it's a file (not a subdirectory)
                elements_to_find = parsing_elements(file_path)
                if filename == "root.html":
                    test_cases = check_elements(driver, args.url, elements_to_find)
                    output_results(test_cases, args.url)
                else:
                    route_name = filename.split('.')[0]
                    url = args.url + "/" + route_name
                    test_cases = check_elements(driver, url, elements_to_find)
                    output_results(test_cases, url)
                    
                    
    elif args.path and args.url:
        elements = parsing_elements(args.path)
        results = check_elements(driver, args.url, elements)
        output_results(results, args.url)

