## Teoría

Aquí podemos ver que tenemos muchas plataformas en el conjunto de datos, lo que hace que la figura sea difícil de interpretar debido a la superposición de etiquetas en el eje x. 
Podemos abordar este problema reduciendo el número de grupos o ajustando el diseño de la figura, reubicando las etiquetas del eje x al eje y.

Seaborn facilita el cambio de diseño: solo necesitamos intercambiar `x` y `y`. 
Sin embargo, para un gráfico de conteo, necesitamos reemplazar `x` con `y` (o viceversa), ya que este tipo de gráfico solo acepta un eje a la vez.

## Tarea

Ajusta el diseño de la figura reemplazando el eje x con el eje y.

## Pistas

<div class="hint" title="¿Cómo debería verse la figura?">
   Ten en cuenta que tu figura puede verse ligeramente diferente debido a la forma en que Seaborn calcula las barras de error.

   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>