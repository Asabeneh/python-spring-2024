

""" 
def read_file_func(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    words = []
    for line in lines:
        word_lst = line.strip('\n').lower().split()
        words.extend(word_lst)
    
    return words 

print(read_file_func('sample.txt'))
print(read_file_func('notes.txt')) """



def read_file_func(filename):
    with open(filename) as file:
        lines = file.readlines()
        file.close()
        words = []
        for line in lines:
            word_lst = line.strip('\n').lower().split()
            words.extend(word_lst)
        return words 

print(read_file_func('sample.txt'))
print(read_file_func('notes.txt'))



