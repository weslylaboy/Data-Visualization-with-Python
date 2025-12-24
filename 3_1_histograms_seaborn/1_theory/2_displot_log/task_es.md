## Teoría

Nuestro gráfico actual no es muy informativo porque los datos tienen una cola larga hacia la derecha: algunos juegos tienen ventas extremadamente altas. Esto expande el eje x, lo que dificulta analizar la distribución principal.

Una forma de abordar este problema es estableciendo un límite superior para las ventas. Sin embargo, ¿cómo podemos determinar un umbral razonable?

Un buen enfoque es aplicar una escala logarítmica al eje x. Esta transformación distribuye los valores más bajos mientras comprime los extremos, haciendo que la distribución sea más clara. Con esta vista, podemos definir un límite significativo para las ventas.

Para aplicar esta transformación, configura el argumento `log_scale` a `True` en la función `displot`.

## Tarea

Aplica una escala logarítmica al eje x del histograma para comprender mejor el límite superior de las ventas.

## Pistas

<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>