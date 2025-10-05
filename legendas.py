def main():
    original = input("Legenda original: ")
    print(legendas(original))

def legendas(original):
    corrigida = original.replace("->", "-->").replace(": ", ":")
    return corrigida

if __name__ == "__main__":
    main()
