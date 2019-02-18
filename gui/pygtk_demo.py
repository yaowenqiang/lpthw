import pygtk
import gtk
import time

class SimpleButtonApp(object):
    def __init__(self, ):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect('destroy', self.quit)
        self.button = gtk.Button('Cock Me')
        self.button.connect('clicked', self.update_button_lable, None)
        
        self.window.add(self.button)
        self.button.show()
        self.window.show()
    
    def quit(self, widget, data=None):
        gtk.main_quit()


    def update_button_lable(self, widget, data=None):
        self.button.set_label(time.asctime())

    def main(self):
        gtk.main()


if __name__ == "__main__":
    s = SimpleButtonApp()
    s.main()
