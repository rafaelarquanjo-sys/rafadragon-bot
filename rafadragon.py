import requests
import os
import time

API_KEY = os.environ.get("API_KEY")

headers = {
    "Content-Type": "application/json",
    "X-API-Key": API_KEY
}

def run():
    for tentativa in range(3):  # tenta até 3 vezes
        try:
            print("Verificando jogos...")
            
            r = requests.get(
                "https://api.moltyroyale.com/api/games?status=waiting",
                timeout=20
            )
            
            data = r.json()

            if data["data"]:
                game_id = data["data"][0]["id"]
                print(f"JOGO ENCONTRADO: {game_id}")

                body = {"name": "Rafadragon"}

                reg = requests.post(
                    f"https://api.moltyroyale.com/api/games/{game_id}/agents/register",
                    headers=headers,
                    json=body,
                    timeout=20
                )

                print("Registrado:", reg.json())
            else:
                print("Nenhum jogo disponível.")

            return

        except Exception as e:
            print(f"Tentativa {tentativa+1} falhou:", e)
            time.sleep(5)

    print("Falhou após 3 tentativas.")

if __name__ == "__main__":
    run()
