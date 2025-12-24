## Tarea

En un reciente evento de degustación, se invitó a los participantes a probar una variedad de panes, quesos y ensaladas.  
Todos tuvieron la oportunidad de votar por hasta tres productos por categoría, compartiendo sus favoritos entre las diversas opciones disponibles.  
Los organizadores del evento han recopilado todas las respuestas y ahora necesitan nuestra ayuda para graficar los datos.  
¡Vamos a ayudarlos!

Para interpretar los datos,  
los organizadores quieren ver la distribución de votos para cada categoría (`category`) en un único gráfico de barras horizontal.  
Debes graficar las categorías de arriba hacia abajo en el mismo orden en que aparecen en los datos: `bread`, `cheese` y `salad`.

Los demás requisitos son:

1. El gráfico de barras debe ser horizontal.  
2. Las barras deben agruparse por categoría.  
3. Los nombres de los productos dentro de cada categoría deben estar ordenados alfabéticamente (de arriba hacia abajo).  
4. El gráfico de barras debe incluir una leyenda.  

Ten en cuenta que no es necesario preprocesar los datos.

Puedes utilizar la función oculta `get_product_order` para obtener el orden correcto de los productos si es necesario.

Si te quedas atascado, no dudes en usar las pistas a continuación, donde también puedes encontrar un ejemplo de cómo debería lucir la figura final.

## Personalización adicional

Si lo deseas, puedes personalizar aún más la figura. Aquí tienes algunas ideas de personalización:

1. Ajustar los pesos y tamaños de las fuentes.  
2. Mover los elementos de la leyenda al eje `y`.  
3. Añadir un valor numérico correspondiente en la parte superior de cada barra.  

Te animamos a explorar estas personalizaciones por tu cuenta, ya que no todas se cubrirán en el curso.

Ten en cuenta que estos cambios no se probarán y podrían causar que las pruebas existentes fallen.

## Pistas

<div class="hint" title="¿Cómo debería lucir la figura?">
    <img src="example.png" alt="Cómo debería lucir la figura" style="max-height: 500px">
</div>

<div class="hint" title="¿Qué tipo de gráfico de barras debo usar?">
    Como necesitamos graficar la distribución de votos, la mejor opción es usar un <a href="https://seaborn.pydata.org/generated/seaborn.catplot.html">gráfico de conteo</a>:  
    <code>sns.catplot(..., kind="count")</code>
</div>

<div class="hint" title="¿Cómo hacer que la barra sea horizontal?">
    Para que una barra sea horizontal, puedes cambiar el argumento <code>x</code> por <code>y</code>.
</div>

<div class="hint" title="¿Cómo agrupar las barras por categoría y añadir una leyenda?">
    Para agrupar las barras por categoría y añadir una leyenda, puedes usar el argumento <code>hue</code>.
</div>

<div class="hint" title="¿Cómo cambiar el orden de los productos?">
    Para cambiar el orden, podrías usar el argumento <code>order</code>.
</div>