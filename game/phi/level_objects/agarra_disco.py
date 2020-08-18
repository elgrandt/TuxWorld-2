import pygame, element
import extra_data.images as ei

class agarrar_disco(element.element):
    def __init__(self,X,Y,NAME):
    	self.element(X,Y,NAME,"Agarrar disco",["Wall"],ei.disco)