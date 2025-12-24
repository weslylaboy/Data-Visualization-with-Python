## Objetivo

El objetivo principal de la lección es **graficar la correlación entre las puntuaciones de los usuarios y las puntuaciones de los críticos**.

## Teoría

En Seaborn, hay varias formas de graficar gráficos relacionales, pero nos centraremos en dos de ellas:

1. [`relplot`](https://seaborn.pydata.org/generated/seaborn.relplot.html) (significa **rel**ational **plot** o gráfico relacional):  
   Esta función puede graficar tanto gráficos de dispersión como gráficos lineales.
2. [`lmplot`](https://seaborn.pydata.org/generated/seaborn.lmplot.html) (significa **l**inear **m**odel **plot** o gráfico de modelo lineal):  
   Esta función se centra en graficar líneas de regresión.  
   Hablaremos de esto un poco más adelante.

Por ahora, trabajaremos con la función `relplot`.

Cada función de graficación en Seaborn acepta tres argumentos principales:

* `data`: La estructura de datos de entrada (por ejemplo, un DataFrame de Pandas o algún mapeo).
* `x`: El nombre de la columna a visualizar en el eje x.
* `y`: El nombre de la columna a visualizar en el eje y.

Ten en cuenta que el argumento `data` es opcional.  
Si no lo proporcionas, `x` y `y` deben ser colecciones que contengan los datos a graficar.

Al usar Seaborn, recomendamos pasar `data` como un argumento posicional  
y cualquier otro argumento (incluyendo `x` e `y`) como argumentos de palabra clave.  
Por ejemplo: `sns.relplot(my_data, x="column_x", y="column_y", some_argument="some_value")`.

La manera más común de importar Seaborn es de la siguiente forma: `import seaborn as sns`.  
Ya hemos hecho esto por ti, así que para llamar a `relplot`, solo necesitas escribir `sns.relplot`.

¡Ahora, practiquemos un poco!

## Tarea

Modifica el `plot` agregando una llamada a la función `relplot`.  
Pasa `games` como los datos, `user_score` como el eje x y `critic_score` como el eje y.

Ten en cuenta que preprocesamos los datos por ti, pero si lo prefieres, puedes hacerlo tú mismo.  
Consulta la pista correspondiente a continuación.

## Pistas

<div class="hint" title="¿Cómo ejecutar el código?">
   Para ejecutar el código, haz clic en el triángulo verde junto al punto de entrada.  
   En caso de errores de ejecución, se mostrarán en la consola dentro del IDE.  
   <img src="../../../common/resources/images/common/entry_point.png" style="max-width: 500px">
</div>

<div class="hint" title="¿Dónde puedo encontrar mi figura?">
   Después de ejecutar el código, el gráfico se generará junto al archivo <code>task.py</code>.  
   <img src="../../../common/resources/images/common/output_location.png" style="max-width: 500px">
</div>

<div class="hint" title="¿Cómo debería preprocesar los datos?">
   Antes de usar los datos, necesitamos realizar varios pasos de preprocesamiento:
   <ol>
      <li>Convertir los nombres de las columnas a minúsculas.</li>
      <li>Eliminar los juegos con puntuaciones de usuario no decididas (donde la puntuación de usuario es igual a <code>tbd</code>).</li>
      <li>Eliminar todos los valores NaN de las siguientes columnas:</li>
      <ul>
         <li><code>critic_score</code></li>
         <li><code>user_score</code></li>
      </ul>
      <li>Convertir la columna <code>user_score</code> a tipo float.</li>
   </ol>
</div>

<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>