def valida_opcoes(valor: str, opcoes: list) -> bool:
    return valor in opcoes

def obter_opcoes(opcoes, msg='Opções'):
    msg = f"{msg} \n {' '.join([f'{key} - {values}' for key, values in opcoes.items()])} Opções:" 
    
    while True:
        valor = input(msg).upper()
    
        if valida_opcoes(valor, opcoes.keys()):
            break
        
        print(f' Entrada Inválida! As opções validas são {", ".join(opcoes.keys())}')
        
    return valor

def obter_valor(msg='', func=float):
    
    while True:
        valor = input(msg)
        try:
            return list(map(func, [valor]))[0]
        except ValueError:
            msg = f'Entrada Inválida! {msg}'