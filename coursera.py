from lxml import etree
import lxml
from io import StringIO, BytesIO
from bs4 import BeautifulSoup
from bs4 import Comment
import requests
import random
from datetime import datetime
from collections import namedtuple
import re
import requests_cache
import sys
import os
import argparse

course_info_class = namedtuple('CourseInfo',
                               ['name', 'url', 'lang', 'start_date', 'duration_in_weeks', 'rating'])

# parser = etree.XMLParser(recover=True)
# courses_list_xml = etree.parse(f, parser)
# courses_list = [b.text for b in courses_list_xml.iter() if b.text.strip()]
# courses_list = random.sample(courses_list, 20)


def get_random_courses_url_list(courses_xml, tag='loc'):
    soup = BeautifulSoup(courses_xml, 'lxml')
    return random.sample([url.string for url in soup.find_all(tag, string=True)], 20)


def get_courses_info_list(courses_url_list):
    return [get_course_info(course_url) for course_url in courses_url_list]


def get_courses_xml(url='https://www.coursera.org/sitemap~www~courses.xml'):
    headers = {'User-agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip'}
    try:
        return requests.get(url, headers=headers).text
    except (ConnectionError, requests.exceptions.ConnectionError) as exc:
        print(exc)
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


def get_course_start_datetime(soup):
    start_date_text = \
        soup.find('div', {'class': 'startdate rc-StartDateString caption-text'}).span.get_text()
    try:
        start_date_action_text = (start_date_text.split()[0])
        start_date = (start_date_text.split()[:-3:-1])
        start_datetime = datetime.strptime(' '.join(start_date), "%d %b")

        # determine the year
        if start_date_action_text == 'Начинается' and (start_datetime.month < datetime.now().month):
            start_datetime = start_datetime.replace(year=datetime.now().year + 1)
        else:
            start_datetime = start_datetime.replace(year=datetime.now().year)
        return start_datetime
    except ValueError:
        return start_date_text


def get_course_rating_numeric_value(soup):
    try:
        rating_text = soup.find("div", "ratings-text bt3-hidden-xs").contents[1]
        return re.findall(r'\d{1}.?\d?', rating_text)[0]
    except AttributeError:
        return None


def get_course_info(course_url='https://www.coursera.org/learn/gis-capstone'):
    course_response = get_course(course_url)
    if course_response:
        soup = BeautifulSoup(utf8_encode(course_response.text, course_response.encoding), 'lxml')
        course_info = course_info_class(
            name=soup.find('h1', {'class': 'title display-3-text'}).get_text(),
            url=course_url,
            lang=soup.find('div', attrs={'class': 'rc-Language'}).contents[1],
            start_date=get_course_start_datetime(soup),
            duration_in_weeks='{number} weeks'.format(number=len(soup.find_all('div', {'class': 'week'}))),
            rating=get_course_rating_numeric_value(soup)
        )
        return course_info


def output_courses_info_to_xlsx(filepath):
    pass


def set_cli_argument_parse():
    parser = argparse.ArgumentParser(description="Displays 20 the most popular repositories")
    parser.add_argument("-cachetime", "--cache_time", default=1200, type=int,
                        dest="cache_time", help="Set cache time interval")
    parser.add_argument('-clearcache', '--clear_cache', action='store_true', help='Clear cache file')
    return parser.parse_args()

if __name__ == '__main__':
    cli_argument_parser = set_cli_argument_parse()

    if not os.path.exists('_cache'):
        os.mkdir('_cache')
    requests_cache.install_cache('_cache/page_cache', backend='sqlite',
                                 expire_after=cli_argument_parser.cache_time)

    if cli_argument_parser.clear_cache:
        requests_cache.clear()

    courses_xml = get_courses_xml()
    courses_list = get_random_courses_url_list(courses_xml)
    courses_info_list = get_courses_info_list(courses_list)
    # print(get_courses_list())

    print(courses_info_list )
    # soup = BeautifulSoup(response.text, 'lxml')

    # courses_xml = get_courses_xml()
    # print(get_random_courses_list(courses_xml))

    # get_course_info()


    # print(response.encoding)
    # print(response.status_code)  # Код ответа
    # print(response.headers) # Заголовки ответа

    # course_url = 'https://www.coursera.org/learn/gis-capstone'
    # course_response = get_course('https://www.coursera.org/learn/assembling-genomes')
    # soup = BeautifulSoup(utf8_encode(course_response.text, course_response.encoding), 'lxml')
    # aa = get_course('https://www.coursera.org/learn/assembling-genomes')
    # print(get_course_info('https://www.coursera.org/learn/gis-capstone'))




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

