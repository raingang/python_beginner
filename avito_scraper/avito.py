import requests, csv
from bs4 import BeautifulSoup


def get_html(url):
	r = requests.get(url)
	return r.text
def write_csv(data):
	with open('avito.csv', 'a') as f:
		writer = csv.writer(f)

		writer.writerow((data['title'], data['price'], data['url'], data['metro']) )

def get_total_page(html):

	soup = BeautifulSoup(html, 'lxml')

	page = soup.find('div', class_ = 'pagination-pages')

	lastPage = page.find_all('a', class_ = 'pagination-page')[- 1].get('href')
	
	totalPages = lastPage.split('=')[1].split('&')[0]
	
	return int(totalPages)
def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')

	ads = soup.find('div', class_ = 'catalog-list').find_all('div', class_= 'item_table')
	for ad in ads:
		name = ad.find('div', class_ = 'description').find('h3').text.strip().lower()
		if 'htc' in name:
		#title, url, price, metro
			try:
				title = ad.find('div', class_ = 'description').find('h3').text.strip()
				print (title)
			except:
				title = ''
			try:
				url = 'https://www.avito.ru' + ad.find('div', class_ = 'description').find('h3').find('a').get('href')
				print (url)
			except: url = ''
			try:
				price = ad.find('div', class_ = 'about').text.strip()
				print (price)
			except: 
				price = ''
			try:
				metro = ad.find('div', class_ = 'data').find_all('p')[-1].text.strip()
				print (metro)
			except:
				price = ''
			data = {'title': title, 'price': price, 'url' : url, 'metro' : metro}
			write_csv(data)
		else: 
			continue	
	#return ads

def main():
	url = 'https://www.avito.ru/moskva/telefony?p=1&q=htc'
	base_url = "https://www.avito.ru/moskva/telefony?"
	page_part = 'p='
	query_part = '&q=htc'
	total_pages = get_total_page(get_html(url))
	for i in range(1, 3):
		url_gen =  base_url + page_part + str(i) + query_part
		html = get_html(url_gen)

		data = get_page_data(html)

	

print (main())

	
