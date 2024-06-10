# Dimensionamiento de Bomba de Desagote
En el presente informe se llevara a cabo una serie de resoluciones de ecuaciones direfenciales ordinarias con el objetivo de simular una inundación provocada por una lluvia intensa, analizar las consecuencias en un edificio residencial con cocheras subterráneas y evaluar las
alternativas para mitigar los efectos de un evento climático. 

Para ello se modelará numéricamente el fenómeno físico analizado,
dimensionando la bomba para mitigar el efecto de inundaciones producidas por lluvias y experimentar con la resolución numérica del sistema.

Para llevar a cabo todo este ánalisis, se nos fueron brindadas las siguientes ecuaciones:


<u>Ecuación 1</u>: La conservación de masa tomando al sótano como volumen de control <br>

<div style="text-align: center">

$\frac{\mathrm{d} V}{\mathrm{d} t} = Q_{ent} - Q_{sal}$
</div>

<u>Ecuación 2</u>: El caudal de entrada <br>

<div style="text-align: center">

$Q_{ent} = C  I  A_{terr}$
</div>


<u>Ecuación 3</u>: El caudal de salida <br>

<div style="text-align: center">

$Q_{sal} = Q_{max}\sqrt{\frac{\Delta H_{max} - \Delta H}{\Delta H_{max} - \Delta H_{min}}}$
</div>


<u>Ecuación 4</u>: El desnivel entre la superficie del agua y el desagote <br>

<div style="text-align: center">

$\Delta H = H_{s} - H$
</div>


<u>Ecuación 5</u>: La altura de agua por encima del fondo del pozo<br>

<div style="text-align: center">

$H = \frac{V}{A_{sot}}$
</div>


<u>Ecuación 6</u>: El coeficiente de infiltración <br>

<div style="text-align: center">

$\frac{\mathrm{d} C}{\mathrm{d} t} = \frac{V}{V_{sot}t_{k}}(C_{sat} - C)$
</div>


Y también se nos brinda el siguiente cuadro:

![Gráfico A1](./assets/intensidades.jpg)

#### Aclaraciones pertinentes:
- El padrón utilizado para llevar a cabo todas las cuentas a lo largo de todo este informe es $109566$.
- El valor de $h$ (el intervalo de tiempo) está siempre calculado en horas.
- Las mediciones físicas siempre se encuentran en $m$ (metros) y se realizarán las cuentas necesarias para realizar el pasaje de unidades de los datos brindados en otras unidades (como la $I$ en $mm/h$ o la $A_{terr}$ en $ha$)


### Punto A1
En una primera instancia, nuestro objetivo es correr el modelo para la precipitación de 60 min y verificar que el volumen de agua almacenado en el sótano coincida con el volumen de lluvia. Esto, suponiendo $C$ = 1 y $Q_{sal}$ = 0. Eso nos termina dejando: 

$\frac{\mathrm{d} V}{\mathrm{d} t} = Q_{ent} = I  A_{terr}$

Teniendo como dato $A_{terr} = 17.32m ∗ \frac{109566}{3000}m = 632,56104m^2$ y $V_{(t=0)} = 0$, aplicamos el método de Euler explícito utilizando un intervalo de tiempo $h = 0,1$. 

$V_{n+1} = V_{n} + h * (\frac{85 * 632,56104}{1000})$

(Dividimos por $1000$ para que la intensidad de lluvia, que se nos da en $mm/h$, nos quede en $m/h$)

Iterando hasta el minuto 60, es decir $h = 1$, obtenemos que el volumen de agua en el sótano es igual a $53,7676884m^2$ al alcanzar la hora.

Al tener un $Q_{ent}$ con valores constantes, el crecimiento del volumen de agua en el sótano en función del tiempo nos termina quedando lineal.

![Gráfico A1](./assets/A1.png)

Entonces, se puede llegar a la conclusión de que nuestro $Q_{ent}$ puede calcularse simplemente multiplicando nuestra intensidad de lluvia ($I$) por el $A_{terr}$, es decir:

$\frac{85 * 632,56104}{1000}m^2 = 53,7676884m^2$

que como podemos observar nos devuelve el mismo valor obtenido anteriormente a través del método de Euler.

### Punto A2
En esta segunda instancia vamos a considerar $C$ y $Q_{sal}$ variables. Para ello utilizaremos todas las ecuaciones brindadas.

Correremos el modelo para todas las duraciones/intensidades de precipitación, en un lapso de tiempo suficiente como para que el sótano se vacíe. 

Ahora, tenemos dos ecuaciones para discretizar:

<div style="text-align: center">

$\frac{\mathrm{d} V}{\mathrm{d} t} = Q_{ent} - Q_{sal}$
</div>

<div style="text-align: center">

$\frac{\mathrm{d} C}{\mathrm{d} t} = \frac{V}{V_{sot}t_{k}}(C_{sat} - C)$
</div>

Como sabemos que $V_{(t=0)} = 0$ y $C_{(t=0)} = 0,6$ ambos son problemas de valores iniciales que pueden resolverse por Euler.

Desarrollando con los siguientes datos:

$A_{terr} = 17.32m ∗ \frac{109566}{3000}m = 632,56104m^2$ <br>
$Q_{max} = 8 m^3/h$ <br>
$\Delta H_{max} = 4m$ <br>
$\Delta H_{min} = 1m$ <br>
$H_{s} = 3,5m$ <br>
$C_{sat} = 0,90$ <br>
$t_{k} = (1 - \frac{109566}{140000})h = 0,2173857143h$ <br>
$A_{sot} = 8,66m * 8,66m = 74,9956m^2$ <br>
$V_{sot} = H_{s} * A_{sot} = 3,5m * 74,9956m^2 = 262,4846m^3$ <br>
$\Delta H = H_{s} - H$ <br>
$H = \frac{V}{A_{sot}} = \frac{V}{74,9956m^2} $ <br>

Planteamos:

$V_{n+1} = V_{n} + h * ((C*I*A_{terr}) - (Q_{max}\sqrt{\frac{\Delta H_{max} - \Delta H}{\Delta H_{max} - \Delta H_{min}}}) )$

$C_{n+1} = C_{n} + h * (\frac{V}{V_{sot}t_{k}}(C_{sat} - C_{n}))$

Quedando:

$V_{n+1} = V_{n} + h * ((C*I*632,56104m^2) - (8 m^3/h\sqrt{\frac{4m - (3,5m - (\frac{V_{n}}{74,9956m^2}))}{4m - 1m}}) )$


$C_{n+1} = C_{n} + h * (\frac{V}{262,4846m^3 * 0,2173857143h}(0,90 - C_{n}))$

Como ambas ecuaciones dependen de la otra, no puede calcularse la siguiente iteración de una sin antes calcular la otra. Por esa razón, comenzamos calculando $C_{1}$ usando los valores de $C_{0}$ Y $V_{0}$, reemplazando a su vez con el $I$ correspondiente en cada entrada de la tabla. Una vez calculado, podemos calcular el $V_{1}$ y así continuamente.

Este planteo nos arrojó los siguientes resultados:


#### <u>Lluvia de 5 minutos</u>
Intensidad = $2414$ $m/h$ <br>
Duración = $5/60$ $h$ <br>

Resultado: tarda $2,25$ $h$ en vaciarse.


![Modelo 5 min](./assets/Modelo%205%20minutos.png)



#### <u>Lluvia de 10 minutos</u>
Intensidad = $1907$ $m/h$ <br>
Duración = $1/6$ $h$ <br>

Resultado: tarda $3,4667$ $h$ en vaciarse.


![Modelo 10 min](./assets/Modelo%2010%20minutos.png)

#### <u>Lluvia de 15 minutos</u>
Intensidad = $162,6$ $m/h$ <br>
Duración = $1/4$ $h$ <br>

Resultado: tarda $4,3667$ $h$ en vaciarse.


![Modelo 15 min](./assets/Modelo%2015%20minutos.png)

#### <u>Lluvia de 30 minutos</u>
Intensidad = $119,6$ $m/h$ <br>
Duración = $1/2$ $h$ <br>

Resultado: tarda $6,2667$ $h$ en vaciarse.


![Modelo 30 min](./assets/Modelo%2030%20minutos.png)

#### <u>Lluvia de 60 minutos</u>
Intensidad = $85$ $m/h$ <br>
Duración = $1$ $h$ <br>

Resultado: tarda $8,8$ $h$ en vaciarse.


![Modelo 60 min](./assets/Modelo%2060%20minutos.png)

#### <u>Lluvia de 3 horas</u>
Intensidad = $41,7$ $m/h$ <br>
Duración = $3$ $h$ <br>

Resultado: tarda $13,4$ $h$ en vaciarse.


![Modelo 3 horas](./assets/Modelo%203%20horas.png)

#### <u>Lluvia de 6 horas</u>
Intensidad = $26,4$ $m/h$ <br>
Duración = $6$ $h$ <br>

Resultado: tarda $17,8$ $h$ en vaciarse.


![Modelo 6 horas](./assets/Modelo%206%20horas.png)

#### <u>Lluvia de 12 horas</u>
Intensidad = $16,7$ $m/h$ <br>
Duración = $12$ $h$ <br>

Resultado: tarda $23,9$ $h$ en vaciarse.


![Modelo 12 horas](./assets/Modelo%2012%20horas.png)

#### <u>Lluvia de 24 horas</u>
Intensidad = $10,9$ $m/h$ <br>
Duración = $24$ $h$ <br>

Resultado: tarda $33,3$ $h$ en vaciarse.


![Modelo 24 horas](./assets/Modelo%2024%20horas.png)

#### <u>Lluvia de 72 horas</u>
Intensidad = $5,2$ $m/h$ <br>
Duración = $72$ $h$ <br>

Resultado: tarda $0$ $h$ en vaciarse, nunca se llena.


![Modelo 72 horas](./assets/Modelo%2072%20horas.png)

Conclusiones
En conclusion, encontramos que el tiempo que tarda en vaciarse el sotano varia considerablemente segun la duracion e intensidad de la lluvia. Cuando la lluvia es corta pero intensa, el sotano se llena rapidamente pero tambien se vacia rapido cuando para la lluvia. Por otro lado, si la lluvia es prolongada pero suave, el sotano no llega a llenarse por completo, pero toma mucho mas tiempo para vaciarse. 

### Punto B
Ahora, nos encontramos ante el desafío de redimensionar la bomba adoptando un nuevo valor para la variable $Q_{max}$ para que la altura del agua sobre el piso del sótano jamás exceda los $0,25m$ para ninguna de las precipitaciones presentes en la tabla brindada. 


Sabiendo que:

<div style="text-align: center">

$H = \frac{V}{A_{sot}}$
</div>

y teniendo el valor $A_{sot} = 74,9956$, se debe cumplir que $H < 0,25$, podemos despejar y nos queda que:

$\frac{V}{74,9956} < 0,25$ <br>
$V < 0,25 * 74,9956$ <br>
$V < 18,7489$ <br>

Si buscamos aproximar a $V$ asumiendo a $Q_{ent}$ y $Q_{sal}$ como constantes, podemos plantear que:

<div style="text-align: center">

$V = h*(Q_{ent} - Q_{sal})$
</div>

Nos termina quedando que: 

<div style="text-align: center">

$h*(Q_{ent} - Q_{sal}) < 18,7489$
</div>

Lo cual es igual a:

<div style="text-align: center">

$h*((\frac{C*I*A}{1000}) - (Q_{max}\sqrt{\frac{\Delta H_{max} - \Delta H}{\Delta H_{max} - \Delta H_{min}}})) < 18,7489$
</div>

Como lo que queremos es maximizar es el $Q_{sal}$ buscamos que  $\sqrt{\frac{\Delta H_{max} - \Delta H}{\Delta H_{max} - \Delta H_{min}}} = 1$ así obtenemos el $Q_{max}$, por lo tanto nos queda:

<div style="text-align: center">

$h*(\frac{C*I*A}{1000} - Q_{max}) < 18,7489$
</div>

El mayor valor posible para nuestro $Q_{ent}$ se da cuando nuestra $C$ es igual $0,9$. En nuestro caso, el valor de $A_{terr}$ es de $632,56104m^2$. 

Esto nos dejaría que nuestro $Q_{ent}$ máximo es:

<div style="text-align: center">

$Q_{ent} = \frac{0,9 * I * 632,56104}{1000}$
</div>

Lo que nos deja:

<div style="text-align: center">

$(\frac{0,9 * I * 632,56104}{1000} - \frac{18,7489}{h}) < Q_{max}$
</div>

Al probar esto con cada una de las intensidades a través de esta función:

![Código Q max](./assets/funcionQmax.jpg)


Se llega a la que conclusión de que para lograr que la altura de agua sobre el piso del sótano no exceda los $0,25m$ para ninguna de las precipitaciones de la tabla se necesita un $Q_{max} >= 32$.


### Punto C

Se nos pide ahora discretizar las ecuaciones 1 y 6 con el método de Runge-Kutta de orden 2, considerando esta solución como “exacta”. Luego, debemos correr este modelo para la precipitación de 60 min con el método de Runge-Kutta de orden 2, y luego con Euler con dos pasos de tiempo distintos. Además, debemos verificar que Euler es de orden 1 analizando la diferencia con la solución “exacta”, utilizando siempre el $Q_{max}$ obtenido anteriormente en el punto B. 

Decidimos correr el modelo primero con un $h = 1 min$ y notamos que los valores de Runge-Kutta y Euler eran bastantes similares, con diferencias bastante pequeñas:

![Punto C h=1min](./assets/Modelo%2060%20minutos%20con%20h%20=%201%20min%20Punto%20C.png)

Para poder ver errores más grandes corrimos nuevamente el modelo pero ahora utilizando $h = 10 min$:

![Punto C h=10min](./assets/Modelo%2060%20minutos%20con%20h%20=%2010%20min%20Punto%20C.png)

y $h = 30 min$

![Punto C h=30min](./assets/Modelo%2060%20min,%20con%20h%20=%2030%20min%20Punto%20C.png)

Corroboramos que Euler es de orden 1...

Comparamos los resultados obtenidos usando diferentes tamanos de paso h y analizamos el error en relacion con la solucion obtenida con el metodo de runge-kutta de orden 2, considerado como la solucion "exacta". Los resultados mostraron que el error global disminuye en proporcion al tamano del paso, confirmando que el metodo de Euler es efectivamente de primer orden.
Ademas, se puede observar que las diferencias entre las soluciones de Euler y RK2 son pequenas para pasos de tiempo pequenos, y aumentan significativamente al incrementar el tamano del paso, lo cual es consistente con el comportamiento esperado de un primer orden.