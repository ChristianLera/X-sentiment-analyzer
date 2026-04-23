# X (Twitter) Sentiment Analyzer con IA (BERT)

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-BERT-yellow.svg)](https://huggingface.co/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📌 ¿Qué hace este proyecto?

Aplicación de escritorio que **analiza sentimientos en tweets escritos en español** usando un modelo de Inteligencia Artificial **BERT** de Hugging Face con precisión del **87%**.

## 🛠️ Tecnologías utilizadas

| Tecnología | Uso |
|------------|-----|
| Python 3.11 | Lenguaje principal |
| Hugging Face Transformers | Modelo BERT |
| PyTorch | Motor de deep learning |
| Tkinter | Interfaz gráfica |
| Pandas | Manejo de datos CSV |
| Matplotlib | Gráficos |
| Tweepy | API de X (Twitter) |

## 🚀 Instalación

```bash
git clone https://github.com/ChristianLera/X-sentiment-analyzer.git
cd X-sentiment-analyzer
pip install -r requirements.txt
python analizadorX.py
```

## 📊 Ejemplo de resultado

```text
📈 RESULTADOS DEL ANÁLISIS CON IA
🔍 Palabra buscada: 'Messi'
📊 Total: 5,234 tweets

😊 POSITIVOS: 3,245 (62.0%)
😞 NEGATIVOS: 1,412 (27.0%)
😐 NEUTRALES: 577 (11.0%)
```

## 📁 Estructura

```text
X-sentiment-analyzer/
├── analizadorX.py        # App principal
├── CreadorDeTweets.py    # Generador de datasets
├── test_modelo.py        # Prueba del modelo
├── prueba.py             # Prueba conexión X
├── requirements.txt      # Dependencias
├── .gitignore           # Archivos ignorados
└── README.md            # Documentación
```

## ⚠️ Limitaciones

- Búsqueda en X requiere plan de pago ($100/mes)
- El modelo no detecta sarcasmo complejo

## 👤 Autor

**Christian Lera**

- GitHub: [@ChristianLera](https://github.com/ChristianLera)

## 📄 Licencia

MIT License

# 3. Ejecutar
python analizadorX.py
