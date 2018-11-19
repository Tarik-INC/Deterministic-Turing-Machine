from turing_machine import MT

if __name__ == "__main__":

    try:
        machine = MT.build_from_file('./test.txt')
        machine.start_computation()
    except Exception as ex:
        print(ex)
    
    print("Final tape confguration is: \n" + str(machine))

    
