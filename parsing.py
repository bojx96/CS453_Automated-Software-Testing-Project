from bs4 import BeautifulSoup

search_list = ["input", "button"]

def get_elements(soup, name):
    return soup.find_all(name)

def parsing(filename):
    with open(filename) as file:
        html_data = file.read()
    soup = BeautifulSoup(html_data, 'html.parser')
    resulted_list = []
    for el in search_list:
        objects = get_elements(soup, el)
        for obj in objects:
            resulted_list.append((el, obj['id']))
    return resulted_list