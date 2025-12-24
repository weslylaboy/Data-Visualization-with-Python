## Teoría

Nuestro gráfico actual no es muy informativo porque la mayor parte de los datos cae en los dos primeros intervalos. ¡Los intervalos restantes son apenas visibles debido a la escala! Algunos juegos en el conjunto de datos tienen ventas extremadamente altas, lo que estira el eje x y dificulta el análisis del resto de los datos.

Una forma de abordar este problema es estableciendo un límite superior para las ventas. Sin embargo, ¿cómo podemos determinar un umbral razonable?

Un buen enfoque es aplicar una escala logarítmica al eje x. Esta transformación dispersa los valores más bajos mientras comprime los extremos, haciendo que la distribución sea más clara. Con esta perspectiva, podemos definir un punto de corte significativo para las ventas.

El método `hist` no nos permite configurar directamente una escala logarítmica para el eje x. En su lugar, podemos aplicar una escala logarítmica al eje llamando al método
[`ax.set_xscale()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale)
con el argumento `log`.

## Tarea

Aplica una escala logarítmica al eje x del histograma para comprender mejor el límite superior de las ventas.

## Pistas

<div class="hint" title="¿Cómo debería lucir la figura?">
   <img src="example.png" alt="Cómo debería lucir la figura" style="max-height: 500px">
</div>