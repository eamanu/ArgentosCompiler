# -*- coding: utf-8 -*-
"""@package Reader
Módulo que lee el código fuente

@author Arias Emmanuel
@date 24/10/2016

"""

SourceCodeArgento = "" #Archivo del código fuente


def readLine(File):
    """Lee una linea del archivo
    
    Parameter
    ---------
    File:file
    
    Return
    ------
    
    Line:string -> Linea del código fuente
    
    """
    
    return File.readline()
    
def closeFile(File):
    """Cierra el archivo
    
    Parameter
    ---------
    File: file -> archivo de código fuente
    
    Return
    ------
    Nothing
    
    """
    File.close()

def openFile(nameFile):
    """Abre el archivo
    
    Parameter
    ---------
    nameFile: Nombre del archivo
    
    Return
    ------
    fo: Archivo
    
    """
    
    SourceCodeArgento = open(nameFile, "r")
    return SourceCodeArgento
