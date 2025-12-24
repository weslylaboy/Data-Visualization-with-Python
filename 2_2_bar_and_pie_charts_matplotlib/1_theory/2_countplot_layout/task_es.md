## Teoría

En este conjunto de datos, hay muchas plataformas, lo que dificulta interpretar la figura debido a las etiquetas superpuestas en el eje x. Podemos resolver este problema reduciendo el número de grupos o cambiando la disposición de la figura, reubicando las etiquetas del eje x al eje y.

Para ajustar la disposición del gráfico de barras, necesitamos usar un método de trazado diferente: [`barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh). Las diferencias clave entre la función `barh` y la anterior `bar` son:
1. `barh` dibuja gráficos de barras horizontales, mientras que `bar` crea gráficos de barras verticales.
2. Debido al cambio en la disposición, el primer argumento ahora es `y`, y el segundo argumento es `width`.

Después de realizar este cambio, es posible que notes que las etiquetas todavía están muy juntas. Para solucionar esto, podemos usar el método [`fig.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html), que ajusta el espacio entre y alrededor de los elementos de la figura. Ten en cuenta que debemos llamar a este método DESPUÉS de trazar todos los datos necesarios en la figura.

## Tarea

Cambia la disposición de la figura a horizontal y ajusta el espacio.

## Pistas

<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>