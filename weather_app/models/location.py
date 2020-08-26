# location.py
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
from gi.repository import GObject

from settings import WEATHER_TO_ICON


class Location(GObject.GObject):
    """Store Location data
    """
    location_id = GObject.property(type=int)
    name = GObject.property(type=str)
    country = GObject.property(type=str)
    temp = GObject.property(type=float)
    icon = GObject.property(type=str)

    def __init__(self, location_id, name, country, temp, weather_icon):
        GObject.GObject.__init__(self)
        self.location_id = location_id
        self.name = name
        self.country = country
        self.temp = temp
        self.icon = WEATHER_TO_ICON.get(weather_icon, 'weather-severe-alert')
