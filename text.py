from duckduckgo_search import DDGS


ddgs = DDGS()


query = "T20 world cup"
results = ddgs.text(query)


for result in results:
    print(result['title'])
    print(result['href'])
    print(result['body'])
    print()
