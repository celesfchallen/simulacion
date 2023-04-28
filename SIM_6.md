## Simulación 6

### Descripción
``Ejercicio 6 de la guía``

**Sistema con un puesto de atención, con su correspondiente cola.**

Los clientes llegan al sistema con una frecuencia que responde a una función
de densidad de probabilidad (f.d.p.) equiprobable entre 5 y 20 minutos.

El tiempo de atención **se conoce desde la llegada del cliente al sistema** y
responde a una función normal de Gauss, entre 10 y 20 minutos.

Todos los clientes están dispuestos a esperar hasta 10 minutos, solo el 60%
espera entre 10 y 20 minutos y el 10% espera más de 20 minutos.

### Parámetros

--

### Análisis
###### Metodología
Evento a evento.
Datos encadenadores de eventos: IA.

###### Variables Exógenas
Datos
- **Intervalo entre llegadas** `IA`

  fdp equiprobable (5, 20)


- **Tiempo de atención** `TA` 

  función normal de Gauss entre 10 y 20

Variable de Control

- En esta simulación no hay variables de control. (_implícita_)
 
###### Variables Endógenas
Estado
- **Tiempo comprometido** `TC`


Resultado
- **Promedio de permanencia en el sistema** `PPS`
  
    Se calcula como (STA + STE) / CLL


- **Porcentaje de tiempo ocioso** `PTO`

    Se calcula como STO * 100 / T


- **Promedio de espera** `PE`

    Se calcula como STE / CLL


- **Promedio de tiempo de atención** `PTA`

    Se calcula como STA / CLL


- **Porcentaje que esperaron más de 15' respecto del total atendidas** `PE15`

    Se calcula como CE15 * 100 / CLL


- **Porcentaje de arrepentidos que tenían que esperar más de 20' respecto al total de arrepentidos** `PARR20`

    Se calcula como CARR20 * 100 / CARR

###### Tabla de eventos independientes
![Tabla de eventos independientes](https://github.com/celesfchallen/simulacion/images/tei6.jpeg "Tabla de eventos independientes ej. 6")

###### Tabla de eventos futuros
TPLL

###### Diagrama de flujo
![Diagrama de flujo](https://github.com/celesfchallen/simulacion/images/icon48.png "Diagrama de flujo ej. 6")