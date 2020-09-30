import operator

def most_frequent(string):
  dict1 = dict()
  for i in string:
    if i not in dict1:
      dict1[i] = 1
    else:
      dict1[i]+=1
  sortedLetters = sorted(dict1.items(), key=operator.itemgetter(1), reverse=True)
    
  return sortedLetters

i = input()
print(most_frequent(i))
