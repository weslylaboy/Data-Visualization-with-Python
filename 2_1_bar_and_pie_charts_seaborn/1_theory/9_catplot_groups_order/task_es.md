## Teoría

La figura se ve bien, pero aún hay algo que podemos ajustar: el orden dentro de cada década.

El orden de las categorías de tono se controla mediante el argumento `hue_order`.
Similar al argumento `order`, acepta una colección de nombres de categoría para definir el orden de visualización deseado.

## Tarea

Usa la función oculta `get_sorted_regions` para obtener la lista de regiones en orden descendente y pásala a la función `catplot`.

Si lo prefieres, puedes ordenar las plataformas manualmente. Consulta la pista correspondiente a continuación.

## Pistas

<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>

<div class="hint" title="¿Cómo debo ordenar las regiones?">
    Para ordenar las plataformas, puedes usar
    el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html"><code>sort_values</code></a> 
    en la columna <code>platform</code>:
    <ol>
        <li>Agrupa los datos por la columna <code>region</code>.</li>
        <li>Calcula la suma de la columna <code>sales</code> utilizando el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.sum.html"><code>sum</code></a>.</li>
        <li>Ordena los valores usando el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html"><code>sort_values</code></a>.</li>
        <li>Utiliza la propiedad <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html"><code>index</code></a> para obtener los nombres de plataformas ordenados.</li>
        <li>Finalmente, convierte el objeto <code>Index</code> a una lista utilizando el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.Index.to_list.html"><code>to_list</code></a>.</li>
    </ol>
</div>