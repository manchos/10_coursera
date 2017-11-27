from lxml import etree
import lxml
from io import StringIO, BytesIO
from bs4 import BeautifulSoup
import requests
import random
import datetime
from collections import namedtuple

course_info_class = namedtuple('CourseInfo', ['name', 'language', 'date_start',])

courses_list = ''


# parser = etree.XMLParser(recover=True)
# courses_list_xml = etree.parse(f, parser)
# courses_list = [b.text for b in courses_list_xml.iter() if b.text.strip()]
# courses_list = random.sample(courses_list, 20)


def get_random_courses_list(courses_xml, tag='loc'):
    soup = BeautifulSoup(courses_xml, 'lxml')
    return [url.string for url in soup.find_all(tag, string=True)]


def get_courses_xml(url = 'https://www.coursera.org/sitemap~www~courses.xml', courses_limit = 20):
    # url ='https://www.coursera.org/learn/abdomen-anatomy'
    headers = {'User-agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip'}
    try:
        return requests.get(url, headers=headers).text
    except ConnectionError:
        return None


def get_course_info(course_slug):
    pass


def output_courses_info_to_xlsx(filepath):
    pass


if __name__ == '__main__':
    pass


if __name__ == '__main__':
    # print(get_courses_list())


    courses_xml = get_courses_xml()
    # print(courses_xml)
    # soup = BeautifulSoup(response.text, 'lxml')
    print(get_random_courses_list(courses_xml))

    # print(response.encoding)
    # print(response.status_code)  # Код ответа
    # print(response.headers) # Заголовки ответа



    # aa = [i for i in soup.root]
    # get_random_courses_list
    # courses_url_list = soup.find_all('loc', string=True)

    # courses_url_list = [url.string for url in soup.find_all('loc', string=True)]

    # title = soup.select('div.title.display-3-text')[0]
    # title1 = soup.find('div', {'class': 'title display-3-text'})
    # start = soup.find_all(attrs={"data-reactid": "82"})[0]
    # weeks_number = soup.find_all(attrs={"data-reactid": "211"})[0]
    # #data-reactid="211"
    # print(start.text)
    # print(weeks_number.text)
    # # datetime.strptime(start.text[],"%b %d")