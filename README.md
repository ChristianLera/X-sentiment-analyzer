# X (Twitter) Sentiment Analyzer con IA (BERT)

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-BERT-yellow.svg)](https://huggingface.co/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## ¿Qué hace este proyecto?

Aplicación de escritorio que **analiza sentimientos en tweets escritos en español** usando un modelo de Inteligencia Artificial (BERT) de Hugging Face.

## Tecnologías utilizadas

- **Python 3.11** - Lenguaje principal
- **Hugging Face Transformers** - Modelo BERT
- **PyTorch** - Motor de deep learning
- **Tkinter** - Interfaz gráfica
- **Pandas** - Manejo de datos CSV
- **Matplotlib** - Gráficos
- **Tweepy** - Conexión a API de X (Twitter)

## El modelo de IA

| Característica | Valor |
|----------------|-------|
| Modelo | BERT multilingual |
| Entrenado con | +500,000 opiniones |
| Precisión en español | 87% |
| Tamaño | 1.2 GB |

## Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/ChristianLera/X-sentiment-analyzer.git
cd X-sentiment-analyzer

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar
python analizadorX.py
