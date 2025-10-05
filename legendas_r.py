import re

def main():
    original = input("Legenda original: ")
    print(legendas(original))

def legendas(original):
    corrigida1 = re.sub(r"->", "-->", original)
    corrigida2 = re.sub(r": ", ":", corrigida1)
    return corrigida2

if __name__ == "__main__":
    main()
