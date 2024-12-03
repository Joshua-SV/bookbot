def main():
    filePath = "./books/frankenstein.txt"
    with open(filePath) as fi:
        fileContents = fi.read()
        counts = wordCount(fileContents)
        dic = letterCount(fileContents.lower())
        letterReport(counts, dic, filePath)

    
def wordCount(txt):
    try:
        return len(txt.split())
    except Exception as e:
        print(f'not a valid text file {e}')

def letterCount(txt):
    dic = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for char in txt:
        if char in dic:
            dic[char] += 1
    return dic 

def letterReport(wordC, diction, fp):
    print(f"------- Begin Book Report of {fp} -------")
    print(f"{wordC} words found in the document \n")
    for key in diction:    
        print(f"The '{key}' character was found {diction[key]} times")

main()