# from functools import *


class MT(object):
    """Classe MT que implementa uma máquina de turing através de propriedades e metódos definidos abaixo
    
    Args:
        object (object): O tipo de um objeto mais básico em python, utilizado para haja sobrecarga 
        do método __str__ 
    
    Raises:
        ValueError: Posição da cabeça de leitura viola o limite esquerdo da máquina de turing
        ValueError: Posição da cabeça de leitura viola o limite direito imposto pelo inpout lido do arquivo
    
    """

    @staticmethod
    def build_from_file(fileName):
        try:
            file_read = open(fileName, 'r', encoding='utf8')
        except FileNotFoundError as FNFE:
            print(FNFE)

        content = []
        separated_content = []
        transactions = []
        mt_input = ""
        # index = 0
        for line in file_read.readlines():
            content.append(line.strip("\n\t" + ", "))

        mt_input = content.pop()

        for item in content:
            if(item.startswith('{') and len(item) > 1):
                separated_content.append(item)
            elif (item.startswith('(') and len(item) > 1):
                transactions.append(item)

        print(separated_content)
        print(transactions)

        return MT(states=separated_content[0], input_alph=separated_content[1], tape_alph=separated_content[2], initial_state=separated_content[3], transactions=transactions, mt_input=mt_input)

    def __init__(self, states, input_alph, tape_alph, initial_state, transactions, mt_input):
        self.states = states
        self.input_alph = input_alph
        self.tape_alph = tape_alph
        self.actual_state = initial_state
        self.transactions = transactions
        self.mt_input = mt_input
        self.current_tape = mt_input
        self.head_position = 0

    def __str__(self):
        return self.current_tape[:self.head_position] + self.actual_state + self.current_tape[self.head_position:]

    def move_right(self, write_symbol, next_state):
        copy_current_tape = list(self.current_tape)
        copy_current_tape[self.head_position] = write_symbol
        self.head_position += 1
        if(self.head_position >= len(self.current_tape)):
            raise ValueError('Head position violates limits to the right')

        self.actual_state = next_state
        self.current_tape = "".join(copy_current_tape)

    def move_left(self, write_symbol, next_state):
        copy_current_tape = list(self.current_tape)
        copy_current_tape[self.head_position] = write_symbol
        self.head_position -= 1
        if(self.head_position >= len(self.current_tape)):
            raise ValueError('Head position violates limits to the left')

        self.actual_state = next_state
        self.current_tape = "".join(copy_current_tape)

    def check_state(self, state):
        if(not(state in self.states)):
            raise ValueError("State given does not equal any state of the turing machine")
    
    def check_symbol_input(self, input_symbol):
        if(not(input_symbol in self.input_alph)):
            raise ValueError("Input symbol given doesn't appear in turing machine's input alphabet")

    def check_symbol_tape(self, tape_symbol):
        if(not(tape_symbol in self.tape_alph)):
            raise ValueError("Tape symbol given doesn't appear in turing machine's tape alphabet")


    def start_computation(self):

        print(self)
        # print("isso é um " + self.current_tape[0])
        # Conferir transações e estados

        for transaction in self.transactions:

            # transaction_ended = False
            read_state = '{' + transaction[1:3]  + '}'
            self.check_state(read_state)
            # print(read_state)
            read_symbol = transaction[4]
            self.check_symbol_tape(read_symbol)
            # print(read_symbol)
            next_symbol = transaction[-4]
            self.check_symbol_tape(next_symbol)
            # print(next_symbol)
            next_state = '{' + transaction[9:11] + '}'
            self.check_state(next_state)
            # print(next_state)
            direction = transaction[-2]
            # print(direction)
            # print("olarrr "  + str(self.head_position))
            while(True):
                if(self.actual_state == read_state and self.current_tape[self.head_position] == read_symbol):
                    
                    if(direction == 'R'):
                        self.move_right(next_symbol, next_state)
                        
                    elif(direction == 'L'):
                        self.move_left(next_symbol, next_state)
                    
                    print("New tape configuration: " + str(self))
                else:
                    break
            # else:
            #     errorMsg = "Invalid transaction!"
            #     if(self.actual_state != read_state):
            #         errorMsg += " actual state does not match transaction's readed state"
            #     elif(self.current_tape[self.head_position] != read_symbol):
            #         errorMsg += " actual tape symbol does not match transaction's readed symbol"
                
            #     raise ValueError(errorMsg)
