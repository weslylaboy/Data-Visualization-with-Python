## Teoría

Ahora podemos distinguir las trazas, pero faltan las etiquetas de las décadas.  
Para añadirlas, podemos usar el conocido método [`ax.set_xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html).

Anteriormente, solo pasábamos las posiciones donde debían colocarse las marcas. Sin embargo,  
también podemos pasar un segundo argumento a este método: las etiquetas para estas marcas.  
Estas etiquetas reemplazarán las numéricas.

Así que volvamos a nuestro ejemplo.  
Necesitamos colocar las etiquetas en el centro de cada grupo.  
Como podemos ver en la imagen, el centro del primer grupo está ubicado en `1.5`.  
No es difícil calcular los otros centros, ya que están igualmente espaciados a una distancia de `group_size + 1`.  
<img src="../../../common/resources/images/bar_and_pie_charts/grouped_bar_chart_5.png" alt="Cómo debería verse la figura" style="max-height: 500px">

Además, añadiremos etiquetas para los ejes x e y, un título y ajustaremos el diseño.

## Tarea

1. Añade etiquetas de las décadas a la figura.  

   Puedes usar la función oculta `get_all_decades` para obtener todas las décadas.  
   Si lo prefieres, también puedes hacerlo por ti mismo. Consulta las pistas correspondientes a continuación.

2. Establece la etiqueta del eje x como `Década`.
3. Establece la etiqueta del eje y como `Ventas`.
4. Establece el título como `Ventas totales por cada región a lo largo de las décadas`.
5. Ajusta el diseño.

## Pistas

<div class="hint" title="¿Cómo establecer una etiqueta para un eje?">
    Para establecer una etiqueta para un eje,  
    puedes usar el método <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html"><code>set_xlabel</code></a>  
    o <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html"><code>set_ylabel</code></a>:  
    <code>ax.set_xlabel("x")</code>.
</div>

<div class="hint" title="¿Cómo establecer un título para una figura?">
    Para establecer un título para una figura, puedes usar el método <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html"><code>set_title</code></a>:  
    <code>ax.set_title("Título")</code>.
</div>

<div class="hint" title="¿Cómo ajustar el diseño?">
   Para ajustar el diseño, puedes usar el método <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html"><code>tight_layout</code></a>:  
   <code>fig.tight_layout()</code>.
</div>

<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>