## Documentação Técnica

Projeto de desenvolvimento e documentação de um **Smart Video Car Kit V2.0**, utilizando uma **Raspberry Pi** como unidade principal de processamento e controle.

---

## Equipe

| Integrante | RM |
|---|---|
| David Denunci | RM98603 |
| Fernando Popolili | RM99919 |
| Lucas de Toledo | RM97913 |
| Matheus Zanardi | RM98832 |
| Augusto Milreu | RM98245 |

---

# 1. Sobre o Projeto

O projeto consiste na utilização e adaptação de um **Smart Video Car Kit V2.0 para Raspberry Pi**, composto por uma estrutura mecânica com motores DC, rodas, sistema de alimentação e componentes eletrônicos responsáveis pelo controle e movimentação do robô.

A Raspberry Pi atua como a unidade principal de processamento do sistema, sendo responsável pelo controle dos componentes eletrônicos e pelo processamento das informações recebidas pelos periféricos.

A documentação apresenta as principais características do chassi, as modificações estruturais, a organização dos componentes eletrônicos, as conexões entre os módulos e o sistema de alimentação do projeto.

---

# 2. Objetivos

Os principais objetivos do projeto são:

- Utilizar a Raspberry Pi como unidade de controle do robô;
- Adaptar a estrutura do chassi para acomodar os componentes eletrônicos;
- Organizar os componentes de forma segura e funcional;
- Documentar as conexões eletrônicas do projeto;
- Documentar o sistema de alimentação;
- Planejar a organização dos cabos e componentes;
- Facilitar futuras manutenções e alterações no projeto.

---

# 3. Componentes Principais

| Componente | Função |
|---|---|
| Raspberry Pi | Processamento e controle do robô |
| Driver/controlador de motores | Controle dos motores DC |
| Motores DC | Movimentação do robô |
| Rodas | Transmissão do movimento |
| Roda caster | Apoio e estabilidade |
| Câmera | Captura de vídeo |
| Sistema de alimentação | Fornecimento de energia aos componentes |

---

# 4. Requisitos do Chassi

## 4.1 Características gerais

O chassi do Smart Video Car Kit V2.0 é responsável pela sustentação dos componentes mecânicos e eletrônicos do robô.

| Parâmetro | Especificação |
|---|---|
| Estrutura | Chassi do Smart Video Car Kit V2.0 |
| Quantidade de motores | 2 motores DC |
| Tração | Duas rodas motrizes |
| Apoio | Roda caster |
| Controlador principal | Raspberry Pi |
| Sistema de controle | Eletrônico |
| Alimentação | Sistema de bateria do projeto |
| Distribuição | Simétrica em relação ao eixo longitudinal |

---

# 5. Mudanças na Estrutura do Chassi

A estrutura original do Smart Video Car Kit V2.0 foi utilizada como base para a montagem do projeto.

A organização do chassi foi planejada considerando o espaço necessário para instalação dos componentes eletrônicos, a distribuição de peso, a passagem dos cabos e a movimentação das partes mecânicas.

As principais adequações realizadas ou previstas são:

- Definição de uma área para instalação da Raspberry Pi;
- Definição da posição do driver dos motores;
- Reserva de espaço para o sistema de alimentação;
- Organização da fiação;
- Definição dos pontos de passagem dos cabos;
- Fixação dos componentes eletrônicos;
- Manutenção de espaço livre para as rodas e motores;
- Organização dos componentes para facilitar a manutenção;
- Utilização de abraçadeiras e organizadores para evitar cabos soltos.

A distribuição dos componentes busca manter o robô equilibrado, evitando concentração excessiva de peso em uma única região do chassi.

---

# 6. Organização dos Componentes

A organização física dos componentes foi planejada considerando três fatores principais:

1. Distribuição de peso;
2. Facilidade de manutenção;
3. Organização e proteção da fiação.

A Raspberry Pi deve permanecer em uma posição que permita acesso aos seus conectores e aos pinos GPIO utilizados no projeto.

O driver dos motores deve permanecer próximo aos motores, reduzindo o comprimento dos cabos responsáveis pelo acionamento.

O sistema de alimentação deve ser instalado em uma região que não interfira na movimentação das rodas e permita acesso para manutenção.

A câmera deve permanecer em uma posição que proporcione uma área adequada de captura do ambiente.

---

# 7. Distribuição Física dos Componentes

A disposição dos componentes segue uma organização funcional:

| Região | Componentes |
|---|---|
| Região central | Raspberry Pi |
| Região próxima aos motores | Driver/controlador dos motores |
| Região traseira ou inferior | Sistema de alimentação |
| Região frontal | Câmera |
| Laterais | Motores e rodas |
| Região inferior/lateral | Passagem e fixação dos cabos |

Essa distribuição busca manter o equilíbrio do robô e reduzir o comprimento dos cabos entre componentes relacionados.

---

# 8. Fixação dos Componentes

Os componentes eletrônicos devem permanecer fixados ao chassi para evitar movimentações durante o funcionamento do robô.

Podem ser utilizados:

- Parafusos;
- Espaçadores;
- Suportes;
- Abraçadeiras;
- Organizadores de cabos;
- Pontos de fixação existentes no chassi.

A Raspberry Pi deve ser instalada de maneira que não exista contato direto inadequado entre a placa e a estrutura metálica ou condutiva do chassi.

Os cabos também devem ser presos ao chassi para evitar que fiquem soltos ou entrem em contato com as rodas e motores.

---

# 9. Conexões dos Componentes Eletrônicos

A arquitetura eletrônica do projeto pode ser dividida em três grupos principais:

- Processamento e controle;
- Movimentação;
- Alimentação.

A Raspberry Pi funciona como unidade central de processamento e controle.

Os comandos destinados aos motores são enviados pela Raspberry Pi ao driver de motores. O driver realiza o acionamento dos motores DC responsáveis pela movimentação do robô.

A câmera é conectada à Raspberry Pi e utilizada para captura de vídeo.

A estrutura lógica das conexões é:

                     +------------------+
                     |   Raspberry Pi   |
                     |                  |
                     |      GPIO        |
                     +--------+---------+
                              |
                 +------------+------------+
                 |            |            |
                 v            v            v
              Câmera       Driver       Outros
                          de motores   periféricos
                              |
                       +------+------+
                       |             |
                       v             v
                    Motor E       Motor D


# 10. Fluxo de Controle
O funcionamento lógico do sistema pode ser representado da seguinte forma:

                 +-------+
                 | INÍCIO|
                 +---+---+
                     |
                     v
              +-------------+
              | Raspberry Pi|
              +------+------+
                     |
                     v
       +---------------------------+
       | Processamento dos comandos|
       +-------------+-------------+
                     |
                     v
              +------+------+
              |             |
              v             v
           Câmera    Controle dos motores
                              |
                              v
                    +------------------+
                    | Driver de motores|
                    +--------+---------+
                             |
                    +--------+--------+
                    |                 |
                    v                 v
                 Motor E           Motor D
                    |                 |
                    +--------+--------+
                             |
                             v
                    Movimentação do robô

# 11. Sistema de Alimentação
O sistema de alimentação é responsável por fornecer energia para a Raspberry Pi, o driver dos motores e os demais componentes eletrônicos.

A alimentação deve ser distribuída de acordo com as necessidades de cada componente.

A Raspberry Pi necessita de uma alimentação compatível com sua especificação. Já os motores possuem uma demanda de corrente diferente e são acionados através do driver de motores.

Por esse motivo, a alimentação dos motores deve ser realizada através do sistema apropriado para o driver utilizado, evitando utilizar diretamente os pinos de alimentação da Raspberry Pi para alimentar os motores.

# 12. Diagrama de Alimentação
O fluxo geral de alimentação do projeto é representado abaixo:

                       +-----------+
                       |  Bateria  |
                       +-----+-----+
                             |
                             v
                 +-----------------------+
                 | Sistema de alimentação|
                 +-----------+-----------+
                             |
                   +---------+---------+
                   |                   |
                   v                   v
            +-------------+     +-------------+
            | Raspberry Pi|     |   Driver    |
            |             |     | de motores  |
            +-------------+     +------+------+
                                      |
                              +-------+-------+
                              |               |
                              v               v
                           Motor E         Motor D

A distribuição apresentada representa a arquitetura geral do sistema.

As tensões e correntes devem seguir as especificações dos componentes utilizados no projeto.

# 13. Organização da Alimentação e dos Cabos
Os cabos de alimentação e de sinal devem ser organizados de maneira a evitar interferências e facilitar a manutenção.

Os principais critérios de organização são:

Manter os cabos presos ao chassi;
Evitar fios próximos às rodas;
Evitar contato com partes móveis;
Evitar tensão excessiva nos cabos;
Manter os conectores acessíveis;
Utilizar abraçadeiras para fixação;
Utilizar organizadores de cabos;
Separar cabos de alimentação e sinal quando possível;
Evitar cruzamentos desnecessários;
Manter comprimento suficiente para permitir manutenção.
A organização da fiação também deve impedir que os cabos se soltem durante a movimentação do robô.


# 14. Conclusão
O Smart Video Car Kit V2.0 foi estruturado utilizando a Raspberry Pi como unidade principal de processamento e controle.

As adequações realizadas no chassi têm como objetivo acomodar os componentes eletrônicos, organizar a fiação e manter uma distribuição adequada dos elementos mecânicos e eletrônicos.

A arquitetura do projeto utiliza um driver para o controle dos motores, permitindo que a Raspberry Pi envie os comandos necessários para a movimentação do robô sem alimentar diretamente os motores através dos seus pinos de controle.

A organização dos componentes e dos cabos busca proporcionar maior segurança, facilitar a manutenção e evitar interferências entre a parte eletrônica e as partes móveis do veículo.

Dessa forma, a documentação apresenta as alterações estruturais do chassi, a organização dos componentes, as conexões eletrônicas e o sistema de alimentação do Smart Video Car Kit V2.0.

# Organização

## MVP

### Quando será minimamente funcional?

O MVP será considerado minimamente funcional quando o Smart Video Car Kit V2.0 conseguir realizar os movimentos básicos utilizando a Raspberry Pi como unidade de controle.

Para isso, deverá ser possível:

- Ligar o sistema;
- Raspberry Pi inicializar corretamente;
- Raspberry Pi comunicar-se com o driver de motores;
- Controlar os dois motores DC;
- Movimentar o robô para frente;
- Movimentar o robô para trás;
- Virar para a esquerda;
- Virar para a direita;
- Parar o robô;
- Alimentação funcionar corretamente;
- Componentes estarem fixados e os cabos organizados.

### Quando estará concluído?

O MVP estará concluído quando todas as funcionalidades essenciais acima forem implementadas e testadas em conjunto, resultando em um robô capaz de se movimentar e ser controlado de forma confiável.

Funcionalidades adicionais, como câmera e recursos de automação, poderão ser desenvolvidas após a conclusão do MVP.

---

## MoSCoW

### Must Have

Funcionalidades obrigatórias para o funcionamento do projeto:

- Raspberry Pi funcionando;
- Chassi montado;
- Dois motores DC;
- Driver de motores;
- Sistema de alimentação;
- Comunicação Raspberry Pi → Driver;
- Movimento para frente;
- Movimento para trás;
- Curva para esquerda;
- Curva para direita;
- Parada do robô;
- Conexões elétricas funcionais;
- Organização dos cabos.

### Should Have

Funcionalidades importantes, mas que não impedem a entrega do MVP:

- Câmera integrada;
- Captura/transmissão de vídeo;
- Melhor organização física dos componentes;
- Melhor acabamento do chassi;
- Teste de autonomia da bateria.

### Could Have

Funcionalidades interessantes que poderão ser implementadas caso haja tempo:

- Sensor ultrassônico;
- Modo autônomo;
- LEDs;
- Buzzer;
- Interface gráfica para controle;
- Indicador de bateria.

### Won't Have

Funcionalidades que não serão implementadas nesta versão:

- GPS;
- RFID;
- Display OLED;
- Inteligência artificial complexa;
- Navegação autônoma avançada;
- Controle de múltiplos robôs.

---

## Backlog

| ID | Tarefa | Responsável | Prioridade | Dependência | Status |
|---|---|---|---|---|---|
| B01 | Levantar componentes | David | Must Have | — | A Fazer |
| B02 | Conferir componentes | Fernando | Must Have | B01 | A Fazer |
| B03 | Avaliar chassi | Lucas | Must Have | B01 | A Fazer |
| B04 | Definir posição dos componentes | Lucas | Must Have | B03 | A Fazer |
| B05 | Montar motores | Matheus | Must Have | B03 | A Fazer |
| B06 | Instalar rodas e caster | Matheus | Must Have | B05 | A Fazer |
| B07 | Fixar Raspberry Pi | Fernando | Must Have | B04 | A Fazer |
| B08 | Fixar driver | Matheus | Must Have | B04 | A Fazer |
| B09 | Montar alimentação | Augusto | Must Have | B02 | A Fazer |
| B10 | Realizar conexões elétricas | Augusto | Must Have | B07, B08, B09 | A Fazer |
| B11 | Organizar cabeamento | Fernando | Must Have | B10 | A Fazer |
| B12 | Configurar Raspberry Pi | David | Must Have | B07 | A Fazer |
| B13 | Desenvolver controle dos motores | David | Must Have | B10, B12 | A Fazer |
| B14 | Testar avanço e ré | David | Must Have | B13 | A Fazer |
| B15 | Testar curvas | David | Must Have | B13 | A Fazer |
| B16 | Testar parada | David | Must Have | B13 | A Fazer |
| B17 | Realizar teste integrado | Todos | Must Have | B14, B15, B16 | A Fazer |
| B18 | Instalar câmera | Lucas | Should Have | B17 | A Fazer |
| B19 | Testar câmera | Lucas | Should Have | B18 | A Fazer |
| B20 | Testar autonomia da bateria | Augusto | Should Have | B17 | A Fazer |
| B21 | Atualizar documentação | Lucas | Must Have | B17 | A Fazer |
| B22 | Preparar demonstração final | Todos | Must Have | B21 | A Fazer |

---

## Kanban

O projeto será organizado em quatro colunas:

### Backlog

Tarefas planejadas para serem realizadas posteriormente:

- Implementar sensor ultrassônico;
- Implementar modo autônomo;
- Implementar LEDs;
- Implementar buzzer;
- Criar indicador de bateria;
- Melhorar interface de controle.

### A Fazer

Tarefas priorizadas que ainda não foram iniciadas:

- Levantar componentes;
- Conferir componentes;
- Avaliar chassi;
- Definir posição dos componentes;
- Montar motores;
- Instalar rodas;
- Fixar Raspberry Pi;
- Fixar driver;
- Montar sistema de alimentação.

### Em Andamento

Tarefas que estão sendo executadas:

- Configuração da Raspberry Pi;
- Desenvolvimento do controle dos motores;
- Montagem eletrônica;
- Organização dos cabos;
- Testes dos motores.

### Concluído

Tarefas que já foram finalizadas e validadas:

- Estrutura inicial do projeto;
- Definição dos componentes principais;
- Documentação inicial do chassi;
- Definição da arquitetura eletrônica;
- Definição do sistema de alimentação.
