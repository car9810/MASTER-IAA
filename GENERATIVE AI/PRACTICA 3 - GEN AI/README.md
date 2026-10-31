# GenAI Marketing Studio

Prototipo académico de una aplicación web para una agencia de marketing y publicidad.

## Funcionalidades

- Generación de imágenes con Stability AI Stable Diffusion 3.5 Large mediante Amazon Bedrock.
- Selección de estilos y formato.
- Galería de imágenes y descarga.
- Edición de contenido con Anthropic Claude:
  - resumir,
  - ampliar,
  - corregir,
  - generar variaciones.
- Historial de versiones.
- Comparación y restauración de versiones.
- Roles: Diseñador, Redactor y Aprobador.
- Comentarios y notas.
- Moderación básica y protección frente a prompt injection.
- Apartado específico de ética y seguridad.

## 1. Instalar Python

Se recomienda Python 3.10 o superior.

## 2. Crear un entorno virtual

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 4. Configurar AWS

Debes disponer de acceso a Amazon Bedrock en la región configurada y permiso para invocar:

- Anthropic Claude.
- Stability AI Stable Diffusion 3.5 Large.

Puedes configurar las credenciales mediante AWS CLI/IAM o mediante los mecanismos de autenticación permitidos por tu cuenta.

Las variables configurables aparecen en `.env.example`.

> Nota: este prototipo no carga automáticamente un archivo `.env`. Puedes crear las variables de entorno en Windows o cambiar temporalmente los valores al comienzo de `app.py`.

## 5. Ejecutar

```bash
streamlit run app.py
```

Streamlit mostrará una dirección local, normalmente:

```text
http://localhost:8501
```

## 6. Pruebas sugeridas

### Generación de imagen
Descripción:

```text
Unas zapatillas sostenibles blancas fabricadas con materiales reciclados sobre un fondo natural con vegetación.
```

Prueba los estilos:
- Realismo
- Anime
- Pintura al óleo
- Minimalista

### Edición de contenido
Texto:

```text
Descubre nuestra nueva colección de zapatillas sostenibles fabricadas con materiales reciclados. Diseñadas para combinar comodidad, estilo y respeto por el medio ambiente.
```

Prueba:
- Resumir
- Ampliar
- Corregir
- Variaciones

### Historial
Genera varias versiones, entra en "Historial" y prueba:
- seleccionar una versión,
- comparar dos versiones,
- restaurar una versión.

### Roles
- Diseñador: imágenes.
- Redactor: edición de contenido.
- Aprobador: revisión de ambos apartados.

## Limitaciones del prototipo

El proyecto demuestra los requisitos académicos de forma sencilla. Para un sistema empresarial real se deberían añadir autenticación robusta, cifrado gestionado, almacenamiento cloud, Bedrock Guardrails, auditoría avanzada y permisos persistentes gestionados.
