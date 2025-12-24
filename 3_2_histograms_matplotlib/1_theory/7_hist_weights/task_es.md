## Teoría

Al comparar distribuciones con diferentes tamaños de muestra, usar recuentos brutos puede ser engañoso. Por ejemplo, si un
editor ha lanzado significativamente más juegos que otro, sus barras serán naturalmente más altas incluso si las
distribuciones son iguales.

Para abordar esto, podemos normalizar los histogramas para que muestren proporciones (o probabilidades) en lugar de recuentos brutos. Esto
asegura que las diferencias en el tamaño de la muestra no afecten los histogramas.

En el método `hist` de Matplotlib, podemos lograr esto configurando el parámetro `weights`, que acepta una colección de valores.
Este parámetro especifica el peso asignado a cada punto de datos:

- Por defecto, cada punto de datos tiene un peso de `1`, lo que significa que la altura de cada barra representa el recuento de valores
  dentro de ella.
- Si se proporciona `weights`, entonces la altura de cada barra está determinada por la suma de los pesos asignados a todos los puntos de datos
  dentro de esa barra.

Para normalizar el histograma de modo que la suma total de las alturas de las barras sea igual a `1`, debemos establecer `weights` como $\frac{1}{n}$,
donde `n` es el número total de puntos de datos.

## Tarea

Modifica tu histograma anterior para que muestre probabilidades en lugar de recuentos. Mantén iguales todos los demás parámetros.

Utiliza la función oculta `get_weights` para calcular los pesos para un conjunto de datos filtrado por editor y ventas globales. Si
quieres calcular los pesos manualmente, consulta la pista correspondiente a continuación.

## Pistas

<div class="hint" title="¿Cómo calcular los pesos?">
    Una forma de hacerlo es usar la función <a href="https://numpy.org/doc/stable/reference/generated/numpy.ones_like.html">
    <code>ones_like</code></a> para generar un arreglo de unos con la misma forma que los datos. Luego, divide este
    arreglo entre el número total de puntos de datos.
</div>

<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>