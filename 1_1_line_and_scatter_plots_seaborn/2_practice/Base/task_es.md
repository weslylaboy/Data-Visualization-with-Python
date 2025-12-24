## Tarea

Durante un experimento, los investigadores registraron la variable `y` del sujeto mientras cambiaban la variable `x`.  
Este fue un estudio confidencial, por lo que no han proporcionado detalles adicionales, pero mencionaron haber encontrado algo inusual en las observaciones.  
Necesitan identificar la tendencia en los datos, así que están buscando ayuda con la visualización de gráficos.  
¡Ayudémosles!

Nuestra figura debe consistir en dos trazos: una línea y un gráfico de dispersión.  
El trazo de línea debe representar una línea de regresión, mientras que el de dispersión debe mostrar los puntos de datos reales.

También debemos hacer varios ajustes visuales:

1. El trazo de línea debe ser de color azul `navy`.
2. El trazo de dispersión debe ser `gris` y casi transparente (`0.05`).

Ten en cuenta que no se requiere preprocesamiento de datos.

Si te quedas atascado,  
no dudes en utilizar las pistas a continuación, las cuales también muestran cómo debería verse la figura final.

## Personalización adicional

Si lo deseas, puedes personalizar aún más la figura. Estas son algunas ideas para la personalización:

1. Puedes cambiar el número de marcas en la figura.
2. Puedes graficar una aproximación más compleja de los datos (usando la columna `approximated_y`).
3. Puedes añadir una leyenda y un título.

Te animamos a explorar cómo realizar estos ajustes por tu cuenta, ya que no todas estas personalizaciones se cubrirán en el curso.

Ten en cuenta que estos cambios no serán evaluados y podrían romper pruebas existentes.

## Pistas

<div class="hint" title="¿Cómo debería verse la figura?">
    <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>

<div class="hint" title="¿Qué función deberíamos usar?">
   Dado que necesitamos graficar tanto un gráfico de dispersión como una línea de regresión, la mejor opción es usar <code>sns.lmplot</code>.
   
   Para personalizar la apariencia de la línea y el gráfico de dispersión dentro de la figura, puedes utilizar los parámetros <code>line_kws</code> y <code>scatter_kws</code>.
</div>

<div class="hint" title="¿Cómo colorear el trazo?">
    Para colorear la línea o el gráfico de dispersión, puedes usar el argumento <code>color</code>:  
    <code>sns.relplot(x="x", y="y", data=my_data, color="color_name")</code>.
</div>

<div class="hint" title="¿Cómo hacer transparente el trazo?">
    Para hacer transparente la línea o el gráfico de dispersión, puedes usar el argumento <code>alpha</code>:  
    <code>sns.relplot(x="x", y="y", data=my_data, alpha=0.5)</code>
</div>