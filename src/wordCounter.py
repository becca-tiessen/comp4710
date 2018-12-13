import collections

def removeUnwantedSymbols(wordlist):
    wordlist = wordlist.replace(",","");
    wordlist = wordlist.replace(".","");
    wordlist = wordlist.replace("!","");
    wordlist = wordlist.replace("@","");
    wordlist = wordlist.replace("#","");
    wordlist = wordlist.replace("$","");
    wordlist = wordlist.replace("%","");
    wordlist = wordlist.replace("^","");
    wordlist = wordlist.replace("&","");
    wordlist = wordlist.replace("*","");
    wordlist = wordlist.replace("()","");
    wordlist = wordlist.replace(")","");
    wordlist = wordlist.replace("-","");
    wordlist = wordlist.replace("}","");
    wordlist = wordlist.replace("{","");
    wordlist = wordlist.replace("=","");
    wordlist = wordlist.replace("|","");
    return wordlist

file = open('../assets/FemaleQuestion.txt', 'r')
wordstring = file.read()

wordlist = removeUnwantedSymbols(wordstring)
wordlist = wordlist.lower().split()

trimmedlist = [];

for word in wordlist:
    if "<" not in word or ">" not in word:
        trimmedlist.append(word)

freq = collections.Counter(trimmedlist)
print freq.most_common(10)
