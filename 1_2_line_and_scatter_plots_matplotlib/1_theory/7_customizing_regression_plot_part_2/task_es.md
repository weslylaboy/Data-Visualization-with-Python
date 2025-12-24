## Teoría

Ahora la figura se ve bien, pero afinémosla un poco.

Por ejemplo, nuestra figura no tiene etiquetas en los ejes. Para configurarlas, podemos usar los métodos [`set_xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html) y [`set_ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html).

También podemos ajustar cómo se distribuyen las marcas de los ejes. Para establecer manualmente las posiciones de las marcas, podemos pasar los valores deseados a los métodos [`set_xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html) y [`set_yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html).

Otra función útil a tener en cuenta es limitar el rango de visualización de los ejes x e y. Para hacer esto, podemos usar los métodos [`set_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html) y [`set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html), respectivamente.

Nuestra figura actualmente parece estar "encerrada" dentro de un cuadro. Estas líneas negras que rodean la figura se llaman [`spines`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine), y hay cuatro de ellas: `top`, `bottom`, `left` y `right`. Podemos referirnos a ellas de las siguientes maneras: `ax.spines['left']` o `ax.spines[['left', 'right']]`. Para hacerlas desaparecer, debemos llamar al método `set_visible` con el argumento `False`.

## Tarea

1. Cambia la etiqueta del eje x a `User Score` y la etiqueta del eje y a `Critic Score`.
2. Configura las marcas del eje x desde `0` hasta `10` sin saltos.
3. Configura las marcas del eje y desde `0` hasta `100` en intervalos de `10`.
4. Elimina las líneas superiores y derechas (`spines`) de la figura.

## Pistas

<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>