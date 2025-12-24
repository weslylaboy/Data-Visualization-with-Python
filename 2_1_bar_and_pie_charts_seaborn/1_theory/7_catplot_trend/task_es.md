## Teoría

Hasta ahora, hemos graficado valores continuos (ventas globales) para cada uno de los valores categóricos (plataformas).  
Pero, ¿qué pasa si tenemos dos variables continuas?  
Más precisamente, ¿qué hacemos si queremos comparar las ventas globales a lo largo de diferentes años?

Podemos hacerlo utilizando un gráfico de líneas.  
Sin embargo, si el número de categorías posibles es pequeño (por ejemplo, si solo observamos décadas),  
un gráfico de barras también es adecuado para este propósito.

## Tarea

Usa la función oculta `add_decades` para agregar una nueva columna llamada `decade` a los datos  
y grafica las ventas globales _**totales**_ por década.

Ten en cuenta que no necesitas reordenar las columnas, ya que se ordenan automáticamente.

Si lo prefieres, puedes agregar las décadas manualmente. Consulta la pista correspondiente a continuación.

## Pistas

<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>

<div class="hint" title="¿Cómo debo graficar las ventas globales totales?">
   Para graficar las ventas globales totales, debes usar el argumento <code>estimator</code>   
   y pasar el valor <code>sum</code>.
</div>

<div class="hint" title="¿Cómo debo agregar las décadas?">
    Para agregar las décadas, podrías usar la función <a href="https://pandas.pydata.org/docs/reference/api/pandas.cut.html"><code>cut</code></a>.
</div>