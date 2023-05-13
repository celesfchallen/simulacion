## Simulación 1

### Descripción
``Ejercicio 2 de la guía``

Los clientes llegan al sistema con una frecuencia que responde a una función
de densidad de probabilidad (f.d.p.) equiprobable entre 0 y 30 minutos y se
ubican en la cola con menor cantidad de personas, en caso de igualdad se
distribuyen aleatoriamente el 60% a la cola 1 y el 40% a la cola 2.

El tiempo de atención se conoce recién cuando el cliente comienza a ser
atendido. Según el trámite varía entre 15 y 35 minutos, y responde a una
f.d.p. lineal donde f(35)=3*f(15) (igual para ambos puestos).

Aquellos clientes que al llegar encuentran hasta 2 personas en la cola se
quedan, si encuentran 3 personas se queda el 60% y más de 3 el 20%.

El sistema es **con vaciamiento y arrepentimiento**.

### Parámetros



### Análisis
###### Metodología
Evento a evento.
Datos encadenadores de eventos: IA y TA.

###### Variables Exógenas
Datos
- **Intervalo entre llegadas** `IA`

  fdp equiprobable (0, 30)


- **Tiempo de atención** `TA` 

  fdp lineal f(35)=3*f(15)

Variable de Control

- En esta simulación no hay variables de control. 
 
###### Variables Endógenas
Estado
- **Cantidad de personas en la cola 1** `NS1`
- **Cantidad de personas en la cola 2** `NS2`


Resultado
- **Promedio de permanencia en la cola 1** `PPS1`
  
    Se calcula como (STS1 - STLL1) / CLL1

- **Promedio de permanencia en la cola 2** `PPS2`
  
    Se calcula como (STS2 - STLL2) / CLL2


- **Porcentaje de tiempo ocioso cola 1** `PTO1`

    Se calcula como STO1 * 100 / T

- **Porcentaje de tiempo ocioso cola 2** `PTO2`

    Se calcula como STO2 * 100 / T


- **Promedio de espera cola 1** `PE1`

    Se calcula como (STS1 - STLL1 - STA1) / CLL1

- **Promedio de espera cola 2** `PE2`

    Se calcula como (STS2 - STLL2 - STA2) / CLL2


- **Porcentaje de no arrepentidos con NS1 < 2 respecto del total atendidas** `PQ21`

    Se calcula como CQ21 * 100 / CLL1

- **Porcentaje de no arrepentidos con NS2 > 2 respecto del total atendidas** `PQ22`

    Se calcula como CQ22 * 100 / CLL2
