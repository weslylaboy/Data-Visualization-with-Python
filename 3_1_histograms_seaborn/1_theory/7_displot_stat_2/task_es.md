## Teoría

Después de aplicar el parámetro `stat="probability"`, notamos que la forma general del gráfico permanece igual. Esto 
se debe a que, por defecto, Seaborn normaliza la probabilidad en todas las categorías combinadas.

Esto significa que la probabilidad de cada intervalo se calcula como una fracción del conjunto de datos completo, en lugar de calcularse 
por separado para cada editor. Como resultado, si un editor tiene más juegos, sus barras aún pueden dominar el histograma, dificultando 
las comparaciones directas.

Para solucionar esto, podemos utilizar el parámetro `common_norm`. Cuando se establece en `False`, asegura que el histograma de cada editor 
se normalice de manera independiente, haciendo que sus distribuciones sean directamente comparables.

## Tarea

Modifica el histograma para que calcule las probabilidades por separado para cada editor.

## Pistas

<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>