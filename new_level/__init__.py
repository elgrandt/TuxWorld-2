import pygame,extra_data.images as img,extra_data.fonts as fonts
import game.com.tran as tran
import utils.pfunctions as pf
import game.phi as phi
import game.phi.level_objects as lo
import game.com.com as com
import generar_nivel, game.game_over.game_over as game_over
import utils.moving_bar as mb
from utils.help import help

class objetos:
	def __init__(self,UP):
		self.bar = None
		self.UP = UP
		self.objetos = UP.seleccionables
		self.iniciado = False
		self.size_buttons = (50,50)
		self.selected = "NO"
		self.ant_selected = "NO"
		self.interpretador = tran.inte()
		self.propiedades = None
		self.events = None
		self.escribiendo_en = ""
		self.last_pressed = []
		self.last_propiedades = None
		self.checkbox_selected = False
		self.LP1 = 0
		self.phi = phi.phi()
		self.phi.playing = False
		self.phi.objetos.append(lo.jugador.jugador(100,100,"Test",False))
		self.indice_jugador = len(self.phi.objetos)-1
		self.indice_selected = 9999
		self.tran = tran.inte()
		self.Values = [["background",0],["Wall",0],["Enemy",0],["Moneda",0],["Esquina",0],["vida_extra",0],["Box",0],["Dinamite",0],["Button",0],["Puerta",0],["Checkpoint",0],["Teletransportador_in",0],["Luz",0],["Laser",0],["Meta",0]]
		self.opciones = None
		self.LT1 = pygame.time.get_ticks()
		pantalla = pygame.display.get_surface()
		size_input = (700,60)
		pos_input = (pantalla.get_size()[0]/2-size_input[0]/2,pantalla.get_size()[1]/2-size_input[1]/2)
		self.nombre_nivel = pf.Input(pantalla,"Nombre del nivel",size_input,pos_input,"END",(255,0,0))
		self.seleccionando_nombre = False
		self.terminado = False
		self.game_over = game_over.looser("Nivel terminado perfectamente")
		self.font2 = pygame.font.Font(fonts.font3,10)
		self.borrando = False
		self.default_save = None
		self.seleccionar_posicion_data = []
		self.seleccionado_seleccionar_posicion = None
		self.LT2 = pygame.time.get_ticks()
		self.seleccionando_posicion = False
		self.objetos_propiedades = 0
		self.barra_activa = False
		self.disferencia_barra = 0
		self.barra = mb.moving_bar()
		self.seleccionando_objeto = False
		self.LT3 = pygame.time.get_ticks()
		self.objeto_seleccionado = "<- Pulse aqui"
		self.dir = ""
		self.FT = True
		self.posicion_marcada = [0,0]
		self.marcando_posicion = False
		self.LT4 = pygame.time.get_ticks()
		self.rango_marcado = 0
		self.pos_marcador = 0
		self.barra2 = mb.moving_bar()
		self.barra2_activa = False
		self.profile_name = None
		self.ayuda = []
		self.ayuda.append(help("Guarda el nivel creado y si es la primera vez que lo guarda se le pedira escribir el nombre del nivel"))
		for q in self.objetos:
			self.ayuda.append(help(q[2]))
		self.tamano_simple_escrito = "1"
		self.escribiendo_tamano_simple = False
		self.last_pressed2 = pygame.key.get_pressed()
		self.LT5 = pygame.time.get_ticks()
	def graphic_update(self,pantalla):
		self.pantalla = pantalla
		if not self.seleccionando_nombre and not self.terminado:
			
			self.posicion_act(pantalla)
			
			self.phi.graphic_update(pantalla)
			
			self.bar_size = (pantalla.get_size()[0], 120)
			self.bar_pos = (0,pantalla.get_size()[1]-self.bar_size[1])
			self.bar = pygame.Surface(self.bar_size)
			self.bar.fill((0,192,255))
			self.font1 = pygame.font.Font(fonts.font3, 20)
			seleccione_objeto = self.font1.render("Seleccione objeto:",1,(0,0,0))
			self.bar.blit(seleccione_objeto,(5,2))
			x_act = 10
			for q in range(len(self.objetos)):
				self.objetos[q][1] = pygame.transform.scale(self.objetos[q][1],self.size_buttons)
				if self.selected == self.objetos[q][0]:
					self.objetos[q][1] = pf.add_border(self.objetos[q][1], 4, 4, 4, 4, (255,0,0))
				else:
					self.objetos[q][1] = pf.add_border(self.objetos[q][1], 4, 4, 4, 4, (0,0,0))
				pos_act_obj = (x_act, 2+seleccione_objeto.get_size()[1]+20)
				self.bar.blit(self.objetos[q][1],pos_act_obj)
				
				self.ayuda[q+1].cambiar_valores((self.bar_pos[0]+pos_act_obj[0],self.bar_pos[1]+pos_act_obj[1]),self.size_buttons)
				
				if len(self.objetos[q]) > 3:
					del self.objetos[q][3]
				self.objetos[q].append((self.bar_pos[0]+x_act,self.bar_pos[1]+30))
				x_act += self.objetos[q][1].get_size()[0]+10
			
			self.pos_propiedades = (x_act+10,5)
			self.propiedades = pygame.Surface((self.bar_size[0]-x_act-20,self.bar_size[1]-10))
			self.propiedades.fill((0,255,255))
			self.title_propiedades = self.font1.render("Propiedades:",1,(0,0,255))
			self.propiedades.blit(self.title_propiedades,(2,2-self.disferencia_barra))
			self.propiedades = self.analizar_propiedades(self.propiedades)
			
			if self.objetos_propiedades > 3:
				self.barra_activa = True
				self.barra.set_scale(1.0/float(self.objetos_propiedades))
				self.barra.set_position((self.propiedades.get_size()[0]-32,2))
				self.barra.global_position = (self.bar_pos[0]+self.pos_propiedades[0],self.bar_pos[1]+self.pos_propiedades[1])
				self.barra.graphic_update(self.propiedades)
				self.disferencia_barra = int(self.barra.position * self.propiedades.get_size()[1])
			else:
				self.barra_activa = False
			
			self.bar.blit(self.propiedades,self.pos_propiedades)
			
			if not self.borrando:
				borrar = self.font1.render("Borrar", 1, (0,0,0))
			else:
				borrar = self.font1.render("Borrar", 1, (255,0,0))
			self.pos_borrar = (seleccione_objeto.get_size()[0]+40, 2)
			self.size_borrar = borrar.get_size()
			self.bar.blit(borrar, self.pos_borrar)
			
			if self.selected == "NO":
				vaciar = self.font1.render("Nada",1,(255,0,0))
			else:
				vaciar = self.font1.render("Nada",1,(0,0,0))
			self.pos_vaciar = (seleccione_objeto.get_size()[0]+40+borrar.get_size()[0]+40, 2)
			self.size_vaciar = vaciar.get_size()
			self.bar.blit(vaciar,self.pos_vaciar)
			
			self.size_enviar = (100,100)
			self.pos_enviar = (pantalla.get_size()[0]-self.size_enviar[0],0)
			self.enviar = pf.boton_redondo(pantalla, self.pos_enviar, self.size_enviar, self.size_enviar[0]/2, "Guardar", True, 4, (255,0,0), (0,0,255), (0,255,0))
			
			pantalla.blit(self.bar,self.bar_pos)
			
			self.ayuda[0].cambiar_valores(self.pos_enviar,self.size_enviar)
			for q in self.ayuda:
				q.graphic_update(pantalla)
			
			self.iniciado = True
		if self.seleccionando_nombre:
			self.nombre_nivel.graphic_update(pantalla)
		if self.terminado:
			self.game_over.graphic_update(pantalla)
	def logic_update(self,events):
		ret = None
		if self.seleccionando_nombre:
			commands = self.nombre_nivel.logic_update(events)
			for command in commands:
				if command.find("END") != -1:
					self.level_name = command[:command.find("END")]
					generar_nivel.crear_nivel(self.phi.objetos,self.level_name,self.profile_name)
					self.terminado = True
		
		if self.terminado:
			ret = self.game_over.logic_update(events)
		
		if self.FT:
			self.FT = False
			self.actualizar_valores()

		self.events = events
		if self.iniciado and not self.seleccionando_nombre and not self.terminado:
			self.phi.logic_update(events)
			seleccionado = None
			mouse = events.get_mouse()
			x,y = mouse.get_position()
			pressed = mouse.get_pressed()
			if pressed[0] and pygame.time.get_ticks() > self.LT1 + 1000:
				self.LT1 = pygame.time.get_ticks()
				for obj in self.objetos:
					X,Y = obj[3]
					if x > X and x < X+self.size_buttons[0] and y > Y and y < Y+self.size_buttons[1]:
						seleccionado = obj[0]
						self.borrando = False
				if x > self.bar_pos[0] + self.pos_borrar[0] and x < self.bar_pos[0] + self.pos_borrar[0] + self.size_borrar[0] and y > self.bar_pos[1] + self.pos_borrar[1] and y < self.bar_pos[1] + self.pos_borrar[1] + self.size_borrar[1]:
					if len(self.phi.objetos) > 1:
						if self.borrando:
							self.borrando = False
						else:
							self.borrando = True
							self.vaciar_seleccionado()
				if x > self.bar_pos[0] + self.pos_vaciar[0] and x < self.bar_pos[0] + self.pos_vaciar[0] + self.size_vaciar[0] and y > self.bar_pos[1] + self.pos_vaciar[1] and y < self.bar_pos[1] + self.pos_vaciar[1] + self.size_vaciar[1]:
					self.vaciar_seleccionado()
				if not self.borrando and not self.seleccionando_posicion and not self.seleccionando_objeto and not self.marcando_posicion:
					if y < self.bar_pos[1] and  not(x > self.pos_enviar[0] and y < self.pos_enviar[1]+self.size_enviar[1]):
						if self.indice_selected != 9999:
							self.phi.objetos.append(self.phi.objetos[self.indice_selected])
							self.phi.objetos[self.indice_selected]._x = self.phi.objetos[self.indice_selected]._x + self.phi._CAM.X
							self.phi.objetos[self.indice_selected]._y = self.phi.objetos[self.indice_selected]._y + self.phi._CAM.Y
							del self.phi.objetos[self.indice_selected]
							self.indice_selected = 9999
							for q in range(len(self.phi.objetos)):
								if self.phi.objetos[q].TYPE == "jugador":
									indice_jugador = q
							del self.phi.objetos[indice_jugador]
							self.phi.objetos.append(lo.jugador.jugador(100,100,"Test",False))
							self.indice_jugador = len(self.phi.objetos)-1
							luces = []
							for q in range(len(self.phi.objetos)):
								if self.phi.objetos[q].TYPE == "Luz":
									luces.append(self.phi.objetos[q])
							for q in range(len(luces)):
								for w in range(len(self.phi.objetos)):
									if self.phi.objetos[w].TYPE == "Luz":
										del self.phi.objetos[w]
										self.indice_jugador -= 1
										break
							for q in luces:
								self.phi.objetos.append(q)
							self.actualizar_valores()
				elif self.borrando:
					for q in range(len(self.phi.objetos)-1,-1,-1):
						if y < self.bar_pos[1]:
							obj = self.phi.objetos[q]
							if x+self.phi._CAM.X > obj._x and x+self.phi._CAM.X < obj._x+obj.W and y+self.phi._CAM.Y > obj._y and y+self.phi._CAM.Y < obj._y+obj.H:
								del self.phi.objetos[q]
								self.indice_selected = 9999
								break
					
				if x > self.pos_enviar[0] and y < self.pos_enviar[1] + self.size_enviar[1]:
					if self.default_save == None:
						self.seleccionando_nombre = True
					else:
						generar_nivel.crear_nivel(self.phi.objetos,self.default_save,self.profile_name,self.dir)
			keys = events.get_keyboard()
			if keys[pygame.K_DELETE]:
				self.vaciar_seleccionado()
			if seleccionado != None:
				self.propiedades.fill((0,255,255))
				self.ant_selected = self.selected
				self.selected = seleccionado
				self.x_esc = "1"
				self.y_esc = "1"
				self.checkbox_selected = False
				self.seleccionada_select = []
				self.disferencia_barra = 0
				self.tamano_simple_escrito = "1"
				self.barra.set_dimensions((30,self.propiedades.get_size()[1]-4))
			if self.barra_activa:
				self.barra.logic_update(events)
			if self.selected != "NO" and not self.seleccionando_posicion and not self.seleccionando_objeto and not self.marcando_posicion:
				self.analizar_propiedades(self.propiedades)
				if self.indice_selected != 9999:
					self.phi.objetos[self.indice_selected] = self.tran.transform(self.crear_phrase())[0]
					self.phi.objetos[self.indice_selected]._x -= self.phi.objetos[self.indice_selected].W/2
					self.phi.objetos[self.indice_selected]._y -= self.phi.objetos[self.indice_selected].H/2
				else:
					self.indice_selected = len(self.phi.objetos)
					self.phi.objetos.append(self.tran.transform(self.crear_phrase())[0])
				if self.phi.objetos[self.indice_selected].TYPE == "Button":
					self.phi.objetos[self.indice_selected].activado = False
		for q in self.ayuda:
			q.profile = self.profile_name
			q.logic_update(events)
		if ret != None:
			return ret
	def actualizar_valores(self):
		for obj in self.phi.objetos:
			if obj.TYPE != "jugador":
				nums = []
				for w in range(len(obj.NAME)-1,-1,-1):
					if obj.NAME[w] != " ":
						nums.append(obj.NAME[w])
					else:
						break
				nums.reverse()
				n = ""
				for w in nums:
					n += str(w)
				n = int(n)
			if obj.TYPE != "Wall":
				for q in range(len(self.Values)):
					if self.Values[q][0] == obj.TYPE:
						self.Values[q][1] = n+1
			else:
				esq = False
				for q in obj.TAGS:
					if q == "Esquina":
						esq = True
				if esq:
					self.Values[4][1] = n+1
				else:
					self.Values[1][1] = n+1
	def vaciar_seleccionado(self):
		if self.selected != "NO":
			self.selected = "NO"
			del self.phi.objetos[self.indice_selected]
			self.indice_selected = 9999
	def posicion_act(self,pantalla):
		for q in range(0,pantalla.get_size()[0],50):
			act = self.phi._CAM.X + q
			text = self.font2.render(str(act), 1, (255,255,255))
			pantalla.blit(text, (q-text.get_size()[0]/2,0))
		
		for q in range(0,pantalla.get_size()[1],50):
			act = self.phi._CAM.Y + q
			text = self.font2.render(str(act), 1, (255,255,255))
			pantalla.blit(text, (0,q-text.get_size()[1]/2))
		
		for q in range(pantalla.get_size()[0]):
			act = self.phi._CAM.X + q
			if act == 0:
				linea = pygame.Surface((2,pantalla.get_size()[1]))
				linea.fill((255,255,255))
				pantalla.blit(linea,(q-1,0))
		
		for q in range(pantalla.get_size()[1]):
			act = self.phi._CAM.Y + q
			if act == 0:
				linea = pygame.Surface((pantalla.get_size()[0],2))
				linea.fill((255,255,255))
				pantalla.blit(linea,(0,q-1))
	def crear_phrase(self):
		phrase = com.declaration(self.selected)
		x,y = pygame.mouse.get_pos()
		if self.selected == "background":
			x_esc = self.x_esc
			y_esc = self.y_esc
			if self.x_esc == "":
				x_esc = "1"
			if self.y_esc == "":
				y_esc = "1"
			cont = [x,y,x_esc,y_esc,"'Background "+str(self.Values[0][1])+"'",self.seleccionada_select[0]]
		elif self.selected == "wall":
			x_esc = self.x_esc
			y_esc = self.y_esc
			if self.x_esc == "":
				x_esc = "1"
			if self.y_esc == "":
				y_esc = "1"
			cont = [x,y,x_esc,y_esc,self.checkbox_selected,"'"+str(self.seleccionada_select[0])+"'","'Wall "+str(self.Values[1][1])+"'"]
		elif self.selected == "enemy":
			cont = [x,y,"'Enemy "+str(self.Values[2][1])+"'","'"+str(self.seleccionada_select[0])+"'",False,"'"+str(self.seleccionada_select[1])+"'",self.seleccionar_posicion_data[0][0],self.seleccionar_posicion_data[2][0],self.seleccionar_posicion_data[1][0],self.seleccionar_posicion_data[3][0]]
		elif self.selected == "coin":
			cont = [x,y,"'Coin "+str(self.Values[3][1])+"'"]
		elif self.selected == "esquina":
			cont = [x,y,str(self.seleccionada_select[0]),"'Esquina "+str(self.Values[4][1])+"'"]
		elif self.selected == "extra_life":
			cont = [x,y,"'Vida extra "+str(self.Values[5][1])+"'"]
		elif self.selected == "box":
			cont = [x,y,"'Box "+str(self.Values[6][1])+"'"]
		elif self.selected == "bomb":
			cont = [x,y,"'Bomba "+str(self.Values[7][1])+"'"]
		elif self.selected == "button":
			cont = [x,y,"'"+self.objeto_seleccionado+"'","'Button "+str(self.Values[8][1])+"'","'"+str(self.seleccionada_select[0])+"'"]
		elif self.selected == "puerta":
			if self.tamano_simple_escrito == "0" or self.tamano_simple_escrito == "":
				tam = "1"
			else:
				tam = self.tamano_simple_escrito
			cont = [x,y,"'"+self.seleccionada_select[0]+"'","'Puerta "+str(self.Values[9][1])+"'",int(tam)]
		elif self.selected == "checkpoint":
			cont = [x,y,"'Checkpoint "+str(self.Values[10][1])+"'"]
		elif self.selected == "teletransportador":
			cont = [x,y,self.posicion_marcada[0],self.posicion_marcada[1],"'Teletransportador "+str(self.Values[11][1])+"'"]
		elif self.selected == "luz":
			x_esc = self.x_esc
			y_esc = self.y_esc
			if self.x_esc == "":
				x_esc = "1"
			if self.y_esc == "":
				y_esc = "1"
			cont = [x,y,x_esc,y_esc,self.rango_marcado,"'Luz "+str(self.Values[12][1])+"'"]
		elif self.selected == "laser":
			cont = [x,y,self.seleccionada_select[0],self.rango_marcado,"'Laser "+str(self.Values[13][1])+"'",False]
		elif self.selected == "meta":
			if self.tamano_simple_escrito == "0" or self.tamano_simple_escrito == "":
				esc = "1"
			else:
				esc = self.tamano_simple_escrito
			cont = [x,y,int(esc),"'"+str(self.seleccionada_select[0])+"'", "'Meta "+str(self.Values[14][1])+"'"]
		for q in range(len(cont)):
			cont[q] = str(cont[q])
		phrase.add_content(cont)
		return phrase
	def escribir(self,events,tipo = str):
		pressed = self.events.get_keyboard()
		escrito1 = pf.Get_written(pressed)
		escrito = ""
		for q in escrito1:
			if tipo == int:
				if q.isdigit() or q == "Backspace":
					if q != "Backspace":
						escrito += q
					else:
						escrito = "Backspace"
						break
			else:
				if q != "Backspace":
					escrito += q
				else:
					escrito = "Backspace"
		if pressed != self.last_pressed:
			self.last_pressed = pressed
			if escrito != "":
				if self.escribiendo_en == "x_esc":
					if self.x_esc == "    ":
						self.x_esc = ""
					if escrito != "Backspace":
						self.x_esc += escrito
					else:
						self.x_esc = self.x_esc[:len(self.x_esc)-1]
				elif self.escribiendo_en == "y_esc":
					if self.y_esc == "    ":
						self.y_esc = ""
					if escrito != "Backspace":
						self.y_esc += escrito
					else:
						self.y_esc = self.y_esc[:len(self.y_esc)-1]
	def tamano(self,surface,mouse,global_pos,x,y,ubicacion=1):
		tamano = self.font1.render("Tamano: ("+str(self.x_esc)+","+str(self.y_esc)+")",1,(0,0,0))
		pos_tamano = (2,2+tamano.get_size()[1]*ubicacion+5*ubicacion-self.disferencia_barra)
		surface.blit(tamano,pos_tamano)
		test1 = self.font1.render("Tamano: (",1,(0,0,0)).get_size()
		test2 = self.font1.render("Tamano: ("+str(self.x_esc),1,(0,0,0)).get_size()
		test3 = self.font1.render("Tamano: ("+str(self.x_esc)+",",1,(0,0,0)).get_size()
		test4 = self.font1.render("Tamano: ("+str(self.x_esc)+","+str(self.y_esc),1,(0,0,0)).get_size()
		if mouse.get_pressed()[0]:
			if x > global_pos[0]+2+test1[0]+1 and x < global_pos[0]+test2[0] and y > global_pos[1]+pos_tamano[1] and y < global_pos[1]+pos_tamano[1]+test1[1]:
				self.escribiendo_en = "x_esc"
			elif x > global_pos[0]+2+test3[0]+1 and x < global_pos[0]+test4[0] and y > global_pos[1]+pos_tamano[1] and y < global_pos[1]+pos_tamano[1]+test1[1]:
				self.escribiendo_en = "y_esc"
			else:
				self.escribiendo_en = ""
		self.escribir(self.events,int)
	def checkbox(self,surface,mouse,global_pos,x,y,titulo,ubicacion=1):
		title = self.font1.render(str(titulo),1,(0,0,0))
		pos_title = (2,2+title.get_size()[1]*ubicacion+5*ubicacion-self.disferencia_barra)
		surface.blit(title,pos_title)
		size_checkbox = (title.get_size()[1]+4,title.get_size()[1]+4)
		checkbox = pygame.Surface(size_checkbox)
		checkbox.fill((255,255,255))
		checkbox = pf.add_border(checkbox, 4, 4, 4, 4, (0,0,0))
		pos_checkbox = (2+title.get_size()[0]+5,pos_title[1]-4)
		x_checkbox = self.font1.render("X",1,(255,0,0))
		if self.checkbox_selected:
			checkbox.blit(x_checkbox,(size_checkbox[0]/2-x_checkbox.get_size()[0]/2,size_checkbox[1]/2-x_checkbox.get_size()[1]/2))
		surface.blit(checkbox,pos_checkbox)
		if mouse.get_pressed()[0] and pygame.time.get_ticks() > self.LP1+100:
			self.LP1 = pygame.time.get_ticks()
			if x > global_pos[0]+pos_checkbox[0] and x < global_pos[0]+pos_checkbox[0]+size_checkbox[0] and y > global_pos[1]+pos_checkbox[1] and y < global_pos[1]+pos_checkbox[1]+size_checkbox[1]:
				if self.checkbox_selected:
					self.checkbox_selected = False
				else:
					self.checkbox_selected = True
	def select(self,surface,mouse,global_pos,x,y,title,opciones,ubicacion,indice=0):
		self.opciones = opciones
		title = self.font1.render(title+": ",1,(0,0,0))
		pos_title = (2,2+title.get_size()[1]*ubicacion+5*ubicacion-self.disferencia_barra)
		self.propiedades.blit(title,pos_title)
		separador = self.font1.render("; ",1,(0,0,0))
		x_actu = pos_title[0]+title.get_size()[0]
		pos_opciones = []
		tamano_opciones = []
		while len(self.seleccionada_select)-1 < indice:
			if type(opciones[0]) == int or type(opciones[0]) == str:
				if opciones[0].isdigit():
					self.seleccionada_select.append(int(opciones[0]))
				else:
					self.seleccionada_select.append(opciones[0])
			else:
				self.seleccionada_select.append(0)
		for q in range(len(opciones)):
			if isinstance(opciones[q],str):
				indice_selected = None
				for w in range(len(opciones)):
					if type(opciones[w]) == int or type(opciones[w]) == str:
						if str(opciones[w]) == str(self.seleccionada_select[indice]):
							indice_selected = w
				if indice_selected == None:
					indice_selected = self.seleccionada_select[indice]
				if q != indice_selected:
					opt_act = self.font1.render(opciones[q],1,(0,0,0))
				else:
					opt_act = self.font1.render(opciones[q],1,(255,0,0))
			else:
				test1 = pygame.Surface((title.get_size()[1]+4,title.get_size()[1]+4))
				if q != self.seleccionada_select[indice]:
					test1.fill((255,255,255))
				else:
					test1.fill((255,0,0))
				test1.blit(pygame.transform.scale(opciones[q],(title.get_size()[1],title.get_size()[1])),(2,2))
				opt_act = test1
			pos_opt = (x_actu,pos_title[1])
			pos_opciones.append(pos_opt)
			tamano_opciones.append(opt_act.get_size())
			self.propiedades.blit(opt_act,pos_opt)
			self.propiedades.blit(separador,(pos_opt[0]+opt_act.get_size()[0],pos_opt[1]))
			x_actu += opt_act.get_size()[0]+separador.get_size()[0]
		if mouse.get_pressed()[0]:
			for q in range(len(opciones)):
				X,Y = pos_opciones[q]
				W,H = tamano_opciones[q]
				if x > global_pos[0]+X and x < global_pos[0]+X+W and y > global_pos[1]+Y and y < global_pos[1]+Y+H:
					if type(self.opciones[q]) == int or type(self.opciones[q]) == str:
						self.seleccionada_select[indice] = self.opciones[q]
					else:
						self.seleccionada_select[indice] = q
	def no_hay_opciones(self,surface):
		title = self.font1.render("No hay propiedades",1,(255,0,0))
		ubicacion = 1
		surface.blit(title,(2,2+title.get_size()[1]*ubicacion+5*ubicacion))
	def mantenimiento(self,surface,texto,ubic = 1):
		title = self.font1.render(texto,1,(255,0,0))
		ubicacion = ubic
		surface.blit(title,(2,2+title.get_size()[1]*ubicacion+5*ubicacion))
	def seleccionar_posicion(self,surface,mouse,global_pos,x,y,title,direccion,ubicacion=1,indice=0,ultimo = False):
		if len(self.seleccionar_posicion_data) == indice:
			self.seleccionar_posicion_data.append([0])
		pos = self.seleccionar_posicion_data[indice][0]
		if self.seleccionado_seleccionar_posicion == title:
			titulo = self.font1.render(title+": "+str(pos),1,(255,0,0))
		else:
			titulo = self.font1.render(title+": "+str(pos),1,(0,0,0))
		pos_title = (2,2+titulo.get_size()[1]*ubicacion+5*ubicacion-self.disferencia_barra)
		self.propiedades.blit(titulo,pos_title)
		if pygame.time.get_ticks() > self.LT2+100:
			if ultimo:
				self.LT2 = pygame.time.get_ticks()
			if mouse.get_pressed()[0]:
				if x > global_pos[0]+pos_title[0] and x < global_pos[0]+pos_title[0]+titulo.get_size()[0] and y > global_pos[1]+pos_title[1] and y < global_pos[1]+pos_title[1]+titulo.get_size()[1]:
					if self.seleccionado_seleccionar_posicion != title:
						self.seleccionado_seleccionar_posicion = title
					else:
						self.seleccionado_seleccionar_posicion = None
				elif y < self.bar_pos[1]:
					if self.seleccionado_seleccionar_posicion == title:
						if direccion == "Vertical":
							self.seleccionar_posicion_data[indice][0] = x + self.phi._CAM.X
						else:
							self.seleccionar_posicion_data[indice][0] = y + self.phi._CAM.Y
		if self.seleccionado_seleccionar_posicion == title:
			self.seleccionando_posicion = True
			if direccion == "Vertical":
				linea = pygame.Surface((2,self.pantalla.get_size()[1]-self.bar_size[1]))
				linea.fill((255,255,255))
				self.pantalla.blit(linea,(x-1,0))
			if direccion == "Horizontal":
				linea = pygame.Surface((self.pantalla.get_size()[0],2))
				linea.fill((255,255,255))
				self.pantalla.blit(linea,(0,y-1))
	def seleccionar_objeto(self,surface,mouse,global_pos,x,y,title,ubicacion):
		if not self.seleccionando_objeto:
			title = self.font1.render(title,1,(0,0,0))
		else:
			title = self.font1.render(title,1,(255,0,0))
		pos_title = (2,2+title.get_size()[1]*ubicacion+5*ubicacion-self.disferencia_barra)
		self.propiedades.blit(title,pos_title)
		texto = self.font1.render(": "+self.objeto_seleccionado,1,(0,0,0))
		self.propiedades.blit(texto,(pos_title[0]+title.get_size()[0],pos_title[1]))
		if mouse.get_pressed()[0]:
			if pygame.time.get_ticks() > self.LT3 + 200:
				self.LT3 = pygame.time.get_ticks()
				if x > global_pos[0] + pos_title[0] and x < global_pos[0] + pos_title[0] + title.get_size()[0] and y > global_pos[1] + pos_title[1] and y < global_pos[1] + pos_title[1] + title.get_size()[1]:
					if self.seleccionando_objeto:
						self.seleccionando_objeto = False
					else:
						self.seleccionando_objeto = True
				elif y < self.bar_pos[1]:
					for q in range(len(self.phi.objetos)-1,-1,-1):
						obj = self.phi.objetos[q]
						if x > obj._x and x < obj._x + obj.W and y > obj._y and y < obj._y + obj.H:
							self.objeto_seleccionado = obj.NAME
							break
	def marcar_posicion(self,surface,mouse,global_pos,x,y,title,ubicacion):
		if self.marcando_posicion:
			color = (255,0,0)
		else:
			color = (0,0,0)
		title = self.font1.render(title,1,color)
		pos_title = (2,2+title.get_size()[1]*ubicacion+5*ubicacion-self.disferencia_barra)
		self.propiedades.blit(title,pos_title)
		texto = self.font1.render(": ("+str(self.posicion_marcada[0])+","+str(self.posicion_marcada[1])+")", 1, color)
		pos_texto = (2 + title.get_size()[0],pos_title[1])
		self.propiedades.blit(texto,pos_texto)
		pressed = mouse.get_pressed()[0]
		if pygame.time.get_ticks() > self.LT4 + 100:
			self.LT4 = pygame.time.get_ticks()
			if x > global_pos[0] + pos_title[0] and x < global_pos[0] + pos_texto[0] + texto.get_size()[0] and y > global_pos[1] + pos_title[1] and y < global_pos[1] + pos_title[1] + title.get_size()[1]:
				if pressed:
					if self.marcando_posicion:
						self.marcando_posicion = False
					else:
						self.marcando_posicion = True
			elif y < self.bar_pos[1]:
				if pressed:
					self.posicion_marcada = [x+self.phi._CAM.X,y+self.phi._CAM.Y]
		if self.marcando_posicion and y < self.bar_pos[1]:
			lineaH = pygame.Surface((self.pantalla.get_size()[0],4))
			lineaH.fill((255,255,255))
			lineaV = pygame.Surface((4,self.pantalla.get_size()[1]-self.bar_size[1]))
			lineaV.fill((255,255,255))
			self.pantalla.blit(lineaH,(0,y-2))
			self.pantalla.blit(lineaV,(x-2,0))
	def bar_range(self,surface,mouse,global_pos,x,y,title,rango,ubicacion):
		title = self.font1.render(title+":",1,(0,0,0))
		pos_title = (2,2+title.get_size()[1]*ubicacion+5*ubicacion-self.disferencia_barra)
		self.propiedades.blit(title,pos_title)
		Rango = rango[1] - rango[0]
		self.barra2_activa = True
		self.barra2.set_scale(1.0/float(Rango))
		self.barra2.set_position((pos_title[0] + title.get_size()[0] + 4, pos_title[1]))
		self.barra2.global_position = global_pos
		self.barra2.set_dimensions((title.get_size()[1] + 4,150))
		self.barra2.set_horizontal_mode()
		self.barra2.set_border((0,0,0))
		self.barra2.logic_update(self.events)
		self.barra2.graphic_update(self.propiedades)
		self.rango_marcado = int(self.barra2.position * float(Rango)) + rango[0]
	def tamano_simple(self,surface,mouse,global_pos,x,y,title,ubicacion):
		if self.escribiendo_tamano_simple:
			title = self.font1.render(title+": "+self.tamano_simple_escrito,1,(255,0,0))
		else:
			title = self.font1.render(title+": "+self.tamano_simple_escrito,1,(0,0,0))
		pos_title = (2,2+title.get_size()[1]*ubicacion+5*ubicacion-self.disferencia_barra)
		self.propiedades.blit(title,pos_title)
		if pygame.time.get_ticks() > self.LT5 + 100:
			self.LT5 = pygame.time.get_ticks()
			if mouse.get_pressed()[0]:
				if x > global_pos[0] + pos_title[0] and x < global_pos[0] + pos_title[0] + title.get_size()[0] and y > global_pos[1] + pos_title[1] and y < global_pos[1] + pos_title[1] + title.get_size()[1]:
					if self.escribiendo_tamano_simple:
						self.escribiendo_tamano_simple = False
					else:
						self.escribiendo_tamano_simple = True
		pressed = self.events.get_keyboard()
		escrito1 = pf.Get_written(pressed)
		escrito = ""
		for q in escrito1:
			if q.isdigit() or q == "Backspace":
				if q != "Backspace":
					escrito += q
				else:
					escrito = "Backspace"
					break
		if self.escribiendo_tamano_simple:
			if pressed != self.last_pressed2:
				self.last_pressed2 = pressed
				if escrito != "Backspace":
					self.tamano_simple_escrito += escrito
				else:
					self.tamano_simple_escrito = self.tamano_simple_escrito[:len(self.tamano_simple_escrito)-2]
	def analizar_propiedades(self,surface):
		if self.events != None:
			self.objetos_propiedades = 0
			mouse = self.events.get_mouse()
			x,y = mouse.get_position()
			global_pos = (self.bar_pos[0]+self.pos_propiedades[0],self.bar_pos[1]+self.pos_propiedades[1])
			self.seleccionando_posicion = False
			self.barra2_activa = False
			if self.selected == "background":
				self.objetos_propiedades += 1
				self.tamano(surface,mouse,global_pos,x,y)
				self.objetos_propiedades += 1
				self.select(surface, mouse, global_pos, x, y, "Tipo", ["1","2","3","4"], self.objetos_propiedades, 0)
			elif self.selected == "wall":
				self.objetos_propiedades += 1
				self.tamano(surface, mouse,global_pos , x, y)
				self.objetos_propiedades += 1
				self.checkbox(surface,mouse,global_pos,x,y,"Vertical",self.objetos_propiedades)
				self.objetos_propiedades += 1
				self.select(surface,mouse,global_pos,x,y,"Posicion",["Arriba","Abajo","Izquierda","Derecha","Centro","Freno"],self.objetos_propiedades)
			elif self.selected == "enemy":
				self.objetos_propiedades += 1
				self.select(surface, mouse, global_pos, x, y, "Tipo", ["1","2"], self.objetos_propiedades)
				self.objetos_propiedades += 1
				self.select(surface,mouse,global_pos,x,y,"Direccion", ["Random","Vertical","Horizontal"], self.objetos_propiedades, 1)
				self.objetos_propiedades += 1
				self.seleccionar_posicion(surface, mouse, global_pos, x, y, "Limite Izq","Vertical",self.objetos_propiedades,0)
				self.objetos_propiedades += 1
				self.seleccionar_posicion(surface, mouse, global_pos, x, y, "Limite Der","Vertical",self.objetos_propiedades,1)
				self.objetos_propiedades += 1
				self.seleccionar_posicion(surface, mouse, global_pos, x, y, "Limite Arr","Horizontal",self.objetos_propiedades,2)
				self.objetos_propiedades += 1
				self.seleccionar_posicion(surface, mouse, global_pos, x, y, "Limite Ab","Horizontal",self.objetos_propiedades,3,True)
			elif self.selected == "coin":
				self.no_hay_opciones(surface)
			elif self.selected == "esquina":
				self.objetos_propiedades += 1
				arr = []
				for q in range(0,271,90):
					arr.append(pygame.transform.rotate(img.esquina,q))
				self.select(surface, mouse, global_pos, x, y, "Rotacion", arr, 1)
			elif self.selected == "extra_life":
				self.no_hay_opciones(surface)
			elif self.selected == "box":
				self.no_hay_opciones(surface)
			elif self.selected == "bomb":
				self.no_hay_opciones(surface)
			elif self.selected == "button":
				self.objetos_propiedades += 1
				self.select(surface, mouse, global_pos, x, y, "Default", ["Disabled","Enabled"], self.objetos_propiedades)
				self.objetos_propiedades += 1
				self.seleccionar_objeto(surface, mouse, global_pos, x, y, "Seleccionar objeto", self.objetos_propiedades)
			elif self.selected == "puerta":
				self.objetos_propiedades += 1
				self.select(surface, mouse, global_pos, x, y, "Angulo", ["Vertical","Horizontal"], self.objetos_propiedades)
				self.objetos_propiedades += 1
				self.tamano_simple(surface, mouse, global_pos, x, y, "Longitud", self.objetos_propiedades)
			elif self.selected == "checkpoint":
				self.no_hay_opciones(surface)
			elif self.selected == "teletransportador":
				self.objetos_propiedades += 1
				self.marcar_posicion(surface, mouse, global_pos, x, y, "Posicion salida", self.objetos_propiedades)
			elif self.selected == "luz":
				self.objetos_propiedades += 1
				self.tamano(surface, mouse, global_pos, x, y, self.objetos_propiedades)
				self.objetos_propiedades += 1
				self.bar_range(surface, mouse, global_pos, x, y, "Potencia", [-20,20], self.objetos_propiedades)
			elif self.selected == "laser":
				self.objetos_propiedades += 1
				im = img.laser
				arr = [im,pygame.transform.rotate(im,270),pygame.transform.rotate(im,180),pygame.transform.rotate(im,90)]
				self.select(surface, mouse, global_pos, x, y, "Posicion", arr, self.objetos_propiedades)
				self.objetos_propiedades += 1
				self.bar_range(surface, mouse, global_pos, x, y, "Velocidad", [0,10], self.objetos_propiedades)
			elif self.selected == "meta":
				self.objetos_propiedades += 1
				self.tamano_simple(surface, mouse, global_pos, x, y, "Longitud", self.objetos_propiedades)
				self.objetos_propiedades += 1
				self.select(surface, mouse, global_pos, x, y, "Direccion", ["Vertical","Horizontal"], self.objetos_propiedades)
				
		return surface

class new_level:
	def __init__(self):
		self.seleccionables = []
		self.seleccionables.append(["background",img.test_background,"Hay distintos tipos de fondos con distintas velocidades y algunos que lastiman al pisarlos"])
		self.seleccionables.append(["wall",img.wall1,"Las paredes bloquean que los tux y los enemigos no puedan salir hacia el vacio"])
		self.seleccionables.append(["enemy",img.test_enemigo,"Mientras mas enemigos, mas dificil va a ser el nivel y hay distintos tipos que lastiman mas"])
		self.seleccionables.append(["coin",img.moneda,"Las monedas se usan para comprar escudos e invulneravilidad y proximamente mas cosas"])
		self.seleccionables.append(["esquina",img.esquina,"Las esquinas son para que queden mejor las paredes al crear el nivel y quede todo mas prolijo"])
		self.seleccionables.append(["extra_life",img.tux_azul,"Cuando el tux agarre una de estas, este obtendra una vida extra"])
		self.seleccionables.append(["box",img.caja,"Nunca se sabe que objeto puede aparecer cuando vayas a abrir esta caja"])
		self.seleccionables.append(["bomb",img.test_bomba,"Cuidado que si la activa puede explotar todo lo de al rededor, incluso si estas cerca cuando explota podes perder vida"])
		self.seleccionables.append(["button",img.boton_no_presionado,"Con este boton puede hacer aparecer o desaparecer cualquier cosa"])
		self.seleccionables.append(["puerta",img.puerta_test,"Una puerta automatica que se abre solo cuando te acercas"])
		self.seleccionables.append(["checkpoint",img.checkpoint_sin_act,"Si el tux pasa por aqui la proxima vez que inicie el juego, aparecera por ahi"])
		self.seleccionables.append(["teletransportador",img.teletransportador_in,"Marque el lugar de salida y luego coloque el objeto donde quiera que este la entrada"])
		self.seleccionables.append(["luz",img.lampara,"Se ve poco? Bueno siempre podes iluminar todo mejor o podes apagar la luz oscureciendo todo"])
		self.seleccionables.append(["laser",img.laser,"Dispara en la direccion de su punta hasta la pared mas cercana"])
		self.seleccionables.append(["meta",img.meta,"Si el jugador llega a la meta, se reiniciaran todos los progresos del nivel y se reiniciara el juego"])
		self.objetos = objetos(self)
	def graphic_update(self,pantalla):
		self.objetos.graphic_update(pantalla)	
	def logic_update(self,events):
		self.objetos.logic_update(events)