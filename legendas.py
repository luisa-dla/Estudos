import re
import sys

def main():
    with open(sys.argv[1], "r") as f:
        original = f.read()
    legendas(original)
    
def legendas(original):
  corrigida = original.replace("->", "-->").replace(": ", ":")
    with open(sys.argv[1], "w") as f:
        f.write(corrigida)

if __name__ == "__main__":
    main()
    
