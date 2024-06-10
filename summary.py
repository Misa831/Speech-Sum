import bs4
import requests
import re
import nltk
from nltk.corpus import stopwords
from collections import Counter

def main():
    url = ('http://analytictech.com/mb021/mlk.htm')
    page = requests.get(url)
    print(f'request returned status code: {page.status_code}')
    page.raise_for_status()
    # soup variable is the html of the text
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    p_elems = [element.text for element in soup.find_all('p')]
    speech = ''.join(p_elems)
    print(speech)


if __name__ == '__main__':
    main()