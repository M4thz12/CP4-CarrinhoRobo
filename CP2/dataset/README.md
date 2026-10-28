# Dataset — CP2

## Sensor utilizado

Foi utilizado o sensor ultrassônico HC-SR04 conectado ao Raspberry Pi.

O sensor realiza a medição da distância entre o carrinho e um obstáculo, utilizando a distância em centímetros como variável de entrada para o modelo de Machine Learning.

### Conexões

| Sensor | Raspberry Pi |
|---|---|
| TRIG | GPIO 16 |
| ECHO | GPIO 20 |
| VCC | 5V |
| GND | GND |

O sinal ECHO utiliza divisor de tensão para adequação do nível lógico ao Raspberry Pi.

## Dados utilizados

O dataset contém medições de distância em centímetros associadas a três classes:

- `seguir` — distância segura para continuar avançando;
- `reduzir` — obstáculo se aproximando, indicando necessidade de atenção;
- `parar` — obstáculo próximo, indicando necessidade de parada.

## Dataset sintético

Para o desenvolvimento do CP2 foi utilizado um dataset sintético, autorizado para utilização no projeto.

Os valores foram gerados buscando representar diferentes situações de distância encontradas durante o funcionamento do carrinho, incluindo pequenas variações de medição.

Arquivo utilizado:

`dados_treino_corrigido.csv`

## Organização

O arquivo possui duas colunas:

| Coluna | Descrição |
|---|---|
| `distancia_cm` | Distância medida em centímetros |
| `classe` | Classificação correspondente à distância |

As faixas utilizadas foram:

| Classe | Faixa aproximada |
|---|---:|
| `parar` | 5–19 cm |
| `reduzir` | 20–40 cm |
| `seguir` | 41–180 cm |

## Objetivo

O objetivo do dataset é permitir o treinamento de um modelo capaz de classificar a situação de aproximação de obstáculos a partir da distância fornecida pelo sensor ultrassônico.