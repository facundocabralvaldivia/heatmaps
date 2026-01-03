## Peru Data Heatmap Visualization

Author:  Facundo Cabral  
Github:   [facundocabralvaldivia](https://github.com/facundocabralvaldivia)  
Linkedin: [Facundo Cabral](www.linkedin.com/in/facundo-cabral-valdivia)

This repository contains heatmap visualizations of economic and social datasets for Peru’s regions.  
The maps highlight regional differences across key metrics, enabling clear comparison and analysis.  
You can find the heatmap analysis on my LinkedIn profile.

Peru Shapefile Source: [GEO GPS PERU](https://www.geogpsperu.com/2014/03/base-de-datos-peru-shapefile-shp-minam.html)

## Estructura de la carpeta maps

A continuación se muestra la estructura principal del repositorio y una breve descripción de los elementos relevantes dentro de la carpeta `maps`:

```text
- maps/
|- README.md
|- peru_regions_shapefile/
| |- peru_departamentos.shp
| |- peru_departamentos.shx
| |- peru_departamentos.dbf
| |- peru_departamentos.prj
| |- peru_departamentos.cpg
| |- peru_departamentos.sbn
| |- peru_departamentos.sbx
|- visualizations/ > mapas generados (si existe)
|- women_entrepreneurs.py > ejemplo de script de procesamiento
```

Nota: Los scripts de procesamiento y generación de mapas se encuentran en archivos Python dentro del repositorio (por ejemplo, `women_entrepreneurs.py`). Las visualizaciones generadas suelen almacenarse en la carpeta `visualizations` cuando está presente.