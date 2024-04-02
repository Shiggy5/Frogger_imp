import os
from supabase import create_client, Client

# Supabase-URL und API-Schlüssel aus Umgebungsvariablen laden
url = "https://fobkwrwilrrkrfpxntiz.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZvYmt3cndpbHJya3JmcHhudGl6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDgxODg2ODUsImV4cCI6MjAyMzc2NDY4NX0.xZKRGJPLqrWmky8h-fO-BsZQrD8R_G16tv96286Li8s"

# Supabase-Client initialisieren
supabase = create_client(url, key)

# Beispiel: Highscore in der Tabelle "highscores" speichern
def save_highscore(player_name, score):
    data, count = supabase.table("Highscore").insert({"name": player_name, "score": score}).execute()
    print(data)
    print(count)

# Beispielaufruf
save_highscore("Martin", 1)

def get_highscores():
    response = supabase.table("Highscore").select("*").order("score", desc=True).execute()
    print(response)
    highscores = response.data
    for rank, score in enumerate(highscores, start=1):
            print(f"{rank}. Player: {score['name']} - Score: {score['score']}")
# Beispielaufruf
get_highscores()