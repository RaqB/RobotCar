# RobotCar!
Se le presenta un escenario en donde usted tendrá que programar un carro seguidor de líneas; el cual será capaz de trasladarse desde un punto hacia otro, dentro del laberinto que se muestra a continuación:

<p align="center">
  <img src="https://github.com/SantiagoONE/Needs/blob/master/RobotCar/images/redmaze.gif?raw=true"/>
</p>

El robot solo puede moverse por las lineas rojas. Aqui esta la leyenda del laberinto:

* Los pequeños circulos negros representan las intersecciones, donde el carro se detiene para decidir su siguiente movimiento.
* El punto morado siempre será la posición inicial del robot.
* Los circulos verdes son posibles puntos de visita.

En cada punto el robot tiene que decidir una de tres opciones:

* `" F "`: avanzar.
* `" R "`: moverse hacia la derecha.
* `" L "`: moverse hacia la izquierda.

Usted puede asumir que el robot siempre realiza un giro de 180° cada vez que llega a un punto de visita, listo para salir en busca de otro.

> Basado en el examen final del curso ARQCO, Por el Ing. Bady Cruz Diaz.

**Entrada:**

> Una lista **L** con puntos de visita del laberinto, a los que el carro deberá trasladarse en orden. `1 <= | L | <= 7` 

**Salida:**

> Un string con las deciciones que el robot debe realizar para visitar todos los punto en **L**, separada por simbolos `'-'`.

**Ejemplos:**

* `RobotCar([[4, 2], [5, 5]]) = "F-R-F-R-R-R-R-F-L-L-F-L-R-R"`
* `RobotCar([[0, 0]])         = "F-R-L-F-L-L-R-R"`
* `RobotCar([[2, 3], [0, 5]]) = "F-R-L-F-R-R-R-F-F-L"`
