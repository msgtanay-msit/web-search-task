from main import WebCrawler
import unittest

class WebCrawlerTests(unittest.TestCase):
    def test_search1(self):
        keyword = "keyword"
        crawler = WebCrawler()
        crawler.index["page1"] = "This has the keyword"
        crawler.index["page2"] = "No keyword here"

        results = crawler.search("keyword")
        self.assertEqual(results, ["page1","page2"])
    
    def test_search2(self):
        keyword = "jobs"
        crawler = WebCrawler()
        crawler.index["page1"] = "This is a test page."
        crawler.index["page2"] = "Another test page."
        
        results = crawler.search(keyword)
       
        self.assertEqual(results, [])

    def test_search3(self):
        keyword = "another"
        crawler = WebCrawler()
        crawler.index["page1"] = "This is a test page."
        crawler.index["page2"] = "Another test page."
        
        results = crawler.search(keyword)
       
        self.assertEqual(results, ["page2"])


if __name__ == "__main__":
    unittest.main()  # Run unit tests