def merge_alternately(word1,word2):
    merged=[]
    i=j=0
    
    while i<len(word1) and j<len(word2):
        merged.append(word1[i])
        merged.append(word2[j])
        i+=1
        j+=1
    merged.append(word1[i:])
    merged.append(word2[j:])
    return ''.join(merged)

word1=input("Enter first string: ")
word2=input("Enter second string: ")

print("The Merged string is:",merge_alternately(word1, word2))
