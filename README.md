# 🚗 Carrinho-Robô — Smart Video Car Kit V2.0

Projeto desenvolvido para a disciplina **Project-based Maker Lab**, com o objetivo de integrar conhecimentos de mecânica, eletrônica, programação e comunicação sem fio por meio do desenvolvimento de um carrinho-robô funcional.

---

## 👥 Equipe

| Integrante        | RM      |
| ----------------- | ------- |
| David Denunci     | RM98603 |
| Fernando Popolili | RM99919 |
| Lucas de Toledo   | RM97913 |
| Matheus Zanardi   | RM98832 |
| Augusto Milreu    | RM98245 |

---

# 1. Sobre o Projeto

O projeto consiste na montagem, adaptação e programação de um **carrinho-robô baseado no Smart Video Car Kit V2.0**, utilizando uma **Raspberry Pi** como unidade principal de processamento e controle.

O carrinho integra componentes mecânicos e eletrônicos responsáveis pela movimentação, direção e alimentação do sistema.

A Raspberry Pi executa o software responsável pelo controle do veículo e disponibiliza uma **interface web**, permitindo que o usuário controle o carrinho remotamente por meio de um celular ou computador conectado à rede Wi-Fi criada pelo próprio robô.

Durante o desenvolvimento, a equipe realizou a montagem da estrutura, organização e conexão dos componentes eletrônicos, configuração da Raspberry Pi, testes individuais dos componentes e desenvolvimento do sistema de controle remoto.

---

# 2. Objetivos

O principal objetivo do projeto é desenvolver um **carrinho-robô funcional**, integrando hardware, software, estrutura mecânica e comunicação sem fio.

### Objetivos específicos

* Utilizar a Raspberry Pi como unidade principal de controle;
* Controlar os motores responsáveis pela movimentação;
* Permitir movimentação para frente e para trás;
* Permitir curvas para esquerda e direita;
* Permitir o alinhamento da direção na posição reta;
* Integrar o sistema de controle dos motores à Raspberry Pi;
* Criar uma rede Wi-Fi própria para comunicação com o robô;
* Desenvolver uma interface web para controle remoto;
* Organizar os componentes eletrônicos e o sistema de alimentação;
* Adaptar e organizar a estrutura física do carrinho;
* Realizar testes individuais antes da integração final;
* Documentar o processo de desenvolvimento, montagem e testes.

---

# 3. Principais Funcionalidades

O carrinho desenvolvido possui as seguintes funcionalidades:

* 🚗 Movimentação para frente;
* 🔙 Movimentação para trás;
* ⬅️ Direcionamento para esquerda;
* ➡️ Direcionamento para direita;
* ⬆️ Retorno da direção para posição reta;
* 🛑 Parada dos motores;
* 📶 Controle remoto através de Wi-Fi;
* 🌐 Interface web para envio dos comandos;
* 🔋 Sistema de alimentação próprio.

---

# 4. Componentes Principais

| Componente              | Função                                                 |
| ----------------------- | ------------------------------------------------------ |
| Raspberry Pi            | Processamento e controle principal do robô             |
| PCA9685                 | Controle PWM utilizado pelo sistema                    |
| Controlador dos motores | Acionamento dos motores responsáveis pela movimentação |
| Motores                 | Movimentação do carrinho                               |
| Sistema de direção      | Controle da orientação das rodas                       |
| Rodas                   | Movimentação do veículo                                |
| Roda de apoio           | Apoio e estabilidade                                   |
| Sistema de alimentação  | Fornecimento de energia aos componentes                |

---

# 5. Estrutura Mecânica

O projeto utiliza como base a estrutura do **Smart Video Car Kit V2.0**, adaptada e organizada para acomodar os componentes mecânicos e eletrônicos utilizados no projeto.

A montagem considerou principalmente:

* Distribuição adequada dos componentes;
* Espaço disponível no chassi;
* Fixação dos componentes eletrônicos;
* Organização e passagem dos cabos;
* Distância entre fios e partes móveis;
* Acesso à Raspberry Pi;
* Acesso ao sistema de alimentação;
* Liberdade de movimentação das rodas;
* Facilidade de manutenção.

Os componentes foram posicionados de forma a não interferir na movimentação do carrinho.

Os cabos também foram organizados para evitar contato com as rodas e demais partes móveis.

---

# 6. Organização dos Componentes

A distribuição física dos componentes foi realizada buscando manter o sistema organizado, funcional e de fácil manutenção.

| Região                | Componentes                            |
| --------------------- | -------------------------------------- |
| Região central        | Raspberry Pi e componentes de controle |
| Próximo aos motores   | Sistema de acionamento dos motores     |
| Região de alimentação | Bateria e conexões de energia          |
| Laterais              | Motores e rodas                        |
| Estrutura interna     | Cabos e conexões                       |

A organização busca manter o equilíbrio do carrinho e evitar que fios ou componentes interfiram na movimentação.

---

# 7. Hardware e Eletrônica

A **Raspberry Pi** funciona como unidade central de processamento e controle do projeto.

Os comandos enviados pelo usuário são recebidos pelo software executado na Raspberry Pi e convertidos em ações de movimentação e direção.

O projeto também utiliza o **PCA9685**, inicializado pelo software para realizar o controle PWM necessário ao sistema.

A arquitetura simplificada pode ser representada da seguinte maneira:

```text
                +--------------------+
                |    Raspberry Pi    |
                +---------+----------+
                          |
                          v
                +--------------------+
                |      PCA9685       |
                +---------+----------+
                          |
                +---------+---------+
                |                   |
                v                   v
             Motores             Direção
                |                   |
                +---------+---------+
                          |
                          v
                Movimento do carrinho
```

---

# 8. Sistema de Alimentação

O sistema de alimentação é responsável por fornecer energia para os componentes utilizados no carrinho.

A alimentação foi organizada considerando as diferentes necessidades dos componentes eletrônicos e dos motores.

Durante a montagem foram considerados os seguintes cuidados:

* Manter os cabos presos ao chassi;
* Evitar fios próximos às rodas;
* Evitar contato com partes móveis;
* Manter os conectores acessíveis;
* Evitar tensão excessiva nos cabos;
* Facilitar a manutenção;
* Manter a alimentação organizada durante a movimentação.

---

# 9. Comunicação sem Fio

O controle remoto do carrinho é realizado através de **Wi-Fi**.

Para isso, a Raspberry Pi é configurada para criar uma rede própria utilizada exclusivamente para comunicação entre o usuário e o carrinho.

O nome da rede criada é:

```text
CarroZ
```

A Raspberry Pi utiliza o endereço:

```text
10.0.0.1
```

Dessa forma, um celular ou computador pode se conectar diretamente à rede do carrinho sem a necessidade de utilizar a mesma rede Wi-Fi de um roteador externo.

A configuração é realizada pelo script:

```text
init_hotspot.sh
```

O script utiliza o `nmcli` para criar o hotspot, definir o endereço IP e configurar a conexão para inicialização automática.

---

# 10. Controle Remoto

O controle do carrinho é realizado através de uma **interface web** executada pela própria Raspberry Pi.

O sistema foi desenvolvido utilizando:

* Python;
* HTML;
* CSS;
* JavaScript;
* HTTP.

O servidor web é executado na porta:

```text
8080
```

Após conectar um celular ou computador à rede Wi-Fi `CarroZ`, a interface pode ser acessada através do navegador.

```text
http://10.0.0.1:8080
```

A interface disponibiliza comandos para:

* Frente;
* Trás;
* Esquerda;
* Direita;
* Reto;
* Stop;
* Inicialização do sistema.

Isso permite controlar o carrinho remotamente sem a necessidade de uma conexão física com o dispositivo utilizado como controle.

---

# 11. Funcionamento do Software

O principal arquivo responsável pelo funcionamento do carrinho é:

```text
web.py
```

O programa implementa uma classe responsável pelo controle do veículo.

Na inicialização, são configurados os componentes utilizados para controlar as rodas e a direção.

A velocidade padrão utilizada pelo sistema é definida através da constante:

```python
MOTOR_SPEED = 30
```

Os principais métodos implementados são:

| Método       | Função                                |
| ------------ | ------------------------------------- |
| `init()`     | Inicializa os componentes necessários |
| `frente()`   | Movimenta o carrinho para frente      |
| `tras()`     | Movimenta o carrinho para trás        |
| `direita()`  | Direciona as rodas para direita       |
| `esquerda()` | Direciona as rodas para esquerda      |
| `reto()`     | Retorna a direção para posição reta   |
| `stop()`     | Interrompe a movimentação             |
| `status()`   | Retorna informações sobre o sistema   |

O servidor HTTP recebe os comandos enviados pelo navegador e executa o método correspondente.

---

# 12. Interface Web

A própria aplicação Python disponibiliza a página utilizada para controlar o carrinho.

A interface possui botões para os principais comandos de movimentação:

```text
                FRENTE
                   ▲

       ESQUERDA   STOP   DIREITA
           ◀        ■        ▶

                   ▼
                  TRÁS

                  RETO
```

Quando um botão é pressionado, o JavaScript envia uma requisição HTTP para o servidor.

O padrão utilizado é:

```text
/command/<comando>
```

Por exemplo:

```text
/command/frente
/command/tras
/command/esquerda
/command/direita
/command/reto
/command/stop
```

O servidor identifica o comando solicitado e executa a ação correspondente no carrinho.

---

# 13. Fluxo de Funcionamento

O funcionamento completo do sistema pode ser representado da seguinte maneira:

```text
┌────────────────────────┐
│   Celular / Notebook   │
└────────────┬───────────┘
             │
             │ Wi-Fi
             ▼
┌────────────────────────┐
│    Rede Wi-Fi CarroZ   │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│      Raspberry Pi      │
│      10.0.0.1:8080     │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│     Servidor Python    │
│        web.py          │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│   Controle eletrônico  │
└────────────┬───────────┘
             │
       ┌─────┴─────┐
       ▼           ▼
    Motores      Direção
       │           │
       └─────┬─────┘
             ▼
┌────────────────────────┐
│ Movimento do carrinho  │
└────────────────────────┘
```

Esse fluxo representa a integração entre **comunicação sem fio, software e hardware** utilizada no projeto.

---

# 14. Testes Realizados

Durante o desenvolvimento foram criados scripts separados para testar individualmente os componentes antes da integração com o sistema final.

## 14.1 Inicialização do PCA9685

Arquivo:

```text
z_init.py
```

Utilizado para verificar a inicialização e comunicação com o PCA9685.

---

## 14.2 Teste dos motores e velocidade

Arquivo:

```text
z_accel.py
```

Utilizado para testar o acionamento dos motores com diferentes valores de velocidade.

---

## 14.3 Teste de frente e trás

Arquivo:

```text
z_frent_tras.py
```

Utilizado para validar a movimentação do carrinho nos dois sentidos.

---

## 14.4 Teste do sistema de direção

Arquivo:

```text
z_direcao.py
```

Utilizado para testar sequencialmente:

* Posição reta;
* Direita;
* Posição reta;
* Esquerda;
* Retorno para posição reta.

---

## 14.5 Testes individuais de direção

Também foram utilizados:

```text
z_direita.py
z_esquerda.py
z_reto.py
```

Esses arquivos permitiram testar cada posição da direção individualmente.

A utilização de scripts separados facilitou a identificação de problemas e a validação dos componentes antes da integração com o sistema web.

---

# 15. Processo de Desenvolvimento

O projeto foi desenvolvido de forma incremental, testando cada parte antes da integração final.

### Etapa 1 — Montagem

Montagem da estrutura física do carrinho e instalação dos componentes eletrônicos.

### Etapa 2 — Inicialização do controlador

Validação da comunicação com o PCA9685 através de um script específico de teste.

### Etapa 3 — Testes dos motores

Teste dos motores responsáveis pela movimentação do carrinho.

Foram verificados diferentes valores de velocidade e os dois sentidos de movimentação.

### Etapa 4 — Testes de direção

A direção foi testada separadamente através de scripts para:

* Direita;
* Esquerda;
* Reto.

### Etapa 5 — Integração

Após os testes individuais, as funcionalidades foram reunidas na aplicação principal `web.py`.

### Etapa 6 — Interface web

Foi criada uma página web com botões para enviar os comandos ao carrinho.

### Etapa 7 — Comunicação sem fio

A Raspberry Pi foi configurada para criar sua própria rede Wi-Fi, permitindo o acesso ao servidor através de outro dispositivo.

### Etapa 8 — Sistema final

Os componentes de hardware, software e comunicação foram integrados para permitir o controle remoto do carrinho.

---

# 16. Como Utilizar

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

O sistema inicializará os componentes responsáveis pelo controle do carrinho.

## 5. Controlar

Utilize os botões da interface para controlar:

* Frente;
* Trás;
* Esquerda;
* Direita;
* Reto;
* Stop.

---

# 17. Resultado Final

O projeto resultou em um **carrinho-robô controlado remotamente através de Wi-Fi**, utilizando uma Raspberry Pi como unidade principal de processamento.

A solução permite que um celular ou computador se conecte diretamente à rede criada pelo carrinho e acesse uma interface web para controlar sua movimentação.

O sistema permite realizar movimentos para frente e para trás, controlar a direção para esquerda e direita, retornar a direção para a posição reta e interromper a movimentação.

Além da aplicação final, foram mantidos os scripts utilizados durante os testes individuais dos componentes, registrando parte do processo de desenvolvimento até chegar à versão integrada.

Dessa forma, o projeto demonstra a integração entre **mecânica, eletrônica, programação e comunicação sem fio** em um sistema funcional.
