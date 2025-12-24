## Teoría

Nuestro histograma ahora luce mejor, pero aún hay algunos ajustes que podemos realizar.

1. Asegúrate de que ambos conjuntos de datos tengan los mismos intervals (bins) – Esto permite una comparación más precisa.
2. Mejora la claridad visual ajustando el parámetro `histtype` en el método `hist`.
3. Añade etiquetas a los ejes, una leyenda y un título al gráfico.

Por defecto, `histtype` está configurado como `bar`, lo que rellena las barras con color. Sin embargo, podemos cambiarlo a `step`, lo que dibuja una línea que conecta los puntos superiores de las barras sin rellenar el área. Esto crea una distribución más limpia y visualmente atractiva.

## Tarea

Modifica el histograma de la siguiente manera:

1. Configura `histtype` como `step` para crear un histograma basado en líneas, sin relleno.
2. Genera la misma colección de intervals (bins) para ambas distribuciones. Deberían ser `10` intervals uniformes, comenzando desde el valor mínimo de ventas globales (a través de ambos publicadores) y terminando en el valor máximo.
3. Nombra el eje x como `Global Sales (millones)` y el eje y como `Proporción`.
4. Añade un título al gráfico: `Distribución de Ventas Globales para Electronic Arts y Ubisoft`.
5. Añade una leyenda al gráfico, con etiquetas correspondientes a los publicadores.

Puedes añadir una leyenda para un histograma de la misma forma que para un gráfico de barras. Lo describimos en detalle en la sección "[Leyenda](course://2_2_bar_and_pie_charts_matplotlib/1_theory/10_grouped_bar_chart_legend)". Consulta la pista correspondiente a continuación para más información.

Usa la función oculta `get_bins` para generar la colección de intervals. ¡Pasa el dataset no filtrado como argumento! Si lo prefieres, puedes encontrar esos valores manualmente. Por favor, consulta la pista correspondiente a continuación.

## Pistas

<div class="hint" title="¿Cómo añadir una leyenda con etiquetas al gráfico?">
    Primero, pasa el parámetro <code>label</code> al método <code>hist</code> para cada conjunto de datos. 
    Luego, llama al método <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html">
    <code>ax.legend()</code></a> para mostrar la leyenda.
</div>

<div class="hint" title="¿Cómo puedo generar la colección de intervals para ambas distribuciones?">
    Extrae los valores mínimo y máximo de la columna <code>global_sales</code> del dataset filtrado usando las funciones 
    <a href="https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min"><code>min</code></a> y 
    <a href="https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max"><code>max</code></a>.
    Recuerda que necesitas encontrar estos valores en ambos publicadores. 
    Luego, usa la función <a href="https://numpy.org/doc/stable/reference/generated/numpy.linspace.html">
    <code>np.linspace</code></a> para generar una colección de <code>10</code> intervals uniformes. Similar a 
    <code>np.logspace</code>, acepta 3 parámetros principales: <code>start</code>, <code>stop</code> y <code>num</code>.
</div>

<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>