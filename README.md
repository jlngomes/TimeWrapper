
# TimeWrapper.py → English 🌐

# What Does This Code Do?
- It's a "function timer"! It measures how long a function takes to execute and displays it on the screen.
- It works as a decorator (a "tag" that you place on top of a function to change its behavior).
- It can be turned on/off by the activated variable.

# How to Use?

First step: Place the @time_wrapper decorator on top of any function you want to time.

Second step: When the function runs, it will display:
- The name of the function.
- How long it took to run.

# How Does It Work Inside?
If enabled = True: 
- The original function is "wrapped" in a timer.
- Before running: shows "Starting method...".
- After running: shows "Method finished in X seconds...".

If activated = False: 
- The function runs normally, without time measurement.

# TimeWrapper.py → Português (Brasil)

# O que este código faz?
- É um "timer de função"! Ele mede quanto tempo uma função leva para ser executada e exibe na tela.
- Ele funciona como um decorador (uma "tag" que você coloca em cima de uma função para mudar seu comportamento).
- Ele pode ser ligado/desligado pela variável activated.

# Como usar?

Primeiro passo: Coloque o decorador @time_wrapper em cima de qualquer função que você queira cronometrar.

Segundo passo: Quando a função for executada, ela exibirá:
- O nome da função.
- Quanto tempo levou para ser executada.

# Como funciona internamente?
Se enabled = True:
- A função original é "encapsulada" em um timer.
- Antes de executar: mostra "Iniciando método...".
- Depois de executar: mostra "Método concluído em X segundos...".

Se activated = False:
- A função é executada normalmente, sem medição de tempo.
