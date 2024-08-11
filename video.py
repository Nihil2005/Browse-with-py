from duckduckgo_search import DDGS


ddgs = DDGS()


query = "OpenAI ChatGPT demo"
results = ddgs.videos(query)


for result in results:
    print(result.get('title'))      
    print(result.get('content'))    
    print(result.get('source'))     
    print(result.get('thumbnail'))  
    print()
