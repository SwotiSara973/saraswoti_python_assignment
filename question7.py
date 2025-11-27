def to_title_case(sentence):
    words = sentence.split()
    new_list = []

    for w in words:
        new_list.append(w[0].upper() + w[1:])
    
    return " ".join(new_list)

print(to_title_case("hello world from python"))
