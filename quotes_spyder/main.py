import os

def crawl():
    os.system("scrapy crawl quotes -o quotes.csv")
    os.system("scrapy crawl authors -o authors.csv")
    os.system("py json_formater.py")

if __name__ == "__main__":
    try:
        crawl()
    except Exception as e: 
        print(str(e))
    else:
        print("You got your scraped data!")