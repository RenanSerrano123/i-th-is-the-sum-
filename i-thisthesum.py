def verificar_soma_indice(tamanho, vetor, indice):
    soma_total = sum(vetor) - vetor[indice]
    return "Sim" if vetor[indice] == soma_total else "Nao"

def main():
    tamanho = int(input())
    vetor = []
    for i in range(tamanho):
        elemento = int(input())
        vetor.append(elemento)
    indice_verificar = int(input())
    resultado = verificar_soma_indice(tamanho, vetor, indice_verificar)
    print(resultado)
main()