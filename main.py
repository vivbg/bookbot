def main():
    book_path = "Books/frankenstein.txt"
    text = get_book_text(book_path)
    words=word_count(text)
    letters=letter_count(text)
    #print text
    #print (words)
    #print (letters)
    report(book_path,words,letters)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def word_count(string):
    words=string.split()
    word_count=len(words)
    return word_count

def letter_count(string):
    letters={}
    ordered_letters=[]
    lowered_string = string.lower()
    for i in lowered_string:
        if i.isalpha():
            letters[i]=letters.get(i,0)+1
    for letter in letters:
        temp_dict={}
        temp_dict={"character":letter,"count":letters[letter]}
        ordered_letters.append(temp_dict)
    ordered_letters.sort(reverse=True, key=lambda x: x['count'])
    return ordered_letters

def report(book_path,words,letters):
    print (f"--- Begin report of {book_path} ---")
    print (f"{words} words found in the document")
    for letter_dict in letters:
        print (f"The '{letter_dict['character']}' character was found {letter_dict['count']} times")
    print ("--- End report ---")

if __name__ == '__main__':
    main()