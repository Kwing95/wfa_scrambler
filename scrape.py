import sys
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
reading = len(sys.argv) == 1
if not reading:
    bookmark = sys.argv[1]

word = dictionary.readline().strip('\n')
with open("thesaurus.txt", "a+") as out_file:
    while(word != ""):
            if(reading):
                out_file.write('"' + word + '" : ' + str(get_synonyms(conn, word)) + ", ")
                # thesaurus[word] = get_synonyms(conn, word)
            reading = reading or bookmark == word
            word = dictionary.readline().strip('\n')

print(thesaurus)
