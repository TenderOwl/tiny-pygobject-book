# weather.py
#
# MIT License
#
# Copyright (c) 2020 Andrey Maksimov <meamka@ya.ru>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import requests


class WeatherService:
    """Weather API service
    """

    # Base URL of weather API
    BASE_API = 'https://api.openweathermap.org/data/2.5'

    def __init__(self, api_key):
        self.api_key = api_key

    def find_locations(self, location):
        """Call Find method to find all locations that matches given location name

        :param location:
        :return:
        """
        uri = self.BASE_API + '/find'
        params = {
            'q': location,
            'appid': self.api_key,
            'lang': 'ru',
            'units': 'metric',
        }

        # Send GET request to weather API
        response = requests.get(uri, params, timeout=2.0)
        response_data = response.json()
        if response_data['cod'] == "200":
            return response_data['list']
        else:
            return []
