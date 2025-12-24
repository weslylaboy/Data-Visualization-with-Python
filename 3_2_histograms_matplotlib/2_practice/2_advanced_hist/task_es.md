## Tarea

La empresa apreció nuestra visualización inicial del histograma, pero ahora quiere obtener información más profunda sobre sus datos de ventas. Aunque los histogramas superpuestos ofrecen una buena visión general de las distribuciones, están particularmente interesados en observar cómo se posicionan los datos individuales de ventas e identificar el valor mediano de ventas para cada ciudad.

Para lograr esto, mejoraremos nuestra visualización con dos ajustes principales:

Primero, añadiremos un diagrama de dispersión unidimensional encima del ya existente:

1. Crea dos objetos `ax` utilizando la función [
   `plt.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html) en lugar de uno solo. Establece `height_ratios` en `[1, 10]`.
2. Traza los puntos de datos en el objeto `ax` correspondiente. Dado que es un gráfico unidimensional, la coordenada `y` será la misma para todos los puntos de la misma ciudad: define la coordenada `y`
   para la distribución de ventas de Belgrado como `0.2`, y como `0.1` para la distribución de Ereván.
3. Los datos de Ereván deben estar coloreados en `crimson` y los de Belgrado en `black`.
4. Establece el parámetro `alpha` en `0.05`.
5. Limita el rango del eje `y` de `0` a `0.3`.
6. Elimina tanto las marcas (`ticks`) del eje `x` como las del eje `y`.
7. Oculta todas las bordes (spines) de este gráfico.

En segundo lugar, cambiaremos el eje principal del histograma. Añadiremos líneas verticales con etiquetas de texto que indiquen el valor mediano de ventas para cada ciudad:

1. Usa los mismos colores que en el diagrama de dispersión para cada ciudad.
2. Dibuja una línea vertical en cada mediana utilizando el método [
   `axvline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html) en los ejes correspondientes.
3. Haz que las líneas sean discontinuas, establece su ancho en `1.5` y asigna el color que corresponda al histograma de cada ciudad.
4. Usa el método [
   `text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html) para añadir los valores de la mediana cerca de las líneas:
    - Para las ventas de Belgrado: establece `x` en el valor mediano de ventas _más_ `25`, `y` en `0.005`, y la alineación horizontal en `left`.
    - Para las ventas de Ereván: establece `x` en el valor mediano de ventas _menos_ `25`, `y` en `0.005`, y la alineación horizontal en `right`.
5. No incluyas las medianas en la leyenda.
6. Elimina el título de los ejes y, en su lugar, añade un supertítulo a la figura utilizando el método [
   `fig.suptitle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle).

Por favor consulta las páginas de documentación correspondientes para descubrir cómo hacerlo.

Puedes usar la función oculta `get_median`, que acepta las ventas de la ciudad para calcular la mediana de las ventas de cada ciudad.

Si tienes dificultades,
no dudes en utilizar las pistas a continuación, donde también encontrarás una vista previa de la figura final.

## Personalización adicional

Si lo deseas, puedes personalizar aún más la figura. Aquí tienes algunas ideas para personalización:

1. Cambia el grosor de la fuente y los tamaños.
2. Añade marcas menores al eje `x` de los histogramas.
3. Añade un poco de dispersión (jitter) al eje `y` del diagrama de dispersión.

Te animamos a explorar estas personalizaciones por tu cuenta, ya que no todas serán cubiertas en este curso.

Ten en cuenta que estos cambios no serán evaluados y podrían romper pruebas existentes.

## Pistas

<div class="hint" title="¿Cómo debería lucir la figura?">
    <img src="example.png" alt="Cómo debería lucir la figura" style="max-height: 500px">
</div>

<div class="hint" title="¿Cómo crear dos ejes y establecer proporciones de altura?">
    Puedes usar la función 
    <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html"><code>plt.subplots</code></a>
    y especificar el parámetro <code>height_ratios</code>:
    <code>fig, (ax1, ax2) = plt.subplots(2, 1, height_ratios=[1, 10])</code>.
</div>

<div class="hint" title="¿Cómo trazar un diagrama de dispersión?">
    Puedes usar el método 
    <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter">
    <code>scatter</code></a> en el objeto <code>ax</code> correspondiente:
    <code>ax.scatter(x, y)</code>.
</div>

<div class="hint" title="¿Cómo generar coordenadas y para el diagrama de dispersión?">
    Puedes usar operaciones con listas de Python para hacer una lista de valores constantes: <code>[1] * 10</code> creará una lista de 
    <code>10</code> unos. También puedes usar la función <code>len</code> para obtener la longitud de los datos de ventas: <code>len(sales)</code>.
</div>

<div class="hint" title="¿Cómo limitar la vista del eje y?">
    Puedes usar el método 
    <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html"><code>set_ylim()</code></a>
    del objeto <code>ax</code>:
    <code>ax.set_ylim(1, 3)</code>.
</div>

<div class="hint" title="¿Cómo eliminar las marcas?">
    Puedes eliminar las marcas de los ejes <code>x</code> y <code>y</code> llamando a los métodos 
    <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html"><code>set_yticks</code>
    </a> y <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html"><code>
    set_xticks</code></a> de los ejes: <code>ax.set_yticks([])</code> y <code>ax.set_xticks([])</code>.
</div>

<div class="hint" title="¿Cómo ocultar todas las bordes de un gráfico?">
    Puedes llamar a <code>ax.spines[["top", "bottom", "left", "right"]].set_visible(False)</code> en el objeto <code>ax</code> correspondiente.
</div>

<div class="hint" title="¿Cómo encontrar la mediana de un arreglo?">
    Puedes usar el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.median.html"><code>median</code></a> 
    de una Serie.
</div>

<div class="hint" title="¿Cómo personalizar una línea vertical?">
    Puedes cambiar la apariencia de la línea con el método <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html"><code>axvline</code></a> configurando los tres parámetros siguientes: usa
    <code>linestyle</code> para definir el estilo de la línea, <code>width</code> para configurar su grosor y <code>color</code> 
    para asignar su color.
</div>

<div class="hint" title="¿Cómo excluir ciertos elementos de la leyenda?">
    Puedes recuperar los manejadores y etiquetas de la leyenda llamando al método 
    <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_legend_handles_labels.html">
    <code>get_legend_handles_labels</code></a> en los ejes correspondientes. 
    Luego, para excluir ciertos elementos de la leyenda, puedes pasar las listas filtradas de manejadores y etiquetas al método <code>legend</code>:
    <code>ax.legend(handles_filtered, labels_filtered)</code>.
</div>

<div class="hint" title="¿Cómo añadir un super título a la figura?">
    Puedes llamar al método
    <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle">
    <code>suptitle</code></a> en el objeto figura:
    <code>fig.suptitle("Título")</code>.
</div>