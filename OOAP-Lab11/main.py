import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

class BookScraper:
    BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

    def __init__(self, start_page, end_page):
        self.start_page = start_page
        self.end_page = end_page

    def scrape_range(self):
        if self.end_page - self.start_page >= 1:
            mid = (self.start_page + self.end_page) // 2
            with ThreadPoolExecutor() as executor:
                executor.submit(BookScraper(self.start_page, mid).scrape_range)
                executor.submit(BookScraper(mid + 1, self.end_page).scrape_range)
        else:
            self.scrape_page(self.start_page)

    def scrape_page(self, page_num):
        url = self.BASE_URL.format(page_num)
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            books = soup.select(".product_pod")

            for book in books:
                title = book.select_one("h3 > a")["title"]
                price = book.select_one(".price_color").text
                rating_class = book.select_one(".star-rating")["class"]
                rating = self.get_star_int(rating_class[1])

                print(f"Сторінка {page_num} | Назва: {title} | Ціна: {price} | Рейтинг: {rating} зірок")

        except requests.RequestException as e:
            print(f"Помилка при обробці сторінки {page_num}: {e}")

    def get_star_int(self, rating):
        return {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
        }.get(rating, 5)


if __name__ == "__main__":
    scraper = BookScraper(1, 3)
    scraper.scrape_range()
