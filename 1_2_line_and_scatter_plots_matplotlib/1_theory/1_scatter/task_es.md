## Objetivo

El objetivo principal de la lección es **graficar la correlación entre las puntuaciones de los usuarios y las puntuaciones de los críticos**.

## Teoría

En Matplotlib, hay varias formas de graficar gráficos relacionales, pero nos centraremos en dos de ellas:

1. Usar [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html).  
   Esta función crea gráficos de dispersión.
2. Usar [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html).  
   Esta función crea gráficos de líneas.

Por ahora, trabajaremos con la función `scatter`.

Cada función de graficado en Matplotlib acepta tres argumentos principales:

* `data`: La estructura de datos de entrada. (por ejemplo, un DataFrame de Pandas o algún mapeo).
* `x`: El nombre de la columna que se visualizará en el eje x.
* `y`: El nombre de la columna que se visualizará en el eje y.

Hay algunos aspectos importantes a tener en cuenta:

1. `data` es opcional. Si no lo proporcionamos, `x` y `y` deben ser colecciones que contengan los datos.
2. Solo podemos especificar el parámetro `data` como un argumento de palabra clave.
3. Debemos especificar los parámetros `x` y `y` como argumentos posicionales.

Al usar Matplotlib, recomendamos pasar cualquier otro argumento como argumento de palabra clave.  
Por ejemplo: `plt.scatter("column_x", "column_y", data=my_data, some_argument="some_value")`.

<hr>

Para comenzar a construir gráficos con Matplotlib, necesitas crear un objeto [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html) y al menos un objeto [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes).  
Podemos pensar en la `Figure` como un contenedor para varios `Axes`, donde se realizan las gráficas.

Para crear una `Figure` y un único `Axes`, podemos usar la función [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html): `fig, ax = plt.subplots()`.  
Aquí, usamos las abreviaturas comunes para `Figure` (`fig`) y `Axes` (`ax`).  
También estamos usando el alias común para Matplotlib (`plt`), que definimos durante la importación: `import matplotlib.pyplot as plt`.

Toma en cuenta la diferencia entre `Axes` y [`Axis`](https://matplotlib.org/stable/api/axis_api.html#axis-objects):  
un objeto `Axes` puede contener varios objetos `Axis` (usualmente el eje x y el eje y).

Como mencionamos anteriormente, la graficación se realiza dentro del `Axes`.  
Para graficar algo en la figura, deberíamos llamar a los métodos desde la instancia de `Axes`.  
Por ejemplo, para crear un gráfico de dispersión, escribiríamos algo como esto: `ax.scatter('x', 'y', data=my_data)`.

¡Ahora, practiquemos!

## Tarea

1. Crea una instancia de `Figure` y `Axes` en la función `plot`.
2. Crea un gráfico de dispersión donde el eje x represente `user_score`, el eje y represente `critic_score` y los datos sean `games`.

Ten en cuenta que hemos preprocesado los datos para ti, pero si prefieres, puedes hacerlo por tu cuenta.  
Consulta la pista correspondiente a continuación.

## Pistas

<div class="hint" title="¿Cómo ejecutar el código?">
   Para ejecutar el código, haz clic en el triángulo verde junto al punto de entrada. Si ocurren errores de ejecución, serán mostrados en la consola dentro del entorno IDE.  
   <img src="../../../common/resources/images/common/entry_point.png" style="max-width: 500px">
</div>

<div class="hint" title="¿Dónde encontrar mi figura?">
   Después de ejecutar el código, el gráfico se generará junto al archivo task.py.

   <img src="../../../common/resources/images/common/output_location.png" style="max-width: 500px">
</div>

<div class="hint" title="¿Cómo debería preprocesar los datos?">
   Antes de usar los datos, necesitas realizar varios pasos de preprocesamiento:
   <ol>
      <li>Convertir los nombres de las columnas a minúsculas.</li>
      <li>Eliminar los juegos con puntuaciones de usuario listadas como "decidir más tarde" (es decir, donde la puntuación del usuario sea <code>tbd</code>).</li>
      <li>Eliminar todos los valores NaN de las siguientes columnas:</li>
      <ul>
         <li><code>critic_score</code></li>
         <li><code>user_score</code></li>
      </ul>
      <li>Convertir la columna <code>user_score</code> a tipo float.</li>
   </ol>

   Ten en cuenta que tu propia función de preprocesamiento no será evaluada.
</div>

<div class="hint" title="¿Cómo debería lucir la figura?">
   <img src="example.png" alt="Cómo debería lucir la figura" style="max-height: 500px">
</div>