## Teoría

En este punto, nuestro histograma luce bastante inusual: un gran cuadrado con un pequeño contenedor (bin) al lado definitivamente no es lo que esperábamos. Esto sucede porque aplicar una escala logarítmica solo estira el eje pero no modifica los contenedores. Los tamaños de los contenedores permanecen sin cambios, lo que lleva a una visualización distorsionada.

Para solucionar esto, necesitamos configurar manualmente los contenedores utilizando el argumento `bins` en el método `hist`. Este argumento acepta lo siguiente:

- Un número entero: La cantidad de contenedores a usar.
- Una colección: Los bordes de los contenedores (admite anchos no uniformes).
- Una cadena: Un método para calcular la cantidad de contenedores. Para una lista completa de cadenas aceptadas,
  consulta la [documentación](https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html).

Por defecto, Matplotlib establece el número de contenedores en `10`.

## Tarea

Traza un histograma con `100` contenedores logarítmicos.

Utiliza la función oculta `get_logarithmic_bins` para generar contenedores logarítmicos para el histograma. Pasa el conjunto de datos y el número de contenedores como argumentos.

Si lo prefieres, puedes generar los contenedores manualmente. Por favor, consulta la pista correspondiente a continuación.

## Pistas

<div class="hint" title="¿Cómo debería lucir la figura?">
    <img src="example.png" alt="Cómo debería lucir la figura" style="max-height: 500px">
</div>

<div class="hint" title="¿Cómo importar la función oculta?">
    Para importarla, coloca el cursor sobre el nombre subrayado de la función oculta en tu código. Luego, presiona &shortcut:ShowIntentionActions; y selecciona <samp>Import 'function_name from data'</samp>:
    <img src="../../../common/resources/images/common/hidden_function_import.gif" alt="Cómo importar funciones ocultas" style="max-height: 500px">
</div>

<div class="hint" title="Cómo generar contenedores logarítmicos">
    Una forma de generar contenedores logarítmicos es definiéndolos como una colección de números uniformemente distribuidos en escala logarítmica, utilizando la función <a href="https://numpy.org/doc/stable/reference/generated/numpy.logspace.html"><code>np.logspace</code></a>. La función acepta los siguientes argumentos:
    <ul>
        <li><code>start</code>: El punto de inicio de la secuencia.</li>
        <li><code>stop</code>: El punto final de la secuencia.</li>
        <li><code>num</code>: La cantidad de muestras a generar.</li>
        <li><code>base</code>: La base del logaritmo.</li>
    </ul>
    Por ejemplo, <code>np.logspace(0, 3, 4, base=10)</code> generará 4 números desde \(10^0\) hasta \(10^3\). 
    <br><br>
    Deja que <code>base</code> esté configurado a <code>10</code> (el valor predeterminado). 
    Ten en cuenta que para el argumento <code>start</code>, debes pasar el logaritmo del valor mínimo en el conjunto de datos.
    De manera similar, para el argumento <code>stop</code>, pasa el logaritmo del valor máximo en el conjunto de datos. Recuerda que estás generando los bordes de los contenedores, por lo que el número de bordes debe ser igual al número de contenedores <code>+ 1</code>.
</div>