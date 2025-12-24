## Teoría

Cuando se comparan distribuciones con tamaños de muestra diferentes, usar conteos brutos puede ser engañoso. Por ejemplo, si un editor ha lanzado significativamente más juegos que otro, sus barras naturalmente serán más altas, incluso si las distribuciones son las mismas.

Para abordar esto, podemos normalizar los histogramas para que muestren proporciones (o probabilidades) en lugar de conteos brutos. Esto asegura que las diferencias en el tamaño de muestra no afecten a los histogramas.

En la función `displot` de Seaborn, podemos lograr esto configurando el parámetro `stat` a uno de los siguientes valores:
- `count` (predeterminado) – Muestra el número de observaciones en cada intervalo.
- `frequency` – Similar a `count` pero normalizado por el ancho del intervalo.
- `probability` o `proportion` – Muestra la proporción de observaciones en cada intervalo (sumando `1`).
- `percent` – Muestra el porcentaje de observaciones en cada intervalo (sumando `100`).
- `density` – Similar a `probability`, pero el área total bajo las barras equivale a `1`.

## Tarea

Modifica el histograma para que muestre probabilidades en lugar de conteos.

## Pistas

<div class="hint" title="¿Cómo debería verse la gráfica?">
   <img src="example.png" alt="¿Cómo debería verse la gráfica?" style="max-height: 500px">
</div>