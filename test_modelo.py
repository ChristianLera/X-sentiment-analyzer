from transformers import pipeline

print("=" * 50)
print("Probando modelo de IA...")
print("=" * 50)

# Probar modelo multilingual
print("\n📥 Cargando modelo (puede tomar 1-2 minutos en la PRIMERA vez)...")
classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Probar en español
textos = [
    "Me encanta este producto, es increíble",
    "Lo odio, pésima calidad",
    "Está bien, normal"
]

print("\n📊 Resultados:\n")
for texto in textos:
    resultado = classifier(texto)
    print(f"Texto: {texto}")
    print(f"Resultado: {resultado[0]}\n")

print("✅ Modelo funcionando correctamente!")
