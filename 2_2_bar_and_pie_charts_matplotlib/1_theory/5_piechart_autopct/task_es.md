## Teoría

Al observar la figura actual, no podemos determinar fácilmente el tamaño exacto de cada sector.
Sería conveniente colocar estos números directamente en el gráfico circular.

Para hacerlo, podemos usar el argumento `autopct`.
Este acepta una cadena de formato y la aplica al tamaño de cada sector.
Por ejemplo, si pasamos `%.1f%%` como cadena de formato, un sector con un tamaño de `32.24` se mostrará como `32.2%`.
Aquí está cómo funciona la cadena de formato:

1. `%.1f` se convierte en `32.2`.
2. `%%` se convierte en `%`.

Por favor, consulta la pista correspondiente a continuación para más detalles sobre la configuración de números de punto flotante.

## Tarea

Añade los tamaños de los sectores al gráfico circular. Deben redondearse a **dos decimales** y tener un símbolo `%` al final.

## Pistas

<div class="hint" title="Detalles adicionales sobre el formato">

- **Números de punto flotante**: El `%.1f` en la cadena de formato especifica que el número debe mostrarse con un
  decimal
  de precisión. Puedes ajustar esto para mostrar más o menos decimales, por ejemplo, `%.2f` para dos decimales o `%.0f`
  para ninguno
  (redondeando efectivamente al número entero más cercano).
- **Signo de porcentaje**: `%%` en la cadena de formato se utiliza para mostrar un signo de porcentaje. Esto se debe a que `%`
  
  es un carácter especial en las cadenas de Python, por lo que si deseas mostrarlo, necesitas usar `%%`.

También puedes pasar una función al argumento `autopct`, que acepta el tamaño del sector y devuelve una cadena.

Para aprender más sobre el lenguaje de cadenas de formato, consulta la 
[documentación](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting).

</div>

<div class="hint" title="¿Cómo redondear los tamaños de los sectores a dos decimales?">
   Puedes usar la cadena de formato del ejemplo, pero reemplazar <code>%.1f</code> con <code>%.2f</code>.
</div>

<div class="hint" title="¿Cómo debería verse la figura?">
   <img src="example.png" alt="Cómo debería verse la figura" style="max-height: 500px">
</div>