import requests
import http.client
from lxml import html

def get_synonyms(conn, word):
    conn.request("GET", "/browse/" + word)
    r1 = conn.getresponse()
    data1 = r1.read()
    if(len(data1.decode("utf-8")) == 0):
        return []
    tree = html.fromstring(data1)
    synonyms = tree.xpath('//a[@class="css-gkae64 etbu2a31"]/text()')
    return synonyms

dictionary = open("words_alpha.txt", "r")
thesaurus = dict()
url = "https://www.thesaurus.com/browse/"
conn = http.client.HTTPSConnection("www.thesaurus.com")

print("honesty = ")
k = get_synonyms(conn, "honesty")

word = dictionary.readline().strip('\n')
while(word != ""):
        thesaurus[word] = get_synonyms(conn, word)
        print(thesaurus)
        word = dictionary.readline().strip('\n')

print(thesaurus)
