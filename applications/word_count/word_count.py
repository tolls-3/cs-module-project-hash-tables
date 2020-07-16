ignored_characters = ['"', ':', ';', ',', '.', '-', '+', '=', '/',
                      "\"", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "\\"]


def word_count(s):
    # Your code here
    storage = {}
    lower_case = s.lower()

    for characters in ignored_characters:
        lower_case = lower_case.replace(characters, "")

    lower_case = lower_case.split()

    for word in lower_case:
        if word not in storage:
            storage[word] = 1
        else:
            storage[word] += 1
    return storage


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
