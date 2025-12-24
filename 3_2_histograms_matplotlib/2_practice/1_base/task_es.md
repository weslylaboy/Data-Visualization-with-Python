## Tarea

Una empresa de bebidas ha estado operando exitosamente en Belgrado, vendiendo una variedad de bebidas durante todo el año. Ahora, han decidido expandir su negocio a Ereván y quieren comparar sus ventas establecidas en Belgrado con los primeros seis meses de ventas en Ereván para evaluar las diferencias del mercado y optimizar su estrategia.

Debido a que los dos mercados difieren en tamaño, estacionalidad y preferencias de los clientes, la empresa desea observar si los patrones de ventas de Ereván, a pesar del periodo de observación más corto, se asemejan a los de Belgrado. Si ambos siguen una distribución similar, esto podría sugerir que los factores que influyen en las ventas son consistentes entre las dos ciudades. Por el contrario, distribuciones distintas podrían indicar influencias locales únicas que afectan las ventas.  

Para revelar estas tendencias generales, la empresa nos ha solicitado crear un único gráfico con dos histogramas superpuestos.  

Requisitos de visualización:

1. El histograma debe ser un gráfico de línea sin rellenar.
2. El histograma debe estar normalizado (las barras deben sumar `1`).
3. Ambos histogramas deben tener barras comunes, que vayan desde el múltiplo de cien más bajo redondeado hacia abajo hasta el múltiplo de cien más alto redondeado hacia arriba entre ambas ciudades, con un paso de `100`.
4. Los datos de Ereván deben estar coloreados en `crimson`, y los datos de Belgrado en `black`.
5. La etiqueta del eje x debe ser `'Ventas'`.
6. La etiqueta del eje y debe ser `'Probabilidad'`.
7. Agregar un título: `'Distribución de Ventas en Belgrado y Ereván'`.
8. Añadir una leyenda con los nombres de las ciudades.

Ten en cuenta que aquí no es necesario preprocesar los datos.

Puedes usar las siguientes funciones ocultas:

1. `get_city_sales`: Recupera los datos de ventas para una ciudad específica. Pasa el conjunto de datos y el nombre de la ciudad como argumentos.
2. `get_weights`: Recupera los pesos para una ciudad específica.
3. `get_bins`: Recupera los bordes de las barras para el gráfico (comunes para ambas ciudades). ¡Pasa el conjunto de datos completo como argumento!

Si te quedas atascado, no dudes en usar las pistas a continuación, donde también puedes encontrar un ejemplo de cómo debería verse el gráfico final.

## Pistas

<div class="hint" title="¿Cómo debería lucir el gráfico?">
    <img src="example.png" alt="Cómo debería lucir el gráfico" style="max-height: 500px">
</div>

<div class="hint" title="¿Cómo graficar dos histogramas en la misma figura?">
    Para graficar dos histogramas en la misma figura, llama al método <code>hist</code> por separado para cada ciudad, asegurándote de que ambos gráficos compartan el mismo objeto <code>ax</code>.
</div>

<div class="hint" title="¿Cómo normalizar el histograma?">
   Para normalizar el histograma, establece el parámetro <code>weights</code> del método <code>hist</code> en 
   \(\frac{1}{n}\) para cada ciudad, donde <code>n</code> es el número de observaciones en esa ciudad.
</div>

<div class="hint" title="¿Cómo hacer que el histograma sea un gráfico de línea sin rellenar?">
   Usa <code>histtype='step'</code> en el método <code>hist</code>. Esto creará una versión del histograma sólo de contorno, sin relleno.
</div>

<div class="hint" title="¿Cómo configurar colores para el histograma?">
   Si usas <code>histtype='step'</code>, el parámetro <code>color</code> establece el color de línea.
</div>

<div class="hint" title="¿Cómo cambiar el número de barras?">
   Para cambiar el número de barras, especifica el parámetro <code>bins</code> en el método <code>hist</code>.
</div>

<div class="hint" title="¿Cómo añadir etiquetas de ejes?">
   Puedes pasar la etiqueta deseada a los métodos 
   <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel">
   <code>set_xlabel</code></a> y 
   <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel">
   <code>set_ylabel</code></a>: <code>ax.set_xlabel('x')</code> y <code>ax.set_ylabel('y')</code>.
</div>

<div class="hint" title="¿Cómo establecer un título?">
    Pasa el título deseado del gráfico al método <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html">
    <code>set_title</code></a>: <code>ax.set_title("title")</code>.
</div>

<div class="hint" title="¿Cómo añadir una leyenda?">
    Primero, especifica el parámetro <code>label</code> en el método <code>hist</code> para cada ciudad.
    Luego, llama al método <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html">
    <code>ax.legend</code></a>.
</div>