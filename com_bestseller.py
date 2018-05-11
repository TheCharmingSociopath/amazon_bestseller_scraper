import csv
import requests
import os
from bs4 import BeautifulSoup
from requests import get


with open('com_book.csv', 'w') as out_file:
    writer = csv.writer(out_file, delimiter=';')
    writer.writerow(['NAME', 'URL', 'AUTHOR', 'PRICE', 'NUMBER OF RATINGS', 'AVERAGE RATING'])

    for i in range(5):
        url = 'https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_{}?_encoding=UTF8&pg={}'
        response = requests.get(url.format(i + 1, i + 1))
        parsed_html = BeautifulSoup(response.text, 'html.parser')
        page_data = parsed_html.find_all('div', class_='zg_itemImmersion')

        for x in page_data:
            ans = []
            link = x.find('a', class_='a-link-normal')
            title = x.find('div', class_='p13n-sc-truncate p13n-sc-line-clamp-1')
            author = x.find('div', class_='a-row a-size-small')
            price = x.find('a', class_='a-link-normal a-text-normal')
            if price is not None:
                price = price.find('span', class_='p13n-sc-price')
            num_rating = x.find('a', class_='a-size-small a-link-normal')
            avg_rating = x.find('div', class_='a-icon-row a-spacing-none')

            if title is None:
                ans.append('Not available')
            else:
                ans.append(title.string.strip())

            if link is None:
                ans.append('Not available')
            else:
                ans.append('https://www.amazon.com' + link['href'].strip())

            if author is None:
                ans.append('Not available')
            else:
                ans.append(author.string.strip())

            if price is None:
                ans.append('Not available')
            else:
                ans.append(price.getText().strip())

            if num_rating is None:
                ans.append('Not available')
            else:
                ans.append(num_rating.string.strip())

            if avg_rating is None:
                ans.append('Not available')
            else:
                ans.append(avg_rating.find('i').string.strip())

            writer.writerow(ans)
