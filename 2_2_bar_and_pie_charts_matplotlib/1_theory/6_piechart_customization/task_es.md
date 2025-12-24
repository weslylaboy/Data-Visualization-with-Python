## Teoría

Ahora, la figura se ve bien, pero todavía hay margen para mejorar.

Primero, vamos a colorear las porciones usando los colores de la marca, 
tal como hicimos con el gráfico de barras. 
Sin embargo, ten en cuenta que el argumento para especificar colores en un gráfico circular se llama <code>color**s**</code>, ¡no `color`!

Segundo, ahora las porciones lucen demasiado juntas. Para añadir algo de espacio entre ellas, 
podemos usar el argumento `explode`. 
Este acepta una colección de valores flotantes que especifican la fracción del radio por la cual desplazar cada porción.

Finalmente, vamos a añadir un título a nuestra figura y ajustar su diseño.

## Tarea

1. Colorea las porciones de la siguiente manera: `PC` con `grey`, `PS4` con `blue`, `XOne` con `green` y `WiiU` con `cyan`.
2. Desplaza cada porción en `0.01`.
3. Establece el título de la figura como `Proportion of games per platform`.
4. Ajusta el diseño.

## Consejos

<div class="hint" title="¿Cómo establecer un título para una figura?">
    Para establecer un título para una figura, puedes usar el método <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html"><code>set_title</code></a>: 
    <code>ax.set_title("Título")</code>.
</div>

<div class="hint" title="¿Cómo ajustar el diseño?">
    Para ajustar el diseño, puedes usar el método <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html"><code>tight_layout</code></a>: <code>fig.tight_layout()</code>.
</div>

<div class="hint" title="¿Cómo debería verse la figura?">
    <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>