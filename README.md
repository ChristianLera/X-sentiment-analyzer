# X (Twitter) Sentiment Analyzer

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-BERT-yellow.svg)](https://huggingface.co/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code style](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/psf/black)

## 📌 ¿Qué hace este proyecto?

Aplicación de escritorio que **analiza sentimientos en tweets escritos en español** usando un modelo de Inteligencia Artificial **BERT** de Hugging Face con una precisión del **87%**.

## 🎯 ¿Para qué sirve?

| Área | Aplicación |
|------|-------------|
| Marketing | Analizar reacciones a lanzamientos de productos |
| Competencia | Comparar percepción entre marcas |
| Investigación | Estudiar tendencias de opinión pública |

## 🛠️ Tecnologías

| Tecnología | Uso |
|------------|-----|
| Python 3.11 | Lenguaje principal |
| Hugging Face Transformers | Modelo BERT |
| PyTorch | Motor de deep learning |
| Tkinter | Interfaz gráfica |
| Pandas | Manejo de datos CSV |
| Matplotlib | Visualización |
| Tweepy | API de X (Twitter) |

## 🧠 El modelo de IA

| Característica | Valor |
|----------------|-------|
| Modelo | `nlptown/bert-base-multilingual-uncased-sentiment` |
| Entrenado con | +500,000 opiniones (incluye español) |
| Precisión | ~87% |
| Tamaño | 1.2 GB |

## 🚀 Instalación

```bash
# 1. Clonar
git clone https://github.com/ChristianLera/X-sentiment-analyzer.git
cd X-sentiment-analyzer

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar
python analizadorX.py
