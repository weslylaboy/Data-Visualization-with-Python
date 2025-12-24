## Teoría

Es interesante notar que las ventas globales totales fueron más bajas en la década de 2010 en comparación con la década de 2000. 
Probablemente se deba a que los datos de los juegos de la década de 2010 están incompletos.

Otra ventaja de los gráficos de barras es que podemos incluir fácilmente una categoría adicional en el análisis. 
Por ejemplo, si queremos distinguir las regiones de ventas más populares para cada década, 
podemos lograr esto utilizando el argumento `hue`. 
Este argumento puede crear barras separadas para cada región, colorearlas de manera diferente y colocarlas una al lado de la otra para cada década. 
¡Si suena demasiado complicado, pasemos a la tarea para ver cómo funciona en la práctica!

## Tarea

1. Usa la función oculta `extract_sales_region` para extraer los datos y valores de las regiones de ventas 
   de las columnas `eu_sales`, `jp_sales`, `na_sales` y `other_sales`.

   Esta función transforma los datos, creando cuatro filas nuevas para cada juego y agregando dos columnas nuevas: 
   `region` (que puede ser `eu`, `jp`, `na` o `other`) y `sales`.

   Si prefieres, puedes extraer las regiones manualmente. Consulta la pista correspondiente a continuación.

2. Representa la columna `sales` en el eje y en lugar de `global_sales`.
3. Pasa el valor `region` al argumento `hue`.

## Pistas

<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>

<div class="hint" title="¿Cómo puedo graficar las ventas globales totales?">
   Para graficar las ventas globales totales, deberías usar el argumento <code>estimator</code> 
   y pasarle el valor <code>sum</code>.
</div>

<div class="hint" title="¿Cómo puedo extraer las regiones?">
    Para extraer las regiones, podrías usar la función <a href="https://pandas.pydata.org/docs/reference/api/pandas.melt.html"><code>melt</code></a>.
</div>