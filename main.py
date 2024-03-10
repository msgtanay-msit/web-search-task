import requests
from bs4 import BeautifulSoup
from collections import defaultdict
from urllib.parse import urljoin, urlparse

class WebCrawler:
    def __init__(self):
        self.index = defaultdict(list)
        self.visited = set()

    def crawl(self, url, base_url=None,depth=0,max_depth=2):
        if depth>max_depth:
            return
        if url.endswith("/"):
            url = url.rstrip("/")
        if url in self.visited:
            return
        self.visited.add(url)
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            self.index[url] = soup.get_text()

            for link in soup.find_all('a'):
                href = link.get('href')
                if href:
                    if urlparse(href).netloc:
# uncomment the following condition to make the function only crawl internal links    
                        #if href.startswith(base_url or url): 
                            self.crawl(href, base_url=base_url or url,depth=depth+1,max_depth=max_depth)
                    if href.startswith("/"):
                        href = urljoin(base_url or url, href)
                        self.crawl(href, base_url=base_url or url,depth=depth+1,max_depth=max_depth)
        except Exception as e:
            print(f"Error crawling {url}: {e}")

    def search(self, keyword):
        results = []
        for url, text in self.index.items():
            if keyword.lower() in text.lower():
                results.append(url)
        return results

    def print_results(self, results):
        if results:
            print("Search results:")
            for result in results:
                print(f"- {result}")
        else:
            print("No results found.")

def main():
    crawler = WebCrawler()
    start_url = "https://example.com"
    crawler.crawl(start_url)

    keyword = "this"
    results = crawler.search(keyword)
    crawler.print_results(results)

if __name__ == "__main__":
    main()
