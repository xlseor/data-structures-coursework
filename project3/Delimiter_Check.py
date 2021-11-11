import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
  # TODO replace pass with an implementation that returns True
  # if the delimiters (), [], and {} are balanced and False otherwise.
    delims = Stack()
    brace_dict = {"(":")", "[":"]", "{":"}"}

    quotes = Stack()
    escapes = Stack()

    #store quotes and escape characters in stacks. methods generate booleans which decide whether
    #a character should be pushed to the delimiter stack, or if it is escaped or part of an
    #string object contained in the program whose delimiters we're checking.
    def handle_quote(quote):
        if(quotes.peek() == None):
            quotes.push(quote)
        elif(quotes.peek() == quote):
            quotes.pop()
        return

    def is_quoted():
        return (quotes.peek() != None)

    def handle_escape(esc):
        if(escapes.peek() == None):
            escapes.push(esc)
        elif(escapes.peek() == "\\"):
            escapes.pop()

    def is_escaped():
        return(escapes.peek() != None)

    with open(filename) as file:
        file = file.read()
        for char in file:
            if(char == "'") or (char == '"'):
                handle_quote(char)
            if((is_quoted() == False) and (is_escaped() == False)):
                if((char == "(") or (char == "[") or (char == "{")):
                    delims.push(char)
                if((char == ")") or (char == "]") or (char == "}")):
                    compare = delims.pop()
                    if brace_dict[compare] != char: #pop the stack for a delimiter to compare, and pass it to the dictionary
                      #for comparison
                        return False
            escapes.pop()#empty escapes stack to avoid escaping more than one char after a backslash.
        check_stack = delims.pop()
        if check_stack is not None: #Check to see if stack is empty once we've parsed the whole file
            return False
    return True

if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')
