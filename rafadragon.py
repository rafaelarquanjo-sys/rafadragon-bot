import requests
import time

API_KEY = "mr_live_cwGRZzU9mbPhlj9XGE2NgxSp5SVlZbOE"

headers = {
    "Content-Type": "application/json",
    "X-API-Key": API_KEY
}

while True:
    try:
        print("Verificando jogos...")
        r = requests.get("https://api.moltyroyale.com/api/games?status=waiting")
        data = r.json()

        if data["data"]:
            game_id = data["data"][0]["id"]
            print(f"JOGO ENCONTRADO: {game_id}")

            body = {
                "name": "Rafadragon"
            }

            reg = requests.post(
                f"https://api.moltyroyale.com/api/games/{game_id}/agents/register",
                headers=headers,
                json=body
            )

            print("Registrado:", reg.json())
            time.sleep(60)

        else:
            print("Nenhum jogo disponível.")

    except Exception as e:
        print("Erro:", e)

    time.sleep(5)
