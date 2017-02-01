from lxml import etree
from io import StringIO, BytesIO
import urllib.request
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
    print(get_courses_list())