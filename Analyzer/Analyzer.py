# -*- coding: utf-8 -*-
"""@package Reader
Módulo que analiza el código fuente

@author Arias Emmanuel
@date 24/10/2016

"""

from Reader import Reader
from logilab.common.debugger import readline

SourceCode = ""

def setSourceCode(source):
    """Recibe el codigo fuente
    
    Parameters
    ----------
    source:file -> el Codigo fuente
    
    """
    
    
    

def AnalizadorCodigo():
    """Analizador del código
    Analiza el código para llevar a cabo los comandos
    
    Parameters
    ----------
    None
    
    Returns
    -------
    Nothing
    
    """    
    SourceCode = Reader.openFile(helloword.argentos)
        
    line = Reader.readLine(SourceCode)
    
    if(line != 'ARGENTOS'):
        print "Error en la apertura del archivo"
    else:
        line = Reader.readLine(SourceCode)
        while(line != "ARGENTOS"):
            print line
            line = readline(SourceCode)
            
            