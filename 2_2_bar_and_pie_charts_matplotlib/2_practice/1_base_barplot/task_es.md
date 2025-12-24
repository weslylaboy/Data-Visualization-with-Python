## Tarea

En un reciente evento de degustación, se invitó a los participantes a probar una variedad de panes, quesos y ensaladas.  
Todos tuvieron la oportunidad de votar por hasta 3 productos por categoría, compartiendo sus favoritos de las diversas opciones.  
Los organizadores recopilaron todas las respuestas y calcularon el porcentaje de votos para cada producto dentro de cada categoría  
(para entender la distribución entre pan, queso y ensalada). Ahora quieren que les ayudemos a graficar los datos.  
¡Vamos a ayudarlos!

Para interpretar los datos,  
los organizadores quieren ver la distribución de votos (`votes`) para cada categoría (`category`) en un único gráfico de barras horizontal.  
Deberás graficar las categorías de arriba hacia abajo en el mismo orden en que aparecen en los datos  
y colorearlas de la siguiente manera:  
`bread` - `sienna`, `cheese` - `goldenrod`, `salad` - `forestgreen`.

Requisitos para el eje Y:

1. Cada barra debe tener el nombre del producto correspondiente en el lado izquierdo (es decir, `cheddar`).  
2. Establece la etiqueta del eje Y como `Nombre del producto`.  
3. Los nombres de los productos dentro de cada categoría deben ordenarse alfabéticamente (de arriba hacia abajo).  

Requisitos para el eje X:

1. El eje X solo debe tener estas marcas: `0`, `25`, `50`, `75` y `100`.  
2. Establece la etiqueta del eje X como `Respuestas, %`.  

Además, realiza algunos ajustes visuales en la figura:  

1. Establece el título del gráfico como `Distribución de votos por categoría`.  
2. Agrega una leyenda.  
3. Ajusta el diseño (tighten layout).  

Ten en cuenta que ya hemos preprocesado los datos para ti. Para aprender cómo lo hicimos, consulta la pista correspondiente a continuación.

Puedes usar las siguientes funciones ocultas:

1. `get_category_product_names`: Recupera todos los nombres de los productos de una categoría específica en orden alfabético (de arriba hacia abajo).  
2. `get_category_votes`: Recupera todos los votos de una categoría específica en el mismo orden que los nombres de los productos.  
3. `get_category_size`: Calcula la cantidad de productos en una categoría específica.  
4. `get_categories`: Recupera una lista de todas las categorías en el orden en que aparecen en los datos.  

Si te quedas atascado, no dudes en usar las pistas a continuación, donde también puedes ver cómo debería lucir la figura final.

## Pistas

<div class="hint" title="¿Cómo debería lucir la figura?">  
    <img src="example.png" alt="Cómo debería lucir la figura" style="max-height: 500px">  
</div>  

<div class="hint" title="¿Cómo debo preprocesar los datos?">  
   Antes de usar los datos, debemos realizar varios pasos de preprocesamiento:  
   <ol>  
      <li>Calcula el número de votos para cada categoría y producto usando  
      los métodos <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html"><code>groupby</code></a>  
      y <a href="https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.count.html"><code>count</code></a>.</li>  
      <li>Normaliza los datos dividiéndolos por el número de participantes y luego multiplícalos por 100 para obtener el porcentaje.  
      Podemos encontrar el número de participantes usando el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nunique.html"><code>nunique</code></a>.</li>  
      <li>Cambia el nombre de la columna <code>participants</code> a <code>votes</code> usando  
      el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html"><code>rename</code></a>.</li>  
      <li>Reinicia el índice usando el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html"><code>reset_index</code></a>.</li>  
   </ol>  
</div>  

<div class="hint" title="¿Cómo establecer los colores de las barras?">  
    Para establecer los colores de las barras, puedes usar el argumento <code>color</code> del método  
    <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html"><code>barh</code></a>:  
    <code>ax.barh(positions, values, color="red")</code>  
</div>  

<div class="hint" title="¿Cómo establecer las etiquetas de los productos?">  
    Para establecer las etiquetas de los productos, puedes usar el método  
    <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html"><code>set_yticks()</code></a>:  
    <code>ax.set_yticks([1, 2, 3], ["pepino", "zanahoria", "tomate"])</code>  
</div>  

<div class="hint" title="¿Cómo limitar el eje X?">  
    Para limitar la vista del eje X, puedes usar el método  
    <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html"><code>set_xlim</code></a>:  
    <code>ax.set_xlim(1, 3)</code>.  
</div>  

<div class="hint" title="¿Cómo establecer las marcas del eje X?">  
    Para establecer las marcas del eje X, puedes usar el método  
    <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html"><code>set_xticks</code></a>:  
    <code>ax.set_xticks([1, 2, 3])</code>.  
</div>  

<div class="hint" title="¿Cómo establecer una etiqueta para un eje?">  
    Para establecer una etiqueta para un eje,  
    puedes usar el método <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html"><code>set_xlabel</code></a>  
    o <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html"><code>set_ylabel</code></a>:  
    <code>ax.set_xlabel("x")</code>.  
</div>  

<div class="hint" title="¿Cómo establecer el título de la figura?">  
    Para establecer el título de la figura, puedes usar el método  
    <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html"><code>set_title</code></a>:  
    <code>ax.set_title("Título")</code>.  
</div>  

<div class="hint" title="¿Cómo agregar una leyenda?">  
    Para agregar una leyenda, debes llamar al método  
    <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html"><code>ax.legend</code></a>.  
</div>  

<div class="hint" title="¿Cómo ajustar el diseño?">  
    Para ajustar el diseño, debes llamar al método  
    <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html"><code>fig.tight_layout</code></a>.  
</div>