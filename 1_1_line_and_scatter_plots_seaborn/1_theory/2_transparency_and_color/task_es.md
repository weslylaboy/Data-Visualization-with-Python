## Teoría

Ahora podemos observar cómo están distribuidos los puntajes,  
pero los puntos están demasiado juntos para entender claramente su densidad.  
Para visualizar mejor la densidad, podemos ajustar la transparencia del gráfico.

En Seaborn, podemos usar el parámetro `alpha` para controlar la transparencia.  
Este parámetro acepta un valor flotante entre 0 y 1.

También exploremos otro parámetro útil, `color`,  
que te permite cambiar el color de los puntos, líneas y formas graficadas.  
Este parámetro puede aceptar una variedad de entradas, tales como:  
* Una tupla RGB o RGBA de valores flotantes, por ejemplo, `(0.1, 0.2, 0.5)` o `(0.1, 0.2, 0.5, 0.3)`.  
* Una cadena hexadecimal RGB o RGBA insensible a mayúsculas, por ejemplo, `#0f0f0f` o `#0f0f0f80`.  
* Nombres simples de colores como `red`, `green`, `blue`, etc.  
* [Nombres de colores X11](https://en.wikipedia.org/wiki/X11_color_names#Color_name_chart).  
* Y [mucho más](https://matplotlib.org/stable/users/explain/colors/colors.html#color-formats)!

## Tarea

Ajusta la transparencia de tu `relplot` a `0.1` y coloréalo de `green`.

## Pistas
<div class="hint" title="¿Cómo debería ser la figura?">
   <img src="example.png" alt="Cómo debería ser la figura" style="max-height: 500px">
</div>