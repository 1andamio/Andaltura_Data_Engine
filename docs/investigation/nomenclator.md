# Investigación · Nomenclátor Geográfico de Andalucía

**Fecha:** 24/07/2026

## Objetivo

Analizar el funcionamiento del buscador oficial del Nomenclátor Geográfico de Andalucía para construir un proveedor reutilizable en Primer.

---

# Estado actual

## ✔ Búsqueda reproducida correctamente

URL:

https://www.ideandalucia.es/nomenclator/enlace.jsp?lang=esp

Se ha conseguido reproducir la búsqueda utilizando `requests.Session()`.

Consulta de prueba:

granada

Resultado:

215 coincidencias.

---

# Descubrimientos

- La primera búsqueda se realiza mediante **POST**.
- La paginación utiliza **GET**.
- Cada página devuelve 10 resultados.
- Cada resultado contiene:
  - Identificador NGA.
  - Nombre.
  - Tipo.
  - Coordenadas UTM.
  - Enlace a la ficha individual.

---

# Archivos utilizados

examples/test_search_form.py

examples/test_search_post.py

data/debug/resultado.html

---

# Próximos pasos

- Analizar `entidadConcreta.jsp`.
- Crear el parser de resultados.
- Implementar `NomenclatorProvider`.
- Descargar todas las páginas automáticamente.
- Extraer la ficha completa de cada entidad.