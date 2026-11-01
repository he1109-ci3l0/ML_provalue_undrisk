# OilyGiant — Selección de región para 200 pozos petroleros bajo riesgo controlado

![Python](https://img.shields.io/badge/Python-3.11-2B595D) ![scikit--learn](https://img.shields.io/badge/scikit--learn-Regresi%C3%B3n%20lineal-376F78) ![Bootstrapping](https://img.shields.io/badge/Bootstrapping-1%2C000%20remuestreos-4A7B8C) ![Riesgo](https://img.shields.io/badge/Riesgo%20de%20p%C3%A9rdida-1.5%25-B82B66) ![Estado](https://img.shields.io/badge/Estado-Completado-1D434F)

Modelo de aprendizaje automático y simulación de riesgo que decide en cuál de tres regiones conviene invertir para desarrollar 200 pozos petroleros nuevos.

📊 **Case study:** [he1109-ci3l0.github.io/ML_provalue_undrisk](https://he1109-ci3l0.github.io/ML_provalue_undrisk/)

## Pregunta de negocio

Con un presupuesto de 100 millones de dólares para 200 pozos nuevos, ¿en qué región se coloca el capital para obtener el mayor beneficio sin que la probabilidad de perder dinero supere el 2.5 %?

## Resultado

**Desarrollar los 200 pozos en la Región 1.** Es la única de las tres con riesgo de pérdida por debajo del 2.5 % y, además, la de mayor beneficio promedio esperado.

| Región | Beneficio promedio | Intervalo de confianza 95 % | Riesgo de pérdida |
|---|---|---|---|
| Región 0 | 3,961,650 USD | −1.11 M a 9.10 M USD | 6.9 % |
| **Región 1** | **4,560,451 USD** | **0.34 M a 8.52 M USD** | **1.5 %** |
| Región 2 | 4,044,039 USD | −1.63 M a 9.50 M USD | 7.6 % |

El límite inferior del intervalo de la Región 1 es positivo: incluso en el escenario desfavorable razonable (percentil 2.5), la inversión gana.

## Lo que gana la empresa

- **Una decisión de inversión con el riesgo medido.** En lugar de elegir por la ganancia más alta de una sola estimación, la recomendación se basa en 1,000 escenarios simulados por región, con su probabilidad de pérdida.
- **Se evita la región más atractiva a primera vista.** Con una sola estimación, la Región 0 parecía la mejor (33.2 M USD de ganancia potencial), pero pierde dinero en el 6.9 % de los escenarios, casi tres veces el límite aceptado.
- **Seleccionar pozos es lo que genera la ganancia.** Ningún pozo promedio llega al punto de equilibrio (111.1 mil barriles); el modelo permite elegir los 200 mejores de cada 500 explorados.
- **Se sabe qué tan sensible es la decisión al precio del crudo.** El análisis de sensibilidad indica a partir de qué precio cada región deja de cumplir el límite de riesgo.

## Hallazgos

1. **El pozo promedio no es rentable en ninguna región:** las reservas medias (92.5, 68.8 y 95.0 mil barriles) están por debajo del equilibrio de 111.1.
2. **La Región 1 se predice casi a la perfección:** RECM (raíz del error cuadrático medio) de 0.89 mil barriles, contra 37.6 y 40.0 en las Regiones 0 y 2.
3. **Precisión vale más que volumen:** la Región 1 tiene el menor volumen promedio, pero como el modelo distingue bien los pozos buenos, su distribución de beneficios es estrecha y su piso es positivo.
4. **La mayor ganancia puntual no es la más segura:** la Región 0 lidera en una sola pasada, pero no pasa el filtro de riesgo.
5. **La decisión tiene poco margen ante el precio:** la Región 1 cumple el límite de riesgo mientras el precio no baje más de 0.3 % del precio base; con una caída de 2 %, su riesgo sube a 11.4 %.

## Cómo está hecho

1. **Datos:** tres regiones de 100,000 puntos de exploración cada una, con tres características (`f0`, `f1`, `f2`) y el volumen de reservas (`product`); sin valores faltantes.
2. **Modelo por región:** división 75/25 en entrenamiento y validación y regresión lineal (el único modelo permitido por el encargo).
3. **Punto de equilibrio:** 100 M USD / 200 pozos / 4,500 USD por mil barriles = 111.1 mil barriles por pozo.
4. **Función de ganancia:** se eligen los 200 pozos con mayor volumen **predicho** y la ganancia se calcula con su volumen **real**.
5. **Bootstrapping:** 1,000 repeticiones; en cada una se toman 500 pozos al azar con reemplazo, se eligen los 200 mejores y se calcula la ganancia. De ahí salen el beneficio promedio, el intervalo de confianza al 95 % y el riesgo de pérdida.
6. **Sensibilidad:** las distribuciones de ganancia se recalculan con precios de 90 % a 110 % del precio base.

### Estructura

```
ML_provalue_undrisk/
├── data/raw/            geo_data_0/1/2.csv (no versionados)
├── src/                 datos, modelado, ganancia y bootstrapping
├── reports/figures/     distribución de ganancias y sensibilidad al precio
├── oilygiant.ipynb      análisis completo
├── index.html           case study (GitHub Pages)
├── environment.yml
└── requirements.txt
```

### Reproducción

```bash
git clone https://github.com/he1109-ci3l0/ML_provalue_undrisk
cd ML_provalue_undrisk
conda env create -f environment.yml
conda activate provalue
```

Coloca los tres archivos de datos en `data/raw/`, abre `oilygiant.ipynb` y selecciona el kernel `provalue`.

## Salvedades

- El encargo solo permite regresión lineal; en las Regiones 0 y 2 el error es cercano al 40 % de la media, así que un modelo no lineal podría cambiar la comparación.
- El precio por barril se toma como fijo; el análisis de sensibilidad muestra que la recomendación depende de que no baje.
- Las características `f0`, `f1` y `f2` no tienen significado declarado, por lo que el modelo no explica por qué un pozo tiene más reservas.
- Hay identificadores repetidos en los datos (10 en la Región 0, 4 en la Región 1 y 4 en la Región 2); se conservaron porque sus filas no son idénticas.

---

*Proyecto desarrollado como parte del bootcamp de Data Science de TripleTen.*

**Belem Cisneros Díaz** · [LinkedIn](https://www.linkedin.com/in/belemcisneros) · [github.com/he1109-ci3l0](https://github.com/he1109-ci3l0)
