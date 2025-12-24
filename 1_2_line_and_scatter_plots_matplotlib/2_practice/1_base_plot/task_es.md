## Tarea

Durante un experimento, los investigadores registraron la variable `y` del sujeto mientras cambiaban la variable `x`.  
Este fue un estudio confidencial, por lo que no han proporcionado más detalles, pero mencionaron haber encontrado algo inusual en las observaciones.  
Los investigadores aproximaron los datos (`approximated_y`) y ahora buscan ayuda para graficarlos y observar este comportamiento inesperado en una figura.  
¡Vamos a ayudarlos!

Nuestra figura debe consistir en dos trazas: una traza de línea y una traza de dispersión.  
La traza de línea debe graficar los datos aproximados, mientras que la traza de dispersión debe graficar los datos reales.

Debemos realizar varios ajustes visuales en la figura:  
1. La traza de línea debe ser de color `navy`.  
2. La traza de dispersión debe ser de color `grey` y casi transparente (`0.05`).  
3. Eliminar los bordes superior y derecho.

También debemos realizar algunas modificaciones en el eje x:  
1. El eje x debe tener únicamente tres marcas: `-4`, `0`, y `4`.  
2. Etiquetar el eje x como `x`.

Y realizar cambios similares en el eje y:  
1. El eje y debe tener únicamente tres marcas: `-1.5`, `0`, y `1.5`.  
2. Etiquetar el eje y como `y`.

Ten en cuenta que no necesitas preprocesar los datos.

Si te quedas atascado,  
no dudes en usar las pistas a continuación, donde también puedes encontrar cómo debería verse la figura final.

## Pistas

<div class="hint" title="¿Cómo debería verse la figura?">  
    <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">  
</div>

<div class="hint" title="¿Cómo darle color a la traza?">  
    Para darle color a la traza de línea o de dispersión, puedes usar el argumento <code>color</code>:  
    <code>ax.line("x", "y", data=my_data, color="nombre_del_color")</code>.  
</div>

<div class="hint" title="¿Cómo hacer que la traza sea transparente?">  
    Para hacer transparente la traza de línea o de dispersión, puedes usar el argumento <code>alpha</code>:  
    <code>ax.scatter("x", "y", data=my_data, alpha=0.5)</code>.  
</div>

<div class="hint" title="¿Cómo establecer las marcas de los ejes?">  
    Para establecer las marcas, puedes usar los métodos <code>set_xticks</code> o <code>set_yticks</code> del objeto <code>Axes</code>:  
    <code>ax.set_xticks([1, 2, 3])</code>.  
</div>

<div class="hint" title="¿Cómo asignar una etiqueta a un eje?">  
    Para asignar una etiqueta a un eje, puedes usar los métodos <code>set_xlabel</code> o <code>set_ylabel</code> del objeto <code>Axes</code>:  
    <code>ax.set_xlabel("x")</code>.  
</div>

<div class="hint" title="¿Cómo eliminar bordes?">  
    Para eliminar un borde, puedes usar el método <code>set_visible</code> del objeto <code>Spine</code>:  
    <code>ax.spines["bottom"].set_visible(False)</code>.  
</div>