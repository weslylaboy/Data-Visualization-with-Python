## Teoría

Al observar el histograma con una escala logarítmica, podemos ver claramente que casi ningún juego supera los
`10` millones en ventas. Pero, ¿es suficiente este umbral? Para comprender mejor la distribución, examinemos las estadísticas resumidas de nuestro
conjunto de datos.

Podemos generar estadísticas resumidas para la columna `global_sales` en el conjunto de datos utilizando el
método [`describe`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html):

| parámetro | global_sales |
|:----------|-------------:|
| count     |        14294 |
| mean      |      0.59205 |
| std       |      1.66266 |
| min       |         0.01 |
| 25%       |         0.06 |
| 50%       |         0.19 |
| 75%       |         0.54 |
| max       |        82.53 |

Como podemos ver, los datos contienen más de `14` mil ventas de juegos distribuidos entre `0.01` y `82.53` millones con
una media
de aproximadamente `0.59` millones. Sin embargo, también hay algunos valores inusuales especificados para `25%`, `50%` y `75%`. Estos se llaman
percentiles.

Un percentil representa el valor por debajo del cual cae un porcentaje dado de puntos de datos en un conjunto de datos. Por ejemplo, podemos
ver que el `75%` de los juegos tiene ventas por debajo de `0.54` millones, mientras que el `25%` restante tiene
ventas que van desde
`0.54` millones hasta `82.53` millones. ¡Esto crea una gran brecha, lo que dificulta la visualización!

Para abordar este problema, vamos a
excluir el `5%` superior de juegos por ventas y centrarnos en aquellos por debajo del percentil 95.

## Tarea

Utiliza la función oculta `filter_by_global_sales` para obtener el conjunto de datos, incluyendo solo los juegos con ventas por debajo del percentil
95. Luego, pásalo a la función `displot`.

Ten en cuenta que no necesitas aplicar una escala logarítmica para esta tarea.

Si lo prefieres, puedes filtrar el conjunto de datos manualmente. Por favor, consulta la pista correspondiente a continuación.

## Pistas

<div class="hint" title="¿Cómo debería lucir la figura?">
   <img src="example.png" alt="¿Cómo debería lucir la figura?" style="max-height: 500px">
</div>

<div class="hint" title="¿Cómo importar la función oculta?">
    Para importarla, coloca el cursor sobre el nombre de la función oculta subrayada en tu código, presiona &shortcut:ShowIntentionActions; y selecciona <samp>Import 'function_name from data'</samp>:
    <img src="../../../common/resources/images/common/hidden_function_import.gif" alt="Cómo importar funciones ocultas" style="max-height: 500px">
</div>

<div class="hint" title="¿Cómo filtrar los datos utilizando un percentil?">
    Para filtrar los datos, necesitas:
    <ol>
    <li> Calcular el umbral utilizando el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.quantile.html"><code>quantile</code></a>
    en la columna <code>global_sales</code>. Ten en cuenta que el método requiere un cuantil, no un percentil.
    Para convertir un percentil en un cuantil, divídelo entre <code>100</code>. 
    Por ejemplo, el percentil 95 corresponde a un cuantil de <code>0.95</code>.</li>
    <li> Filtrar los datos por la columna <code>global_sales</code> utilizando indexación booleana.</li>
    </ol>
</div>