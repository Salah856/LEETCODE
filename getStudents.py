def get_students(text):
    return [text[1],text[-1]]

_ = get_students([input() for x in range(4)])

print(len(set(_[0].split()) & set(_[-1].split())))
