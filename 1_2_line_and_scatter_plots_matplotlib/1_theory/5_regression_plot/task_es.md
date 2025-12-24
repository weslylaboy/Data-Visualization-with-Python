## Teoría

Ahora podemos observar definitivamente una tendencia alcista, pero no es una línea recta.  
¿Cómo trazamos una línea recta que muestre una tendencia?  
Para ello, podemos utilizar un método llamado regresión lineal.  
En términos sencillos, este intenta trazar una línea a través de nuestros puntos de datos de tal manera que minimice el error promedio.

La función `aggregate` ahora estima las puntuaciones de los críticos utilizando la línea de regresión.  
Si lo deseas, puedes implementarlo por tu cuenta.  
Por favor, consulta la pista correspondiente a continuación.

Anteriormente, usamos solo un tipo de visualización, pero ¿qué pasa si queremos construir un diagrama de dispersión junto con la línea?  
Con Matplotlib, podemos hacer esto fácilmente—solo  
llama a otro método de `Axes`, y se trazará sobre las visualizaciones anteriores.

Por ejemplo, podemos hacerlo de esta manera:
```python
ax.plot("x1", "y1", data=my_data)
ax.scatter("x2", "y2", data=my_data)
```

## Tarea

Traza la línea de regresión y añade el diagrama de dispersión.

## Pistas

<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>

<div class="hint" title="¿Cómo funciona la regresión lineal?">
   La regresión lineal encuentra la línea recta que mejor se ajusta a los datos minimizando la diferencia entre 
   los valores predichos y los valores reales. Esto se realiza minimizando los errores cuadrados entre la línea y los puntos de datos. 
   La ecuación de la línea es: <code>y = mx + b</code>, donde <code>m</code> es la pendiente y <code>b</code> es la
   intersección.

   Recuerda nuevamente que Matplotlib no proporciona un método integrado para realizar regresión lineal, 
   por lo que necesitas agregar los datos tú mismo.
</div>

<div class="hint" title="¿Cómo debería agregar los datos?">
   Para agregar los datos, podemos usar NumPy:
   <ol>
      <li>Calcula los coeficientes de la línea de regresión usando <a href="https://numpy.org/doc/stable/reference/generated/numpy.polyfit"><code>polyfit</code></a>. El grado del polinomio de ajuste debe ser 1.</li>
      <li>Crea una función de regresión usando <a href="https://numpy.org/doc/stable/reference/generated/numpy.poly1d"><code>poly1d</code></a>. Esta función aceptará <code>user_score</code> y devolverá la aproximación de <code>critic_score</code>.</li>
      <li>Crea un nuevo DataFrame donde la columna <code>user_score</code> contenga solo valores únicos, y <code>critic_score</code> sea el resultado de aplicar la función del segundo paso a la nueva columna <code>user_score</code>.</li>
   </ol>

   Ten en cuenta que tu propia función de agregación no será probada.
</div>