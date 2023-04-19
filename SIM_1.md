## Simulación 1

### Descripción
``Ejercicio 1 de la guía``

Sistema con un puesto de atención, con su correspondiente cola.
Los clientes llegan al sistema con una frecuencia que responde a una función
de densidad de probabilidad uniforme entre 0 y 10 minutos.

El tiempo de atención que varía entre 10 y 20 minutos, se conoce recién cuando el cliente
comienza a ser atendido y responde a una fdp lineal donde f(20)=2*f(10).

Aquellos clientes que al llegar encuentran hasta 4 personas en la cola se
quedan, si encuentran hasta 8 se queda sólo el 40% y si encuentran más de 8
se retiran todos.

El sistema es **con vaciamiento y arrepentimiento**.

### Parámetros
``
run_simulation_1(simulation_duration)
``

- **simulation_duration**: Tiempo que dura la simulación, es del tipo **Time**, ej: Time(8, 30) representa 8hs 30min

### Análisis
###### Metodología
Evento a evento.
Datos encadenadores de eventos: IA y TA.

###### Variables Exógenas
Datos
- **Intervalo entre llegadas** `IA`

  Equiprobables en un rango dado en minutos. ej:(10, 30)


- **Tiempo de atención** `TA` 

  Equiprobables en un rango dado en minutos.

Variable de Control

- En esta simulación no hay variables de control. 
 
###### Variables Endógenas
Estado
- **Cantidad de personas en la fila** `NS`


Resultado
- **Promedio de permanencia en el sistema** `PPS`
  
    Se calcula como (STS - STLL) / CLL


- **Porcentaje de tiempo ocioso** `PTO`

    Se calcula como STO * 100 / T