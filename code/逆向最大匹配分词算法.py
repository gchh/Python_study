def wordseg(sentence,word_dic,maxl):
    end=len(sentence)
    words=[]
    while end>0:
        for begin in range(max(end-maxl,0),end,1):
            word=sentence[begin:end]
            if word in word_dic:
                words.append(word)
                break
        end=begin
    return words

phrases=raw_input().split(" ")
wordslists=[]
maxlength=0
for phrase in phrases:
    t=len(phrase)
    if t>maxlength:
        maxlength=t
while True:
    characters=wordseg(raw_input(),phrases,maxlength)
    if characters!=[]:
        wordslists.append(characters)
    else:
        break
for wordslist in wordslists:
    listlen=len(wordslist)
    for i in range(0,listlen,1):
        if i+1!=listlen:
            print wordslist[-i-1],
        else:
            print wordslist[-i-1]
