#!/usr/bin/env python3
import os

# Limpiar la terminal
def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def crear_tablero (filas,columnas):
	lista_columna=[]
	for columna in range(columnas):
		lista_fila=[]
		for _ in range(filas):
			lista_fila.append('.')
		lista_columna.append(lista_fila)
	return lista_columna
	

def insertar_ficha (tablero,columna,color):
	tope=-len(tablero)
	fila=-1
	while (fila>=tope)and(tablero[fila][columna]!='.'):
		fila-=1
	if (fila>=tope):
		tablero[fila][columna]=color
	else:
		print('La fila esta llena insertar en otra columna')
		nuevaColumna=int(input())
		insertar_ficha(tablero,nuevaColumna,color)
	return tablero

def revisar_filas_vertical(tablero,color):
	tamaño_filas=len(tablero)
	tamaño_columnas=len(tablero[0])
	gano=False
	for i in range(tamaño_columnas):
		cont=0
		for j in range(tamaño_filas):
			if (tablero[j][i]==color):
				cont+=1
				if (cont==4):
					gano=True
			else:
				cont=0
	return gano

def revisar_filas_horizontal(tablero,color):
	tamaño_filas=len(tablero)
	tamaño_columnas=len(tablero[0])
	gano=False
	for i in range(tamaño_filas):
		cont=0
		for j in range(tamaño_columnas):
			if (tablero[i][j]==color):
				cont+=1
				if (cont==4):
					gano=True
			else:
				cont=0
	return gano

def revisar_filas_diagonal_arriba(tablero,color):
	tamaño_filas=len(tablero)
	tamaño_columnas=len(tablero[0])
	x=0
	y=0
	gano=False
	for i in range(tamaño_columnas-3):
		cont=0
		aux_i=i
		for j in range(3,tamaño_filas):
			aux_j=j
			while (aux_i<tamaño_columnas and tablero[aux_j][aux_i]==color and cont<4):
				#print(f'Posicion en columnas :i {aux_i}, posicion en filas:j : {aux_j} contenido : {tablero[aux_j][aux_i]}')
				cont+=1
				aux_i+=1
				aux_j-=1
			
			if (cont==4):
				gano=True
				break
			else:
				cont=0
		if (gano==True) :
			break
	return gano

def revisar_filas_diagonal_abajo(tablero,color):
	tamaño_filas=len(tablero)
	tamaño_columnas=len(tablero[0])
	x=0
	y=0
	gano=False
	for i in range(tamaño_columnas-3):
		cont=0
		aux_i=i
		for j in range(tamaño_filas-3):
			aux_j=j
			while (aux_i<tamaño_columnas and tablero[aux_j][aux_i]==color and cont<4):
				#print(f'Posicion en columnas :i {aux_i}, posicion en filas:j : {aux_j} contenido : {tablero[aux_j][aux_i]}')
				cont+=1
				aux_i+=1
				aux_j+=1
			
			if (cont==4):
				gano=True
				break
			else:
				cont=0
		if (gano==True) :
			break
	return gano

def comprobar_ganador(tablero,color):
	gano1=revisar_filas_diagonal_abajo(tablero,color)
	gano2=revisar_filas_diagonal_arriba(tablero,color)
	gano3=revisar_filas_horizontal(tablero,color)
	gano4=revisar_filas_vertical(tablero,color)
	
	return (gano1 or gano2 or gano3 or gano4)
	
	
def imprimir_tablero(tablero):
	print(['0','1','2','3','4','5','6'])
	for fila in tablero:
		print(fila)
	print("--------------------------------------")

	
#Primer []=filas Segundo[]=columnas
tablero=crear_tablero(7,6)

win_x="""

 ██████╗  █████╗ ███╗   ██╗ █████╗ ██████╗  ██████╗ ██████╗            
██╔════╝ ██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔═══██╗██╔══██╗           
██║  ███╗███████║██╔██╗ ██║███████║██║  ██║██║   ██║██████╔╝           
██║   ██║██╔══██║██║╚██╗██║██╔══██║██║  ██║██║   ██║██╔══██╗           
╚██████╔╝██║  ██║██║ ╚████║██║  ██║██████╔╝╚██████╔╝██║  ██║           
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝           
                                                                       
     ██╗██╗   ██╗ ██████╗  █████╗ ██████╗  ██████╗ ██████╗     ██╗  ██╗
     ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    ╚██╗██╔╝
     ██║██║   ██║██║  ███╗███████║██║  ██║██║   ██║██████╔╝     ╚███╔╝ 
██   ██║██║   ██║██║   ██║██╔══██║██║  ██║██║   ██║██╔══██╗     ██╔██╗ 
╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██████╔╝╚██████╔╝██║  ██║    ██╔╝ ██╗
 ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝
                                                                       
"""

win_o="""

 ██████╗  █████╗ ███╗   ██╗ █████╗ ██████╗  ██████╗ ██████╗             
██╔════╝ ██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔═══██╗██╔══██╗            
██║  ███╗███████║██╔██╗ ██║███████║██║  ██║██║   ██║██████╔╝            
██║   ██║██╔══██║██║╚██╗██║██╔══██║██║  ██║██║   ██║██╔══██╗            
╚██████╔╝██║  ██║██║ ╚████║██║  ██║██████╔╝╚██████╔╝██║  ██║            
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝            
                                                                        
     ██╗██╗   ██╗ ██████╗  █████╗ ██████╗  ██████╗ ██████╗      ██████╗ 
     ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    ██╔═══██╗
     ██║██║   ██║██║  ███╗███████║██║  ██║██║   ██║██████╔╝    ██║   ██║
██   ██║██║   ██║██║   ██║██╔══██║██║  ██║██║   ██║██╔══██╗    ██║   ██║
╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██████╔╝╚██████╔╝██║  ██║    ╚██████╔╝
 ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ 
                                                                        


"""

print('Comienza el jugador X , luego Jugador O, intercaladamente')
movimiento=0
imprimir_tablero(tablero)
while True:
	gano=False
	colorGanador=''
	if ((movimiento%2)==0):
		print(f'Ingresar la columna del 0 al {len(tablero[0])} donde se colocará su signo X')
		columna=int(input('----> '))
		insertar_ficha(tablero,columna,'X')
		if (comprobar_ganador(tablero,'X')==True):
			colorGanador=win_x
	else:
		print(f'Ingresar la columna del 0 al {len(tablero[0])} donde se colocará su signo O')
		columna=int(input('----> '))
		insertar_ficha(tablero,columna,'O')
		if (comprobar_ganador(tablero,'O')==True):
			colorGanador=win_o
	movimiento+=1
	limpiar_terminal()
	imprimir_tablero(tablero)
	if (colorGanador!=''):
		print(f'{colorGanador}')
		break
