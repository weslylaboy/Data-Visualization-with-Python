## Teoría

Intentemos entender qué está sucediendo en nuestro gráfico.  
Nuestros datos consisten en pares de puntuaciones de usuarios y puntuaciones de críticos.  
Para cada puntuación de usuario, pueden existir varias puntuaciones de críticos: por ejemplo, si tenemos dos juegos con la misma puntuación de usuario, pueden tener diferentes puntuaciones de críticos porque son juegos distintos.  

Sin embargo, Matplotlib no realiza preprocesamiento adicional,  
por lo que el método `plot` simplemente conecta los puntos en el orden en que aparecen en el conjunto de datos.  
Por esta razón, terminamos con un confuso efecto de "bola de hilo".  

Para resolver este problema, necesitamos preprocesar los datos nosotros mismos.  
Por ejemplo, podemos calcular la media de las puntuaciones de críticos para cada puntuación de usuario.  

## Tarea

Añade una llamada a la función oculta `aggregate`.  
Esta función calculará la media y devolverá una tabla con las columnas: `user_score` y `critic_score`.  

Si lo prefieres, puedes agregar los datos tú mismo. Consulta la pista correspondiente a continuación.  

## Pistas

<div class="hint" title="¿Cómo debería lucir la figura?">
   <img src="example.png" alt="Cómo debería lucir la figura" style="max-height: 500px">
</div>

<div class="hint" title="¿Cómo importar funciones ocultas?">
    Para importarla, puedes colocar el cursor sobre el nombre subrayado de la función oculta en tu código, luego presionar &shortcut:ShowIntentionActions;, y seleccionar <samp>Import 'function_name from data'</samp>:
    <img src="../../../common/resources/images/common/hidden_function_import.gif" alt="Cómo debería lucir la figura" style="max-height: 500px">
</div>

<div class="hint" title="¿Cómo debo agregar los datos?">
   Para agregar los datos, puedes usar Pandas:

   <ol>
   <li>Agrupa los datos por la columna <code>user_score</code>.</li>
   <li>Usa el método <a href="https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.mean.html"><code>mean</code></a> para agregar la columna <code>critic_score</code>.</li>
   <li>Restaura el índice para convertir la serie en un DataFrame.</li>
   </ol>

Nota que tu propia función de agregación no será evaluada.  
</div>