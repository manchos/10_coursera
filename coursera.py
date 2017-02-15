from lxml import etree
import lxml
from io import StringIO, BytesIO
from bs4 import BeautifulSoup
import requests
import random
import datetime
from collections import namedtuple
import sys

course_info_class = namedtuple('CourseInfo', ['name', 'language', 'date_start',])


def get_courses_list():
    parser = etree.XMLParser(recover=True)
    with urllib.request.urlopen('https://www.coursera.org/sitemap~www~courses.xml') as f:
        courses_list_xml = etree.parse(f, parser)
    courses_list = [b.text for b in courses_list_xml.iter() if b.text.strip()]
    courses_list = random.sample(courses_list, 20)

    return courses_list

def utf8_encode(txt,encoding):
    return bytes(txt, encoding).decode('utf-8')

def get_course_info(course_slug):
    pass


def output_courses_info_to_xlsx(filepath):
    pass


if __name__ == '__main__':
    pass


if __name__ == '__main__':
    # print(get_courses_list())

    url ='https://www.coursera.org/learn/abdomen-anatomy'
    headers = {'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0', 'Connection': 'keep-alive'}
    response = requests.get(url, headers=headers)
    print(response.encoding)
    print(response.status_code)  # Код ответа
    print(response.headers) # Заголовки ответа


    soup = BeautifulSoup(response.text, 'lxml')
    # title = soup.select('div.title.display-3-text')[0]
    title1 = soup.find('h1', {'class': 'title display-3-text'})
    # start = soup.find_all(attrs={"data-reactid": "86"})[0]
    start = soup.find('div', {"class": "startdate rc-StartDateString caption-text"}).span.string
    weeks_number = soup.find('td', {"class": "td-data"}).string

    # rating = soup.find_all('i', 'c-course-rating-icon cif-star')
    scores = soup.find('div', {"class": "rc-CourseRatingIcons"}).find_all('i', 'c-course-rating-icon cif-star')
    half_scores = soup.find('div', {"class": "rc-CourseRatingIcons"}).find_all('i', 'c-course-rating-icon cif-star-half-empty')
    rating = len(scores)+len(half_scores)/2
    #data-reactid="211"
    print(utf8_encode(title1.text, response.encoding))
    print(utf8_encode(weeks_number, response.encoding))
    print(utf8_encode(start, response.encoding))
    print(rating)
    # print(weeks_number.text)
    # datetime.strptime(start.text[],"%b %d")