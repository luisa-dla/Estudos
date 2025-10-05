import re
import sys

def main():
    with open(sys.argv[1], "r") as f:
        original = f.read()
    legendas(original)
    
def legendas(original):
    corrigida1 = re.sub(r"->", "-->", original)
    corrigida2 = re.sub(r": ", ":", corrigida1)
    with open(sys.argv[1], "w") as f:
        f.write(corrigida2)

if __name__ == "__main__":
    main()
