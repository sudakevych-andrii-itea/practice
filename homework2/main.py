# Создать консольную программу-парсер, с выводом прогноза погоды. Дать
# возможность пользователю получить прогноз погоды в его локации ( по
# умолчанию) и в выбраной локации, на определенную пользователем дату.
# Можно реализовать, как консольную программу, так и веб страницу.
# Используемые инструменты: requests, beatifulsoup, остальное по желанию.
# На выбор можно спарсить страницу, либо же использовать какой-либо API.


import requests
from bs4 import BeautifulSoup
import datetime


class WeatherForecast:
    def __init__(self, city=None, date=datetime.datetime.now().strftime('%Y-%m-%d')):
        self._city = city
        self._date = date

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value.lower()

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    def _get_url(self):
        if self._city:
            return f'https://sinoptik.ua/погода-{self._city}/{self._date}'
        else:
            return f'https://sinoptik.ua/'

    def _get_request(self):
        try:
            req = requests.get(self._get_url())
            req.raise_for_status()
            return req
        except requests.RequestException:
            raise SystemExit('This city doesn\'t exist')

    def _get_page(self):
        page = self._get_request().text
        return BeautifulSoup(page, 'html.parser')

    def get_info(self):
        title = self._get_page().find(class_='cityName').find('h1').text.lstrip()
        total_info = self._get_page().find(class_='main loaded')
        date = total_info.find(class_='date').text
        month = total_info.find(class_='month').text
        day = total_info.find(class_='day-link').text
        temperature = total_info.find(class_='temperature').text.lstrip()
        details = total_info.find(class_='weatherIco').attrs['title']
        return f'{title} \n' \
               f'{date} {month} \n' \
               f'{day} \n' \
               f'{temperature} \n' \
               f'{details} \n'


if __name__ == '__main__':
    forecast = WeatherForecast('Киев')
    print(forecast.get_info())
