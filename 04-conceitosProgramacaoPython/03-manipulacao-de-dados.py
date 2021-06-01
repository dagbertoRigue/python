"""
    Dizemos que o Python é uma linguagem de tipagem dinâmica, diferente de outras linguagens que
    precisam de variáveis declaradas explicitamente.
"""

# Autor : Dagberto Rigue

num_int = 5
num_dec = 7.2
valor_str = "qualquer texto"

# concatenando dados de tipos diferentes
print("O valor é :", num_int)
print("O valor é : %i" %num_int)
print("Concatenando strings : " + str(num_int))

print("O valor é : ", num_dec)
print("O valor é : %.10f" %num_dec)
print("Concatenando strings : ", valor_str)
print("Concatenando strings : %s" %valor_str)

# fazendo casting da variável inteira para string, para concatenar dados de mesmo tipo

print("Concatenando strings : " + str(num_dec))
print("Concatenando strings : " + str(valor_str))