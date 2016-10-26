# -*- coding: utf-8 -*-
"""@package Reader
Módulo que analiza el código fuente

@author Arias Emmanuel
@date 24/10/2016

"""

from Reader import Reader

class Analyzer:
    
    SourceCode=""
    SourceFile=""
    
    def __init__(self):
        self.SourceCode = ""
    
    def setSourceCode(self, nameFile):
        """Recibe el nombre del codigo fuente
        Parameters
        
        ----------
        source:file -> el Codigo fuente
        
        """
        
        self.SourceCode = nameFile
    
    def getSourceCode(self):
        """Devuelve el nombre del archivo
        Parameters
        ----------
        none
        
        Returns
        -------
        
        NameFile:string
        """
        
        return self.SourceCode
        
    def AnalizadorCodigo(self):
        """Analizador del código
        Analiza el código para llevar a cabo los comandos
        
        Parameters
        ----------
        
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
                print line
                line = Reader.readLine(self.SourceFile)
                
                