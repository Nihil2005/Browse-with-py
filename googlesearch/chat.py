from googlesearch import search

def get_google_news_results(query):
    search_query = f"{query} site:news"
    results = search(search_query, num_results=10)
    return results

query = "latest technology news"
news_results = get_google_news_results(query)

for result in news_results:
    print(result)
    print()
