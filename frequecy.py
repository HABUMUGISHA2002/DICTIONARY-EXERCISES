def word_frequencies(sentence):
    words = sentence.split()
    frequency_dict = {}
    
    for word in words:
        word = word.lower()
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
            
    return frequency_dict

sentence = "Ghadi HABUMUGISHA Ghadi"
frequencies = word_frequencies(sentence)
print(frequencies)  
