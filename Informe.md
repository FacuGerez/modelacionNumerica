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
- El valor de $h$ (el intervalo de tiempo) también es llamado $\Delta t$.
- Las mediciones físicas siempre se encuentran en $m$ (metros) y se realizarán las cuentas necesarias para realizar el pasaje de unidades de los datos brindados en otras unidades (como la $I$ en $mm/h$ o la $A_{terr}$ en $ha$)
-Los datos llevados acabo estan en los presentes $Excels$ puestos con sus respectivos links en el archivo $README.md$
-Ademas presentamos una version del trabajo en python en un archivo llamado $tp.py$ el cual presenta todos los puntos hechos y pasandole el padron deseado al correr dicho archivo, transcribe en el archivo adjunto llamado $tablas.txt$ todas las tablas de todos los puntos presentados


### Punto A1
En una primera instancia, nuestro objetivo es correr el modelo para la precipitación de 60 min y verificar que el volumen de agua almacenado en el sótano coincida con el volumen de lluvia. Esto, suponiendo $C$ = 1 y $Q_{sal}$ = 0. Eso nos termina dejando:

$\frac{\mathrm{d} V}{\mathrm{d} t} = Q_{ent} = I  A_{terr}$

Teniendo como dato $A_{terr} = 17.32m ∗ \frac{109566}{3000}m = 632,56104m^2$ y $V_{(t=0)} = 0$, aplicamos el método de Euler explícito utilizando un intervalo de tiempo $\Delta t = 0,1$.

$V_{n+1} = V_{n} + h * (\frac{85 \frac{m}{h} * 632,56104m^2}{1000})$

(Dividimos por $1000$ para que la intensidad de lluvia, que se nos da en $mm/h$, nos quede en $m/h$)

Iterando hasta el minuto 60, obtenemos que el volumen de agua en el sótano es igual a $53,7676884m^3$ al alcanzar la hora.

Al tener un $Q_{ent}$ con valores constantes, el crecimiento del volumen de agua en el sótano en función del tiempo nos termina quedando lineal.

![Gráfico A1](./assets/A1.png)

Entonces, se puede llegar a la conclusión de que nuestro $Q_{ent}$ puede calcularse simplemente multiplicando nuestra intensidad de lluvia ($I$) por el $A_{terr}$, es decir:

$\frac{I_{60min} * A_{terr}}{1000} * \Delta t = 53,7676884m^3$

$\frac{85 \frac{m}{h} * 632,56104m^2}{1000} * 1h = 53,7676884m^3$

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

Teniendo entonces:

$\frac{\mathrm{d} V}{\mathrm{d} t} = (C_{n}*I*A_{terr}) - (Q_{max}\sqrt{\frac{\Delta H_{max} - \Delta H}{\Delta H_{max} - \Delta H_{min}}})$ <br>

$\frac{\mathrm{d} C}{\mathrm{d} t} = \frac{V_{n}}{V_{sot}t_{k}}(C_{sat} - C_{n})$ <br>


Planteamos el euler:

$V_{n+1} = V_{n} + h * ((C_{n}*I*A_{terr}) - (Q_{max}\sqrt{\frac{\Delta H_{max} - \Delta H}{\Delta H_{max} - \Delta H_{min}}}) )$

$C_{n+1} = C_{n} + h * (\frac{V_{n}}{V_{sot}t_{k}}(C_{sat} - C_{n}))$

Quedando:

$V_{n+1} = V_{n} + h * ((C_{n}*I*632,56104m^2) - (8\frac{m^3}{h} \sqrt{\frac{4m - (3,5m - (\frac{V_{n}}{74,9956m^2}))}{4m - 1m}}) )$


$C_{n+1} = C_{n} + h * (\frac{V_{n}}{262,4846m^3 * 0,2173857143h}(0,90 - C_{n}))$

Ambas ecuaciones dependen de la otra, pero como partimos de unos valores iniciales siempre puede calcularse la siguiente iteración $n+1$ habiendo calculado la iteracion $n$ para ambas ecuaciones planteadas. Por esa razón, comenzamos calculando $C_{1}$ y $V_{1}$ usando los valores de $C_{0}$ Y $V_{0}$, reemplazando a su vez con el $I$ correspondiente en cada entrada de la tabla. Una vez calculado la iteracion $1$, podemos calcular el $C_{2}$ y $V_{2}$ y así continuamente.

Este planteo nos arrojó los siguientes resultados:


#### <u>Lluvia de 5 minutos</u>
Intensidad = $241,4$ $mm/h$ <br>
Duración = $5/60$ $h$ <br>

Resultado: tarda $2,25$ $h$ en vaciarse.


![Modelo 5 min](./assets/Modelo%205%20minutos.png)



#### <u>Lluvia de 10 minutos</u>
Intensidad = $190,7$ $mm/h$ <br>
Duración = $1/6$ $h$ <br>

Resultado: tarda $3,4667$ $h$ en vaciarse.


![Modelo 10 min](./assets/Modelo%2010%20minutos.png)

#### <u>Lluvia de 15 minutos</u>
Intensidad = $162,6$ $mm/h$ <br>
Duración = $1/4$ $h$ <br>

Resultado: tarda $4,3667$ $h$ en vaciarse.


![Modelo 15 min](./assets/Modelo%2015%20minutos.png)

#### <u>Lluvia de 30 minutos</u>
Intensidad = $119,6$ $mm/h$ <br>
Duración = $1/2$ $h$ <br>

Resultado: tarda $6,2667$ $h$ en vaciarse.


![Modelo 30 min](./assets/Modelo%2030%20minutos.png)

#### <u>Lluvia de 60 minutos</u>
Intensidad = $85,0$ $mm/h$ <br>
Duración = $1$ $h$ <br>

Resultado: tarda $8,76$ $h$ en vaciarse.


![Modelo 60 min](./assets/Modelo%2060%20minutos.png)

#### <u>Lluvia de 3 horas</u>
Intensidad = $41,7$ $mm/h$ <br>
Duración = $3$ $h$ <br>

Resultado: tarda $13,35$ $h$ en vaciarse.


![Modelo 3 horas](./assets/Modelo%203%20horas.png)

#### <u>Lluvia de 6 horas</u>
Intensidad = $26,4$ $mm/h$ <br>
Duración = $6$ $h$ <br>

Resultado: tarda $17,8$ $h$ en vaciarse.


![Modelo 6 horas](./assets/Modelo%206%20horas.png)

#### <u>Lluvia de 12 horas</u>
Intensidad = $16,7$ $mm/h$ <br>
Duración = $12$ $h$ <br>

Resultado: tarda $23,8$ $h$ en vaciarse.


![Modelo 12 horas](./assets/Modelo%2012%20horas.png)

#### <u>Lluvia de 24 horas</u>
Intensidad = $10,9$ $mm/h$ <br>
Duración = $24$ $h$ <br>

Resultado: tarda $33,2$ $h$ en vaciarse.


![Modelo 24 horas](./assets/Modelo%2024%20horas.png)

#### <u>Lluvia de 72 horas</u>
Intensidad = $5,2$ $mm/h$ <br>
Duración = $72$ $h$ <br>

Resultado: tarda $0$ $h$ en vaciarse, nunca se llena.


![Modelo 72 horas](./assets/Modelo%2072%20horas.png)

La simulación reveló que el caudal de entrada $Q_{ent}$ varía significativamente con la intensidad de la precipitación, mientras que el caudal de salida $Q_{sal}$ depende directamente de la capacidad de la bomba y el desnivel $\Delta H$.

En situaciones de baja precipitación pero de larga duración, como las lluvias de 3, 6 y 12 horas, el modelo arrojó los valores de volumen más elevados. Esto se debe a que la acumulación de agua se da de manera continua y sostenida. La entrada constante de agua, incluso a baja intensidad, supera la capacidad de desagote de la bomba durante periodos prolongados, lo que lleva a mayores volúmenes de agua acumulada.

Mientras que en condiciones de alta precipitación y corta duración, como las lluvias de 5, 10 y 15 minutos, se observan los valores de volumen más bajos. Esto se debe a que estas lluvias provocan una entrada de agua muy intensa pero breve. La bomba de desagote puede manejar el pico de entrada de agua de manera eficiente, dado que la duración es limitada y no permite una acumulación significativa de agua en el sótano.

La bomba tiene una capacidad máxima de desagote que puede manejar altos caudales por períodos cortos. En cambio, durante lluvias prolongadas, la capacidad de desagote puede no ser suficiente para compensar la entrada continua de agua.

En el caso específico de la lluvia de 72 horas, la intensidad de lluvia es tan baja que el caudal de entrada $Q_{ent}$ nunca supera el caudal de salida $Q_{sal}$. Esto resulta en que el volumen de agua en el sótano se mantiene en cero o en valores negativos. Esto significa que cualquier agua que entre en el sistema es desagotada inmediatamente. La bomba de desagote es capaz de manejar completamente el caudal de entrada, desagotando el agua de manera eficiente y manteniendo el volumen de agua en el sótano en cero.


### Punto B
Ahora, nos encontramos ante el desafío de redimensionar la bomba adoptando un nuevo valor para la variable $Q_{max}$ para que la altura del agua sobre el piso del sótano jamás exceda los $0,25m$ para ninguna de las precipitaciones presentes en la tabla brindada.


Sabiendo que:

<div style="text-align: center">

$H = \frac{V}{A_{sot}}$
</div>

y teniendo el valor $A_{sot} = 74,9956$, se debe cumplir que $H < 0,25$, podemos despejar y nos queda que:

$\frac{V}{74,9956m^2} < 0,25m$ <br>
$V < 0,25m * 74,9956m^2$ <br>
$V < 18,7489m^3$ <br>

Buscamos aproximar a $V$ y sabemos por la ecuacion 1 que:

$$ V = \int_{0}^{t} Q_{ent} - Q_{sal}\, dt$$

Y para $\Delta t$ muy chicos con $\Delta t = h$ podemos plantear que
<div style="text-align: center">

$V \approx h *(Q_{ent} - Q_{sal})$
</div>

Nos termina quedando que:

<div style="text-align: center">

$h *(Q_{ent} - Q_{sal}) < 18,7489m^3$
</div>

Lo cual es igual a:

<div style="text-align: center">

$h *((\frac{C*I*A_{terr}}{1000}) - (Q_{max}\sqrt{\frac{\Delta H_{max} - \Delta H}{\Delta H_{max} - \Delta H_{min}}})) < 18,7489m^3$


$Q_{max} > \frac{\frac{C*I*A_{terr}}{1000} - \frac{18,7489m^3}{h}}{\sqrt{\frac{\Delta H_{max} - \Delta H}{\Delta H_{max} - \Delta H_{min}}}}$
</div>

Reemplazando con los valores que tenemos:

<div style="text-align: center">

$Q_{max} > \frac{\frac{C*I*632,56104m^2}{1000} - \frac{18,7489m^3}{h}}{\sqrt{\frac{4m - 3,25m}{4m - 1m}}}$

$Q_{max} > \frac{\frac{C*I*632,56104m^2}{1000} - \frac{18,7489m^3}{h}}{0,5}$

</div>

Aplicamos esta cuenta con cada una de las intensidades, considerando $Q_{ent}$ y $Q_{sal}$ como variables. Como es una aproximacion a V, este resultado no es exacto pero se llega a la que conclusión de que para lograr que la altura de agua sobre el piso del sótano no exceda los $0,25m$ en ninguna de las precipitaciones de la tabla se necesita aproximadamente un $Q_{max} > 32,5m^3/h$. Este máximo se alcanza con el modelo de $1$ hora.

Con este nuevo valor de $Q_{max}$ el sistema tiene la capacidad suficiente para drenar el agua de manera eficiente, incluso durante las precipitaciones más intensas registradas en la tabla, ya que la bomba puede manejar el flujo de agua entrante de manera adecuada, sin exceder los $0,25m$.

### Punto C

Se nos pide ahora discretizar las ecuaciones 1 y 6 con el método de Runge-Kutta de orden 2, considerando esta solución como “exacta”. Luego, debemos correr este modelo para la precipitación de 60 min con el método de Runge-Kutta de orden 2, y luego con Euler con dos pasos de tiempo distintos. Además, debemos verificar que Euler es de orden 1 analizando la diferencia con la solución “exacta”, utilizando siempre el $Q_{max}$ obtenido anteriormente en el punto B.

Decidimos correr el modelo primero con un $\Delta t = 1/60 h$ y notamos que los valores de Runge-Kutta y Euler eran bastantes similares, con diferencias bastante pequeñas:

![Punto C h=1min](./assets/Modelo%2060%20minutos%20con%20h%20=%201%20min%20Punto%20C.png)

Para poder ver errores más grandes corrimos nuevamente el modelo pero ahora utilizando $\Delta t = 1/6 h$:

![Punto C h=10min](./assets/Modelo%2060%20minutos%20con%20h%20=%2010%20min%20Punto%20C.png)

y $\Delta t = 1/2h$

![Punto C h=30min](./assets/Modelo%2060%20min,%20con%20h%20=%2030%20min%20Punto%20C.png)


Al comparar los resultados obtenidos utilizando diferentes tamaños de paso $h$, hemos examinado el error en relación con la solución obtenida mediante el método de Runge-Kutta de segundo orden, considerado como la solución "exacta". Los resultados destacan una disminución proporcional y lineal del error global con respecto al tamaño del paso, lo que confirma la naturaleza de primer orden del método de Euler. <br>

Cuando comparamos los errores relativos con un paso de tiempo $\Delta t = 1/60 h$ vamos que son linealmente proporcionales a los obtenidos cuando $\Delta t = 1/2 h$. Es decir, se cumple que teniendo $\epsilon_{1}$ y $\epsilon_{2}$ para pasos de tiempo $\Delta t_{1}$ y $\Delta t_{2} = \Delta t_{1} / 3 $, encontramos que:

$\frac{\epsilon_{2}}{\epsilon_{1}} \approx \frac{\Delta t_2}{\Delta t_1} = \frac{\Delta t_{1} / 3}{\Delta t_1} =  \frac{1}{3}$

Como esto se cumple y el error se reduce aproximadamente a un tercio cuando reducimos el paso de tiempo a un tercio, se confirma que el método de Euler es de orden 1. Lo mismo ocurre cuando comparamos $\Delta t = 1/60h$ con $\Delta t = 1/2h$, solo que esta vez:

$\frac{\epsilon_{2}}{\epsilon_{1}} \approx \frac{\Delta t_2}{\Delta t_1} = \frac{\Delta t_{1} / 30}{\Delta t_1} =  \frac{1}{30}$

Además, es notable que las disparidades entre las soluciones de Euler y RK2 son insignificantes para pasos de tiempo reducidos, pero aumentan significativamente al incrementar el tamaño del paso. Este comportamiento también es coherente con las expectativas de un método de primer orden. <br>

### Punto D

#### Conclusiones finales <br>

En este trabajo práctico se abordó la resolución numérica de un problema físico de gran relevancia: el dimensionamiento de una bomba de desagote en un edificio con sótano, afectado por lluvias intensas. A continuación, se detallan las conclusiones principales derivadas del análisis y la modelación realizados: <br>

1. **Relación Problema Físico-Problema Numérico**: <br>
   El problema físico consiste en gestionar el agua de lluvia que ingresa a un sótano durante una inundación. Este fenómeno se modeló mediante ecuaciones diferenciales ordinarias que describen la conservación de masa y la variación del coeficiente de infiltración. <br>
   La transformación del problema físico a un problema numérico permitió utilizar métodos de resolución como Euler y Runge-Kutta, facilitando la simulación y análisis del sistema en distintos escenarios de precipitación. <br>

2. **Tipos de Errores en la Resolución Numérica**: <br>
   **Error de Truncamiento**: En el método de Euler, este error es del orden de $\Delta t$, mientras que en Runge-Kutta de segundo orden, el error es del orden de $(\Delta t)^2$. Esto se evidenció en las diferencias observadas al comparar los resultados de Euler con los de Runge-Kutta. <br>
   **Error de Redondeo**: Proviene de la precisión finita de las computadoras. Al tener una mantisa finita y limitada, los resultados que utilizan los programas empleados para desarrollar este trabajo práctico no son exactos. <br>

3. **Importancia y Efecto de los Errores**: <br>
   Los errores numéricos pueden influir en la precisión del cálculo del caudal necesario y, por ende, en la selección de la bomba adecuada. Un error significativo podría llevar a subdimensionar o sobredimensionar la bomba.<br>
   La diferencia entre las soluciones obtenidas con distintos métodos numéricos demuestra la necesidad de seleccionar adecuadamente el método y el paso de tiempo según la precisión requerida.<br>

4. **Estabilidad y Consistencia**:<br>
   **Estabilidad**: Ambos métodos utilizados son condicionalmente estables y dependen del tamaño del paso de tiempo $\Delta t$ elegido. Un $\Delta t$ demasiado grande puede llevar a soluciones inestables. <br>
   **Consistencia**: Ambos métodos son consistentes, pero el orden de consistencia varía. Runge-Kutta de segundo orden es más preciso para el mismo paso de tiempo en comparación con Euler.<br>

En resumen, el trabajo realizado demuestra la importancia de un enfoque numérico adecuado para resolver problemas físicos complejos. La elección de los métodos y parámetros numéricos a utilizar es esencial para obtener soluciones precisas y eficientes.
