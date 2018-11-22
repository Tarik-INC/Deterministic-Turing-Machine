from aux import TransactionVerificator


class MT(object):
    """Classe MT que implementa uma máquina de turing através de propriedades e metódos definidos abaixo

    Args:
        object (object): O tipo de um objeto mais básico em python, utilizado para haja sobrecarga 
        do método __str__ 

    Raises:
        ValueError: Posição da cabeça de leitura viola o limite esquerdo da máquina de turing
        ValueError: Posição da cabeça de leitura viola o limite direito imposto pelo inpout lido do arquivo
        ValueError: Métodos de erro tratados no módulo aux.py
    """

    @staticmethod
    def build_from_file(fileName):
        """Metódo responsável por extrair as informações necessárias, presentes no arquivo, para a implementação da máquina
        de Turing. Entre as informações obtidas no arquivo estão conjuto de estados, alfabeto de entrada, alfabeto da fita,
        estado inicial, conjunto de transações e a cadeia de entrada. Como um arquivo não possui um padrão de codificação conhecido como JSON ou Xml,
        o algoritimo de extração se baseia solenemente na formatação disposta pelo arquivo teste disponibilizado, por exemplo,
        para extrair a cadeia de entrada foi utilizada a leitura de arquivo linha linha, na qual a entrada se encontra na penultima
        posição do buffer de linhas resultante,
        
        Args:
            fileName (string): Caminho relativo do arquivo de leitura
        
        Returns:
            MT: Um objeto MT instanciado com as informações obtidas na leitura do arquivo
        """

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
        """Construtor responsável por inicializar corretamente os atributos de uma classe
        
        Args:
            states (String): Conjunto de estados de uma máquina de Turing
            input_alph (String): Alfabeto que compõe a cadeia de entrada
            tape_alph (String): Alfabeto que compõe a fita
            initial_state (String): Estado inicial
            transactions (String): Conjunto de transações responsáveis por toda a computação da máquina
            mt_input (String): Cadeia de entrada
        """
        self.states = states
        self.input_alph = input_alph
        self.tape_alph = tape_alph
        self.actual_state = initial_state
        self.transactions = transactions
        self.mt_input = mt_input
        self.current_tape = mt_input
        self.head_position = 0

    def __str__(self):
        """Metodo sobrecarregado para representação de uma MT, em que é retornado uma string com a
        configuração corrente da fita, construido através dos simbolos atuais da fita mesclado com o
        estado atual em sua posição condicionada pela cabeça de leitura.
        
        Returns:
            String: Demonstra a atual configuração da fita 
        """
        return self.current_tape[:self.head_position] + self.actual_state + self.current_tape[self.head_position:]

    def move_right(self, write_symbol, next_state):
        """Método utilziado para movimentar a cabeça de leitura para a direita devido a uma computação,
        além de escrever o próximo simbolo da fita e determinar o próximo estado.
        
        Args:
            write_symbol (String): Símbolo que será escrito na fita
            next_state (String): Estado determinado como novo estado atual
        
        """
        copy_current_tape = list(self.current_tape)
        copy_current_tape[self.head_position] = write_symbol
        self.head_position += 1
        if(self.head_position >= len(self.current_tape)):
            raise ValueError('Head position violates limits to the right')

        self.actual_state = next_state
        self.current_tape = "".join(copy_current_tape)

    def move_left(self, write_symbol, next_state):
        """Método utilizado para movimentar a cabeça de leitura para a esquerda em decorrencia de uma computação,
        além de escrever o próximo simbolo da fita e determinar o próximo estado.

        Args:
            write_symbol (String): Símbolo que será escrito na fita
            next_state (String): Estado determinado como novo estado atual

        """
        copy_current_tape = list(self.current_tape)
        copy_current_tape[self.head_position] = write_symbol
        self.head_position -= 1
        if(self.head_position >= len(self.current_tape)):
            raise ValueError('Head position violates limits to the left')

        self.actual_state = next_state
        self.current_tape = "".join(copy_current_tape)

    def start_computation(self):
        """Método que realiza a computação; extraindo uma transição de cada vez, é verificado se o simbolo lido
         na fita é igual ao símbolo presente na transição, bem como o estado atual e o estado presente na transição,
         se o símbolo lido e o próximo na transição pertence ao alfabeto da fita e, por fim, se o estado atual e o 
         próximo estado são pertencentes ao conjunto de estados válidos da MT. Com isso, são chamados os metódos
         de movimentação, direta ou esquerda, dependendo da direção especificada na transição, com o final da 
         computação printando a configuração resultante da fita
        """
        print(self)
        TransactionVerificator.check_initial_state_first_transaction(self.actual_state, self.transactions[0])

        for transaction in self.transactions:

            print(self.states + " teste")
            read_state =  transaction [1:3] 
            TransactionVerificator.check_state(self, read_state) 
            read_state = '{' + read_state + '}'
            
            read_symbol = transaction[4]
            TransactionVerificator.check_symbol_tape(self, read_symbol)
            
            next_symbol = transaction[-4]
            TransactionVerificator.check_symbol_tape(self, next_symbol)
            
            next_state = transaction[9:11]
            TransactionVerificator.check_state(self, next_state)
            next_state = '{' + next_state + '}'

            direction = transaction[-2]
            TransactionVerificator.check_direction(direction)
           
            while(True):
                if(self.actual_state == read_state and self.current_tape[self.head_position] == read_symbol):

                    if(direction == 'R'):
                        self.move_right(next_symbol, next_state)

                    elif(direction == 'L'):
                        self.move_left(next_symbol, next_state)

                    print("New tape configuration: " + str(self))
                else:
                    break
        
