## Objetivo

El objetivo principal de esta lección es **explorar la distribución de las ventas de videojuegos utilizando histogramas**. Analizaremos:

1. La distribución general de las ventas globales.
2. La distribución de las ventas globales por editor.

## Teoría

En Seaborn, las distribuciones pueden visualizarse utilizando la función [
`displot`](https://seaborn.pydata.org/generated/seaborn.displot.html). Similar a 
[`catplot`](https://seaborn.pydata.org/generated/seaborn.catplot.html), acepta un argumento especial, `kind`, que define el tipo de distribución a construir. Por defecto, `kind="hist"`, y la función crea un histograma, en el que nos enfocaremos en este módulo.

Como otras funciones de Seaborn, `displot` acepta tres argumentos principales: `data`, `x` y `y`.
Los describimos en detalle en la sección 
"[Gráficos de líneas y dispersión](course://1_1_line_and_scatter_plots_seaborn/1_theory/1_relplot_scatter)".

## Tarea

Crea un histograma que muestre la distribución de las ventas globales utilizando la función `displot`. Pasa `games` como
`data` y `global_sales` como el eje x.

Ten en cuenta que hemos preprocesado los datos por ti. Para aprender cómo se realizó este proceso, consulta la pista correspondiente a continuación.

## Pistas

<div class="hint" title="¿Cómo ejecutar el código?">
   Para ejecutar el código, haz clic en el triángulo verde al lado del punto de entrada.
   En caso de errores de ejecución, los problemas se mostrarán en la consola dentro del IDE. 
   <img src="../../../common/resources/images/common/entry_point.png" style="max-width: 500px">
</div>

<div class="hint" title="¿Dónde puedo encontrar mi figura?">
   Después de ejecutar el código, el gráfico se generará al lado del archivo `task.py`.
   <img src="../../../common/resources/images/common/output_location.png" style="max-width: 500px">
</div>

<div class="hint" title="¿Cómo se preprocesaron los datos?">
Antes de usar los datos, necesitamos realizar varios pasos de preprocesamiento:
   <ol>
      <li>Convertir los nombres de las columnas a minúsculas.</li>
      <li>Eliminar los juegos con puntuaciones de usuario no definidas (donde la puntuación de usuario es igual a <code>tbd</code>).</li>
      <li>Eliminar todos los valores NaN de las siguientes columnas:</li>
      <ul>
         <li><code>platform</code></li>
         <li><code>critic_score</code></li>
         <li><code>user_score</code></li>
         <li><code>global_sales</code></li>
         <li><code>eu_sales</code></li>
         <li><code>jp_sales</code></li>
         <li><code>na_sales</code></li>
         <li><code>other_sales</code></li>
      </ul>
      <li>Convertir la columna <code>user_score</code> a tipo float.</li>
   </ol>
</div>

<div class="hint" title="¿Cómo debería lucir la figura?">
   <img src="example.png" alt="Cómo debería lucir la figura" style="max-height: 500px">
</div>