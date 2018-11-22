
class TransactionVerificator(object):
    """Classe auxiliar que dispõe de métodos de verificação de uma transição,
    a serem utilziados pelo método de computação atrelado a classe MT
    
    Args:
        object (object): Tipo de objeto mais básico em python
    
    Raises:
        ValueError: Estado provido não pertence ao conjunto de estados de uma máquina de Turing
        ValueError: Símbolo de entrada não aparece no alfabeto de entrada da máquina de Turing
        ValueError: Símbolo da fita não pertence ao alfabeto da fita da máquina de Turing
        ValueError: A direção provida em uma transição é invalida
        ValueError: Estado que inicia uma computação em uma MT é diferente daquele determinado como estado
        de leitura pela primeira transição
    """
    
    @staticmethod
    def check_state(MT, state):
        if(not(state in MT.states)):
            raise ValueError(
                "State given does not equal any state of the turing machine")

    @staticmethod
    def check_symbol_input( MT, input_symbol):
        if(not(input_symbol in MT.input_alph)):
            raise ValueError(
                "Input symbol given doesn't appear in turing machine's input alphabet")
                
    @staticmethod
    def check_symbol_tape( MT, tape_symbol):
        if(not(tape_symbol in MT.tape_alph)):
            raise ValueError(
                "Tape symbol given doesn't appear in turing machine's tape alphabet")
    
    @staticmethod
    def check_direction(direction):
        if(direction != 'L' and direction != 'R'):
            raise ValueError("The direction provided is not valid!")
    
    @staticmethod
    def check_initial_state_first_transaction(first_state, first_transaction):
        first_state_transaction = '{' + first_transaction[1:3] + '}'
        if(first_state != first_state_transaction):
            raise ValueError("First machine transaction does not begins with inital state")
