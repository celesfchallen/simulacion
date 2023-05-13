# Simulación

Simulación - UTN FRBA 2023

## Cómo correr las simulaciones

En la clase main.py importas el método run_simulation_x de la simulación que quieras correr. 
Tener en cuenta que solo se puede correr **una simulación a la vez**.

```python
from simulations.sim_1 import run_simulation_1
```

Dentro del método main se hace el llamado con los parámetros correspondientes a cada una.

A continuación están los enlaces para ver detallada cada simulación con su análisis previo, tablas y diagramas de flujo, y qué parámetros necesita para correrla.

Al final del archivo se detalla que representan los nombres de cada variable en la sección: [Definición de variables]

## Simulaciones

- [Simulación 1] NS - 1 puesto de atención, 1 cola
- [Simulación 2] NS - 2 puestos de atención, 2 colas
- [Simulación 3] NS - n puestos de atención, n colas
- [Simulación 4] NS - n puestos de atención, 1 cola
- [Simulación 5] NS - 2 puestos de atención, 2 colas con prioridades
- [Simulación 6] TC - 1 puesto de atención, 1 cola
- [Simulación 7] TC - 2 puestos de atención, 2 colas
- [Simulación 8] TC - n puestos de atención, n colas

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
- PE = Promedio de espera
- CQ = Cantidad de personas que no se arrepintieron
- CARR = Cantidad de personas que se arrepintieron
- STA = Sumatoria de tiempo de atención
- TC = Tiempo comprometido

[Definición de variables]: https://github.com/celesfchallen/simulacion#definici%C3%B3n-de-variables
[Simulación 1]: https://github.com/celesfchallen/simulacion/blob/main/simulations_readme/SIM_1.md
[Simulación 1]: https://github.com/celesfchallen/simulacion/blob/main/simulations_readme/SIM_2.md
[Simulación 6]: https://github.com/celesfchallen/simulacion/blob/main/simulations_readme/SIM_6.md