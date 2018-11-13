from turing_machine import MT 

if __name__ == "__main__":
    machine = MT.build_from_file('./test.txt')
    machine.start_computation()