from bs4 import BeautifulSoup
import requests


response = requests.get("https://www.gutenberg.org/browse/scores/top")
print("Status code:", response.status_code)
print("Headers:",response.headers)

soup = BeautifulSoup(response.text, "html.parser")

top_ebooks = soup.find(id="books-last1")
print(top_ebooks)

book_list = top_ebooks.find_next()
print(book_list)


response = requests.get("https://www.gutenberg.org/browse/scores/top")
soup = BeautifulSoup(response.text, "html.parser")
top_100_ebooks = soup.find(id="books-last1")
list_of_books = top_100_ebooks.find_next('ol').find_all('li')
for book in list_of_books:
	print(book.get_text())
	


