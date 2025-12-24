## Teoría

Como podemos observar, algo definitivamente ha cambiado en nuestra figura: graficamos varias trazas, pero solo podemos ver algunas de ellas.  
Esto ocurrió porque las graficamos en las mismas coordenadas del eje x, lo que provocó que se superpusieran.

Para solucionar esto, necesitamos aumentar la distancia entre décadas para que quepa cada región.

Por ejemplo, si tenemos 3 grupos, cada uno de tamaño 4,  
necesitaríamos una distancia de 4 para acomodar los datos de todas las regiones:  
<img src="../../../common/resources/images/bar_and_pie_charts/grouped_bar_chart_2.png" alt="Cómo debería verse la figura" style="max-height: 500px">

Sin embargo, si hacemos esto, no habrá espacio entre los grupos:  
<img src="../../../common/resources/images/bar_and_pie_charts/grouped_bar_chart_3.png" alt="Cómo debería verse la figura" style="max-height: 500px">

Para solucionar esto, deberíamos aumentar artificialmente el tamaño de cada grupo en 1 unidad:  
<img src="../../../common/resources/images/bar_and_pie_charts/grouped_bar_chart_4.png" alt="Cómo debería verse la figura" style="max-height: 500px">

Como resultado, la distancia total será de 5.

Además, algo importante a tener en cuenta es que el ancho de cada barra debe ser igual a 1 para que no haya espacio entre las barras.  
Para lograr esto, podemos usar el argumento `width`.

## Tarea

Modifica la función `plot_region` para graficar los datos de cada región con el espaciado correcto y utiliza el argumento `trace` para desplazar la traza de cada región.

Puedes usar la función oculta `get_number_of_regions` para calcular el número de regiones.  
Si lo prefieres, puedes obtener todas las regiones manualmente. Por favor, consulta los consejos correspondientes a continuación.

## Consejos

<div class="hint" title="¿Cómo calcular el número de regiones?">
   Para calcular el número de regiones, puedes usar el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nunique.html"><code>nunique</code></a> en la columna <code>region</code>.
</div>

<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>