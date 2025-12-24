## Teoría

¡Genial! Ahora nuestro histograma muestra claramente el patrón clave: hay muchos menos juegos con altas ventas que con bajas ventas. A continuación, usemos histogramas para comparar las distribuciones de ventas de diferentes distribuidores.

El método `hist` de Matplotlib permite trazar múltiples distribuciones en la misma figura de varias maneras:

1. Superpuestas en el mismo eje con diferentes niveles de transparencia.
2. Apiladas unas sobre otras.
3. Separadas en subgráficos para cada distribución.
4. Histogramas agrupados. A diferencia de los histogramas superpuestos, los contenedores (bins) se colocan uno al lado del otro en lugar de superponerse.

Nos centraremos en los histogramas superpuestos, ya que son ideales para realizar comparaciones directas. Para lograr esto, podemos trazar histogramas uno a la vez llamando a `hist` para cada distribución.

## Tarea

1. Dibuja dos histogramas superpuestos para las distribuciones de ventas globales de los juegos publicados por `Electronic Arts` y `Ubisoft`.

2. Para cada histograma, establece `alpha` en `0.7` y utiliza el valor predeterminado para `bins`. Describimos el parámetro `alpha` en detalle en la sección "[Transparencia y color](course://1_2_line_and_scatter_plots_matplotlib/1_theory/2_transparency_and_color)". Encuentra más detalles en la pista correspondiente a continuación.

3. Usa la función oculta `filter_by_publisher` para filtrar los datos del distribuidor dado. Pasa el conjunto de datos y el nombre del distribuidor como argumentos. Luego, utiliza la función oculta `filter_by_global_sales` para filtrar las ventas globales superiores al percentil 95.

Si lo prefieres, puedes filtrar manualmente el conjunto de datos. Consulta la pista correspondiente a continuación.

## Pistas

<div class="hint" title="¿Cómo debo filtrar los datos?">
    Para filtrar los datos por distribuidor, puedes usar indexación booleana en la columna <code>publisher</code>.
</div>

<div class="hint" title="¿Cómo establecer transparencia?">
    Especifica el parámetro <code>alpha</code> en el método <code>hist</code>.
</div>

<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>