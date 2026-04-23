# X (Twitter) Sentiment Analyzer con IA (BERT)

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-BERT-yellow.svg)](https://huggingface.co/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📌 ¿Qué hace este proyecto?

Aplicación de escritorio que **analiza sentimientos en tweets escritos en español** usando un modelo de Inteligencia Artificial **BERT** de Hugging Face con precisión del **87%**.

El proyecto incluye:
- Analizador de sentimientos con IA
- Generador de datasets masivos para pruebas
- Pruebas de conexión a X (Twitter)
- Interfaz gráfica profesional

---

## 📁 Explicación de cada archivo del proyecto

### 1. `analizadorX.py` - Aplicación principal

**¿Qué hace?**
Es el núcleo del proyecto. Crea una ventana con interfaz gráfica donde puedes:
- Cargar archivos CSV con tweets
- Buscar tweets por palabra clave
- Analizar sentimientos usando IA (BERT)
- Ver gráficos de resultados
- Exportar resultados a CSV

**Tecnologías que usa:** Tkinter, Hugging Face, Pandas, Matplotlib, Tweepy

**Cómo ejecutarlo:**
```bash
python analizadorX.py
```

**Lo que aprendes con este archivo:**
- Cómo crear interfaces gráficas profesionales en Python
- Cómo integrar un modelo de IA real en una aplicación
- Cómo procesar grandes volúmenes de texto
- Cómo manejar hilos (threading) para que la app no se congele

---

### 2. `CreadorDeTweets.py` - Generador de datasets

**¿Qué hace?**
Genera archivos CSV con tweets **falsos pero realistas** para poder probar el analizador sin necesidad de tener tweets reales de X (Twitter). Puede generar desde 10,000 hasta 500,000 tweets.

**¿Por qué es útil?**
- La API de X ya no es gratuita (cuesta $100/mes)
- Con este generador puedes probar el analizador con grandes volúmenes de datos
- Los tweets generados incluyen sentimientos variados (positivos, negativos, neutrales)

**Cómo ejecutarlo:**
```bash
python CreadorDeTweets.py
```
Luego elige una opción:
- 1 → 10,000 tweets (rápido)
- 2 → 50,000 tweets (mediano)
- 3 → 100,000 tweets (grande)
- 4 → 500,000 tweets (muy grande)

**Lo que aprendes con este archivo:**
- Cómo generar datos sintéticos para pruebas
- Cómo estructurar un dataset de texto
- Cómo trabajar con probabilidades y distribuciones
- Cómo guardar grandes volúmenes de datos en CSV

---

### 3. `test_modelo.py` - Prueba del modelo de IA

**¿Qué hace?**
Un script **independiente** que solo carga el modelo de IA y prueba su funcionamiento con 3 ejemplos (positivo, negativo, neutral). No necesita interfaz gráfica ni archivos CSV.

**¿Para qué sirve?**
- Verificar que el modelo de IA está correctamente instalado
- Probar rápidamente si la librería Hugging Face funciona
- Depurar problemas sin abrir la aplicación completa

**Cómo ejecutarlo:**
```bash
python test_modelo.py
```

**Salida esperada:**
```text
📥 Cargando modelo...
📊 Resultados:
Texto: Me encanta este producto, es increíble
Resultado: {'label': '5 stars', 'score': 0.98}

Texto: Lo odio, pésima calidad
Resultado: {'label': '1 star', 'score': 0.95}
```

**Lo que aprendes con este archivo:**
- Cómo probar componentes de forma aislada
- Cómo verificar la instalación de modelos de IA
- Cómo interpretar la salida del modelo BERT

---

### 4. `prueba.py` - Prueba de conexión a X (Twitter)

**¿Qué hace?**
Verifica que puedes **conectarte a X (Twitter)** con tus credenciales (API Key, Access Token, etc.). No busca tweets, solo comprueba que la autenticación funciona.

**¿Para qué sirve?**
- Confirmar que tu app de desarrollador está bien configurada
- Verificar que las claves del archivo `.env` son correctas
- Solucionar problemas de conexión antes de usar la app principal

**Cómo ejecutarlo:**
```bash
python prueba.py
```

**Salida esperada (si funciona):**
```text
🔑 Probando conexión con Twitter...
✅ ¡Conexión exitosa!
📱 Conectado como: @tu_usuario
```

**Salida esperada (si NO funciona):**
```text
❌ Error: 403 Forbidden
```
(Esto significa que no tienes permisos de búsqueda, lo cual es normal si no pagas)

**Lo que aprendes con este archivo:**
- Cómo autenticarse en APIs modernas (OAuth)
- Cómo manejar variables de entorno (archivo `.env`)
- Cómo interpretar errores de API (403, 401, etc.)

---

### 5. `requirements.txt` - Dependencias del proyecto

**¿Qué contiene?**
La lista de librerías necesarias para ejecutar el proyecto:

```txt
torch               # Motor de deep learning
transformers        # Modelos de Hugging Face
sentencepiece       # Tokenizador para BERT
tweepy              # Conexión a X (Twitter)
textblob            # NLP básico (fallback)
pandas              # Manejo de datos CSV
matplotlib          # Gráficos
python-dotenv       # Variables de entorno
```

**Cómo instalarlas:**
```bash
pip install -r requirements.txt
```

**Lo que aprendes:**
- Cómo gestionar dependencias en Python
- Qué librerías se usan en proyectos de IA

---

### 6. `.gitignore` - Archivos que NO se suben a GitHub

**¿Qué hace?**
Evita que archivos privados o innecesarios se suban al repositorio:

```gitignore
.env        # Tus claves secretas (¡NUNCA se suben!)
*.csv       # Datos grandes (opcional)
__pycache__ # Archivos temporales de Python
```

**Lo que aprendes:**
- Buenas prácticas de seguridad al compartir código
- Cómo mantener el repositorio limpio y profesional

---

## 🧠 El modelo de IA (BERT)

El proyecto usa el modelo `nlptown/bert-base-multilingual-uncased-sentiment`:

| Característica | Valor |
|----------------|-------|
| Entrenado con | +500,000 opiniones en 6 idiomas |
| Precisión en español | ~87% |
| Tamaño | 1.2 GB |
| Salida | 1-5 estrellas (convertido a positivo/negativo/neutral) |

---

## 🚀 Instalación completa (paso a paso)

```bash
# 1. Clonar el repositorio
git clone https://github.com/ChristianLera/X-sentiment-analyzer.git
cd X-sentiment-analyzer

# 2. Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. (Opcional) Probar que el modelo funciona
python test_modelo.py

# 5. (Opcional) Probar conexión a X
python prueba.py

# 6. (Opcional) Generar dataset de prueba
python CreadorDeTweets.py

# 7. Ejecutar la aplicación principal
python analizadorX.py
```

---

## 📊 Flujo de trabajo recomendado

```text
1. Ejecutas prueba.py → Verificas que puedes conectar a X
2. Ejecutas test_modelo.py → Verificas que la IA funciona
3. Ejecutas CreadorDeTweets.py → Generas datos para probar
4. Ejecutas analizadorX.py → Analizas sentimientos
```

---

## ⚠️ Limitaciones conocidas

| Limitación | Explicación | Solución |
|------------|-------------|----------|
| Búsqueda en X | Requiere plan de pago de X ($100/mes) | Usar el generador `CreadorDeTweets.py` para pruebas |
| Sarcasmo | El modelo no detecta ironía compleja | Limitación de todos los modelos actuales |
| Memoria RAM | El modelo necesita ~2 GB | Cerrar otros programas o usar modelo más ligero |

---

## 🚧 Líneas de expansión (trabajo futuro)

Este proyecto es **completo y funcional**. Las siguientes ideas son extensiones naturales que no se implementaron por:
- **Tiempo** (el proyecto ya demuestra las habilidades clave)
- **Enfoque** (prioricé un MVP funcional sobre features adicionales)

| Idea | Dificultad | ¿Por qué no está? |
|------|------------|-------------------|
| API REST | Media | El enfoque fue desktop, pero el modelo está listo |
| Dashboard web | Alta | Requiere frontend (React) - fuera del alcance |
| Análisis de emociones | Baja | Se puede hacer con otro modelo de HF |

---

## 👤 Autor

**Christian Lera**

- GitHub: [@ChristianLera](https://github.com/ChristianLera)

---

## 📄 Licencia

MIT License - Puedes usar, modificar y distribuir este código libremente.

---

## ⭐ ¿Te gustó?

Dale una estrella ⭐ en GitHub. ¡Me ayuda mucho!
