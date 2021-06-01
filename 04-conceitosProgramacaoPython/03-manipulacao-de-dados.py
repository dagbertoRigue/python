"""
    Dizemos que o Python é uma linguagem de tipagem dinâmica, diferente de outras linguagens que
    precisam de variáveis declaradas explicitamente.
"""

# Autor : Dagberto Rigue

num_int = 5
num_dec = 7.2
valor_str = "qualquer texto"

# concatenando dados de tipos diferentes ou casting
print("O valor é :", num_int)
print("O valor é : %i" % num_int)
print("Concatenando strings : " + str(num_int)) # fazendo cast da variável inteira para string, para concatenar dados de mesmo tipo

print("O valor é : ", num_dec)
print("O valor é : %.10f" % num_dec)
print("Concatenando strings : " + str(num_dec)) # fazendo cast da variável decimal para string, para concatenar dados de mesmo tipo

print("Concatenando strings : ", valor_str)
print("Concatenando strings : %s" % valor_str)
print("Concatenando strings : " + valor_str)