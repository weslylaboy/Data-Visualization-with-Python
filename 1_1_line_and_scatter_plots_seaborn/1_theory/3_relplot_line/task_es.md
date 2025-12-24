## Teoría

Esta visualización es mucho mejor, ya que ahora podemos identificar el gran grupo denso en nuestro conjunto de datos.  
Además, podemos observar una posible relación lineal entre los dos puntajes.  
Para explorar esto más a fondo, intentemos una aproximación lineal de los datos.  

Como se mencionó anteriormente, `relplot` puede construir no solo gráficos de dispersión, sino también gráficos de líneas.  
Para especificar el tipo de gráfico, podemos usar el parámetro `kind`,  
el cual acepta una de las siguientes cadenas: `scatter` para gráficos de dispersión y `line` para gráficos de líneas.  
En los pasos anteriores, no era necesario establecer explícitamente este parámetro en `scatter`  
porque ese es su valor predeterminado.  

## Tarea

Haz que `relplot` construya un gráfico de líneas. Ten en cuenta que no necesitas ajustar la transparencia ni cambiar el color para este gráfico.

## Pistas
<div class="hint" title="¿Cómo debería verse la figura?">
  <img src="example.png" alt="¿Cómo debería verse la figura?" style="max-height: 500px">
</div>