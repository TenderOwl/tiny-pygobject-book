#!/usr/bin/env python3

import sys
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio

class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='com.github.tenderowl.tiny-app',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = Gtk.ApplicationWindow(application=self)
            win.set_default_size(400, 300)
            win.set_title('Tiny App')

            label = Gtk.Label(label='Welcome to PyGObject!', visible=True)
            win.add(label)
        win.present()


def main():
    app = Application()
    return app.run(sys.argv)


if __name__ == '__main__':
    main()
