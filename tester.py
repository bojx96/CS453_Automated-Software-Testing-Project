import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import os
import time
# Class used to handle routes.txt
class TextParser():
    def __init__(self) -> None:
        self.__tuples = []
    
    def readText(self, filename):
        with open(filename) as file:
            lines = file.read().splitlines()
        for line in lines:
            line = tuple(line.split(","))
            self.__tuples.append(line)
    def getTuples(self):
        return self.__tuples
    
class FileParser():
    def __init__(self) -> None:
        self.dictionary = {} # {element : {pages found}}
        self.paths = {} # {"page_from" : {(button, page_to_go )}, ....}
        self.error_redirections = {} # {(from_page, page_to_go) : button1, ....} this to store all buttons that don't work
        self.succ_covered_paths = 0
        self.failed_paths = 0
    def add_path_keys(self, url):
        self.paths[url] = set()
        
    def handleTuples(self, list_of_tups):
        # print(self.dictionary)
        for (element_id, pagename) in list_of_tups:
            if element_id in self.dictionary:
                pages = self.dictionary[element_id]
                pagename = (f"http://localhost:3000/{pagename}") if pagename != "root" else "http://localhost:3000"
                # print(f"{element_id} in pages {pages}")
                for page in pages:
                    self.paths[page].add((element_id,pagename))
    
    def get_elements(self, soup, name):
        return soup.find_all(name)

    def parsing_elements(self, filename):
        with open(filename) as file:
            html_data = file.read()
        soup = BeautifulSoup(html_data, 'html.parser')
        resulted_list = []
        for el in search_list:
            objects = self.get_elements(soup, el)
            for obj in objects:
                resulted_list.append((el, obj['id']))
        return resulted_list

    def startDriver(self):
        return webdriver.Chrome()
    
    def append_dictionary(self, element, url):
        if element not in self.dictionary:
            self.dictionary[element] = [url]
        else:
            self.dictionary[element].append(url)

    def check_elements(self, driver, url, elements):
        self.add_path_keys(url)
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
                
                self.append_dictionary(id, url)

            except Exception as e:
                test_cases[test_counter] = (e, tag_type, id)

            test_counter += 1
        return test_cases

    def output_results(self, test_cases, url):
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

    def beautify(self, path):
        res = ""
        for i in range(len(path)):
            page = path[i]
            res += page + " "
            if i != len(path) - 1:
                res += "-> "
        return res

    def path_coverage(self, driver, cur_page, used_edges):
        driver.get(cur_page)
        end_path = True #flag to check that the current page is the end of path
        for (button_id, to_page) in self.paths[cur_page]:
            if (cur_page, button_id, to_page) in used_edges: #checking that this edge already used in current path
                continue
            end_path = False
            elem = driver.find_element(By.ID, button_id)
            elem.click()
            new_page = driver.current_url #page after clicking on button
            used_edges.add((cur_page, button_id, to_page))
            if new_page != to_page: 
                #print(f"Button {button_id} doesn't work on page with url {cur_page} to redirect to page {to_page}")
                self.error_redirections[(cur_page, to_page)] = button_id #remember the errorous button
                driver.get(cur_page)
                self.failed_paths += 1
            else:
                #print(f"Redirection from {cur_page} to {new_page} is successful!")
                self.path_coverage(driver, new_page, used_edges) #call recursion for next_page
                driver.get(cur_page)
            used_edges.remove((cur_page, button_id, to_page))
        if end_path:
            self.succ_covered_paths += 1
# do sth to the inputs

if __name__ == "__main__":
    # MVP2
    search_list = ["input", "button"]
    parser = argparse.ArgumentParser("Input")

    # add the arguments
    parser.add_argument('-p', '--path', type=str, required=False)
    parser.add_argument('-u', '--url', type=str, required=True)
    parser.add_argument('-f', '--folder', type = str, required= False)
    parser.add_argument('-t', '--text', type = str, required = False )
    
    
    # get the inputs
    args = parser.parse_args()
    fileParser = FileParser()
    driver = fileParser.startDriver()
    if args.folder and args.url:
        for filename in os.listdir(args.folder):
            file_path = os.path.join(args.folder, filename)
            if os.path.isfile(file_path): 
                # Check if it's a file (not a subdirectory)
                elements_to_find = fileParser.parsing_elements(file_path)
                if filename == "root.html":
                    test_cases = fileParser.check_elements(
                        driver, args.url, elements_to_find)
                    # print(fileParser.dictionary)
                    fileParser.output_results(test_cases, args.url)
                else:
                    route_name = filename.split('.')[0]
                    url = args.url + "/" + route_name
                    test_cases = fileParser.check_elements(
                        driver, url, elements_to_find)
                    # print(fileParser.dictionary)
                    fileParser.output_results(test_cases, url)
        
    # mvp2 -> includes txt
    if args.text:
        textParser = TextParser()
        textParser.readText(args.text)
        tuples = textParser.getTuples()
        fileParser.handleTuples(tuples)
        # In order to get the paths, access fileParser.paths
        #print(fileParser.paths)
        fileParser.path_coverage(driver, args.url, set())
        print(f"Errors appered here: {fileParser.error_redirections}")
        print(f"Successfully covered paths: {fileParser.succ_covered_paths}")
        print(f"Failed paths: {fileParser.failed_paths}")
        #print(f"All paths list: {fileParser.succ_covered_paths}")
        '''
        {'http:localhost:3000': {('loginbutton-button', 'http:localhost:3000/homepage'), ('createaccount-button', 'http:localhost:3000/create')},
        'http:localhost:3000/homepage': {('mail-button', 'http:localhost:3000/mail'), ('settings-button', 'http:localhost:3000/settings'), ('signout-button', 'http:localhost:3000'), ('home-button', 'http:localhost:3000/homepage')},
        'http:localhost:3000/create': {('registercancel-button', 'http:localhost:3000'), ('registeraccount-button', 'http:localhost:3000')},
        'http:localhost:3000/mail': {('mail-button', 'http:localhost:3000/mail'), ('settings-button', 'http:localhost:3000/settings'), ('signout-button', 'http:localhost:3000'), ('home-button', 'http:localhost:3000/homepage')}, 
        'http:localhost:3000/settings': {('changesubmit-button', 'http:localhost:3000/settings'), ('settings-button','http:localhost:3000/settings'), ('signout-button', 'http:localhost:3000'), ('home-button', 'http:localhost:3000/homepage'), ('mail-button', 'http:localhost:3000/mail')}}
        '''
    elif args.path and args.url:
        elements = fileParser.parsing_elements(args.path)
        results = fileParser.check_elements(driver, args.url, elements)
        fileParser.output_results(results, args.url)

