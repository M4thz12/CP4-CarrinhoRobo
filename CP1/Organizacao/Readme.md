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