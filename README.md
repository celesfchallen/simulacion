# Simulación

Simulación - UTN FRBA 2023

## Cómo correr las simulaciones

En la clase main.py importas el método run_simulation_x de la simulación que quieras correr. 
Tener en cuenta que solo se puede correr **una simulación a la vez**.

``
from simulations.sim_1 import run_simulation_1
``

Dentro del método main la llamas con los parámetros correspondientes a cada una.

A continuación está detallada cada simulación y qué parámetros necesita.
Al final del archivo se detalla que representan los [nombres de cada variable]

## Simulación 1
### Parámetros
``
run_simulation_1(first_input, end_simulation_time)
``

- **first_input**: Horario en el que fue el primer input en el sistema, es del tipo **Time**, ej: Time(8, 30) representa 8hs 30min
- **end_simulation_time**: Horario en el que termina la simulación, también del tipo **Time**.

### Descripción
Simulamos un sistema en el que ingresan y egresan usuarios.
Nuestro dato encadenador de eventos es la llegada de usuarios en un rango de tiempo

La idea de esta simulación es estimar los valores de promedio de permanencia en el sistema ``average_stay`` y el porcentaje de tiempo ocioso ``idle_time_percentage``

#### Metodología
**Evento a evento.**
Datos encadenadores de eventos: IA y TA.

#### Variables Exógenas
###### Datos
- **Intervalo entre llegadas**: Equiprobables en un rango dado en minutos. ej:(10, 30)
- **Tiempo de atención**: Equiprobables en un rango dado en minutos.

###### Variable de Control
En esta simulación no hay variables de control 
 
#### Variables Endógenas
###### Estado
- **Cantidad de personas en la fila** ``current_users``  


###### Resultado
- **Promedio de permanencia en el sistema** ``average_stay`` 

    Se calcula como (STS - STLL) / CLL


- **Porcentaje de tiempo ocioso** ``idle_time_percentage``

    Se calcula como STO * 100 / T 


## Definición de Variables

- TA = Tiempo de atención
- IA = Intervalo entre arribos
- NS = Cantidad de personas en la cola
- CLL = Cantidad de llegadas
- STS = Sumatoria de tiempos de salida
- STLL = Sumatoria de tiempos de llegada
- ITO = Intervalo de tiempo oscioso
- STO = Sumatoria de tiempo oscioso
- T = Tiempo
- PTO = Porcentaje de tiempo oscioso
- PPS = Promedio de permanencia en el sistema

[nombres de cada variable]: https://github.com/celesfchallen/simulacion#definici%C3%B3n-de-variables