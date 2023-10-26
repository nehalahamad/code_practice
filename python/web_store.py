from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import re
from bs4.element import Comment
import copy
import timeit
import random
# from random_words import RandomWords


class KeywordEntry:
    def __init__(self, word: str, url: str = None, location: int = None):
        self._word = word.upper()
        if url:
            self._sites = {url: [location]}
        else:
            self._sites = {}

    def add(self, url: str, location: int) -> None:
        if url in self._sites:
            self._sites[url].append(location)
        else:
            self._sites[url] = [location]

    def get_locations(self, url: str) -> list:
        try:
            return self._sites[url]
        except IndexError:
            return []

    @property
    def sites(self) -> list:
        return [key for key in self._sites]
    
    def __lt__(self, other):
        if isinstance(other, str):
            return self._word < other.upper()
        return self._word < other._word.upper()
    
    def __gt__(self, other):
        if isinstance(other, str):
            return self._word > other.upper()
        return self._word > other._word.upper()
    
    def __eq__(self, other):
        if isinstance(other, str):
            return self._word == other.upper()
        return self._word == other._word.upper()
    
    def __hash__(data):
        return hash((data._word.upper()))

# ---------------------link fisher----------------------------------
def link_fisher(url, depth=0, reg_ex=""):
    res = _link_fisher(url, depth, reg_ex)
    res.append(url)
    return list(set(res))


def _link_fisher(url, depth, reg_ex):
    link_list = []
    if depth == 0:
        return link_list
    headers = {
        'User-Agent': ''}
    try:
        page = requests.get(url, headers=headers)
    except:
        print("Cannot retrieve", url)
        return link_list
    data = page.text
    soup = BeautifulSoup(data, features="html.parser")
    for link in soup.find_all('a', attrs={'href': re.compile(reg_ex)}):
        link_list.append(urljoin(url, link.get('href')))
    for i in range(len(link_list)):
        link_list.extend(_link_fisher(link_list[i], depth - 1, reg_ex))
    return link_list

# -------------------------------Text Harvester-----------------------
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def words_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.find_all(string=True)
    visible_texts = filter(tag_visible, texts)
    text_string = " ".join(t for t in visible_texts)
    words = re.findall(r'\w+', text_string)
    return words


def text_harvester(url):
    headers = {
        'User-Agent': ''}
    try:
        page = requests.get(url, headers=headers)
    except:
        return []
    res = words_from_html(page.content)
    return res


# ==================================================
class WebStore:
    def __init__(self, ds):
        self._store = ds
    
    def crawl(self, url: str, depth=0, reg_ex=""):
        list_of_links = link_fisher(url, depth, reg_ex="")
        
        for link in list_of_links:
            words_on_a_link = text_harvester(link)
            for word in words_on_a_link:
                if len(word) < 4 or not word.isalpha():
                    continue
                self._store.insert( KeywordEntry(word, link) )

    def crawl_and_list(self, url, depth=0, reg_ex=''):
        word_set = set()
        for link in link_fisher(url, depth, reg_ex):
            for word in text_harvester(link):
                if len(word) < 4 or not word.isalpha():
                    continue
                word_set.add(word)
        return list(word_set)

    def search(self, keyword: str):
        return self._store.find(keyword).sites
      
    def search_list(self, kw_list: list):
        found, not_found = 0, 0
        for kw in kw_list:
            try:
                list_of_link = self.search(kw)
                found += 1
            except:
                not_found += 1
        return (found, not_found)
