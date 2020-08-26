# location_row.py
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

import gi

from models.location import Location

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class LocationRow(Gtk.ListBoxRow):
    """Widget to display weather data for given `location`
    """
    def __init__(self, location: Location):
        super().__init__()

        # Create layout box
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                      spacing=6,
                      margin=6)

        # Construct labels
        name_label = Gtk.Label(label=location.name)
        country_label = Gtk.Label(label=location.country)
        temp_label = Gtk.Label(label=f'{location.temp:.0f} C')
        weather_icon = Gtk.Image.new_from_icon_name(location.icon, Gtk.IconSize.LARGE_TOOLBAR)

        # Add labels to the layout
        box.pack_start(name_label, False, True, 0)
        box.pack_start(country_label, False, False, 0)
        box.pack_end(temp_label, False, False, 0)
        box.pack_end(weather_icon, False, False, 0)
        box.show_all()

        self.add(box)
