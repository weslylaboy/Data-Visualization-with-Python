## Teoría

Nuestro histograma ahora ofrece una visión más clara de la distribución, pero aún puede ser demasiado detallado. Usar demasiados intervalos (bins) puede hacer que pequeñas fluctuaciones en los datos generen una apariencia ruidosa, dificultando la visualización de las tendencias generales.

El número de intervalos determina el equilibrio entre detalle y suavidad:

- Demasiados intervalos: Revela detalles finos pero introduce ruido.
- Muy pocos intervalos: Suaviza los datos pero puede ocultar patrones importantes.
- Equilibrado: Preserva las tendencias clave mientras reduce el ruido innecesario.

Por defecto, Seaborn determina el número de intervalos seleccionando el ancho mínimo de intervalo según
la [regla de Sturges](https://es.wikipedia.org/wiki/Regla_de_Sturges)
y la [regla de Freedman-Diaconis](https://es.wikipedia.org/wiki/Regla_de_Freedman-Diaconis).
Sin embargo, puedes configurar manualmente los intervalos usando el argumento `bins` en la función `displot`. Este argumento acepta:

- Un entero: El número de intervalos a usar.
- Una colección: Los bordes de los intervalos (soporta anchos no uniformes).
- Una cadena: El método utilizado para calcular el número de intervalos. Para una lista completa de cadenas aceptadas,
  consulta la [documentación](https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html).

## Tarea

Configura el número de intervalos en el histograma a `10`.

## Sugerencias

<div class="hint" title="¿Cómo debería verse la figura?">
    <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>