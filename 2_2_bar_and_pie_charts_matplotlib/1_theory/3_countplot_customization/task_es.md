## Teoría

Ahora la figura luce bien, pero aún hay margen para mejorar.

Primero, hay muchas plataformas de videojuegos y muchas de ellas están desactualizadas.
Centrémonos únicamente en plataformas modernas como `WiiU`, `PS4`, `XOne` y `PC`.

En segundo lugar, cada una de estas plataformas tiene su propio color de marca, 
por lo que sería conveniente colorear cada barra en consecuencia.
Para cambiar el color de las barras, podemos usar el argumento `color`. Este acepta:
1. Un solo color: En este caso, todas las barras tendrán el mismo color.
2. Una colección de colores: En este caso, los colores se aplicarán a las barras correspondientes.  
   No obstante, ten en cuenta que, dado que nuestro gráfico de barras es horizontal, los colores se aplicarán de abajo hacia arriba.

El formato para definir colores se explica en detalle en la lección 
"[Gráficos de líneas y dispersión](course://1_2_line_and_scatter_plots_matplotlib/1_theory/2_transparency_and_color)".

Por último, sería ideal agregar etiquetas a los ejes y a la figura misma.

## Tarea

1. Usa la función oculta `filter_platforms` para incluir únicamente `WiiU`, `PS4`, `XOne` y `PC` en los datos.

   Si prefieres, puedes realizar el filtrado tú mismo. Por favor, consulta la pista correspondiente a continuación.

2. Colorea las barras de la siguiente manera: `WiiU` con `cyan`, `PS4` con `blue`, `XOne` con `green` y `PC` con `grey`.
3. Configura la etiqueta del eje x como `Count`.
4. Configura la etiqueta del eje y como `Platform`.
5. Asigna el título de la figura como `Número de juegos por plataforma`.

## Pistas

<div class="hint" title="¿Cómo debo filtrar las plataformas?">
    Para filtrar las plataformas innecesarias, puedes utilizar
    el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html"><code>isin</code></a>
    en la columna <code>platform</code>.

   Ten en cuenta que tu función personalizada no será evaluada.
</div>

<div class="hint" title="¿Cómo configurar una etiqueta para un eje?">
    Para configurar la etiqueta de un eje,
    puedes usar el método <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html"><code>set_xlabel</code></a>
    o <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html"><code>set_ylabel</code></a>:
    <code>ax.set_xlabel("x")</code>.
</div>

<div class="hint" title="¿Cómo configurar un título para una figura?">
    Para configurar un título de figura, puedes usar el método <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html"><code>set_title</code></a>:
    <code>ax.set_title("Título")</code>.
</div>

<div class="hint" title="¿Cómo debería lucir la figura?">
   <img src="example.png" alt="Cómo debería lucir la figura" style="max-height: 500px">
</div>