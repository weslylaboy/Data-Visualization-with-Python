## Tarea

A los organizadores les gustó nuestra figura pero nos solicitaron hacerla más legible.  
Específicamente, no les gusta que sea difícil encontrar el valor exacto de cada producto  
y que los elementos de la leyenda estén en orden inverso.  
¡Vamos a solucionar estos problemas!

Primero, añadamos marcas menores al eje x inferior y dupliquemos todas las marcas en el eje superior:  
1. Para añadir marcas menores, puedes usar  
   el conocido método [`set_xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html).  
   Distribuye estas marcas desde `0` hasta `100` con un paso de `5`.  
2. Para duplicar las marcas inferiores en el eje superior, puedes usar  
   el método [`tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html).

En segundo lugar, añadamos un valor textual a cada producto.  
Puedes usar el método [`text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html) para hacerlo.  
Posiciona el texto a la derecha de la parte superior de cada barra  
(la coordenada `x` debe ser `1` más que el número de participantes, y `y` debe coincidir con la posición de la barra).  
Redondea cada valor a un dígito después del punto decimal.

Y la última cosa: para reorganizar los elementos de la leyenda, podemos usar  
el método [`get_legend_handles_labels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_legend_handles_labels.html)  
junto con el método [`legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html).  

Consulta las páginas de documentación correspondientes para entender cómo hacerlo.

Si te quedas atascado,  
no dudes en usar las pistas a continuación, donde también puedes encontrar cómo debería verse la figura final.  

## Personalización adicional

Si lo deseas, puedes personalizar aún más la figura. Aquí tienes algunas ideas para la personalización:

1. Cambiar el peso y el tamaño de las fuentes.  
2. Mover los elementos de la leyenda al eje y.  
3. Graficar categorías en diferentes ejes dentro de la misma figura.

Te animamos a explorar estas personalizaciones por tu cuenta, ya que no todas se cubrirán en este curso.

Ten en cuenta que estos cambios no serán evaluados y podrían romper pruebas existentes.  

## Pistas

<div class="hint" title="¿Cómo debería verse la figura?">
    <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>

<div class="hint" title="¿Cómo añadir marcas menores?">
    Para añadir marcas menores, puedes usar el método <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html"><code>set_xticks</code></a> con el argumento <code>minor</code>:  
    <code>ax.set_xticks([1, 2, 3], minor=True)</code>.
</div>

<div class="hint" title="¿Cómo añadir marcas al borde superior?">
    Para añadir marcas al borde superior, puedes usar el método <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html"><code>tick_params</code></a>:  
    <code>ax.tick_params(top=True, labeltop=True, axis="x", which="both")</code>.
</div>

<div class="hint" title="¿Cómo añadir un valor textual para cada producto?">
    Para añadir un valor textual para cada producto, puedes usar el método <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html"><code>text</code></a>  
    junto con la función <code>round</code> para formatear los valores:  
    <code>ax.text(value + 1, bar_y_position, f"{round(value, 1)}", verticalalignment="center")</code>.<br><br>
    Ten en cuenta que usamos el argumento <code>verticalalignment</code> aquí para alinear correctamente el texto.
</div>

<div class="hint" title="¿Cómo reorganizar los elementos de la leyenda?">
    Para obtener una lista de los objetos y etiquetas de la leyenda, puedes usar el método <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_legend_handles_labels.html"><code>get_legend_handles_labels</code></a>:  
    <code>handles, labels = ax.get_legend_handles_labels()</code>.<br><br>
    Después de eso, podemos pasar los valores invertidos al método <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html"><code>legend</code></a>:  
    <code>ax.legend(reversed(handles), reversed(labels))</code>
</div>