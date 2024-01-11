import random
import string
from threading import Thread
import requests
from bs4 import BeautifulSoup


class MovieItem:
    def __init__(self, title, score, people_num, quote, description, url, pic):
        self.pic = pic
        self.title = title
        self.score = score
        self.people_num = people_num
        self.quote = quote
        self.description = description
        self.url = url


class MyThread(Thread):
    def __init__(self, func, args):
        Thread.__init__(self)
        self.func = func
        self.args = args
        self.result = None

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        return self.result


top250Url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 "
                  "Safari/537.36 Edg/121.0.0.0",
    "Cookie": "bid=%s" % "".join(random.sample(string.ascii_letters + string.digits, 11))  # random cookie
}


def change_cookie():
    headers["Cookie"] = "bid=%s" % "".join(random.sample(string.ascii_letters + string.digits, 11))  # random cookie


# def get_movie_detail(url):
#     # change_cookie()
#     response = requests.get(url, headers=headers)
#     while response.status_code == 403:  # forbidden
#         change_cookie()
#         response = requests.get(url, headers=headers)
#     # print("satus_code:", response.status_code)
#     soup = BeautifulSoup(response.text, "html.parser")
#     pic = soup.find("img", rel="v:image")["src"]
#     title = soup.find("span", property="v:itemreviewed").text
#     score = soup.find("strong", property="v:average").text
#     # quote = soup.find("span", class_="short").text
#     quote = ""
#     description = soup.find("span", property="v:summary").text
#     return MovieItem(title, score, quote, description, url, pic)


def parse_movie(soup):
    for movie in soup.find_all("div", class_="item"):
        url = movie.find("a")["href"]
        if movie.find("span", class_="inq"):
            quote = movie.find("span", class_="inq").text
        else:
            quote = ""
        title = movie.find("span", class_="title").text
        score = movie.find("span", class_="rating_num").text
        people_num = movie.find("div", class_="star").find_all("span")[-1].text[:-3]
        pic = movie.find("img")["src"]
        movie_item = MovieItem(title, score, people_num, quote, "", url, pic)
        yield movie_item


def get_top250_movies(page=1):
    print("crawling top250 movies...")
    if page != 1:
        s = (page - 1) * 25
        url = "https://movie.douban.com/top250?start={}&filter=".format(s)
    else:
        url = top250Url

    # change_cookie()
    response = requests.get(url, headers=headers)
    while response.status_code == 403:  # forbidden
        change_cookie()
        response = requests.get(url, headers=headers)
    # print("satus_code:", response.status_code)
    soup = BeautifulSoup(response.text, "html.parser")
    movie_items = []
    movie_items.extend(parse_movie(soup))
    return movie_items


def get_top250_movies_with_thread():
    print("crawling top250 movies...")
    movie_items = []
    threads = []
    for page in range(1, 11):
        if 1 != page:
            s = (page - 1) * 25
            url = "https://movie.douban.com/top250?start={}&filter=".format(s)
        else:
            url = top250Url
        # change_cookie()
        response = requests.get(url, headers=headers)
        while response.status_code == 403:  # forbidden
            change_cookie()
            response = requests.get(url, headers=headers)
        # print("satus_code:", response.status_code)
        soup = BeautifulSoup(response.text, "html.parser")
        thread = MyThread(parse_movie, (soup,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
        movie_items.extend(thread.get_result())
    return movie_items


def getImg(title, url, path):
    import os
    if not os.path.exists(path):
        os.mkdir(path)
    response = requests.get(url, headers=headers)
    while response.status_code == 403:  # forbidden
        change_cookie()
        response = requests.get(url, headers=headers)
    with open(path + title + ".jpg", "wb") as f:
        f.write(response.content)


def get_top_20_img(movies, path):
    print("crawling top20 movies' img...")
    import os
    if os.path.exists(path):
        return

    for i in range(20):
        getImg(movies[i].title, movies[i].pic, path)
