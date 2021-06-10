#programa que verifique si una palabra es palindromo 
palabra = input("Ingrese una palabra para verificar si es palindromo \t")

if (palabra == palabra[::-1]):
    print("palindormo")
else:
    print("no es palindromo")