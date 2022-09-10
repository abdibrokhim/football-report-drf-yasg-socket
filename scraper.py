import requests
from bs4 import BeautifulSoup

LINK = "https://stadion.uz/"

titles = []

data = {}

datas = []

match = {}

info = [
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

    for i in table:
        title = i.find_all("div", id="online_tablo_title")
        # for i in title:
        #     print('Liga titles:', i.b.text)
        #     titles.append(i.b.text)
        #
        #     data[f'{i.b.text}'] = ""
        #
        #     datas.append(i.b.text)

        num = i.ul.find_all("ul")
        # print('num num num: ', num)
        for l in num:
            # print('d d d d: ', l)
            # print('Liga titles:', l[1].b.text)
            get_game(l)

    # print("-"*200)

    print('Length:', len(num))


def get_title(soup):
    global date

    title = soup.find_all("div", id="online_tablo_title")
    for i in title:
        print('Liga titles:', i.b.text)
        titles.append(i.b.text)

        data[f'{i.b.text}'] = ""

        datas.append(i.b.text)

    print('array:', datas)
    print('dict:', data)

    return titles


def get_game(soup):
    global dates

    game = soup.find_all("ul", id="online_tablo_game")

    for i in game:
        date = i.find_all("li", id="online_tablo_day")
        team1 = i.find_all("li", id="online_tablo_team1")
        team2 = i.find_all("li", id="online_tablo_team2")

        get_date(date)
        get_team1(team1)
        get_team2(team2)


def get_date(date):
    for i in date:
        print('Date:', i.text, end=' | ')


def get_team1(team1):
    for i in team1:
        print('Team1:', i.text, end=' | ')


def get_team2(team2):
    for i in team2:
        print('Team2:', i.text)


def main():
    page = get_page(LINK)
    soup = BeautifulSoup(page.text, "html.parser")

    # get_title(soup)
    # get_game(soup)
    get_table(soup)


if __name__ == '__main__':
    main()
