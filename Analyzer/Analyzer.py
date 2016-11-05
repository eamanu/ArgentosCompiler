# -*- coding: utf-8 -*-
"""@package Reader
Módulo que analiza el código fuente

@author Arias Emmanuel
@date 24/10/2016

"""

from Reader import Reader
from enum import Enum
import string
import numpy as np

class campoCaracter:
    
    def __init__(self):
        self.mVariable = np.array([['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'  ], #A
                                    ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P' ], #R
                                    ['Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X' ], #G
                                    ['Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f' ], #E
                                    ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ], #N
                                    ['o', 'p', 'q', 'r', 's', 't', 'u', 'v' ], #T
                                    ['w', 'x', 'y', 'z',  1 ,  2 ,  3 ,  4  ], #O
                                    [ 5 ,  6 ,  7 ,  8 ,  9 ,  0 ,  99, -99 ]  #S
                                   ])        
                                    # A    R    G    E    N    T    O     S
    def DameCaracter (self, y, x, caballo):
      self.y, self.x = caballo.damePosCaballo()
      return self.mVariable[self.y][self.x]
            
        
        

class coor(Enum):
    """Coordenadas del tablero
    """
    a = 0
    r = 1
    g = 2
    e = 3
    n = 4 
    t = 5
    o = 6
    s = 7
    

class caballo:
    
    def __init__(self):
        self.y = coor.s
        self.x = coor.r
    
    def dameCoordenadasEnNumero(self, yy,xx):
        y = yy.lower()
        x = xx.lower()
        
        #Coloca coordenada en y
        if y == 'a':
            y = coor.a
        if y == 'r':
            y = coor.r
        if y == 'g':
            y = coor.g
        if y == 'e':
            y = coor.e
        if y == 'n':
            y = coor.n
        if y == 't':
            y = coor.t
        if y == 'o':
            y = coor.o
        if y == 's':
            y = coor.s
        
        #Coloca coordenada en x
        if x == 'a':
            x = coor.a
        if x == 'r':
            x = coor.r
        if x == 'g':
            x = coor.g
        if x == 'e':
            x = coor.e
        if x == 'n':
            x = coor.n
        if x == 't':
            x = coor.t
        if x == 'o':
            x = coor.o
        if x == 's':
            x = coor.s
        
        return y, x 
        
    def mover (self, yy, xx):
        y = yy.lower()
        x = xx.lower()
        
        #Coloca coordenada en y
        if y == 'a':
            self.y = coor.a
        if y == 'r':
            self.y = coor.r
        if y == 'g':
            self.y = coor.g
        if y == 'e':
            self.y = coor.e
        if y == 'n':
            self.y = coor.n
        if y == 't':
            self.y = coor.t
        if y == 'o':
            self.y = coor.o
        if y == 's':
            self.y = coor.s
        
        #Coloca coordenada en x
        if x == 'a':
            self.x = coor.a
        if x == 'r':
            self.x = coor.r
        if x == 'g':
            self.x = coor.g
        if x == 'e':
            self.x = coor.e
        if x == 'n':
            self.x = coor.n
        if x == 't':
            self.x = coor.t
        if x == 'o':
            self.x = coor.o
        if x == 's':
            self.x = coor.s
           
     
    def damePosCaballo (self):
           return self.y, self.x
        
    
    def isCorrectMove(self, yy, xx):
        """Funcion para saber si movimiento del caballo es correcto
        
        Parameters
        ----------
        
        yy: int -> Es la nueva posición del caballo en Y
        
        xx: int -> Es la nueva posición del caballo en X
        
        Return
        ------
        
        1 : correcto
        
        -1 : incorrecto
        
        """
        yy, xx = self.dameCoordenadasEnNumero(yy, xx)    
                
        #Me aseguro que las nuevas posiciones no estén fuera del tablero
        if xx > 7 or xx < 0:
            #Fuera del tablero en x
            return -1
        if yy > 7 or yy < 0:
            #Fuera del tablero en y
            return -1   
            
        if ( ( self.x + 2 ) == xx ) or ( ( self.x - 2 ) == xx ):
            #Significa que moví al caballo dos lugares a la derecha o a la izquierda
            if ( ( self.y + 1 ) == yy ) or ( ( self.y + 1 ) == yy ):
                #Significa que esta todo bien
                return 1                
                
        elif ( ( self.y + 2 ) == yy ) or ( ( self.y - 2 ) == yy ):
            #Significa que moví al caballo dos lugares Para abajo o arriba
            if ( ( self.x + 1 ) == xx ) or ( ( self.x + 1 ) == xx ):
                #Significa que esta todo bien
                return 1    
        else:
            #Esta todo mal
            return -1

class Analyzer:
    def __init__(self):
        self.SourceCode = ""
        self.caballo = caballo()
        self.geFin = 0 #Variable para saber si el printeo ya termino
        self.cCaracter = campoCaracter() 
        self.sParaMostrarEnPantallita = ""
        
        """
        Estados 
        0 = campo principal
        1 = campo de caracteres
        2 = campo de variables
        """

        self.estado = 0 #campo principal
    
    
    def setSourceCode(self, nameFile):
        """Recibe el nombre del codigo fuente
        Parameters
        
        ----------
        source:file -> el Codigo fuente
        
        """
        
        self.SourceCode = nameFile
    
    def getSourceCode(self):
        """Devuelve el nombre del archivo
        
        Parameter
        ---------

        none
        
        Returns
        -------
        
        NameFile : string
        """
        
        return self.SourceCode
        
    def AnalizadorCodigo(self):
        """Analizador del código
        Analiza el código para llevar a cabo los comandos
        
        Parameter
        ---------
        
        None
        
        Returns
        -------
        Nothing
        
        """    

        self.SourceFile = Reader.openFile(self.SourceCode)
            
        line = Reader.readLine(self.SourceFile)
        
        if(line != 'ARGENTOS\n'):
            print "\n\nMal pibe, no hiciste bien la apertura del archivo. Ponele ARGENTOS en el primer renglón"
            exit
        else:
            line = Reader.readLine(self.SourceFile)
            while(line != "ARGENTOS\n"):
                line = string.split(string.split(line, "\n")[0], " ")
                #line = string.split(string.split(Reader.readLine(self.SourceFile), "\n")[0], " ")
                
                i = 0 
                while i < len(line):
                    #Verifico si viene un comando de cambio de posición del caballo
                    if line[i] == "argento":
                        y = list(line[i+1])[0]
                        x = list(line[i+1])[1]
                                
                        #Verifico si es legal el movimiento del caballo
                        if self.caballo.isCorrectMove(y,x) == -1:
                            print "\n\nError Chabon: Moviste mal el caballo \n\n"
                            exit(-1)
                        
                        #El movimiento del caballo es ok, por lo tanto continúo
                        self.caballo.mover(y, x)    
                        
                        i = i + 2 #Aumento el índice
                        if(y == 't' and x == 'a'):
                            #Ingreso al campo de caracteres
                            self.estado = 1
                        
                    elif(line[i] == 'ge' and self.geFin == 0):
                        #Se necesita imprimir
                        line = Reader.readLine(self.SourceFile)
                        line = string.split(string.split(line, "\n")[0]," " )
                        while(line[0] != 'ge'):
                            j = 0
                            while j < len(line):
                                #Me encuentro en el campo principal   
                                if line[0] == '' and len(line) == 1:
                                    line  = Reader.readLine(self.SourceFile)
                                    line = string.split(string.split(line, "\n")[0]," " )
                                    
                                if self.estado == 0:
                                    if line[j] == "argento":
                                        y = list(line[j+1])[0]
                                        x = list(line[j+1])[1]
                                        
                                        #Verifico si es legal el movimiento del caballo
                                        if self.caballo.isCorrectMove(y,x) == -1:
                                            print "\n\nError Chabon: Moviste mal el caballo \n\n"
                                            exit(-1)
                                        
                                        #El movimiento del caballo es ok, por lo tanto continúo                                            
                                        self.caballo.mover(y, x)          

                                        j = j + 2 #Aumento el índice
                                        
                                    if(line[j] == "aaa"):
                                        y = list(line[j-1])[0]
                                        x = list(line[j-1])[1]
                                        
                                        if(y == 'T' and x == 'A'):
                                            #Ingreso al campo de caracteres
                                            self.estado = 1
                                        if(y == 'N' and x == 'A'):
                                            self.sParaMostrarEnPantallita += ' '
                                        break
                                    
                                
                                #Me encuentro en el campo de caracteres
                                elif self.estado == 1:
                                    if line[j] == "argento":
                                        y = list(line[j+1])[0]
                                        x = list(line[j+1])[1]
                                        
                                        #Verifico si es legal el movimiento del caballo
                                        if self.caballo.isCorrectMove(y,x) == -1:
                                            print "\n\nError Chabon: Moviste mal el caballo \n\n"
                                            exit(-1)
                                        
                                        #El movimiento del caballo es ok, por lo tanto continúo   
                                        self.caballo.mover(y, x)          

                                        j = j + 2 #Aumento el índice
                                        
                                    elif(line[j] == "aaa"):
                                        y = list(line[j-1])[0]
                                        x = list(line[j-1])[1]
                                        
                                        #Aquí leo en el campo de caracteres
                                        self.sParaMostrarEnPantallita += self.cCaracter.DameCaracter(y,x, self.caballo)
                                        j += 1
                                        
                                    elif(line[j] == "oo"):
                                        self.estado = 0                                         
                                        break
                                    
                                    elif (line[j] != "argento" and line[j] != "aaa"  and line[j] != "oo"):
                                        j += 1
                                    
                            line  = Reader.readLine(self.SourceFile)
                            line = string.split(string.split(line, "\n")[0]," " )
                            
                            #Para dar por finalizado el printeo                            
                            if (line[0] == 'ge'):
                                print self.sParaMostrarEnPantallita
                                self.sParaMostrarEnPantallita = ""
                                self.geFin = 1;
                    i += 1
                 
                line = Reader.readLine(self.SourceFile)          
                                
                                        
                                        