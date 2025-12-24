## Teoría

Ahora que tenemos menos categorías, puede ser más conveniente representar los mismos datos como un gráfico de pastel.  
Esto se debe a que las proporciones son más relevantes para nosotros que los valores absolutos.

Para realizar un gráfico de pastel utilizando Matplotlib, podemos usar  
el método [`pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie).  
Este acepta tres argumentos principales:
* `x` — Una colección de tamaños de los sectores.
* `labels` — Una colección de etiquetas para cada sector (debe pasarse como un argumento clave).
* `data` — La estructura de datos de entrada.

Tenga en cuenta que no es necesario normalizar los valores proporcionados,  
ya que Matplotlib dividirá automáticamente cada elemento de `x` por `sum(x)`.

## Tarea

1. Reemplace la llamada al método `barh` con el método `pie`.  
2. Pase `count` como los tamaños de los sectores, `platform` como las etiquetas y `games` como los datos.

Tenga en cuenta que no es necesario personalizar la figura en esta etapa.

## Pistas

<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>