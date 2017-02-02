from lxml import etree
import lxml
from io import StringIO, BytesIO
from bs4 import BeautifulSoup
import requests
import random


def get_courses_list():
    parser = etree.XMLParser(recover=True)
    with urllib.request.urlopen('https://www.coursera.org/sitemap~www~courses.xml') as f:
        courses_list_xml = etree.parse(f, parser)
    courses_list = [b.text for b in courses_list_xml.iter() if b.text.strip()]
    courses_list = random.sample(courses_list, 20)
    return courses_list


def get_course_info(course_slug):
    pass


def output_courses_info_to_xlsx(filepath):
    pass


if __name__ == '__main__':
    pass


if __name__ == '__main__':
    # print(get_courses_list())

    url ='https://www.coursera.org/learn/abdomen-anatomy'
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    print(response.status_code)  # Код ответа
    print(response.headers) # Заголовки ответа
    # print(response.content) # Тело ответа
    soup = BeautifulSoup(response.text, 'lxml')
    title = soup.select('.title .display-3-text')
    title1 = soup.find('div', {'class': 'title display-3-text'})
    # title = soup.find_all("div", class_="title display-3-text")
    print(title1.text)
