import os
import json
import math
import sys


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding="Windows-1251") as handler:
        return json.load(handler)


def get_biggest_bar(data):
    return max(data, key=lambda x: x['SeatsCount'])


def get_smallest_bar(data):
    return min(data, key=lambda x: x['SeatsCount'])


def get_closest_bar(data, longitude, latitude):
    return min(data,
               key=lambda x:
                   math.hypot(x['geoData']['coordinates'][0] - longitude,
                              x['geoData']['coordinates'][1] - latitude))


if __name__ == '__main__':
    print('Этот скрипт находит самый большой, самый маленький '
          'и самый близкий к Вам бар в Москве.')
    longitude = float(input('Введите долготу: '))
    latitude = float(input('Введите широту: '))
    biggest_bar = get_biggest_bar(load_data(sys.argv[1]))
    smallest_bar = get_smallest_bar(load_data(sys.argv[1]))
    closest_bar = get_closest_bar(load_data(sys.argv[1]), longitude, latitude)
    print('Самый большой бар: {0} расположен по адресу: {1}'.format(
        biggest_bar['Name'], biggest_bar['Address']))
    print('Самый маленький бар: {0} расположен по адресу: {1}'.format(
        smallest_bar['Name'], smallest_bar['Address']))
    print('Ближайший к вам бар: {0} расположен по адресу: {1}'.format(
        closest_bar['Name'], closest_bar['Address']))
