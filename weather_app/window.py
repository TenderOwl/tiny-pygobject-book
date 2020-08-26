# window.py
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
from services.weather import WeatherService
from settings import OPENWEATHERMAP_KEY
from widgets.location_row import LocationRow

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio


class WeatherWindow(Gtk.ApplicationWindow):
    """Main window of the application
    """

    def __init__(self, application):
        super().__init__(application=application)
        self.set_default_size(240, 240)
        self.set_title('Weather App')

        # Create Box layout widget with margins and spacing props
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, margin=6, spacing=6)

        # Create SearchEntry widget
        self.search_entry = Gtk.SearchEntry(placeholder_text='Enter location name')

        # We use ::search-changed signal to make it more reactive.
        self.search_entry.connect('search-changed', self.search_changed)

        # Model to store locations
        self.locations_model = Gio.ListStore()

        # Create list view to show locations
        self.locations_list = Gtk.ListBox()
        self.locations_list.bind_model(self.locations_model, LocationRow)
        self.locations_list.show_all()

        # Add locations_list to ScrolledWindow to make it scrollable
        scroll_window = Gtk.ScrolledWindow()
        scroll_window.add(self.locations_list)

        # Add widgets to the box
        box.pack_start(self.search_entry, False, True, 0)
        box.pack_start(scroll_window, True, True, 0)

        # And finally add the box as central widget to the window
        self.add(box)

        # Set visibility of all widgets to visible
        self.show_all()

    def search_changed(self, sender):
        """Handler for `::search-changed` signal.
        Checks for the text in SearchEntry
        and sends a request to the weather API to find locations

        """
        weather_service = WeatherService(OPENWEATHERMAP_KEY)

        search_text = sender.get_text()
        if not search_text:
            self.locations_model.remove_all()
            return

        locations = weather_service.find_locations(search_text)

        if locations:
            # Remove all existed location items if we've found new ones
            self.locations_model.remove_all()
            for location in locations:
                self.locations_model.append(
                    Location(
                        location_id=location['id'],
                        name=location['name'],
                        country=location['sys']['country'],
                        temp=location['main']['temp'],
                        weather_icon=location['weather'][0]['icon'],
                    )
                )
