# ArgentosCompiler
Compilador para el lenguaje ARGENTOS

Argentos nació como producto del concurso CALESYTA 2016 (Concurso Argentino de Lenguajes Esotéricos y Tarpits). En un principio iba a ser un lenguaje más “clásico”, pero me aburrí de lo mismo.

Así fue que en una tarde, mientras desarrollaba unas de mis partidas de ajedrez más importante… bueno no, iba en el bondi, y en una de esas epifanías que tienen los que hacen programación, me surgió la idea de hacer una tablero de ajedrez, y tratar de programar con el movimiento de una de las piezas. Me pareció interesante hacerlo con el caballo… hacer… el lenguaje.

Para mayor información del lenguaje visitar: http://freektc.blogspot.com.ar/2016/10/argentos-nuevo-lenguaje-esoterico-bien.html

# Características principales

    El control de todo el programa se realiza moviendo una pieza del ajedrez: el caballo.
    Existen tres campos de movimiento, basados en el tablero de ajedrez: el principal, el de variables y el de caracteres.
    Las coordenadas de los campos (8x8) son 'A’, ‘R’, ‘G’, ‘E’, ‘N’, ‘T’, ‘O’, ‘S’.
    Las variables se almacenan en el campo de variables (matriz 8x8), solo se pueden almacenar 64 variables.
    Las variables son de 1 Bytes.
    Para asignar valores a las variables, se debe utilizar el campo de caracteres. 
    Los únicos flujos de control son: condicional y repetitivo.

# Fundamentos

Para lograr cumplir con lo esperado de un lenguaje, como control de flujo, almacenar variables, realizar operaciones; fue necesario crear varios campos o tableros de ajedrez.

Para ello  ARGENTOS proporciona un campo de movimiento, que llevaría el flujo principal del programa, y donde se encuentran los códigos principales de control (salto de linear, retorno de carro, espacio, +, -, <, >, =, etc).

Para hacerlo más interesante, la libertard del programador tendría ciertas limitaciones, lo que representa un divertido desafío.

En primer lugar todos los datos que se ingresan en un programa (caracteres, numeros) ya son previstos por ARGENTOS. Para almacenar datos en memoria, también tiene sus limitaciones. Los datos se almacenan en un tablero 8x8 y es necesario recordar la posición en la que esa variable fue almacenada.

El campo donde se encuentran los caracteres se llama campo de caracteres y el campo donde se almacenan las variables se llama campo de variables. 
