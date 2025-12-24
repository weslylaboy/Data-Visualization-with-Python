## Tarea

Los investigadores han recibido la figura que creamos para ellos y quedaron muy satisfechos con los resultados. Sin embargo, nos pidieron hacer algunos ajustes a la figura.

En primer lugar, los investigadores nos pidieron limitar la vista del eje `x` al intervalo de `-4` a `4`, y la vista del eje `y` al intervalo de `-2` a `2`.  
Podemos hacerlo utilizando los métodos [`set_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html) o [`set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html).

También notaron un pequeño pico en nuestros datos y nos pidieron graficar este detalle más de cerca en la misma figura, así que hagámoslo.

Para lograr esto, podemos usar _ejes insertados_. Consulta la página de la [documentación](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html) para entender cómo hacerlo.

Puedes colocar los ejes insertados donde desees y ajustar el tamaño según sea necesario.  
Por ejemplo, puedes colocarlos en las coordenadas `(0.15, 0.7)` y establecer el tamaño en `(0.3, 0.3)`.

Los ejes insertados deben mostrar solo el área de los ejes principales que va de `x = 0.5` a `x = 1.5`, y de `y = 0.6` a `y = 1.1`. Las marcas de las divisiones (ticks) solo deben señalar los límites.

Después de eso, podemos conectar nuestros nuevos ejes con el área relevante de los ejes principales utilizando el método [`indicate_inset_zoom`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset_zoom.html).

Si te atascas, no dudes en usar las pistas a continuación, donde también puedes encontrar cómo debería verse la figura final.

## Personalización adicional

Si lo deseas, puedes personalizar aún más la figura. Aquí tienes algunas ideas para la personalización:

1. Puedes cambiar el color y el estilo del zoom de los ejes insertados.
2. Puedes ajustar el grosor de todas las líneas en la figura para que sean uniformes.
3. Puedes agregar una leyenda y un título.

Te animamos a explorar estas personalizaciones por tu cuenta, ya que no todas serán cubiertas en el curso.

Ten en cuenta que estos cambios no serán evaluados y podrían alterar las pruebas existentes.

## Pistas

<div class="hint" title="¿Cómo debería verse la figura?">
    <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>

<div class="hint" title="¿Cómo limitar la vista de un eje?">
    Para limitar la vista de un eje, puedes usar el método <code>set_xlim</code> o <code>set_ylim</code> del objeto <code>Axes</code>:  
    <code>ax.set_xlim(1, 3)</code>.
</div>

<div class="hint" title="¿Cómo agregar ejes insertados?">
    Para agregar ejes insertados, puedes usar el método <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html"><code>inset_axes</code></a> del objeto <code>Axes</code>:  
    <code>ax.inset_axes([0.1, 0.5, 0.4, 0.4])</code>.
</div>

<div class="hint" title="¿Cómo graficar los datos en los ejes insertados?">
    Para graficar los datos en los ejes insertados, puedes usar los mismos métodos y parámetros que usarías para graficar en un objeto <code>Axes</code> regular, ya que es del mismo tipo de objeto:  
    <code>inset_ax.scatter("x", "y", data=my_data, color="color_name", alpha=0.5)</code>.
</div>

<div class="hint" title="¿Cómo limitar el área de los ejes insertados?">
    Para limitar el área de los ejes insertados, puedes usar el método <code>set_xlim</code> o <code>set_ylim</code> del objeto <code>Axes</code>:  
    <code>inset_ax.set_xlim(1, 3)</code>.<br><br>
    También puedes establecer estos límites al pasar el parámetro <code>xlim</code> o <code>ylim</code> al crear un nuevo eje insertado:  
    <code>ax.inset_ax(..., xlim=[1, 3])</code>.
</div>

<div class="hint" title="¿Cómo configurar las divisiones (ticks) en los ejes insertados?">
    Para configurar las divisiones (ticks) en los ejes insertados, puedes usar el método <code>set_xticks</code> o <code>set_yticks</code> del objeto <code>Axes</code>:  
    <code>inset_ax.set_xticks([1, 2, 3])</code>.<br><br>
    También puedes configurar estas divisiones al pasar el parámetro <code>xticks</code> o <code>yticks</code> al crear un nuevo eje insertado:  
    <code>ax.inset_ax(..., xticks=[1, 2, 3])</code>.
</div>

<div class="hint" title="¿Cómo conectar los ejes insertados con el área de los ejes principales?">
    Para conectar los ejes insertados con el área de los ejes principales, puedes usar el método <code>indicate_inset_zoom</code> del objeto <code>Axes</code>:  
    <code>ax.indicate_inset_zoom(inset_ax)</code>.
</div>