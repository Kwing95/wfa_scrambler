import http.client
from lxml import html

conn = http.client.HTTPSConnection("www.thesaurus.com")
conn.request("GET", "/browse/honesty")
r1 = conn.getresponse()
data1 = r1.read()

# print(data1)
# raw html


tree = html.fromstring(data1)

synonyms = tree.xpath('//a[@class="css-3kshty etbu2a31"]/text()')
print(synonyms)