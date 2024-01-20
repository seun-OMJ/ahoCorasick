#--------------------------------------------
# NAME: SEUN OMOJOLA
# STUDENT NUMBER: 7880480 
# COURSE: COMP 4820
#---------------------------------------------

def count_pattern_occurrences(sequence, list):
    string_frequency = {}
    for string in list:
        string_len = len(string)
        counter = 0
        for i in range(len(sequence) - string_len + 1):
            if (sequence[i:i + string_len] == string):
                counter += 1
        string_frequency[string] = counter
    return string_frequency
