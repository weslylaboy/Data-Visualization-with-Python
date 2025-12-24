La visualización de datos es una parte crucial de cualquier análisis de datos.  
Nos permite transformar información compleja y multimodal en formatos visuales intuitivos que podemos comprender rápidamente.  
Esto nos facilita identificar patrones y tendencias que podrían estar ocultos en los datos en bruto.  
Aunque un análisis estadístico riguroso es muy importante para un procesamiento completo de datos,  
a veces, un vistazo rápido a una visualización puede revelar aún más.  
Exploremos este concepto utilizando un ejemplo famoso: [el cuarteto de Anscombe](https://es.wikipedia.org/wiki/Cuarteto_de_Anscombe).

El cuarteto de Anscombe consiste en cuatro conjuntos de datos, es decir, conjuntos de valores X-Y, que se muestran a continuación:  
<table style="margin: auto; border-collapse: collapse; border: 3px solid; text-align: center; ">
    <thead style="border-bottom: 2px solid">
        <tr>
            <th colspan="2" style="border-right: 2px solid">Conjunto de datos I</th>
            <th colspan="2" style="border-right: 2px solid">Conjunto de datos II</th>
            <th colspan="2" style="border-right: 2px solid">Conjunto de datos III</th>
            <th colspan="2" style="border-right: 2px solid">Conjunto de datos IV</th>
        </tr>
        <tr>
            <th>x</th>
            <th style="border-right: 2px solid">y</th>
            <th>x</th>
            <th style="border-right: 2px solid">y</th>
            <th>x</th>
            <th style="border-right: 2px solid">y</th>
            <th>x</th>
            <th>y</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>10.0</td>
            <td style="border-right: 2px solid">8.04</td>
            <td>10.0</td>
            <td style="border-right: 2px solid">9.14</td>
            <td>10.0</td>
            <td style="border-right: 2px solid">7.46</td>
            <td>8.0</td>
            <td>6.58</td>
        </tr>
        <tr>
            <td>8.0</td>
            <td style="border-right: 2px solid">6.95</td>
            <td>8.0</td>
            <td style="border-right: 2px solid">8.14</td>
            <td>8.0</td>
            <td style="border-right: 2px solid">6.77</td>
            <td>8.0</td>
            <td>5.76</td>
        </tr>
        <tr>
            <td>13.0</td>
            <td style="border-right: 2px solid">7.58</td>
            <td>13.0</td>
            <td style="border-right: 2px solid">8.74</td>
            <td>13.0</td>
            <td style="border-right: 2px solid">12.74</td>
            <td>8.0</td>
            <td>7.71</td>
        </tr>
        <tr>
            <td>9.0</td>
            <td style="border-right: 2px solid">8.81</td>
            <td>9.0</td>
            <td style="border-right: 2px solid">8.77</td>
            <td>9.0</td>
            <td style="border-right: 2px solid">7.11</td>
            <td>8.0</td>
            <td>8.84</td>
        </tr>
        <tr>
            <td>11.0</td>
            <td style="border-right: 2px solid">8.33</td>
            <td>11.0</td>
            <td style="border-right: 2px solid">9.26</td>
            <td>11.0</td>
            <td style="border-right: 2px solid">7.81</td>
            <td>8.0</td>
            <td>8.47</td>
        </tr>
        <tr>
            <td>14.0</td>
            <td style="border-right: 2px solid">9.96</td>
            <td>14.0</td>
            <td style="border-right: 2px solid">8.10</td>
            <td>14.0</td>
            <td style="border-right: 2px solid">8.84</td>
            <td>8.0</td>
            <td>7.04</td>
        </tr>
        <tr>
            <td>6.0</td>
            <td style="border-right: 2px solid">7.24</td>
            <td>6.0</td>
            <td style="border-right: 2px solid">6.13</td>
            <td>6.0</td>
            <td style="border-right: 2px solid">6.08</td>
            <td>8.0</td>
            <td>5.25</td>
        </tr>
        <tr>
            <td>4.0</td>
            <td style="border-right: 2px solid">4.26</td>
            <td>4.0</td>
            <td style="border-right: 2px solid">3.10</td>
            <td>4.0</td>
            <td style="border-right: 2px solid">5.39</td>
            <td>19.0</td>
            <td>12.50</td>
        </tr>
        <tr>
            <td>12.0</td>
            <td style="border-right: 2px solid">10.84</td>
            <td>12.0</td>
            <td style="border-right: 2px solid">9.13</td>
            <td>12.0</td>
            <td style="border-right: 2px solid">8.15</td>
            <td>8.0</td>
            <td>5.56</td>
        </tr>
        <tr>
            <td>7.0</td>
            <td style="border-right: 2px solid">4.82</td>
            <td>7.0</td>
            <td style="border-right: 2px solid">7.26</td>
            <td>7.0</td>
            <td style="border-right: 2px solid">6.42</td>
            <td>8.0</td>
            <td>7.91</td>
        </tr>
        <tr>
            <td>5.0</td>
            <td style="border-right: 2px solid">5.68</td>
            <td>5.0</td>
            <td style="border-right: 2px solid">4.74</td>
            <td>5.0</td>
            <td style="border-right: 2px solid">5.73</td>
            <td>8.0</td>
            <td>6.89</td>
        </tr>
    </tbody>
</table>

Si aplicas un análisis estadístico básico a estos datos,  
descubrirás que muchas métricas son idénticas o casi idénticas en los conjuntos: la media, la varianza, la correlación, la regresión, etc.  
Esto podría llevarte a creer que, aunque estos conjuntos de datos son distintos, son fundamentalmente muy similares.  

<table style="margin: auto; border-collapse: collapse; border: 3px solid; text-align: center;">
    <thead style="border-bottom: 2px solid;">
        <tr>
            <th>Propiedad</th>
            <th>Valor</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><a href="https://es.wikipedia.org/wiki/Media_aritm%C3%A9tica">Media</a> de x</td>
            <td>9</td>
        </tr>
        <tr>
            <td><a href="https://es.wikipedia.org/wiki/Varianza_muestral">Varianza muestral</a> de x</td>
            <td>11</td>
        </tr>
        <tr>
            <td>Media de y</td>
            <td>7.50</td>
        </tr>
        <tr>
            <td>Varianza muestral de y</td>
            <td>4.125 (±0.003)</td>
        </tr>
        <tr>
            <td><a href="https://es.wikipedia.org/wiki/Correlaci%C3%B3n">Correlación</a></td>
            <td>0.816</td>
        </tr>
        <tr>
            <td><a href="https://es.wikipedia.org/wiki/Regresi%C3%B3n_lineal">Recta de regresión</a></td>
            <td>y = 3.00 + 0.500x</td>
        </tr>
        <tr>
            <td><a href="https://es.wikipedia.org/wiki/Coeficiente_de_determinaci%C3%B3n" target="_blank">Coeficiente de determinación</a></td>
            <td>0.67</td>
        </tr>
    </tbody>
</table>

Sin embargo, en cuanto los visualizas, surge una imagen completamente diferente.  
Se puede observar que estos conjuntos de datos son, de hecho, muy diferentes,  
y el concepto de regresión lineal ni siquiera se aplica a todos ellos.  
Observa detenidamente estos gráficos y analiza cuán únicos son y cuán distinto podrías interpretar o analizar cada uno.  
Es notable que todo este conocimiento provenga simplemente de un vistazo a cuatro diagramas de dispersión básicos.  

<figure>
    <img src="../../../common/resources/images/intro/anscombe.svg">
    <figcaption style="text-align: center; font-size: 0.6rem">Datos por <a href="https://doi.org/10.1080%2F00031305.1973.10478966">F. J. Anscombe</a></figcaption>
</figure>