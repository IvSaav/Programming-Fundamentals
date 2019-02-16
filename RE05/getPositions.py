def get_positions(word_list, sentence):
    if word_list[0] + " " + word_list[1] == sentence:
        position = "0 1"
    elif word_list[0] + " " + word_list[2] == sentence:
        position = "0 2"
    elif word_list[1] + " " + word_list[0] == sentence:
        position = "1 0"
    elif word_list[1] + " " + word_list[2] == sentence:
        position = "1 2"
    elif word_list[2] + " " + word_list[1] == sentence:
        position = "2 1"
    elif word_list[2] + " " + word_list[0] == sentence:
        position = "2 0"
    return position


print(get_positions(["hello", "brave", "hello"], "hello hello"))