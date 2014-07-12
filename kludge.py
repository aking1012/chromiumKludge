#!/usr/bin/env python3

from gi.repository import Wnck, Gtk
import signal, time

class KludgyWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_decorated(False)
        self.set_size_request(1,1)
        self.set_opacity(0)
        self.set_keep_above(True)
        self.show_all()
        self.set_skip_taskbar_hint(True)
        self.stick()

class Kludge:
    def __init__(self):
        self.first = True
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        self.win = KludgyWindow()
        self.win.hide()
    def fire_the_kludge(self, data_a, data_b):
        time.sleep(.1)
        self.win.show()
        time.sleep(.01)
        self.win.hide()


    def main(self):
        screen = Wnck.Screen.get_default()
        screen.connect("active-workspace-changed", self.fire_the_kludge)
        Gtk.main()

if __name__ == '__main__':
    print("Here comes the kludge")
    kludge = Kludge()
    kludge.main()