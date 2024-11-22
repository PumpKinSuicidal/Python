def soma_lista(valores=[]):
    '''A função "soma_lista", recebe todos os numeros de uma lista e os somam, retornado "resultado".'''
    resultado = 0
    for i in valores:
        resultado+=i
    
    return resultado

def maior_lista(lista):
    '''A função "maior_lista" encontra o maior valor dentro de uma lista numérica e retorna um resultado.'''
    m = lista[0]
    for i in lista:
        if i > m:
            m = i
    
    return m

def inverter(palavra=""):
    '''A função "inverter" usa o comando len() para obter a quantidade de letras de uma palavra.'''
    qtd = len(palavra)
    invertida = ""
    for i in range(qtd-1,-1,-1):
        invertida+=palavra[i]
    return invertida

def palindromo(palavra=""):
    invertida = inverter(palavra).lower()
    if palavra.lower() == invertida:
        return "É um palindromo."
    else: return "Não é um palindromo."


