import requests
from bs4 import BeautifulSoup
import json

URL= 'https://en.wikipedia.org/wiki/History_of_Mexico'
page =requests.get(URL)
print(page.content)

# soup=BeautifulSoup(page.content,'html.parser')

def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    all_paragraphs = soup.find_all('p')

    paragraphs_that_contain_citations = ''

    for paraph in all_paragraphs:

        citations = paraph.find_all('sup',class_='noprint Inline-Template Template-Fact')
        if citations :
            paragraphs_that_contain_citations += paraph.text


    return paragraphs_that_contain_citations.count('citation needed')



def get_citations_needed_report(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content,'html.parser')


    all_paragraphs = soup.find_all('p')

    list_of_paragraphs_that_contain_citations = []
    for paraph in all_paragraphs:
        citations = paraph.find_all('sup',class_='noprint Inline-Template Template-Fact')
        if citations :
            list_of_paragraphs_that_contain_citations.append(paraph.text)

    return list_of_paragraphs_that_contain_citations
        
print(get_citations_needed_count(URL))
print(get_citations_needed_report(URL))


#     return get_citations_needed_report()