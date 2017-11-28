from lxml import etree
import lxml
from io import StringIO, BytesIO
from bs4 import BeautifulSoup
from bs4 import Comment
import requests
import random
import datetime
from collections import namedtuple
import re
import sys

course_info_class = namedtuple('CourseInfo', ['name', 'lang', 'date_start', 'weeks_number', "rating"])



# parser = etree.XMLParser(recover=True)
# courses_list_xml = etree.parse(f, parser)
# courses_list = [b.text for b in courses_list_xml.iter() if b.text.strip()]
# courses_list = random.sample(courses_list, 20)


def get_random_courses_list(courses_xml, tag='loc'):
    soup = BeautifulSoup(courses_xml, 'lxml')
    return random.sample([url.string for url in soup.find_all(tag, string=True)], 20)


def get_courses_xml(url = 'https://www.coursera.org/sitemap~www~courses.xml', courses_limit = 20):
    headers = {'User-agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip'}
    try:
        return requests.get(url, headers=headers).text
    except ConnectionError:
        return None


def get_course(course_url):
    # headers = {'User-agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip', 'Connection': 'keep-alive',
    #            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3'}
    headers = {'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
               'Connection': 'keep-alive'}
    try:
        return requests.get(course_url, headers=headers)
    except ConnectionError:
        return None


def utf8_encode(txt, encoding):
    return bytes(txt, encoding).decode('utf-8')


def get_open_repo_issues_list(repo_owner, repo_name):
    repo_issues_dict = requests.get('https://api.github.com/repos/{}/{}/issues'.format(repo_owner, repo_name)).json()
    return [repo_issue for repo_issue in repo_issues_dict if 'pull_request' not in repo_issue]


def get_course_info(course_url='https://www.coursera.org/learn/data-scientists-tools'):
    course_info_dict = {}
    # course_page = requests.get(course_url, headers=headers)
    # название, язык, ближайшую дату начала, количество недель и среднюю оценку.
    course_response = get_course(course_url)
    if course_response:
        soup = BeautifulSoup(course_response.text, 'lxml')
        course_info_dict['name'] = soup.find('h1', {'class': 'title display-3-text'}).string
        course_info_dict['lang'] = soup.find("div", attrs={"class": "rc-Language"}).contents[1]
        course_info_dict['start_date'] = \
            soup.find('div', {"class": "startdate rc-StartDateString caption-text"}).span.string
        # course_info_dict['weeks_number'] = soup.find('td', {'class': 'td-data'}).string

        course_info_dict['weeks_number'] = soup.find("td", string="Выполнение").next_siblings("td")
        # half_scores = soup.find('div', {"class": "rc-CourseRatingIcons"}).\
        #     find_all('i','c-course-rating-icon cif-star-half-empty')
        # scores = soup.find('div', {"class": "rc-CourseRatingIcons"}).find_all('i', 'c-course-rating-icon cif-star')
        # course_info_dict['rating'] = len(scores) + len(half_scores) / 2
        course_info_dict['rating'] = soup.find("div", "ratings-text bt3-hidden-xs").contents[1]
        course_info_dict['rating'] = re.findall(r'\d{1}.?\d?', course_info_dict['rating'])[0]
        print(course_info_dict)

        # return repository_info_class(repo['owner']['login'], repo['name'], repo["html_url"],
        #                           get_open_repo_issues_list(repo['owner']['login'], repo['name']))
        # print(course_html.status_code)  #Код ответа
        # print(course_html.headers) #Заголовки ответа

        # return {key: utf8_encode(value, course_response.encoding) for key, value in course_info_dict.items()}
    else:
        return "Проверьте состояние подключения"
    # rating = soup.find_all('i', 'c-course-rating-icon cif-star')



    #data-reactid="211"

    # print(utf8_encode(title1.text, response.encoding))
    # print(utf8_encode(weeks_number, response.encoding))
    # print(utf8_encode(start, response.encoding))
    # print(rating)
    # print(utf8_encode(weeks_number, response.encoding))

    # print(weeks_number.text)
    # datetime.strptime(start.text[],"%b %d")


def output_courses_info_to_xlsx(filepath):
    pass


if __name__ == '__main__':
    pass


if __name__ == '__main__':
    # print(get_courses_list())

    # print(courses_xml)
    # soup = BeautifulSoup(response.text, 'lxml')

    # courses_xml = get_courses_xml()
    # print(get_random_courses_list(courses_xml))

    get_course_info()
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

