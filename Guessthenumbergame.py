import random
import sys

def main():
    sys.stdout.buffer.write(b'Input a minimum number.\n')
    sys.stdout.flush()
    n = sys.stdin.buffer.readline()

    sys.stdout.buffer.write(b'Input a max number.\n')
    sys.stdout.flush()
    m = sys.stdin.buffer.readline()

    n_int = int(n.decode())
    m_int = int(m.decode())

    if n_int < m_int:
        guessTheNumber(n_int, m_int)
    else:
        print('The generation is fail. Please input again.\n')
        main()
    
def guessTheNumber(n_int, m_int):
    correct_value = random.randint(n_int, m_int)
    while True:
        sys.stdout.buffer.write(b'Input a predicated value.\n')
        sys.stdout.flush()
        predicated_value = sys.stdin.buffer.readline()
        predicated_value_int = int(predicated_value.decode())
        if correct_value == predicated_value_int:
            print('Corrent!')
            break
        else:
            sys.stdout.buffer.write(b'Wrong!\n')
            sys.stdout.flush()

main()
    
