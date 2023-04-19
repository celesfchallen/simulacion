# Simulación

Simulación - UTN FRBA 2023

## Cómo correr las simulaciones

En la clase main.py importas el método run_simulation_x de la simulación que quieras correr. 
Tener en cuenta que solo se puede correr **una simulación a la vez**.

``
from simulations.sim_1 import run_simulation_1
``

Dentro del método main se hace el llamado con los parámetros correspondientes a cada una.

A continuación están los enlaces para ver el detallada cada simulación y qué parámetros necesita.

Al final del archivo se detalla que representan los nombres de cada variable en la sección: [Definición de variables].



## Simulaciones

- [Simulación 1]


## Definición de Variables

- TA = Tiempo de atención
- IA = Intervalo entre arribos
- NS = Cantidad de personas en la cola
- CLL = Cantidad de llegadas
- TPLL = Tiempo de próxima llegada
- TPS = Tiempo de próxima salida
- STS = Sumatoria de tiempos de salida
- STLL = Sumatoria de tiempos de llegada
- ITO = Intervalo de tiempo oscioso
- STO = Sumatoria de tiempo oscioso
- T = Tiempo
- PTO = Porcentaje de tiempo oscioso
- PPS = Promedio de permanencia en el sistema
- PARR = Porcentaje de arrepentimiento

[Definición de variables]: https://github.com/celesfchallen/simulacion#definici%C3%B3n-de-variables
[Simulación 1]: https://github.com/celesfchallen/simulacion/blob/main/SIM_1.md