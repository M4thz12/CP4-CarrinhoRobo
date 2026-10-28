# Modelo de Machine Learning

## Objetivo

O modelo tem como objetivo classificar a situação do carrinho a partir da distância medida pelo sensor ultrassônico HC-SR04.

## Entrada

A variável utilizada pelo modelo é:

- `distancia_cm` — distância entre o carrinho e o obstáculo, em centímetros.

## Classes

O modelo possui três categorias:

| Classe | Distância |
|---|---:|
| `parar` | 5–19 cm |
| `reduzir` | 20–40 cm |
| `seguir` | 41–180 cm |

## Dataset

O dataset utilizado possui 1.000 amostras sintéticas:

- 250 amostras da classe `parar`;
- 250 amostras da classe `reduzir`;
- 500 amostras da classe `seguir`.

O dataset foi autorizado pela professora para utilização no desenvolvimento do projeto.

## Funcionamento

Durante a execução, o Raspberry Pi realiza a leitura da distância pelo HC-SR04 e utiliza o modelo para classificar a situação.

```text
HC-SR04
   ↓
distancia_cm
   ↓
Modelo ML
   ↓
seguir / reduzir / parar
   ↓
Camada de segurança
   ↓
Ação no carrinho
```

## Integração

O modelo treinado é salvo em formato `.pkl` e carregado pelo código do carrinho utilizando Joblib.

O arquivo esperado é:

`modelo_carro.pkl`

## Aplicação

No funcionamento atual, o Machine Learning atua como uma camada de segurança.

O controle manual continua sendo utilizado pelo operador. Quando o carrinho está avançando e é identificada uma situação de risco, o sistema pode interromper o movimento para frente.

A marcha à ré permanece disponível para permitir que o carrinho se afaste do obstáculo.