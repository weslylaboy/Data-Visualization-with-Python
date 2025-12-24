## Teoría

Hasta ahora, solo hemos construido gráficos de barras simples, pero a veces es necesario trazar varias trazas en el mismo gráfico.  
Por ejemplo, podríamos querer comparar las ventas totales a lo largo de las décadas para diferentes regiones.

El método `bar` te permite colocar manualmente las barras donde lo necesites.  
Por ejemplo, si pasamos `range(3)` como eje x y `[5, 4, 3]` como las alturas, el resultado se vería algo así:

<img src="../../../common/resources/images/bar_and_pie_charts/grouped_bar_chart_1.png" alt="Cómo debería verse la figura" style="max-height: 500px">

Como podemos observar, `bar` colocó la primera barra en 0, la segunda en 1 y la tercera en 2.

Para nuestra figura, tendremos varios grupos (décadas) y para cada grupo trazaremos varias trazas (regiones).  
¡Comencemos con una tarea sencilla!

## Tarea

1. Usa la función oculta `aggregate` para calcular las ventas totales (`sales`) a lo largo de las décadas (`decade`) para cada región (`region`).  
   
   Si lo prefieres, también puedes hacerlo manualmente. Por favor, consulta las sugerencias correspondientes más abajo.

2. Implementa la función `plot_region`. Esta debería graficar las ventas regionales totales a lo largo de las décadas, como en el ejemplo.

   Puedes usar la función oculta `get_number_of_decades` para calcular el número total de décadas 
   y la función `get_region_sales` para obtener los datos de ventas de una región específica.

   Si lo prefieres, también puedes hacerlo manualmente. Por favor, consulta las sugerencias correspondientes más abajo.

   Nota que no necesitas usar el argumento `trace` por ahora.

3. Usa la función `plot_region` para graficar las ventas totales de la región de Norteamérica (`na`).

## Sugerencias

<div class="hint" title="¿Cómo agrupar los datos?">
   Para calcular las ventas totales por década para cada región:
   <ol>
      <li>Usa la función <a href="https://pandas.pydata.org/docs/reference/api/pandas.cut.html"><code>cut</code></a> para convertir el año de lanzamiento en décadas.</li>
      <li>Usa la función <a href="https://pandas.pydata.org/docs/reference/api/pandas.melt.html"><code>melt</code></a> para extraer las regiones de ventas.</li>
      <li>Agrupa los datos por las columnas de década y región utilizando el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html"><code>groupby</code></a>, y calcula las ventas totales usando el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.sum.html"><code>sum</code></a>.</li>
   </ol>

   Nota que tu función personalizada no será evaluada.
</div>

<div class="hint" title="¿Cómo calcular el número de décadas?">
   Para calcular el número de décadas, puedes usar el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nunique.html"><code>nunique</code></a> en la columna <code>decade</code>.

   Nota que tu función personalizada no será evaluada.
</div>

<div class="hint" title="¿Cómo filtrar las ventas por región?">
   Para filtrar las ventas de una región específica, usa el <a href="https://pandas.pydata.org/pandas-docs/version/1.0/getting_started/intro_tutorials/03_subset_data.html#how-do-i-filter-specific-rows-from-a-dataframe">notación de corchetes</a> junto con una condición en la columna <code>region</code>.

   Nota que tu función personalizada no será evaluada.
</div>

<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>