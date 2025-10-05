import re
import sys

def main():
    for line in sys.stdin:
        print(line.replace("->", "-->").replace(": ", ":"))
        

if __name__ == "__main__":
    main()
    
