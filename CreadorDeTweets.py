import pandas as pd
import random
from datetime import datetime, timedelta
import numpy as np

class GeneradorDatasetTwitter:
    def __init__(self):
        # ========== CATEGORÍAS PRINCIPALES ==========
        self.categorias = {
            "Tecnología": 35,      # Porcentaje de aparición
            "Entretenimiento": 25,
            "Deportes": 15,
            "Actualidad": 15,
            "Estilo de vida": 10
        }
        
        # ========== PRODUCTOS Y TEMAS ==========
        self.productos = {
            "Tecnología": ["Python", "JavaScript", "ChatGPT", "Tesla", "iPhone", "Android", 
                          "Windows", "Mac", "Linux", "GitHub", "VS Code", "Docker", "AWS", 
                          "Netflix", "Spotify", "Twitter", "Instagram", "TikTok", "WhatsApp",
                          "Zoom", "Slack", "Discord", "Telegram", "Gmail", "Google Drive"],
            
            "Entretenimiento": ["Netflix", "Disney+", "HBO Max", "Prime Video", "YouTube", 
                               "Spotify", "Apple Music", "TikTok", "Twitch", "Fortnite", 
                               "Minecraft", "GTA", "Call of Duty", "FIFA", "League of Legends"],
            
            "Deportes": ["Messi", "Cristiano", "Real Madrid", "Barcelona", "NBA", "Lakers",
                        "Fórmula 1", "Verstappen", "Hamilton", "Tennis", "Nadal", "Djokovic",
                        "UEFA", "Champions", "Mundial", "Super Bowl", "Boxeo"],
            
            "Actualidad": ["Política", "Economía", "Clima", "Salud", "Educación", 
                          "Trabajo", "Inflación", "Empleo", "Crisis", "Elecciones"],
            
            "Estilo de vida": ["Café", "Yoga", "Gimnasio", "Running", "Meditación", 
                              "Cocina", "Viajes", "Moda", "Mascotas", "Jardinería"]
        }
        
        # ========== ADJETIVOS Y EXPRESIONES ==========
        self.adjetivos_pos = [
            "increíble", "genial", "fantástico", "excelente", "maravilloso", "espectacular",
            "brillante", "asombroso", "perfecto", "sensacional", "extraordinario", "magnífico",
            "estupendo", "fabuloso", "impresionante", "formidable", "óptimo", "superior"
        ]
        
        self.adjetivos_neg = [
            "terrible", "malo", "horrible", "pésimo", "frustrante", "decepcionante",
            "ridículo", "inaceptable", "desastroso", "lamentable", "deplorable", "detestable",
            "mediocre", "deficiente", "regular", "mejorable", "obsoleto", "caro"
        ]
        
        self.adjetivos_neu = [
            "interesante", "normal", "común", "regular", "típico", "habitual",
            "corriente", "estándar", "básico", "simple", "sencillo", "directo"
        ]
        
        # ========== VERBOS Y ACCIONES ==========
        self.verbos_pos = [
            "funciona", "anda", "sirve", "ayuda", "mejora", "optimiza", "facilita",
            "resuelve", "simplifica", "acelera", "potencia", "transforma", "revoluciona"
        ]
        
        self.verbos_neg = [
            "falla", "crashea", "laguea", "tilda", "empeora", "complica", "frustra",
            "estresa", "molesta", "desespera", "aburre", "decepciona", "defrauda"
        ]
        
        # ========== INTENSIFICADORES ==========
        self.intensificadores = [
            "muy", "bastante", "extremadamente", "increíblemente", "realmente",
            "absolutamente", "totalmente", "completamente"
        ]
        
        # ========== EMOJIS ==========
        self.emojis_pos = ["😊", "🎉", "❤️", "🔥", "✨", "👍", "💪", "🚀", "⭐", "🎯"]
        self.emojis_neg = ["😞", "💔", "🤬", "👎", "😤", "💀", "😡", "🤮", "😠", "💢"]
        self.emojis_neu = ["😐", "🤔", "💭", "📝", "👀", "ℹ️", "🔍", "📌", "✍️", "💡"]
        
        # ========== ESTRUCTURAS DE TWEETS ==========
        self.estructuras_pos = [
            "{producto} es {adjetivo}, {verbo} perfectamente",
            "Me encanta {producto}, {adjetivo} experiencia",
            "¡{intensificador} {adjetivo}! {producto} {verbo} de maravilla",
            "Recomiendo {producto} a todos, {adjetivo} calidad",
            "{producto} {verbo} excelente, muy {adjetivo}",
            "Contento con {producto}, {adjetivo} decisión",
            "¡{producto} es lo mejor! {adjetivo} {emoji}",
            "{intensificador} {adjetivo} {producto}, {verbo} genial",
            "No puedo vivir sin {producto}, {adjetivo} herramienta",
            "{producto} superó mis expectativas, {adjetivo}"
        ]
        
        self.estructuras_neg = [
            "{producto} es {adjetivo}, {verbo} mal",
            "Odio {producto}, {adjetivo} experiencia {emoji}",
            "¡{intensificador} {adjetivo}! {producto} no {verbo} bien",
            "No recomiendo {producto}, {adjetivo} calidad",
            "{producto} {verbo} fatal, muy {adjetivo}",
            "Decepcionado con {producto}, {adjetivo} producto",
            "¡Qué {adjetivo} está {producto}! {emoji}",
            "{intensificador} {adjetivo} {producto}, {verbo} cada vez peor",
            "El servicio de {producto} es {adjetivo}",
            "{producto} es una estafa, {adjetivo}"
        ]
        
        self.estructuras_neu = [
            "{producto} está {adjetivo} hoy",
            "Vi algo sobre {producto}, parece {adjetivo}",
            "Hoy usé {producto}, {adjetivo} experiencia",
            "{producto} tiene opiniones {adjetivo}",
            "El precio de {producto} está {adjetivo}",
            "Sin novedades sobre {producto}, todo {adjetivo}",
            "Probé {producto}, resultado {adjetivo}",
            "La competencia de {producto} está {adjetivo}",
            "Mencionaron {producto} en las noticias",
            "Habrá actualizaciones de {producto} pronto"
        ]
    
    def generar_tweet(self):
        """Genera un tweet realista"""
        
        # Elegir categoría según porcentaje
        categoria = random.choices(
            list(self.categorias.keys()),
            weights=list(self.categorias.values())
        )[0]
        
        # Elegir producto de la categoría
        producto = random.choice(self.productos[categoria])
        
        # Determinar sentimiento (distribución realista)
        sentimiento = random.choices(
            ["positivo", "negativo", "neutral"],
            weights=[45, 35, 20]  # 45% positivos, 35% negativos, 20% neutrales
        )[0]
        
        # Generar tweet según sentimiento
        if sentimiento == "positivo":
            adjetivo = random.choice(self.adjetivos_pos)
            verbo = random.choice(self.verbos_pos)
            intensificador = random.choice(self.intensificadores)
            emoji = random.choice(self.emojis_pos)
            estructura = random.choice(self.estructuras_pos)
            
            tweet = estructura.format(
                producto=producto,
                adjetivo=adjetivo,
                verbo=verbo,
                intensificador=intensificador,
                emoji=emoji
            )
            
        elif sentimiento == "negativo":
            adjetivo = random.choice(self.adjetivos_neg)
            verbo = random.choice(self.verbos_neg)
            intensificador = random.choice(self.intensificadores)
            emoji = random.choice(self.emojis_neg)
            estructura = random.choice(self.estructuras_neg)
            
            tweet = estructura.format(
                producto=producto,
                adjetivo=adjetivo,
                verbo=verbo,
                intensificador=intensificador,
                emoji=emoji
            )
            
        else:  # neutral
            adjetivo = random.choice(self.adjetivos_neu)
            estructura = random.choice(self.estructuras_neu)
            
            tweet = estructura.format(
                producto=producto,
                adjetivo=adjetivo
            )
        
        # Añadir hashtags ocasionalmente (30% de los tweets)
        if random.random() < 0.3:
            hashtags = [f"#{producto.replace(' ', '')}", f"#{sentimiento}"]
            tweet += f" {random.choice(hashtags)}"
        
        # Añadir menciones ocasionalmente (15% de los tweets)
        if random.random() < 0.15:
            tweet += f" @{random.choice(['usuario', 'cliente', 'fan', 'seguidor'])}{random.randint(1, 999)}"
        
        return tweet, sentimiento, categoria, producto
    
    def generar_dataset(self, cantidad=100000):
        """Genera dataset masivo"""
        
        print("=" * 60)
        print(f"📊 GENERANDO DATASET DE {cantidad:,} TWEETS")
        print("=" * 60)
        
        tweets_data = []
        
        # Estadísticas de progreso
        stats = {"positivo": 0, "negativo": 0, "neutral": 0}
        categorias_stats = {cat: 0 for cat in self.categorias.keys()}
        
        for i in range(cantidad):
            # Generar tweet
            tweet, sentimiento, categoria, producto = self.generar_tweet()
            
            # Actualizar estadísticas
            stats[sentimiento] += 1
            categorias_stats[categoria] += 1
            
            # Añadir datos
            tweets_data.append({
                'id': i + 1,
                'texto': tweet,
                'sentimiento_generado': sentimiento,
                'categoria': categoria,
                'producto': producto,
                'longitud': len(tweet),
                'tiene_hashtag': '#' in tweet,
                'tiene_mencion': '@' in tweet
            })
            
            # Mostrar progreso cada 10,000 tweets
            if (i + 1) % 10000 == 0:
                porcentaje = ((i + 1) / cantidad) * 100
                print(f"   Progreso: {i+1:,} tweets ({porcentaje:.1f}%)")
        
        # Crear DataFrame
        df = pd.DataFrame(tweets_data)
        
        # Añadir fecha aleatoria (últimos 30 días)
        fechas = []
        for _ in range(cantidad):
            fecha = datetime.now() - timedelta(days=random.randint(0, 30))
            fechas.append(fecha)
        df['fecha'] = fechas
        
        # Guardar CSV
        nombre_archivo = f'dataset_twitter_{cantidad:,}.csv'.replace(',', '')
        df.to_csv(nombre_archivo, index=False, encoding='utf-8-sig')
        
        # Mostrar estadísticas finales
        print("\n" + "=" * 60)
        print("📈 ESTADÍSTICAS DEL DATASET")
        print("=" * 60)
        
        print(f"\n✅ Archivo guardado: {nombre_archivo}")
        print(f"📊 Total de tweets: {len(df):,}")
        print(f"📋 Columnas: {', '.join(df.columns)}")
        
        print("\n📊 Distribución de sentimientos:")
        for sentimiento, count in stats.items():
            porcentaje = (count / cantidad) * 100
            emoji = "😊" if sentimiento == "positivo" else "😞" if sentimiento == "negativo" else "😐"
            print(f"   {emoji} {sentimiento.capitalize()}: {count:,} ({porcentaje:.1f}%)")
        
        print("\n📂 Distribución por categoría:")
        for categoria, count in categorias_stats.items():
            porcentaje = (count / cantidad) * 100
            print(f"   📌 {categoria}: {count:,} ({porcentaje:.1f}%)")
        
        # Mostrar ejemplos
        print("\n📝 EJEMPLOS DE TWEETS GENERADOS:")
        print("-" * 60)
        
        for sentimiento in ['positivo', 'negativo', 'neutral']:
            muestra = df[df['sentimiento_generado'] == sentimiento].head(3)
            print(f"\n{sentimiento.upper()}:")
            for _, row in muestra.iterrows():
                print(f"   • {row['texto'][:100]}...")
        
        # Guardar estadísticas en archivo separado
        stats_df = pd.DataFrame({
            'metrico': ['Total tweets', 'Positivos', 'Negativos', 'Neutrales'] + list(categorias_stats.keys()),
            'valor': [len(df), stats['positivo'], stats['negativo'], stats['neutral']] + list(categorias_stats.values())
        })
        stats_df.to_csv('estadisticas_dataset.csv', index=False)
        
        print("\n✅ Archivos generados exitosamente:")
        print(f"   📁 {nombre_archivo}")
        print(f"   📁 estadisticas_dataset.csv")
        
        return df

# ========== FUNCIONES ADICIONALES ÚTILES ==========

def dividir_dataset(archivo_original, num_partes=5):
    """Divide un dataset grande en partes más pequeñas"""
    df = pd.read_csv(archivo_original)
    chunk_size = len(df) // num_partes
    
    for i in range(num_partes):
        inicio = i * chunk_size
        fin = inicio + chunk_size if i < num_partes - 1 else len(df)
        df_part = df.iloc[inicio:fin]
        df_part.to_csv(f'dataset_parte_{i+1}.csv', index=False)
    
    print(f"✅ Dataset dividido en {num_partes} partes")

def mezclar_dataset(archivo_original):
    """Mezcla aleatoriamente los tweets"""
    df = pd.read_csv(archivo_original)
    df_mezclado = df.sample(frac=1).reset_index(drop=True)
    df_mezclado.to_csv('dataset_mezclado.csv', index=False)
    print("✅ Dataset mezclado")

# ========== EJECUTAR GENERACIÓN ==========

if __name__ == "__main__":
    # Crear generador
    generador = GeneradorDatasetTwitter()
    
    # Preguntar tamaño
    print("\n🎯 GENERADOR DE DATASET DE TWITTER")
    print("-" * 40)
    print("¿Cuántos tweets quieres generar?")
    print("1. 10,000 tweets (rápido)")
    print("2. 50,000 tweets (mediano)")
    print("3. 100,000 tweets (grande)")
    print("4. 500,000 tweets (muy grande - puede tardar)")
    
    opcion = input("\nElige una opción (1-4): ")
    
    tamanos = {
        '1': 10000,
        '2': 50000,
        '3': 100000,
        '4': 500000
    }
    
    cantidad = tamanos.get(opcion, 100000)
    
    # Confirmar
    print(f"\n⚠️ Vas a generar {cantidad:,} tweets. ¿Continuar? (s/n)")
    confirmar = input()
    
    if confirmar.lower() == 's':
        # Generar dataset
        df = generador.generar_dataset(cantidad)
        
        print("\n🎉 ¡DATASET GENERADO CON ÉXITO!")
        print("\n💡 Ahora puedes:")
        print("   1. Abrir tu analizador Tkinter")
        print("   2. Cargar el archivo CSV generado")
        print("   3. Analizar los sentimientos")
    else:
        print("Cancelado. Ejecuta de nuevo cuando quieras.")
