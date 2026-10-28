# 🚗 Carrinho-Robô — Smart Video Car Kit V2.0

Projeto desenvolvido para a disciplina **Project-based Maker Lab**, com o objetivo de integrar conhecimentos de mecânica, eletrônica, programação, comunicação sem fio e Machine Learning por meio do desenvolvimento e evolução de um carrinho-robô funcional.

---

# 👥 Equipe

| Integrante | RM |
|---|---|
| David Denunci | RM98603 |
| Fernando Popolili | RM99919 |
| Lucas de Toledo | RM97913 |
| Matheus Zanardi | RM98832 |
| Augusto Milreu | RM98245 |

---

# 1. Sobre o Projeto

O projeto consiste na montagem, adaptação e programação de um **carrinho-robô baseado no Smart Video Car Kit V2.0**, utilizando uma **Raspberry Pi** como unidade principal de processamento e controle.

No CP1, o projeto foi desenvolvido com foco na montagem do carrinho, controle dos motores, sistema de direção, comunicação Wi-Fi e desenvolvimento de uma interface web para controle remoto.

No CP2, o projeto foi evoluído com a integração de um **sensor ultrassônico HC-SR04** e uma aplicação de **Machine Learning**, permitindo que o carrinho analise a distância até obstáculos e utilize o resultado da inferência para interferir em seu comportamento.

A evolução mantém a arquitetura principal do CP1 e acrescenta uma camada inteligente de segurança ao controle do carrinho.

---

# 2. Objetivos

## Objetivo geral

Desenvolver e evoluir um carrinho-robô funcional utilizando Raspberry Pi, integrando hardware, software, comunicação sem fio, sensores e Machine Learning.

## Objetivos específicos

- Utilizar a Raspberry Pi como unidade principal de controle;
- Controlar os motores responsáveis pela movimentação;
- Permitir movimentação para frente e para trás;
- Permitir curvas para esquerda e direita;
- Permitir o alinhamento da direção na posição reta;
- Integrar o sistema de controle dos motores à Raspberry Pi;
- Criar uma rede Wi-Fi própria para comunicação com o robô;
- Desenvolver uma interface web para controle remoto;
- Integrar o sensor ultrassônico HC-SR04;
- Realizar leituras de distância;
- Criar um conjunto de dados para treinamento;
- Treinar um modelo de Machine Learning;
- Realizar inferências utilizando os dados do sensor;
- Integrar o resultado da inferência ao comportamento do carrinho;
- Implementar uma camada de segurança contra colisões;
- Manter a possibilidade de movimentação em ré para permitir a retirada do carrinho de situações de obstáculo;
- Documentar a evolução do projeto entre CP1 e CP2.

---

# 3. Principais Funcionalidades

O carrinho desenvolvido possui as seguintes funcionalidades:

- 🚗 Movimentação para frente;
- 🔙 Movimentação para trás;
- ⬅️ Direcionamento para esquerda;
- ➡️ Direcionamento para direita;
- ⬆️ Retorno da direção para posição reta;
- 🛑 Parada dos motores;
- 📶 Controle remoto através de Wi-Fi;
- 🌐 Interface web para envio dos comandos;
- 📏 Medição de distância utilizando HC-SR04;
- 🤖 Classificação da situação utilizando Machine Learning;
- 🛡️ Parada automática diante de obstáculos;
- 🔋 Sistema de alimentação próprio.

A camada de Machine Learning atua como **mecanismo de segurança**, sem substituir o controle manual do usuário.

---

# 4. Componentes Principais

| Componente | Função |
|---|---|
| Raspberry Pi | Processamento, controle e execução do modelo |
| HC-SR04 | Medição da distância até obstáculos |
| PCA9685 | Controle PWM utilizado pelo sistema |
| Controlador dos motores | Acionamento dos motores |
| Motores | Movimentação do carrinho |
| Sistema de direção | Controle da orientação das rodas |
| Rodas | Movimentação do veículo |
| Roda de apoio | Apoio e estabilidade |
| Sistema de alimentação | Fornecimento de energia |

---

# 5. Estrutura Mecânica

O projeto utiliza como base a estrutura do **Smart Video Car Kit V2.0**, adaptada e organizada para acomodar os componentes mecânicos e eletrônicos utilizados no projeto.

A montagem considerou principalmente:

- Distribuição adequada dos componentes;
- Espaço disponível no chassi;
- Fixação dos componentes eletrônicos;
- Organização e passagem dos cabos;
- Distância entre fios e partes móveis;
- Acesso à Raspberry Pi;
- Acesso ao sistema de alimentação;
- Liberdade de movimentação das rodas;
- Facilidade de manutenção.

Os componentes foram posicionados de forma a não interferir na movimentação do carrinho.

---

# 6. Organização dos Componentes

A distribuição física dos componentes foi realizada buscando manter o sistema organizado, funcional e de fácil manutenção.

| Região | Componentes |
|---|---|
| Região central | Raspberry Pi e componentes de controle |
| Próximo aos motores | Sistema de acionamento dos motores |
| Região de alimentação | Bateria e conexões de energia |
| Laterais | Motores e rodas |
| Parte frontal | Sensor HC-SR04 |
| Estrutura interna | Cabos e conexões |

A organização busca manter o equilíbrio do carrinho e evitar que fios ou componentes interfiram na movimentação.

---

# 7. Hardware e Eletrônica

A **Raspberry Pi** funciona como unidade central de processamento e controle do projeto.

Os comandos enviados pelo usuário são recebidos pelo software executado na Raspberry Pi e convertidos em ações de movimentação e direção.

O projeto também utiliza o **PCA9685**, inicializado pelo software para realizar o controle PWM necessário ao sistema.

No CP2, foi adicionado o sensor ultrassônico **HC-SR04**, responsável pela medição da distância entre o carrinho e possíveis obstáculos.

## Arquitetura simplificada

```text
                 +----------------------+
                 |     Raspberry Pi     |
                 +----------+-----------+
                            |
                +-----------+-----------+
                |                       |
                v                       v
        +---------------+       +---------------+
        |    PCA9685    |       |    HC-SR04    |
        +-------+-------+       +-------+-------+
                |                       |
                v                       v
        Motores / Direção         Distância
                |                       |
                +-----------+-----------+
                            |
                            v
                    Machine Learning
                            |
                            v
                     Ação no carrinho
```

---

# 8. Sistema de Alimentação

O sistema de alimentação é responsável por fornecer energia para os componentes utilizados no carrinho.

Durante a montagem foram considerados os seguintes cuidados:

- Manter os cabos presos ao chassi;
- Evitar fios próximos às rodas;
- Evitar contato com partes móveis;
- Manter os conectores acessíveis;
- Evitar tensão excessiva nos cabos;
- Facilitar a manutenção;
- Manter a alimentação organizada durante a movimentação.

---

# 9. Comunicação sem Fio

O controle remoto do carrinho é realizado através de **Wi-Fi**.

A Raspberry Pi é configurada para criar uma rede própria utilizada para comunicação entre o usuário e o carrinho.

### Rede

```text
CarroZ
```

### Endereço da Raspberry Pi

```text
10.0.0.1
```

A configuração é realizada pelo script:

```text
init_hotspot.sh
```

O script utiliza `nmcli` para criar o hotspot, definir o endereço IP e configurar a conexão para inicialização automática.

---

# 10. Controle Remoto

O controle do carrinho é realizado através de uma **interface web** executada pela própria Raspberry Pi.

O sistema foi desenvolvido utilizando:

- Python;
- HTML;
- CSS;
- JavaScript;
- HTTP.

O servidor web é executado na porta:

```text
8080
```

Após conectar um celular ou computador à rede Wi-Fi `CarroZ`, a interface pode ser acessada através de:

```text
http://10.0.0.1:8080
```

A interface disponibiliza comandos para:

- Frente;
- Trás;
- Esquerda;
- Direita;
- Reto;
- Stop;
- Inicialização do sistema.

---

# 11. Machine Learning e TinyML — CP2

Como evolução do projeto desenvolvido no CP1, foi adicionada uma camada de Machine Learning responsável por analisar as informações provenientes do sensor HC-SR04.

O objetivo é permitir que o carrinho utilize a distância medida para identificar diferentes situações e tomar uma ação relacionada à segurança do movimento.

## 11.1 Sensor utilizado

Foi utilizado o sensor ultrassônico **HC-SR04**.

O sensor realiza medições da distância entre o carrinho e um obstáculo.

No Raspberry Pi foram utilizados:

```text
TRIG → GPIO 16
ECHO → GPIO 20
```

O pino ECHO utiliza adaptação de tensão para proteção da entrada da Raspberry Pi.

---

# 12. Dataset

Para o treinamento do modelo foram utilizadas medições de distância em centímetros.

As informações foram organizadas em classes relacionadas ao comportamento esperado do carrinho.

## Classes

| Classe | Faixa aproximada | Comportamento |
|---|---:|---|
| `parar` | 5–19 cm | Interromper o movimento para frente |
| `reduzir` | 20–40 cm | Reduzir a velocidade |
| `seguir` | 41–180 cm | Permitir o movimento normal |

O dataset utilizado no projeto está armazenado na pasta de dados do CP2.

Arquivo principal:

```text
dados_treino_corrigido.csv
```

---

# 13. Treinamento do Modelo

O modelo foi treinado utilizando Python e posteriormente salvo para utilização no Raspberry Pi.

O arquivo do modelo é:

```text
modelo_carro.pkl
```

O modelo recebe como entrada a distância medida pelo sensor e produz uma das três classificações:

```text
seguir
reduzir
parar
```

O fluxo de Machine Learning utilizado foi:

```text
Dados de distância
       ↓
Dataset
       ↓
Treinamento
       ↓
Modelo
       ↓
Arquivo .pkl
       ↓
Raspberry Pi
```

---

# 14. Inferência no Raspberry Pi

Durante a execução do carrinho, a Raspberry Pi realiza novas leituras do HC-SR04 e utiliza o modelo treinado para realizar a classificação.

O modelo é carregado pelo programa através do arquivo:

```text
modelo_carro.pkl
```

A cada nova medição, o sistema avalia a situação atual do carrinho.

Exemplo:

```text
Distância: 70 cm
        ↓
    Modelo ML
        ↓
     seguir
        ↓
Carrinho pode continuar
```

Outro exemplo:

```text
Distância: 15 cm
        ↓
    Modelo ML
        ↓
      parar
        ↓
Carrinho interrompe o movimento
```

---

# 15. Integração do Machine Learning com o Carrinho

O resultado da inferência possui efeito direto no comportamento do carrinho.

A camada de Machine Learning foi desenvolvida como uma **camada de segurança sobre o controle manual**.

## Comportamento

### `seguir`

Quando não existe uma situação de risco, o usuário pode continuar controlando o carrinho normalmente.

### `reduzir`

Quando o obstáculo se aproxima, o sistema pode utilizar a classificação para indicar uma situação de atenção e redução de velocidade.

### `parar`

Quando o modelo identifica uma situação de risco, o carrinho interrompe automaticamente o movimento para frente.

## Controle manual preservado

O Machine Learning não substitui o controle do usuário.

O usuário continua podendo:

- avançar;
- virar;
- parar;
- retornar;
- utilizar a ré.

A **ré permanece disponível mesmo quando existe um obstáculo próximo**, permitindo que o operador retire o carrinho da situação de risco.

---

# 16. Arquitetura do CP2

O fluxo completo da evolução pode ser representado da seguinte maneira:

```text
                    +----------------+
                    |    HC-SR04     |
                    +-------+--------+
                            |
                            v
                    +----------------+
                    |     Dados      |
                    |   de distância |
                    +-------+--------+
                            |
                            v
                    +----------------+
                    |    Dataset     |
                    +-------+--------+
                            |
                            v
                    +----------------+
                    |   Treinamento  |
                    |       ML       |
                    +-------+--------+
                            |
                            v
                    +----------------+
                    | modelo_carro   |
                    |     .pkl       |
                    +-------+--------+
                            |
                            v
                    +----------------+
                    |  Raspberry Pi  |
                    |    Inferência  |
                    +-------+--------+
                            |
                            v
                 +----------+-----------+
                 |                      |
                 v                      v
              seguir                  parar
                 |                      |
                 v                      v
          Controle normal         Stop automático
```

---

# 17. Funcionamento do Software

O principal arquivo responsável pelo funcionamento do carrinho é:

```text
web.py
```

Além do controle dos motores e da interface web, o programa passou a integrar o monitoramento do sensor e o modelo de Machine Learning.

Entre as principais responsabilidades do software estão:

| Função | Responsabilidade |
|---|---|
| `init()` | Inicializa os componentes necessários |
| `frente()` | Movimenta o carrinho para frente |
| `tras()` | Movimenta o carrinho para trás |
| `direita()` | Direciona as rodas para direita |
| `esquerda()` | Direciona as rodas para esquerda |
| `reto()` | Retorna a direção para posição reta |
| `stop()` | Interrompe a movimentação |
| `status()` | Retorna informações sobre o sistema |
| Monitor ML | Monitora distância e realiza inferência |

A aplicação também possui um processo de monitoramento contínuo do sensor para identificar situações de risco.

---

# 18. Interface Web

A interface possui botões para os principais comandos de movimentação:

```text
                 FRENTE
                    ▲

          ESQUERDA  STOP  DIREITA
             ◀        ■       ▶

                    ▼
                   TRÁS

                   RETO
```

Quando um botão é pressionado, o JavaScript envia uma requisição HTTP para o servidor.

O padrão utilizado é:

```text
/command/<comando>
```

Exemplos:

```text
/command/frente
/command/tras
/command/esquerda
/command/direita
/command/reto
/command/stop
```

---

# 19. Fluxo de Funcionamento Final

```text
┌──────────────────────────┐
│     Celular / Notebook   │
└─────────────┬────────────┘
              │
              │ Wi-Fi
              ▼
┌──────────────────────────┐
│     Rede Wi-Fi CarroZ    │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│       Raspberry Pi       │
│      10.0.0.1:8080       │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│      Servidor Python     │
│          web.py          │
└─────────────┬────────────┘
              │
       ┌──────┴───────┐
       │              │
       ▼              ▼
┌─────────────┐ ┌─────────────┐
│   Controle  │ │   HC-SR04   │
│   manual    │ │   distância │
└──────┬──────┘ └──────┬──────┘
       │               │
       │               ▼
       │        ┌──────────────┐
       │        │  Modelo ML   │
       │        └──────┬───────┘
       │               │
       │               ▼
       │       seguir/reduzir/parar
       │               │
       └───────┬───────┘
               ▼
      ┌──────────────────┐
      │  Controle motor  │
      └────────┬─────────┘
               ▼
      ┌──────────────────┐
      │ Carrinho-Robô    │
      └──────────────────┘
```

---

# 20. Testes Realizados

Durante o desenvolvimento foram criados scripts separados para testar individualmente os componentes antes da integração com o sistema final.

## 20.1 Inicialização do PCA9685

Arquivo:

```text
z_init.py
```

Utilizado para verificar a inicialização e comunicação com o PCA9685.

## 20.2 Teste dos motores e velocidade

Arquivo:

```text
z_accel.py
```

Utilizado para testar o acionamento dos motores com diferentes valores de velocidade.

## 20.3 Teste de frente e trás

Arquivo:

```text
z_frent_tras.py
```

Utilizado para validar a movimentação do carrinho nos dois sentidos.

## 20.4 Teste do sistema de direção

Arquivo:

```text
z_direcao.py
```

Utilizado para testar sequencialmente:

- Posição reta;
- Direita;
- Posição reta;
- Esquerda;
- Retorno para posição reta.

## 20.5 Testes individuais de direção

Também foram utilizados:

```text
z_direita.py
z_esquerda.py
z_reto.py
```

Esses arquivos permitiram testar cada posição da direção individualmente.

## 20.6 Teste do sensor

O HC-SR04 foi testado individualmente para validar a leitura de distância antes da integração com o modelo de Machine Learning.

## 20.7 Teste do modelo

O modelo foi testado utilizando diferentes valores de distância para verificar a classificação entre:

```text
seguir
reduzir
parar
```

## 20.8 Teste integrado

Após a integração, o carrinho foi testado com obstáculos posicionados à frente.

O comportamento esperado foi:

```text
Distância segura → controle normal

Obstáculo próximo → parada automática

Obstáculo próximo + ré → ré permanece disponível
```

---

# 21. Processo de Desenvolvimento

O projeto foi desenvolvido de forma incremental.

## CP1

### Etapa 1 — Montagem

Montagem da estrutura física do carrinho e instalação dos componentes eletrônicos.

### Etapa 2 — Inicialização do controlador

Validação da comunicação com o PCA9685.

### Etapa 3 — Testes dos motores

Teste dos motores responsáveis pela movimentação.

### Etapa 4 — Testes de direção

Validação dos movimentos de direita, esquerda e posição reta.

### Etapa 5 — Integração

Integração das funcionalidades na aplicação principal `web.py`.

### Etapa 6 — Interface web

Criação da página de controle remoto.

### Etapa 7 — Comunicação sem fio

Configuração da Raspberry Pi para criação da rede Wi-Fi.

### Etapa 8 — Sistema final

Integração dos componentes de hardware, software e comunicação.

---

# 22. Evolução CP2 — Machine Learning

A segunda etapa do projeto adicionou inteligência ao sistema existente.

### Etapa 1 — Integração do sensor

Instalação e teste do HC-SR04.

### Etapa 2 — Dataset

Organização das medições de distância em classes:

```text
seguir
reduzir
parar
```

### Etapa 3 — Treinamento

Treinamento do modelo de Machine Learning utilizando os dados preparados.

### Etapa 4 — Exportação

O modelo treinado foi salvo como:

```text
modelo_carro.pkl
```

### Etapa 5 — Inferência

Integração do modelo ao Raspberry Pi.

### Etapa 6 — Integração com o carrinho

O resultado da classificação passou a interferir no comportamento do carrinho.

### Etapa 7 — Segurança

Implementação da parada automática diante de obstáculos, mantendo o controle manual e a possibilidade de ré.

---

# 23. Como Utilizar

## 1. Ligar o carrinho

Ligue o sistema de alimentação e aguarde a inicialização da Raspberry Pi.

## 2. Conectar ao Wi-Fi

No celular ou computador utilizado como controle, procure pela rede:

```text
CarroZ
```

Conecte-se à rede do carrinho.

## 3. Acessar a interface

Abra o navegador e acesse:

```text
http://10.0.0.1:8080
```

## 4. Inicializar

Na interface web, pressione:

```text
INIT
```

O sistema inicializará os componentes responsáveis pelo controle do carrinho e pelo monitoramento do sensor.

## 5. Controlar

Utilize os botões da interface para controlar:

- Frente;
- Trás;
- Esquerda;
- Direita;
- Reto;
- Stop.

Durante o movimento para frente, o sistema de Machine Learning monitora a distância e pode interromper o carrinho caso seja identificada uma situação de risco.

---

# 24. Estrutura do Projeto

A estrutura principal do projeto está organizada da seguinte forma:

```text
CP4-CarrinhoRobo/
│
├── codigo/
│   ├── web.py
│   └── scripts de teste
│
├── CP2/
│   ├── dataset/
│   │   └── dados_treino_corrigido.csv
│   │
│   ├── modelo/
│   │   └── modelo_carro.pkl
│   │
│   ├── codigo/
│   │   └── web.py
│   │
│   └── README.md
│
├── docs/
│   └── evidencias/
│
├── software/
│
├── Organizacao/
│
├── Precos/
│
├── Medidas.xlsx
│
└── README.md
```

---

# 25. Resultado Final

O projeto resultou em um **carrinho-robô controlado remotamente através de Wi-Fi**, utilizando uma Raspberry Pi como unidade principal de processamento.

A evolução do CP2 adicionou um sensor ultrassônico e uma aplicação de Machine Learning capaz de analisar a distância até obstáculos e interferir no comportamento do carrinho.

O sistema final integra:

**Mecânica + Eletrônica + Raspberry Pi + HC-SR04 + Python + Machine Learning + Interface Web + Controle dos Motores**

O fluxo principal do sistema é:

```text
SENSOR
   ↓
COLETA DE DADOS
   ↓
DATASET
   ↓
TREINAMENTO
   ↓
MODELO ML
   ↓
INFERÊNCIA
   ↓
DECISÃO
   ↓
AÇÃO NO CARRINHO
```

Dessa forma, o projeto demonstra a evolução do carrinho desenvolvido no CP1 para uma aplicação integrada de **sensoriamento, Machine Learning e automação**, mantendo o controle manual do usuário e adicionando uma camada inteligente de segurança contra obstáculos.