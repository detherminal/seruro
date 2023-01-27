#!/usr/bin/python

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class Pordo(Gtk.ApplicationWindow):
    def __init__(self, app):
        super(Pordo, self).__init__(application=app)
        self.set_title("Pordo")
        self.set_default_size(1000, 600)
        self.set_resizable(False)


def on_activate(app):
    win = Pordo(app)
    win.present()

app = Gtk.Application(application_id='org.seruro.pordo')
app.connect('activate', on_activate)
app.run(None)