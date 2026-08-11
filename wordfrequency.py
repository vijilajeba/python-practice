words=[]
while True:
    word=input("Enter The word(q to quit):")
    if word.lower()=='q':
        break
    else:
        words.append(word)
unique_words=set(words)
for u_word in unique_words:
    count=0
    for word in words:
        if word==u_word:
            count+=1
    print(f"{u_word}:{count}")

