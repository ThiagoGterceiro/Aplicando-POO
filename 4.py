#4
def conversor_moedas(montante, moeda_original, moeda_convertida):
    taxas_conversao = {
        'BRL': {'BRL': 1.0, 'USD': 0.19, 'EUR': 0.16},
        'USD': {'BRL': 5.24, 'USD': 1.0, 'EUR': 0.85},
        'EUR': {'BRL': 6.23, 'USD': 1.18, 'EUR': 1.0}
    }

    taxa_conversao = taxas_conversao[moeda_original][moeda_convertida]
    montante_convertido = montante * taxa_conversao

    return montante_convertido

# Exemplo de uso
montante = 100
moeda_original = 'BRL'
moeda_convertida = 'USD'

montante_convertido = conversor_moedas(montante, moeda_original, moeda_convertida)

print(f'{montante} {moeda_original} é equivalente a {montante_convertido} {moeda_convertida}.')
