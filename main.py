from turing_machine import MT
import sys
if __name__ == "__main__":

    filename = sys.stdin
    try:
        machine = MT.build_from_file(filename)
        machine.start_computation()
    except Exception as ex:
        print(ex)
    
    print("Final tape confguration is: \n" + str(machine))

    
