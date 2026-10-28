# Software — Carro Z

## Visão geral

O controle do carrinho é feito via **Wi-Fi**, sem necessidade de app externo: a Raspberry Pi cria um hotspot próprio e serve uma página web com os controles, acessível por qualquer celular/notebook conectado à rede.

```
[Celular/Notebook] --Wi-Fi--> [Hotspot "CarroZ" na Raspberry Pi]
                                        |
                                        v
                              [Servidor web (web.py:8080)]
                                        |
                                        v
                          [Biblioteca picar -> PCA9685 -> Motores]
```

## Arquivos

| Arquivo | Função |
|---|---|
| `init_hotspot.sh` | Cria o hotspot Wi-Fi `CarroZ` (interface `wlan1`, IP `10.0.0.1`) usando `nmcli`, para permitir controle remoto sem depender de rede externa |
| `carroz.service` | Serviço systemd que inicia `web.py` automaticamente no boot da Raspberry Pi (com restart automático em caso de falha) |
| `web.py` | Servidor HTTP (porta 8080) que serve a interface web de controle e expõe endpoints `/command/<ação>` (frente, tras, direita, esquerda, reto, stop, init) |
| `z_init.py` | Teste isolado: inicialização do controlador PCA9685 (driver PWM que comanda os motores) |
| `z_accel.py` | Teste isolado: variação de velocidade do motor traseiro (30 → 50 → 100) |
| `z_frent_tras.py` | Teste isolado: movimento para frente e para trás |
| `z_direcao.py` | Teste isolado: sequência completa de direção (reto → direita → reto → esquerda → reto) |
| `z_direita.py` / `z_esquerda.py` / `z_reto.py` | Testes isolados de cada comando de direção individualmente |

Os arquivos `z_*.py` foram usados para testar cada função do carrinho isoladamente antes de integrá-las ao servidor web (`web.py`).

## Como funciona

1. **Boot:** o systemd inicia `carroz.service`, que roda `web.py` continuamente.
2. **Conexão:** o usuário conecta o celular na rede Wi-Fi `CarroZ` (criada pelo `init_hotspot.sh`) e acessa `http://10.0.0.1:8080`.
3. **Interface:** a página HTML (embutida no próprio `web.py`) mostra botões de controle (frente, trás, esquerda, direita, reto, stop).
4. **Comando:** cada clique dispara uma requisição `GET /command/<ação>`.
5. **Execução:** o servidor recebe o comando, inicializa o PCA9685 (se necessário) e aciona os motores via biblioteca `picar` (`back_wheels` para frente/trás, `front_wheels` para direção).

## Bibliotecas utilizadas

- `picar` (SunFounder) — abstração para controle dos motores via PCA9685
- `http.server` (Python padrão) — servidor web, sem dependências externas
