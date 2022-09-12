import requests
from bs4 import BeautifulSoup

# import below, to work Telegram Bot with Django Rest Framework properly
# start
import sys

sys.dont_write_bytecode = True

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

import django
django.setup()

from app import models, serializers
# end

LINK = "https://stadion.uz/"

team = []
titles = []

dict = [
    {
        "name": "",
        "matches": [
            {
                "date": "",
                "team1": {
                    "name": "",
                    "score": "",
                },
                "team2": {
                    "name": "",
                    "score": "",
                },
            },
        ],
    },
]


def get_page(link):
    return requests.get(link)


def get_table(soup):
    global num
    table = soup.find_all("div", id="online_tablo")
    print('Length table:', len(table))

    for i in table:
        title = i.find_all("div", id="online_tablo_title")
        print('Length Title:', len(title))

        title_info = i.ul.li.ul.find_all("ul")
        print('title_info:', title_info[0])
        # for i in title:


        set_title(get_soup())

        num = i.ul.find_all("ul")
        for l in range(0, len(num)):
            get_game(num[l], len(title))

    print('Length:', len(num))


def set_title(soup):
    global date
    title = soup.find_all("div", id="online_tablo_title")
    for i in title:
        titles.append(i.b.text)
    print(titles)
    return titles


def get_title(soup):
    for i in titles:
        print('Game Titles', i)
        return i


def get_game(soup, len):
    global dates

    game = soup.find_all("ul", id="online_tablo_game")

    for i in game:
        date = i.find_all("li", id="online_tablo_day")
        team1 = i.find_all("li", id="online_tablo_team1")
        team2 = i.find_all("li", id="online_tablo_team2")
        point = i.find_all("li", id="online_tablo_result")

        # models.Game(
        #     liga_name=get_title(get_soup())[len],
        #     date=get_date(date),
        #     team1=get_team1(team1),
        #     point=get_point(point),
        #     team2=get_team2(team2),
        # ).save()

        # print(f'id: #{len}')
        # print('liga title:', get_title(get_soup())[len])
        # print('date time:', get_date(date))
        # print('team 1:', get_team1(team1))
        # print('team 2:', get_team2(team2))
        # print('point:', get_point(point))
        # print('\n')


def get_point(point):
    score = ""
    for i in point:
        score += i.a.text
    return score


def get_date(date):
    datetime = ""
    print('date date date', len(date))
    for i in date:
        datetime += i.text
    return datetime


def get_team1(team1):
    team = ""
    for i in team1:
        q = i.text
        q = q.split("\n")
        q = q[1].strip(" ")
        team += q
    return team


def get_team2(team2):
    team = ""
    for i in team2:
        team += i.text
    return team


def get_soup():
    page = get_page(LINK)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup


def main():
    get_title(get_soup())
    get_table(get_soup())


if __name__ == '__main__':
    main()
