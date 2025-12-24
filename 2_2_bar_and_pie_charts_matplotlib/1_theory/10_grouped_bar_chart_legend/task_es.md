## Teoría

¡Genial!  
Ahora finalmente tenemos todas las regiones graficadas juntas.  
Sin embargo, no está claro qué traza corresponde a cada región.  
Añadir una leyenda podría resolver este problema.

Para añadir una leyenda a nuestra figura en Matplotlib,  
necesitamos llamar al método [`ax.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend).  

Sin embargo, si hacemos esto sin realizar ajustes adicionales, no sucederá nada.  
Esto se debe a que Matplotlib no conoce los nombres de las regiones.  
Para corregir esto, debemos pasar el nombre de la región al método `bar` utilizando el argumento `label`.

## Tarea

1. Pasa el nombre de la región como el argumento `label` al método `bar`.  
2. Añade la leyenda a la figura.

## Pistas

<div class="hint" title="¿Cómo debería verse la figura?">  
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">  
</div>