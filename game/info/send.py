import utils.pfunctions as pf

def send(name,menu,UP):
    if name == "Ayuda" and menu == "Creadores":
        UP.UP.objetos_pantalla.append(pf.window((500,400),(0,255,0),"TEST DE VENTANA",["boton numero 1","boton numero 2","boton numero 3","boton numero 4"]))