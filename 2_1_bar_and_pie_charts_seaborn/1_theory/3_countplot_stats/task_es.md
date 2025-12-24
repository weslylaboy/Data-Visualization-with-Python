## Teoría

Finalmente, podemos ver todos los nombres de las plataformas, pero los datos actuales no muestran claramente qué porcentaje representa cada plataforma en comparación con las demás.

Afortunadamente, el gráfico de conteo tiene un argumento especial llamado `stat`, que modifica las estadísticas calculadas.  
Este argumento acepta los siguientes valores:  
1. `count`: El número de observaciones por categoría.  
2. `proportion`: Similar a `count`, pero normalizado para que todas las barras sumen `1`.  
3. `percent`: Similar a `count`, pero normalizado para que todas las barras sumen `100`.  
4. `probability`: Un alias para `proportion`.

## Tarea

Actualiza la estadística configurándola a `percent`.

## Pistas

<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>