## Teoría

Ahora que hemos explorado la popularidad de las plataformas, veamos las ventas globales en algunas de ellas.
Para lograr esto, podemos seguir utilizando `catplot`, pero esta vez con un tipo diferente: `bar`.

Como vimos en los gráficos anteriores, tenemos muchas plataformas de videojuegos, incluidas algunas "antiguas".
Para simplificar nuestro análisis, vamos a enfocarnos solo en las plataformas más modernas: `PS4`, `PC`, `XOne` y `WiiU`. 

## Tarea

1. Usa la función oculta `filter_platforms` para filtrar las plataformas de videojuegos más antiguas.

   Si lo prefieres, puedes filtrar las plataformas manualmente. Por favor, consulta la pista correspondiente más abajo.

2. Cambia el argumento `kind` a `bar` y grafica `global_sales` en el eje y.

Ten en cuenta que no necesitas especificar los argumentos `order` y `stat`, 
y que el gráfico de barras ahora debería usar la orientación vertical.

## Pistas

<div class="hint" title="¿Cómo debería verse la figura?">
   Ten en cuenta que tu figura podría verse ligeramente diferente debido a la forma en que Seaborn calcula las barras de error. 
   
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>

<div class="hint" title="¿Cómo debo filtrar las plataformas?">
    Para filtrar las plataformas innecesarias, puedes usar
    el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html"><code>isin</code></a>
    en la columna <code>platform</code>.
</div>