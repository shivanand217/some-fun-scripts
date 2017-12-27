'''
Simple Turing machine, which complements a binary input on the tape, like an input "1100111" will be turned into "0011000". 
Σ = {0, 1} 
Q = {initial state, final state} 
q0 = init 
qf = final 

'''


from turing_machine_class import TuringMachine

initial_state = "init",
accepting_states = ["final"],
transition_function = {("init","0"):("init", "1", "R"),
                       ("init","1"):("init", "0", "R"),
                       ("init"," "):("final"," ", "N"),
                       }
final_states = {"final"}

t = TuringMachine("010011 ", 
                  initial_state = "init",
                  final_states = final_states,
                  transition_function=transition_function)

print("Input on Tape:\n" + t.get_tape())

while not t.final():
    t.step()

print("Result of the Turing machine calculation:")    
print(t.get_tape())
