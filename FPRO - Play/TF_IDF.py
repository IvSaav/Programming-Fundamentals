'''
TF-IDF
'''


def tfidf(documents):
    
    from math import log
     
    # vocabulary
    vocab = []
    for doc in documents:
        vocab.append(doc.lower().split(" "))
    
    # frequency vector
    tf = {}
    for i in range(len(vocab)):
        for word in vocab[i]:
            if word in tf:
                tf[word][i] += 1
            else:
                tf[word] = [0 for n in range(len(vocab))] # creting vector
                tf[word][i] = 1
     
    # IDF
    keys = tf.keys()
    N = len(vocab)
    for key in keys:
        vector = tf[key]
        # numbers of docs were the word appears
        n = 0 
        for x in vector:
            if x != 0:
                n += 1
        # updating vector
        for j in range(len(documents)):
            vector[j] = round(vector[j]*log(N/n), 3)
        # updating tf with new vector   
        tf[key] = vector
        
    return tf
        
        
            
        
    
     
     
     
     
                     
     
    
print(tfidf(["To be or not to be", "Impossible is a word to be found only in the dictionary of fools", "There is nothing impossible to him who will try"]))