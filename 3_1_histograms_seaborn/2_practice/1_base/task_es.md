## Tarea

Una empresa de bebidas ha estado operando con éxito en Belgrado, vendiendo una variedad de bebidas durante todo el año. Ahora, la empresa ha decidido expandir su negocio a Ereván y desea comparar sus ventas establecidas en Belgrado con los primeros seis meses de ventas en Ereván para evaluar las diferencias en el mercado y optimizar su estrategia.

Debido a que los dos mercados difieren en tamaño, estacionalidad y preferencias de los clientes, la empresa quiere analizar si los patrones de ventas de Ereván, a pesar del período de observación más corto, se asemejan a los de Belgrado. Si ambos siguen una distribución similar, podría sugerir que los factores que influyen en las ventas son consistentes en ambas ciudades. Por el contrario, distribuciones distintas podrían indicar influencias locales únicas que afectan las ventas.

Para revelar estas tendencias generales, la empresa nos ha pedido que creemos un único gráfico con dos histogramas superpuestos.

Requisitos de la visualización:

1. El histograma debe estar normalizado (es decir, los intervalos para cada ciudad deben sumar `1`).
2. Ambos histogramas deben compartir intervalos comunes. Estos intervalos deben ir desde el menor múltiplo de cien redondeado hacia abajo hasta el mayor múltiplo de cien redondeado hacia arriba en ambas ciudades, con un paso de `100`.

Ten en cuenta que no es necesario procesar los datos aquí.

Puedes usar la función oculta `get_bins` para obtener los bordes de los intervalos para el gráfico (los mismos para ambas ciudades). Pasa el conjunto de datos completo como argumento.

Si tienes dificultades, siéntete libre de usar las pistas a continuación, donde también puedes encontrar una vista previa de la figura final.

## Personalización adicional

Si quieres, puedes personalizar la figura aún más. Aquí tienes algunas ideas para la personalización:

1. Cambiar la paleta de colores de las barras.
2. Agregar un título descriptivo a la figura y etiquetas claras en los ejes.
3. Añadir observaciones individuales utilizando un diagrama de dispersión.

Te animamos a explorar estas personalizaciones por tu cuenta, ya que no todas estarán cubiertas en este curso.

Ten en cuenta que estas modificaciones no serán evaluadas y podrían romper las pruebas existentes.

## Pistas

<div class="hint" title="¿Cómo debería verse la figura?">
    <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>

<div class="hint" title="¿Cómo trazar dos histogramas en el mismo gráfico?">
    Para trazar dos histogramas en la misma figura, usa la función <code>displot</code> y especifica el
    parámetro <code>hue</code>.
</div>

<div class="hint" title="¿Cómo normalizar el histograma?">
    Para normalizar el histograma, configura el parámetro <code>stat</code> de la función <code>displot</code> como 
    <code>probability</code>. Además, establece el parámetro <code>common_norm</code> como <code>False</code> para asegurar que cada 
    histograma se normalice por separado.
</div>

<div class="hint" title="¿Cómo cambiar el número de intervalos?">
    Para cambiar el número predeterminado de intervalos, configura el parámetro <code>bins</code> en la función <code>displot</code>.
</div>

<div class="hint" title="¿Cómo generar los bordes de los intervalos requeridos?">
    Primero, extrae los valores mínimo y máximo en la columna <code>sales</code> del conjunto de datos, usando los métodos
    <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.min.html#pandas.Series.min"><code>min</code></a>
    y 
    <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.max.html#pandas.Series.max"><code>max</code></a>, respectivamente. Luego,
    redondea el valor mínimo hacia abajo y el valor máximo hacia arriba al centenar más cercano. Finalmente, genera un arreglo de bordes de los intervalos con un tamaño de paso de <code>100</code>, por ejemplo, utilizando la función integrada <code>range</code> para garantizar intervalos equidistantes.
</div>