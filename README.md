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
