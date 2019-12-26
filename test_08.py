import urllib.request
from bs4 import BeautifulSoup as BS

class Scraper():
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r=urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BS(html, parser)
#define a file
        filename = "//Users/KellerZhang/Desktop/python_lab/"+self.site[7:] + ".txt"
        with open(filename,"w+") as fl:
            print("file in processing...")
            for tag in sp.find_all("a"):
                url=tag.get("href")
                if url is None:
                    continue
                if "html" in url:
                    fl.write("\n"+url)
            print("mission completed")
if __name__ == "__main__":
    news = "http://news.baidu.com"
    Scraper(news).scrape()