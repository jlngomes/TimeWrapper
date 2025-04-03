from time import time

# Controle liga/desliga do cronômetro
# True = mede tempo das funções | False = desativa medição
activated = True

def time_wrapper(met):
    """
    DECORADOR TIMER PARA FUNÇÕES
    -----------------------------------
    Como usar:
        @time_wrapper
        def sua_funcao():
            pass

    Funcionalidade:
        - Mostra o nome da função ao iniciar
        - Calcula e exibe o tempo que levou
        - Pode ser desligado mudando 'activated' para False

    Exemplo:
        @time_wrapper
        def teste():
            for i in range(1000000):
                pass

        teste() → Mostra:
            Starting method: teste
            Method finished in 0.045 seconds.
    """
    if activated:
        def wrapped_method(*args, **kwargs):
            print(f'Starting method: {met.__name__}')  # Mostra nome da função
            start_time = time()  # Inicia cronômetro
            ret_val = met(*args, **kwargs)  # Executa a função original
            print(f'Method finished in {time() - start_time:.4f} seconds.')  # Mostra tempo
            return ret_val  # Retorna o valor normal da função
    else:
        wrapped_method = met  # Versão sem cronômetro

    return wrapped_method