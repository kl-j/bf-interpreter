# program: the Brainfuck source code.
# memory: 30,000 cells initialized to zero.
# pointer: the current memory cell.
# pc: the position of the instruction we're executing.


class BrainfuckInterpreter:
    def __init__(self, program):
        self.program = program 
        self.memory = [0] * 30000  
        self.pointer = 0  
        self.pc = 0  
        self.bracket_map = self._build_bracket_map()

    #this function takes one bf instruction and performs the corresponding action
    # 

    def execute_basic(self, command):
        if command == '>':
            self.pointer += 1
        elif command == '<':
            self.pointer -= 1
        elif command == '+':
            self.memory[self.pointer] = (self.memory[self.pointer] + 1) % 256
        elif command == '-':
            self.memory[self.pointer] = (self.memory[self.pointer] - 1) % 256
        elif command == '.':
            print(chr(self.memory[self.pointer]), end='')
        elif command == ",":
            character = input("Input one character: ")
            if character:
                self.memory[self.pointer] = ord(character[0]) % 256


    def run(self):
        while self.pc < len(self.program):
            command = self.program[self.pc]

            if command in "><+-.,":
                self.execute_basic(command)

            elif command == "[":
                if self.memory[self.pointer] == 0:
                    self.pc = self.bracket_map[self.pc]

            elif command == "]":
                if self.memory[self.pointer] != 0:
                    self.pc = self.bracket_map[self.pc]

            self.pc += 1


    def _build_bracket_map(self):
        stack = []
        bracket_map = {}

        for position, command in enumerate(self.program):
            if command == "[":
                stack.append(position)

            elif command == "]":
                if not stack:
                    raise ValueError(
                        f"Unmatched ']' at position {position}"
                    )

                opening = stack.pop()
                bracket_map[opening] = position
                bracket_map[position] = opening

        if stack:
            raise ValueError(
                f"Unmatched '[' at position {stack[-1]}"
            )

        return bracket_map

if __name__ == "__main__":
    program = "+++++[>+++++++++++++<-]>."
    interpreter = BrainfuckInterpreter(program)
    interpreter.run()
    print()