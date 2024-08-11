from duckduckgo_search import DDGS

# Create a DDGS object
ddgs = DDGS()

# Perform an image search
query = "OpenAI logo"
results = ddgs.images(query)

# Print the results
for result in results:
    print(result['image'])  # URL of the image
    print(result['title'])  # Title of the image
    print(result['source']) # Source of the image
    print()
