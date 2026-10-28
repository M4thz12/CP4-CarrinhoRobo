#!/usr/bin/env python3

from picar.SunFounder_PCA9685 import PCA9685
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from picar import back_wheels, front_wheels
import json
import threading


HOST = "0.0.0.0"
PORT = 8080
MOTOR_SPEED = 30


# ============================================================
# CONTROLE DO PICAR
# ============================================================

class PiCar:

    def __init__(self):
        self.bw = None
        self.fw = None
        self.initialized = False
        self.lock = threading.Lock()

    def init(self):

        with self.lock:

            if self.initialized:
                return

            print("Inicializando CarroZ...")


            self.pwm = PCA9685.PWM(bus_number=1, address=0x40)
            self.pwm.setup()

            print("PCA9685 OK")


            self.bw = back_wheels.Back_Wheels( debug=True )
            self.fw = front_wheels.Front_Wheels( debug=True )
            self.bw.speed = MOTOR_SPEED

            self.initialized = True

            print("Carro-Z inicializado.")

    def frente(self):

        self.init()

        with self.lock:
            print(">>> FRENTE")

            self.bw.speed = MOTOR_SPEED
            self.bw.backward()

    def tras(self):

        self.init()

        with self.lock:
            print(">>> TRÁS")

            self.bw.speed = MOTOR_SPEED
            self.bw.forward()

    def direita(self):

        self.init()

        with self.lock:
            print(">>> DIREITA")

            self.fw.turn_right()

    def esquerda(self):

        self.init()

        with self.lock:
            print(">>> ESQUERDA")

            self.fw.turn_left()

    def reto(self):

        self.init()

        with self.lock:
            print(">>> RETO")

            self.fw.turn_straight()

    def stop(self):

        if not self.initialized:
            return

        with self.lock:
            print(">>> STOP")

            self.bw.stop()

    def status(self):

        return {
            "initialized": self.initialized,
            "speed": MOTOR_SPEED
        }


# ============================================================
# OBJETO GLOBAL
# ============================================================

car = PiCar()


# ============================================================
# PÁGINA HTML
# ============================================================

HTML = """
<!DOCTYPE html>

<html lang="pt-br">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>Carro Z</title>

<style>

body {
    margin: 0;
    padding: 20px;

    font-family: Arial, sans-serif;

    background: #202124;
    color: white;

    text-align: center;
}

h1 {
    margin-bottom: 10px;
}

#status {

    margin: 15px auto;

    padding: 10px;

    width: 280px;

    background: #303134;

    border-radius: 8px;

    font-size: 18px;
}

.controls {

    width: 360px;

    max-width: 100%;

    margin: auto;
}

button {

    width: 100px;
    height: 70px;

    margin: 6px;

    border: none;

    border-radius: 12px;

    font-size: 18px;

    font-weight: bold;

    cursor: pointer;

    color: white;

    touch-action: manipulation;
}

button:active {

    transform: scale(0.94);
}


/* Movimento */

.forward,
.backward {

    background: #1976d2;
}


/* Direção */

.left,
.right,
.straight {

    background: #388e3c;
}


/* Stop */

.stop {

    background: #d32f2f;
}


/* Init */

.init {

    background: #616161;
    width: 220px;
}


/* Layout */

.row {

    display: flex;

    justify-content: center;

    align-items: center;
}

</style>

</head>


<body>

<h1>🚗 Carro Z</h1>

<div id="status">

    Aguardando...

</div>


<div class="controls">


    <!-- INIT -->

    <div class="row">

        <button class="init"
                onclick="zcommand('init');">

            INIT

        </button>

    </div>


    <!-- FRENTE -->

    <div class="row">

        <button class="forward"
                onclick="zcommand('frente');">

            ▲<br>
            FRENTE

        </button>

    </div>


    <!-- ESQUERDA / STOP / DIREITA -->

    <div class="row">

        <button class="left"
                onclick="zcommand('esquerda');">

            ◀<br>
            ESQUERDA

        </button>


        <button class="stop"
                onclick="zcommand('stop');">

            ■<br>
            STOP

        </button>


        <button class="right"
                onclick="zcommand('direita');">

            ▶<br>
            DIREITA

        </button>

    </div>


    <!-- TRÁS -->

    <div class="row">

        <button class="backward"
                onclick="zcommand('tras');">

            ▼<br>
            TRÁS

        </button>

    </div>


    <!-- RETO -->

    <div class="row">

        <button class="straight"
                onclick="zcommand('reto');">

            ↑<br>
            RETO

        </button>

    </div>

</div>


<script>


function zcommand(cmd) {

    const status =
        document.getElementById("status");


    status.innerHTML =
        "Enviando: " + cmd;

    console.log(status, cmd);

    fetch("/command/" + cmd)


        .then(response => {

            if (!response.ok) {

                throw new Error(
                    "HTTP " + response.status
                );

            }

            return response.json();

        })


        .then(data => {

            if (data.ok) {

                status.innerHTML =
                    "✓ " + data.command;

            } else {

                status.innerHTML =
                    "✗ " + data.error;

            }

        })


        .catch(error => {

            status.innerHTML =
                "Erro: " + error;

        });

}


</script>

</body>

</html>
"""


# ============================================================
# HTTP HANDLER
# ============================================================

class RequestHandler(BaseHTTPRequestHandler):


    def send_json(self, data):

        response = json.dumps(
            data,
            ensure_ascii=False
        ).encode("utf-8")


        self.send_response(200)


        self.send_header(
            "Content-Type",
            "application/json; charset=utf-8"
        )


        self.send_header(
            "Content-Length",
            str(len(response))
        )


        self.send_header(
            "Cache-Control",
            "no-cache"
        )


        self.end_headers()


        self.wfile.write(response)


    def send_html(self):

        response = HTML.encode("utf-8")


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


        self.wfile.write(response)


    def do_GET(self):

        path = urlparse(self.path).path


        # ----------------------------------------------------
        # PÁGINA INICIAL
        # ----------------------------------------------------

        if path == "/":

            self.send_html()

            return


        # ----------------------------------------------------
        # STATUS
        # ----------------------------------------------------

        if path == "/status":

            self.send_json(
                car.status()
            )

            return


        # ----------------------------------------------------
        # COMANDOS
        # ----------------------------------------------------

        if path.startswith("/command/"):

            command = path[
                len("/command/"):
            ].lower()


            try:

                if command == "init":

                    car.init()


                elif command == "frente":

                    car.frente()


                elif command == "tras":

                    car.tras()


                elif command == "direita":

                    car.direita()


                elif command == "esquerda":

                    car.esquerda()


                elif command == "reto":

                    car.reto()


                elif command == "stop":

                    car.stop()


                else:

                    self.send_json({

                        "ok": False,

                        "command": command,

                        "error":
                            "Comando desconhecido"

                    })

                    return


                self.send_json({

                    "ok": True,

                    "command": command

                })


            except Exception as e:

                print(
                    "ERRO no comando:",
                    command,
                    e
                )


                self.send_json({

                    "ok": False,

                    "command": command,

                    "error": str(e)

                })


            return


        # ----------------------------------------------------
        # 404
        # ----------------------------------------------------

        self.send_response(404)

        self.send_header(
            "Content-Type",
            "text/plain; charset=utf-8"
        )

        self.end_headers()

        self.wfile.write(
            b"404 - Not Found"
        )


    def log_message(self, format, *args):

        print(
            "[HTTP]",
            format % args
        )


# ============================================================
# MAIN
# ============================================================

def main():

    print()
    print("=" * 60)
    print("       SUNFOUNDER PICAR-V WEB SERVER")
    print("=" * 60)
    print()

    print(
        "Acesse: http://IP_DO_RASPBERRY:{}".format(PORT)
    )

    print()

    server = HTTPServer(
        (HOST, PORT),
        RequestHandler
    )


    try:

        server.serve_forever()


    except KeyboardInterrupt:

        print()
        print("Encerrando...")


        try:
            car.stop()

        except Exception:
            pass


        server.server_close()


if __name__ == "__main__":

    main()

