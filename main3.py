import pygame
import iosys.events as iv
import gui

import pygtk
pygtk.require('2.0')
import gtk

def main():
    clipboard = gtk.clipboard_get()
    
    clipboard.set_text("test")
        
    clipboard.store()
    
    clipboard = gtk.clipboard_get()
    
    print "rta="+str(clipboard.wait_for_text())
main()