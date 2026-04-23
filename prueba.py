import tweepy
from dotenv import load_dotenv
import os

# Cargar claves
load_dotenv()

API_KEY = os.getenv('TWITTER_API_KEY')
API_SECRET = os.getenv('TWITTER_API_SECRET')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

print("🔑 Probando conexión con Twitter...")

# Crear cliente
cliente = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

try:
    # Intentar obtener mi propio perfil (prueba simple)
    me = cliente.get_me()
    print("✅ ¡Conexión exitosa!")
    print(f"📱 Conectado como: @{me.data.username}")
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nPosibles causas:")
    print("- Access Token no generado aún")
    print("- Bearer Token tiene caracteres raros")
    print("- La app no tiene permisos correctos")
