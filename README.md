# Proyecto Esperanza (2025) · archivado

> **Aviso:** esto no es una herramienta clínica y no debe usarse para diagnosticar. Lo dejo publicado como registro de cómo empezó el proyecto.

En 2025, durante mi tratamiento de cáncer de mama, me fijé en que las imágenes de histología de mi propio tejido me recordaban a las muestras de minerales que llevaba años analizando como ingeniera de minas. De ahí salió este primer prototipo: una red convolucional pequeña y una aplicación web que clasificaba imágenes como benignas o malignas.

## Por qué lo he archivado

Revisé este trabajo con más rigor en octubre de 2026 y las cifras que publiqué entonces (precisión 82,17 %, AUC 90,35 %) **no están validadas**:
- la descripción de los datos no es coherente (el documento técnico cita Mini-MIAS, que son mamografías, y un conjunto «sintético», mientras que la aplicación trabaja con histología);
- no separé las imágenes por paciente, y así el modelo puede examinarse de pacientes que ya vio al entrenar;
- no hubo validación con un conjunto externo e independiente.

Por eso he retirado las cifras de la aplicación y he dejado avisos en los documentos. Prefiero decirlo claramente a que alguien se fíe de un número que no aguanta una revisión seria.

## Dónde sigue el proyecto

Esperanza continúa, ahora con variantes genéticas de BRCA1: un atlas que explica por qué cada variante rompe o no la proteína (estructura de AlphaFold, cálculo de estabilidad), contrastado con 1.694 variantes medidas en laboratorio (Findlay et al., Nature 2018). Cuando lo publique, enlazaré aquí la nueva versión.

## Contenido (histórico)

- `src/`: aplicación Flask del prototipo de 2025.
- `models/`: pesos del modelo de 2025 (sin validar).
- `docs/historia_personal.md`: cómo nació la idea.
- `docs/paper_tecnico.md`: documento técnico de 2025, con aviso.

## Autora

María Jesús Puerta Angulo · [mariajesuspuertaangulo.com](https://mariajesuspuertaangulo.com) · [LinkedIn](https://www.linkedin.com/in/mariajesuspuertaangulo)

Licencia MIT
