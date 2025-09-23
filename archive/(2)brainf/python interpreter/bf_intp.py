import sys
import random
def bf(code):
    num_zeros = 100  
    tape = [0] * num_zeros
    tickerpos = 0

    def remove_non_commands(code):
        commands = list("><+-.,[]?")
        return ''.join(c for c in code if c in commands)
    
    i = 0
    while i < len(code):
        char = code[i]
        
        if char == '>':
            tickerpos += 1
            if tickerpos >= num_zeros:
                tickerpos = 0
        elif char == '<':
            tickerpos -= 1
            if tickerpos < 0:
                tickerpos = num_zeros - 1
        elif char == '+':
            tape[tickerpos] = (tape[tickerpos] + 1) % 256
        elif char == '-':
            tape[tickerpos] = (tape[tickerpos] - 1) % 256
        elif char == '?':
            tape[tickerpos] = random.randint(0, 255)
        elif char == '.':
            print(chr(tape[tickerpos]), end='')
        elif char == ',':
            inp = input()
            if inp:
                tape[tickerpos] = ord(inp[0]) % 256
            else:
                tape[tickerpos] = 0
        elif char == '[':
            if tape[tickerpos] == 0:
                    # find matching ]
                    count = 1
                    i
                    while count > 0:
                        i += 1
                        if code[i] == "[":
                            count += 1
                        elif code[i] == "]":
                            count -= 1
        elif char == ']':
            if tape[tickerpos] != 0:
                    # find matching [
                    count = 1
                    while count > 0:
                        i -= 1
                        if code[i] == "]":
                            count += 1
                        elif code[i] == "[":
                            count -= 1
        else:
            pass
        i += 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            bf(file.read())
    else:
        print("Usage: python bf_intp.py [file]")