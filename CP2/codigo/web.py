```python
#!/usr/bin/env python3

import http.server
import socketserver
import json
import threading
import time
import os

from gpiozero import DistanceSensor

import joblib

from picar.SunFounder_PCA9685 import PCA9685
from picar import back_wheels, front_wheels


# ============================================================
# CONFIGURAÇÕES
# ============================================================

HOST = "0.0.0.0"
PORT = 8080

MOTOR_SPEED = 60

TRIGGER_PIN = 16
ECHO_PIN = 20

MODEL_PATH = "/home/pi/modelo_carro.pkl"

DISTANCIA_SEGURANCA = 20.0
DISTANCIA_LIBERAR = 40.0


# ============================================================
# VARIÁVEIS DO ML
# ============================================================

ml_bloqueado = False
ml_distancia = 999.0
ml_acao = "seguir"

movimento_atual = "parado"

ml_lock = threading.Lock()


# ============================================================
# SENSOR
# ============================================================

sensor_ml = DistanceSensor(
    echo=ECHO_PIN,
    trigger=TRIGGER_PIN,
    max_distance=2
)


# ============================================================
# MODELO
# ============================================================

modelo = None

try:
    modelo = joblib.load(MODEL_PATH)
    print("[ML] Modelo carregado com sucesso.")

except Exception as e:
    print("[ML] Erro ao carregar modelo:", e)


# ============================================================
# CLASSE DO CARRINHO
# ============================================================

class PiCar:

    def __init__(self):

        self.pwm = PCA9685.PWM(
            bus_number=1,
            address=0x40
        )

        self.pwm.setup()

        self.bw = back_wheels.Back_Wheels(
            debug=True
        )

        self.fw = front_wheels.Front_Wheels(
            debug=True
        )

        self.bw.speed = MOTOR_SPEED

        self.initialized = False

        print("[CAR] Carrinho criado.")

    # --------------------------------------------------------

    def init(self):

        if not self.initialized:

            self.bw.speed = MOTOR_SPEED

            self.initialized = True

            print("[CAR] Carrinho inicializado.")

    # --------------------------------------------------------

    def frente(self):

        global movimento_atual

        self.init()

        with ml_lock:

            bloqueado = ml_bloqueado

        if bloqueado:

            print(
                "[SEGURANCA] Avanço bloqueado pelo ML."
            )

            self.stop()

            return

        movimento_atual = "frente"

        self.bw.speed = MOTOR_SPEED

        # Mantém a orientação original do projeto
        self.bw.backward()

        print("[CAR] Frente.")

    # --------------------------------------------------------

    def tras(self):

        global movimento_atual

        self.init()

        movimento_atual = "tras"

        self.bw.speed = MOTOR_SPEED

        # Mantém a orientação original do projeto
        self.bw.forward()

        print("[CAR] Ré.")

    # --------------------------------------------------------

    def direita(self):

        self.init()

        self.fw.turn_right()

        print("[CAR] Direita.")

    # --------------------------------------------------------

    def esquerda(self):

        self.init()

        self.fw.turn_left()

        print("[CAR] Esquerda.")

    # --------------------------------------------------------

    def reto(self):

        self.init()

        self.fw.turn_straight()

        print("[CAR] Reto.")

    # --------------------------------------------------------

    def stop(self):

        global movimento_atual

        self.bw.stop()

        movimento_atual = "parado"

        print("[CAR] Parado.")

    # --------------------------------------------------------

    def status(self):

        with ml_lock:

            distancia = ml_distancia
            acao = ml_acao
            bloqueado = ml_bloqueado

        return {
            "initialized": self.initialized,
            "speed": MOTOR_SPEED,
            "distance_cm": round(
                distancia,
                2
            ),
            "ml_action": acao,
            "ml_blocked": bloqueado,
            "movement": movimento_atual
        }


# ============================================================
# INSTÂNCIA DO CARRINHO
# ============================================================

car = PiCar()


# ============================================================
# MONITORAMENTO DO SENSOR + ML
# ============================================================

def monitorar_obstaculo():

    global ml_bloqueado
    global ml_distancia
    global ml_acao

    print("[ML] Monitoramento iniciado.")

    while True:

        try:

            distancia = sensor_ml.distance * 100

            # Limita valores absurdos
            if distancia < 0:

                distancia = 0

            with ml_lock:

                ml_distancia = distancia

            # ------------------------------------------------
            # INFERÊNCIA
            # ------------------------------------------------

            acao = "seguir"

            if modelo is not None:

                try:

                    resultado = modelo.predict(
                        [[distancia]]
                    )

                    acao = str(
                        resultado[0]
                    )

                except Exception as e:

                    print(
                        "[ML] Erro na inferência:",
                        e
                    )

            with ml_lock:

                ml_acao = acao

            # ------------------------------------------------
            # SEGURANÇA
            # ------------------------------------------------

            # IMPORTANTE:
            # O ML só bloqueia quando o carrinho está indo
            # para frente.
            #
            # A RÉ continua disponível.

            if movimento_atual == "frente":

                if (
                    distancia <= DISTANCIA_SEGURANCA
                    or acao == "parar"
                ):

                    with ml_lock:

                        ml_bloqueado = True

                    print(
                        "[SEGURANCA] "
                        f"Obstáculo a {distancia:.1f} cm. "
                        "Parando."
                    )

                    car.stop()

                elif distancia >= DISTANCIA_LIBERAR:

                    with ml_lock:

                        ml_bloqueado = False

            else:

                # Fora do movimento para frente,
                # não bloqueia a ré nem os demais comandos.

                if distancia >= DISTANCIA_LIBERAR:

                    with ml_lock:

                        ml_bloqueado = False

            # ------------------------------------------------
            # INTERVALO
            # ------------------------------------------------

            time.sleep(0.05)

        except Exception as e:

            print(
                "[ML] Erro no monitoramento:",
                e
            )

            time.sleep(0.2)


# ============================================================
# HTML
# ============================================================

HTML = """
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width,
               initial-scale=1.0">

<title>Carro Z</title>

<style>

body {

    font-family: Arial, sans-serif;

    background: #f2f2f2;

    text-align: center;

    margin: 0;

    padding: 20px;
}

h1 {

    margin-bottom: 10px;
}

button {

    width: 140px;

    height: 60px;

    margin: 8px;

    font-size: 18px;

    border-radius: 12px;

    border: none;

    cursor: pointer;
}

button:active {

    transform: scale(0.95);
}

.frente {

    background: #4CAF50;

    color: white;
}

.tras {

    background: #2196F3;

    color: white;
}

.direcao {

    background: #9C27B0;

    color: white;
}

.stop {

    background: #f44336;

    color: white;
}

.info {

    background: white;

    border-radius: 12px;

    padding: 15px;

    margin: 20px auto;

    max-width: 400px;

    box-shadow:
        0 2px 8px
        rgba(0,0,0,0.1);
}

#status {

    font-size: 18px;

    line-height: 1.8;
}

</style>

</head>

<body>

<h1>Carro Z</h1>

<div>

<button
    class="frente"
    onclick="comando('frente')">
    Frente
</button>

</div>

<div>

<button
    class="direcao"
    onclick="comando('esquerda')">
    Esquerda
</button>

<button
    class="stop"
    onclick="comando('stop')">
    STOP
</button>

<button
    class="direcao"
    onclick="comando('direita')">
    Direita
</button>

</div>

<div>

<button
    class="tras"
    onclick="comando('tras')">
    Ré
</button>

</div>

<div>

<button
    class="direcao"
    onclick="comando('reto')">
    Reto
</button>

<button
    onclick="comando('init')">
    INIT
</button>

</div>

<div class="info">

<h2>Status</h2>

<div id="status">

Carregando...

</div>

</div>

<script>

function comando(cmd) {

    fetch(
        '/command/' + cmd
    )
    .then(
        response => response.json()
    )
    .then(
        data => {

            atualizarStatus();

        }
    )
    .catch(
        error => {

            console.log(error);

        }
    );
}


function atualizarStatus() {

    fetch('/status')

    .then(
        response => response.json()
    )

    .then(
        data => {

            document.getElementById(
                'status'
            ).innerHTML =

                'Distância: ' +
                data.distance_cm +
                ' cm<br>' +

                'Ação ML: ' +
                data.ml_action +
                '<br>' +

                'ML bloqueado: ' +
                data.ml_blocked +
                '<br>' +

                'Movimento: ' +
                data.movement +
                '<br>' +

                'Velocidade: ' +
                data.speed;

        }
    )

    .catch(
        error => {

            console.log(error);

        }
    );
}


setInterval(
    atualizarStatus,
    300
);

atualizarStatus();

</script>

</body>

</html>
"""


# ============================================================
# SERVIDOR HTTP
# ============================================================

class RequestHandler(
    http.server.BaseHTTPRequestHandler
):

    def _send_json(self, data):

        response = json.dumps(
            data
        ).encode("utf-8")

        self.send_response(200)

        self.send_header(
            "Content-Type",
            "application/json"
        )

        self.send_header(
            "Content-Length",
            str(len(response))
        )

        self.end_headers()

        self.wfile.write(
            response
        )

    # --------------------------------------------------------

    def _send_html(self):

        response = HTML.encode(
            "utf-8"
        )

        self.send_response(200)

        self.send_header(
            "Content-Type",
            "text/html; charset=utf-8"
        )

        self.send_header(
            "Content-Length",
            str(len(response))
        )

        self.end_headers()

        self.wfile.write(
            response
        )

    # --------------------------------------------------------

    def do_GET(self):

        path = self.path

        # --------------------------------------------
        # Página principal
        # --------------------------------------------

        if path == "/":

            self._send_html()

            return

        # --------------------------------------------
        # Status
        # --------------------------------------------

        if path == "/status":

            self._send_json(
                car.status()
            )

            return

        # --------------------------------------------
        # Comandos
        # --------------------------------------------

        if path.startswith(
            "/command/"
        ):

            comando = path[
                len("/command/"):
            ]

            try:

                if comando == "init":

                    car.init()

                elif comando == "frente":

                    car.frente()

                elif comando == "tras":

                    car.tras()

                elif comando == "direita":

                    car.direita()

                elif comando == "esquerda":

                    car.esquerda()

                elif comando == "reto":

                    car.reto()

                elif comando == "stop":

                    car.stop()

                else:

                    self._send_json(
                        {
                            "error":
                            "Comando inválido"
                        }
                    )

                    return

                self._send_json(
                    {
                        "success": True,
                        "command": comando
                    }
                )

            except Exception as e:

                print(
                    "[WEB] Erro:",
                    e
                )

                self._send_json(
                    {
                        "success": False,
                        "error": str(e)
                    }
                )

            return

        # --------------------------------------------
        # Página não encontrada
        # --------------------------------------------

        self.send_response(404)

        self.end_headers()


# ============================================================
# MAIN
# ============================================================

def main():

    print(
        f"[WEB] Iniciando servidor em "
        f"{HOST}:{PORT}"
    )

    # Thread do monitoramento ML
    thread_ml = threading.Thread(
        target=monitorar_obstaculo,
        daemon=True
    )

    thread_ml.start()

    # Servidor
    server = socketserver.ThreadingTCPServer(
        (HOST, PORT),
        RequestHandler
    )

    server.allow_reuse_address = True

    print(
        f"[WEB] Servidor disponível na porta {PORT}"
    )

    try:

        server.serve_forever()

    except KeyboardInterrupt:

        print(
            "\n[WEB] Encerrando..."
        )

    finally:

        try:

            car.stop()

        except Exception:
            pass

        try:

            sensor_ml.close()

        except Exception:
            pass

        server.server_close()


# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == "__main__":

    main()
```