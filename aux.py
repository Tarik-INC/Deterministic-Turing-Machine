from turing_machine import MT

class Aux(object):
    
    @staticmethod
    def check_state(MT, state):
        if(not(state in MT.states)):
            raise ValueError(
                "State given does not equal any state of the turing machine")

    @staticmethod
    def check_symbol_input(self, MT, input_symbol):
        if(not(input_symbol in MT.input_alph)):
            raise ValueError(
                "Input symbol given doesn't appear in turing machine's input alphabet")
                
    @staticmethod
    def check_symbol_tape(self, MT, tape_symbol):
        if(not(tape_symbol in MT.tape_alph)):
            raise ValueError(
                "Tape symbol given doesn't appear in turing machine's tape alphabet")
