## Teoría

Ahora podemos ver cómo se distribuyen las puntuaciones, pero los puntos están demasiado juntos como para entender claramente su densidad.  
Para visualizar mejor la densidad, podemos ajustar la transparencia del gráfico.

En Matplotlib, podemos usar el parámetro `alpha` para controlar la transparencia. Este parámetro acepta un valor flotante entre 0 y 1.

Exploremos también otro parámetro útil, `color`, que nos permite cambiar el color de los puntos, líneas y formas trazados. Este parámetro puede aceptar una variedad de entradas, tales como:
* Una tupla RGB o RGBA de valores flotantes, por ejemplo, `(0.1, 0.2, 0.5)` o `(0.1, 0.2, 0.5, 0.3)`.
* Una cadena hexadecimal RGB o RGBA sin distinción de mayúsculas y minúsculas, por ejemplo, `#0f0f0f` o `#0f0f0f80`.
* Nombres de colores simples como `red`, `green`, `blue`, etc.
* [Nombres de colores X11](https://en.wikipedia.org/wiki/X11_color_names#Color_name_chart).  
* Y [mucho más](https://matplotlib.org/stable/users/explain/colors/colors.html#color-formats)!

## Tarea

Establece la transparencia de tu `scatter` en `0.1` y coloréalo de `green`.

## Pistas
<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>