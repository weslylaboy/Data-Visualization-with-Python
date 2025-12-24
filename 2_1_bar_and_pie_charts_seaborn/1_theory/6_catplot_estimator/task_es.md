## Teoría

Ahora podemos observar las ventas globales por plataforma, pero cada barra tiene una línea extraña llamada *barra de error*.

Para cada plataforma, tenemos múltiples puntos de datos de ventas globales. 
Seaborn agrupa estos valores para trazar un único valor para cada plataforma 
y proporciona una señal visual que indica qué tan bien este valor representa los puntos de datos subyacentes.

Nos encontramos con algo similar cuando analizamos tendencias utilizando un gráfico de líneas en una de las
[lecciones anteriores](course://1_1_line_and_scatter_plots_seaborn/1_theory/4_lmplot) de Seaborn.
Ahora es momento de mirar más de cerca el argumento `estimator`.

El argumento `estimator` controla cómo se agregan los datos. Acepta lo siguiente:
1. Una función que sea invocable y que mapee un vector a datos escalares.
2. Nombres de funciones de Numpy como `min`, `max`, `sum`, `mean` o `median`.

De manera predeterminada, Seaborn utiliza `mean` como el estimador.

Existen [varios tipos de barras de error](https://seaborn.pydata.org/tutorial/error_bars.html),
que se pueden configurar con el parámetro `errorbar`.
Para deshabilitar las barras de error por completo, solo debemos pasar `None` como valor.

## Tarea

1. Configura el estimador como `median` y elimina la barra de error.
2. Ordena las plataformas utilizando la función oculta `get_sorted_platforms`.

   Si lo prefieres, puedes ordenar las plataformas manualmente. Consulta la pista correspondiente a continuación.

## Pistas

<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>

<div class="hint" title="¿Cómo debo ordenar las plataformas?">
    Para ordenar las plataformas, necesitas:
    <ol>
        <li>Agrupar los datos por la columna <code>platform</code> utilizando el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html"><code>groupby</code></a>.</li>
        <li>Calcular la mediana de la columna <code>global_sales</code> utilizando el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.median.html"><code>median</code></a>.</li>
        <li>Ordenar los valores utilizando el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html"><code>sort_values</code></a>.</li>
        <li>Usar la propiedad <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html"><code>index</code></a> para obtener los nombres de las plataformas ordenadas.</li>
        <li>Convertir el objeto <code>Index</code> a una lista utilizando el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.Index.to_list.html"><code>to_list</code></a>.</li>
    </ol>
</div>