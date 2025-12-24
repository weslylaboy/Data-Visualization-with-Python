## Objetivo

El objetivo principal de esta lección es **explorar la distribución de las ventas de videojuegos utilizando histogramas**. Analizaremos:

1. La distribución general de las ventas globales.
2. La distribución de las ventas globales por editor.

## Teoría

En Matplotlib, las distribuciones pueden visualizarse utilizando la función [
`hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist).

La función acepta dos argumentos principales: `x` y `data`. Los describimos en detalle en la sección "[Gráficos de Línea y Dispersión](course://1_2_line_and_scatter_plots_matplotlib/1_theory/1_scatter)".

## Tarea

Crea un histograma para visualizar la distribución de las ventas globales usando el método `hist` llamado en el objeto `Axes`. Utiliza 
`games` como argumento `data` y `global_sales` como el eje x.

Ten en cuenta que hemos preprocesado los datos para ti. Para aprender cómo lo hicimos, consulta la pista correspondiente a continuación.

## Pistas

<div class="hint" title="¿Cómo ejecutar el código?">
   Para ejecutar el código, haz clic en el triángulo verde junto al punto de entrada.
   Si hay errores de ejecución, se mostrarán en la consola dentro del IDE.
   <img src="../../../common/resources/images/common/entry_point.png" style="max-width: 500px">
</div>

<div class="hint" title="¿Dónde encontraré mi figura?">
   Después de ejecutar el código, el gráfico se generará junto al archivo `task.py`.
   <img src="../../../common/resources/images/common/output_location.png" style="max-width: 500px">
</div>

<div class="hint" title="¿Cómo se preprocesaron los datos?">
Antes de usar los datos, necesitamos realizar varios pasos de preprocesamiento:
   <ol>
      <li>Convertir los nombres de las columnas a minúsculas.</li>
      <li>Eliminar los juegos con puntuaciones de usuario no decididas (donde la puntuación del usuario es igual a <code>tbd</code>).</li>
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
      <li>Convertir la columna <code>user_score</code> a un formato de número flotante.</li>
   </ol>
</div>

<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>