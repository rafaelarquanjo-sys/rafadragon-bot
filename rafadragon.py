import requests
import os

API_KEY = os.environ.get("API_KEY")

headers = {
    "Content-Type": "application/json",
    "X-API-Key": API_KEY
}

def run():
    try:
        print("Verificando jogos...")
        r = requests.get("https://api.moltyroyale.com/api/games?status=waiting", timeout=10)
        data = r.json()

        if data["data"]:
            game_id = data["data"][0]["id"]
            print(f"JOGO ENCONTRADO: {game_id}")

            body = {"name": "Rafadragon"}

            reg = requests.post(
                f"https://api.moltyroyale.com/api/games/{game_id}/agents/register",
                headers=headers,
                json=body,
                timeout=10
            )

            print("Registrado:", reg.json())
        else:
            print("Nenhum jogo disponível.")

    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    run()
