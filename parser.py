from bs4 import BeautifulSoup
import requests

file = open('parser.txt', 'w')

for url_num in range(34):
    url = 'https://stroka.kg/kupit-kvartiru/?&p={0}#paginator'.format(url_num)

    html_template = requests.get(url).text

    soup = BeautifulSoup(html_template, "lxml")

    tbodyes = soup.find_all("tbody")

    for n, i in enumerate(tbodyes):
        line = ''
        for td in i.find_all('td'):
            if 'topics-item-topic_cost' in td['class']:
                line += td['title'] + ' '
            if 'topics-item-topic_rooms' in td['class']:
                line += td.text + ' '
            if 'topics-item-topic_area' in td['class']:
                line += td.text + ' '
            if 'topics-item-topic_name' in td['class']:
                a = td.find('a')
                line += a['href'] + '\n'
                file.write(line)

file.close()


