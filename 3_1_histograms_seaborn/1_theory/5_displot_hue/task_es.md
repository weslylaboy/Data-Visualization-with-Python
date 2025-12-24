## Teoría

¡Genial! Ahora, nuestro histograma muestra claramente el patrón clave: hay muchos menos juegos con altas ventas que aquellos con bajas ventas. A continuación, utilizaremos histogramas para comparar las distribuciones de ventas de diferentes editoriales.

El `displot` de Seaborn permite graficar múltiples distribuciones en la misma figura de varias maneras:

1. Superpuestas en el mismo eje con transparencia  
2. Apiladas unas sobre otras  
3. Separadas en subgráficos para cada distribución  

Nos centraremos en histogramas superpuestos, ya que son ideales para comparaciones directas. Para lograr esto, podemos usar el argumento `hue` para dividir los datos según una columna categórica.

## Tarea

1. Usa la función oculta `filter_by_publisher` para filtrar los datos solo para `Ubisoft` y `Electronic Arts`. Luego, utiliza la función oculta `filter_by_global_sales` para excluir ventas globales por encima del percentil 95.

2. Pasa la columna `publisher` al argumento `hue` para distinguir las distribuciones.

Si lo prefieres, puedes filtrar manualmente el conjunto de datos. Por favor, consulta la pista correspondiente a continuación.

## Pistas

<div class="hint" title="¿Cómo debería filtrar los datos?">
    Para filtrar los datos por editorial, 
    puedes usar indexación booleana y el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html#pandas.Series.isin"><code>isin</code></a> en la columna <code>publisher</code>.
</div>

<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>