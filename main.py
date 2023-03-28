class Stack:
    def __init__(self):
        self.stack = list()

    def is_empty(self):
        return not any(self.stack)

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

def checking(variant):
    bopen = ('(', '[', '{')
    bclose = (')', ']', '}')
    check = Stack()
    for element in variant:
        if element in bopen:
          check.push(element)
        elif element in bclose:
            if check.size() == 0:
                return False
            else:
                if (ord(element) == ord(check.peek()) + 1) or (ord(element) == ord(check.peek()) + 2):
                    check.pop()
                else:
                    return False
    return check.is_empty()

if __name__ == '__main__':
    list_of_variant = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']
    for variant in list_of_variant:
        if checking(variant):
            print('Сбалансированно')
        else:
            print('Несбалансированно')
