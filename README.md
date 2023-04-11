# Simulación

Simulación - UTN FRBA 2023

## Cómo correr las simulaciones

En la clase main.py importas el método run_simulation_x de la simulación que quieras correr. 

``
from sim_1 import run_simulation_1
``

Dentro del método main la llamas con los parámetros correspondientes a cada una.

A continuación está detallada cada simulación y qué parámetros necesita.

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

La llegada de usuarios al sistema y el tiempo que se tarda en despachar a un usuario son equiprobables dentro de un rango dado