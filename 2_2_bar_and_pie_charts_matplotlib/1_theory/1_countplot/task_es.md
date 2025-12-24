## Objetivo

El objetivo principal de la lección es **graficar estadísticas descriptivas sobre diferentes plataformas de videojuegos y sus ventas globales**:
1. Número de plataformas diferentes (como gráfico de barras y gráfico circular).
2. Ventas totales por década para cada región.

## Teoría

En Matplotlib, hay varias funciones para graficar gráficos categóricos:
1. [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar): Construye gráficos de barras verticales.
2. [`barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html#matplotlib.pyplot.barh): Similar a `bar` pero construye gráficos de barras horizontales.
3. [`pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html#matplotlib.pyplot.pie): Construye gráficos circulares.

Por ahora, comenzaremos con la función `bar`.

Como otras funciones de Matplotlib, `bar` acepta tres argumentos principales: 
`x`, `height` (similar a `y` en otros tipos de gráficos) y `data`.
Los describimos en detalle en la sección 
"[Gráficos Lineales y de Dispersión](course://1_2_line_and_scatter_plots_matplotlib/1_theory/1_scatter)".

Lamentablemente, Matplotlib no agrega los datos por nosotros, por lo que necesitamos hacerlo manualmente.

## Tarea

1. Usa la función oculta `aggregate` para calcular el número de videojuegos (`count`) para cada plataforma (`platform`) en orden descendente.

   Si lo prefieres, puedes agregar los datos por tu cuenta. Por favor, consulta la pista correspondiente a continuación.

2. Llama al método `bar` del objeto `Axes` para graficar un gráfico de barras. 
   Establece `platform` como el eje x, `count` como la altura y `games` como los datos.

Ten en cuenta que hemos preprocesado los datos para ti. Para aprender cómo lo hicimos, consulta la pista correspondiente a continuación.

## Pistas
<div class="hint" title="¿Cómo ejecutar el código?">
   Para ejecutar el código, haz clic en el triángulo verde junto al punto de entrada.
   Si hay errores de ejecución, se mostrarán en la consola dentro del IDE. 
   <img src="../../../common/resources/images/common/entry_point.png" style="max-width: 500px">
</div>

<div class="hint" title="¿Cómo importar funciones ocultas?">
    Para importarlas, puedes colocar el cursor sobre el nombre subrayado de la función oculta en tu código, luego presiona &shortcut:ShowIntentionActions;, y selecciona <samp>Import 'function_name from data'</samp>:
   <img src="../../../common/resources/images/common/hidden_function_import.gif" alt="Cómo importar funciones ocultas" style="max-height: 500px">
</div>

<div class="hint" title="¿Dónde encontrar mi gráfico?">
   Después de ejecutar el código, el gráfico se generará junto al archivo <code>task.py</code>.
   <img src="../../../common/resources/images/common/output_location.png" style="max-width: 500px">
</div>

<div class="hint" title="¿Cómo se preprocesaron los datos?">
   Antes de usar los datos, necesitamos realizar varios pasos de preprocesamiento:
   <ol>
      <li>Convertir los nombres de las columnas a minúsculas.</li>
      <li>Eliminar todos los valores NaN de las siguientes columnas:</li>
      <ul>
         <li><code>platform</code></li>
         <li><code>year_of_release</code></li>
         <li><code>global_sales</code></li>
         <li><code>eu_sales</code></li>
         <li><code>jp_sales</code></li>
         <li><code>na_sales</code></li>
         <li><code>other_sales</code></li>
      </ul>
      <li>Convertir la columna <code>year_of_release</code> a un entero.</li>
   </ol>
</div>

<div class="hint" title="¿Cómo debo agregar los datos?">
   Para calcular el número total de videojuegos por plataforma:
   <ol>
      <li>Usa el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html"><code>value_counts</code></a> en la columna <code>platform</code> para calcular el número de filas por cada plataforma.</li>
      <li>Convierte el resultado en un <code>DataFrame</code> utilizando el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.reset_index.html"><code>reset_index</code></a>.</li>
   </ol>

   Nota que tu función personalizada no será evaluada.
</div>

<div class="hint" title="¿Cómo debería verse el gráfico?"> 
   <img src="example.png" alt="Cómo debería verse el gráfico" style="max-height: 500px">
</div>