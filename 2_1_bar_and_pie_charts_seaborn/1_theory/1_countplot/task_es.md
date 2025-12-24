## Objetivo

El objetivo principal de esta lección es **graficar estadísticas descriptivas sobre diferentes plataformas de videojuegos y sus ventas globales**:
1. Número de plataformas diferentes
2. Ventas globales totales por plataforma
3. Ventas totales por década para cada región

Seaborn no admite gráficos de torta, por lo que esta lección se centrará exclusivamente en construir gráficos de barras.  
Si deseas aprender cómo crear un gráfico de torta, consulta [la lección de Matplotlib](course://2_2_bar_and_pie_charts_matplotlib/1_theory/1_countplot).

## Teoría

En Seaborn, existe una función universal que puede construir casi cualquier tipo de gráfico categórico:  
[`catplot`](https://seaborn.pydata.org/generated/seaborn.catplot.html).  
Similar a [`relplot`](https://seaborn.pydata.org/generated/seaborn.relplot.html), acepta un argumento especial, `kind`, que define el tipo de gráfico a construir.

En esta sección, nos centraremos en dos tipos de gráficos categóricos:
1. `bar`: Se utiliza para crear gráficos de barras de propósito general  
2. `count`: Se utiliza para crear un tipo especial de gráfico de barras llamado **gráfico de conteo**, donde el eje y representa el número de observaciones para cada categoría  

Al igual que otras funciones de Seaborn, `catplot` acepta tres argumentos principales: `data`, `x` y `y`.  
Los describimos en detalle en la sección  
"[Gráficos de línea y dispersión](course://1_1_line_and_scatter_plots_seaborn/1_theory/1_relplot_scatter)".

## Tarea

Utiliza la función `catplot` para construir un gráfico de conteo simple.  
Pasa `games` como los datos, `platform` como el eje x, y `count` como el tipo (`kind`).

Ten en cuenta que hemos preprocesado los datos por ti. Para aprender cómo lo hicimos, consulta la pista correspondiente a continuación.

## Pistas
<div class="hint" title="¿Cómo ejecutar el código?">
   Para ejecutar el código, haz clic en el triángulo verde junto al punto de entrada.  
   En caso de errores de ejecución, se mostrarán en la consola dentro del IDE.  
   <img src="../../../common/resources/images/common/entry_point.png" style="max-width: 500px">
</div>

<div class="hint" title="¿Dónde encuentro mi figura?">
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

<div class="hint" title="¿Cómo debería verse la figura?"> 
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>