# -*- coding: utf-8 -*-
"""@package Reader
Módulo que analiza el código fuente

@author Arias Emmanuel
@date 24/10/2016

"""

from Reader import Reader
from enum import Enum
import string

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
    
    def mover (self, y, x):
        
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
    
        
    
    def isCorrectMove(self, y, x):
        return 1

class Analyzer:
    def __init__(self):
        self.SourceCode = ""
        self.caballo = caballo()
        
        
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
            print "Error en la apertura del archivo"
            exit
        else:
            line = Reader.readLine(self.SourceFile)
            while(line != "ARGENTOS\n"):
                line = string.split(Reader.readLine(self.SourceFile), " ")
    
                for i in range(len(line)):
                    #Verifico si viene un comando de cambio de posición del caballo
                    if line[i] == "argento":
                        y = list(line[i+1])[0]
                        x = list(line[i+1])[1]
                        self.caballo.mover(y, x)          
                        #TODO: Verificar si es posible moverlo según regla de ajedrez
                        i = i + 2 #Aumento el índice
                        if(y == 't' and x == 'a'):
                            #Ingreso al campo de caracteres
                            self.estado = 1
                        
                    elif(line[i] == 'ge'):
                        line = Reader.readLine(self.SourceFile)
                        while(line != 'ge'):
                            line = string.split(line, " ")
#FIXME: aquí hay que poner un for comun porque si no continua con el range                            
                            for j in range(len(line)):
                                if line[j] == "argento":
                                    y = list(line[j+1])[0]
                                    x = list(line[j+1])[1]
                                    self.caballo.mover(y, x)          
                                    #TODO: Verificar si es posible moverlo según regla de ajedrez
                                    j = j + 2 #Aumento el índice
                                    
                                if(line[j] == "aaa"):
                                    y = list(line[j-1])[0]
                                    x = list(line[j-1])[1]
                                    
                                    print y,x
                                    if(y == 't' and x == 'a'):
                                        #Ingreso al campo de caracteres
                                        self.estado = 1
                                        
                                        