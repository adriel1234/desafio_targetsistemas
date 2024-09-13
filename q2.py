
def qtde_letra_a(palavra):
    cont = 0
    
    for letra in palavra:
        if letra == "a" or letra == "A":
            cont+=1
    return cont
    
    

def main():
    palavra = input("Informe uma palavra: ")
    print(f"Quantade de letras a ou A: {qtde_letra_a(palavra)}")


if __name__ == "__main__":
    main()
