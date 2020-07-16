def no_dups(s):
    # Your code here
    keys = s.split()
    storage = {}
    string = ''
    
    for i, _ in enumerate(keys):
        storage[keys[i]] = True
    
    for key in storage:
        if string == '':
            string += key
        else:
            string += ' ' + key
    return string

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))