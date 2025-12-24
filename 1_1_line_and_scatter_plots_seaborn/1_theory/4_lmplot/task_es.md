## Teoría

Intentemos entender qué está sucediendo en nuestro gráfico. Podemos ver claramente una tendencia alcista, pero no es una línea recta.  
Esto ocurre porque `relplot` solo puede trazar líneas simples, y cuando se trata del preprocesamiento de datos antes de trazar,  
realiza agregaciones comunes como calcular la media, la mediana, el mínimo, el máximo, etc.

En nuestro caso, de manera predeterminada, calculó la media de los valores de `critic_score` que corresponden a un mismo `user_score`.  
La función de agregación se puede personalizar con el parámetro `estimator`.  
El área alrededor de la línea representa una barra de error, indicando qué tan bien la agregación representa los datos iniciales.  
Hay [varios tipos de barras de error](https://seaborn.pydata.org/tutorial/error_bars.html), las cuales se pueden configurar con el  
parámetro `errorbar`.

Aprenderemos más sobre `estimator` y `errorbar` en la [siguiente sección de Seaborn](course://2_1_bar_and_pie_charts_seaborn/1_theory/3_countplot_stats).

Entonces, ¿cómo trazamos una línea recta que muestre una tendencia?  
Para eso, podemos usar la función de Seaborn [`lmplot`](https://seaborn.pydata.org/generated/seaborn.lmplot.html),  
que dibuja los datos junto con un modelo de regresión lineal ajustado.

## Tarea

Modifica la función `plot` reemplazando la llamada a `relplot` con `lmplot` y eliminando el parámetro `kind`.

## Pistas

<div class="hint" title="¿Cómo funciona la regresión lineal?">
    La regresión lineal encuentra la línea recta que mejor se ajusta a los datos minimizando la diferencia entre los valores predichos
    y los valores reales. Esto se logra minimizando los errores cuadrados entre la línea y los puntos de datos. 
    La ecuación de la línea es: <code>y = mx + b</code>, donde <code>m</code> es la pendiente y <code>b</code> es la intersección.
</div>

<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>