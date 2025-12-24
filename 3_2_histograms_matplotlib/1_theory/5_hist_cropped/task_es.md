## Teoría

Al observar el histograma con una escala logarítmica, podemos ver claramente que casi ningún juego supera los 
`10` millones en ventas. Pero, ¿es este umbral suficiente? Para entender mejor la distribución, analicemos las estadísticas resumidas de nuestro
conjunto de datos.

Podemos generar estadísticas resumidas para la columna `global_sales` en el conjunto de datos utilizando el método 
[`describe`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html):

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

Como podemos observar, los datos contienen más de `14` mil ventas de juegos distribuidas entre `0.01` y `82.53` millones, con un promedio 
de aproximadamente `0.59` millones. Sin embargo, hay algunos números inusuales especificados para `25%`, `50%` y `75%`. Estos se llaman
percentiles.

Un percentil representa el valor por debajo del cual cae un porcentaje dado de puntos de datos en un conjunto de datos. Por ejemplo, podemos
ver que el `75%` de los juegos tiene ventas por debajo de `0.54` millones, mientras que el `25%` restante tiene
ventas en un rango de
`0.54` millones a `82.53` millones. ¡Esto crea una gran disparidad, lo que dificulta la visualización!

Para abordar este problema, excluyamos el `5%` superior de los juegos por ventas y centrémonos en aquellos por debajo del percentil 95.

## Tarea

Utiliza la función oculta `filter_by_global_sales` para recuperar el conjunto de datos, incluyendo solo los juegos con ventas globales por debajo del percentil 95,
y pásalo al método `hist`.

Ten en cuenta que no necesitas establecer una escala logarítmica para esta tarea. También, mantén el número predeterminado de contenedores (bins).

Si lo prefieres, puedes filtrar el conjunto de datos manualmente. Por favor, consulta la pista correspondiente a continuación.

## Pistas

<div class="hint" title="¿A qué debe parecerse la figura?">
   <img src="example.png" alt="¿A qué debe parecerse la figura?" style="max-height: 500px">
</div>

<div class="hint" title="¿Cómo filtrar los datos usando percentiles?">
    Para filtrar los datos, necesitas hacer lo siguiente:
    <ol>
    <li> Calcular el umbral usando el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.quantile.html"><code>quantile</code></a>
    en la columna <code>global_sales</code>. Ten en cuenta que este método requiere un cuantil, no un percentil.
    Para convertir un percentil a un cuantil, divídelo entre <code>100</code>. 
    Por ejemplo, el percentil 95 corresponde a un cuantil de <code>0.95</code>.</li>
    <li> Filtrar los datos de la columna <code>global_sales</code> usando indexación booleana.</li>
    </ol>
</div>