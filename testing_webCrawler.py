from main import WebCrawler
import unittest
from unittest.mock import patch, MagicMock
import requests
#from bs4 import BeautifulSoup
#from collections import defaultdict
#from urllib.parse import urljoin, urlparse

class WebCrawlerTests(unittest.TestCase):
    @patch('requests.get')
    def test_crawl_success(self, mock_get):
        sample_html = """
        <html><body>
            <h1>Welcome!</h1>
            <a href="https://www.external.com/about">About Us</a>
            <a href="https://www.external.com">External Link</a>
        </body></html>
        """
        mock_response = MagicMock()
        mock_response.text = sample_html
        mock_get.return_value = mock_response

        crawler = WebCrawler()
        crawler.crawl("https://www.external.com")

        # Assert that 'about' was added to visited URLs
        self.assertIn("https://www.external.com/about", crawler.visited)

    @patch('requests.get')
    def test_crawl_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Test Error")

        crawler = WebCrawler()
        crawler.crawl("https://example.com")
    
    # def test_crawl(self):
    #     crawler = WebCrawler()
    #     url1 = "https://www.msit.ac.in/"
    #     url2 = "https://www.msit.ac.in/about"
    #     crawler.crawl(url1)
    #     crawler.crawl(url2, base_url=url1)
    #     self.assertIn(url1, crawler.visited)
    #     self.assertIn(url2, crawler.visited)

if __name__ == "__main__":
    unittest.main()  # Run unit tests