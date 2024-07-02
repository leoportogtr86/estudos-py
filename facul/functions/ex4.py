# #### Exercício 4: Função com Valor Padrão para Parâmetros
#
# **Pergunta**: Defina uma função chamada `saudacao_completa` que recebe um
# parâmetro `nome` com valor padrão "visitante" e imprime "Olá, [nome]!".
#

def saudacao_completa(nome="visitante"):
    print(f"Olá, {nome}!")


saudacao_completa()

# ```python
# # Seu código aqui
# def saudacao_completa(nome="visitante"):
#     print(f"Olá, {nome}!")
#
#
# saudacao_completa()  # Deve imprimir: Olá, visitante!
# saudacao_completa("Bob")  # Deve imprimir: Olá, Bob!
# ```
