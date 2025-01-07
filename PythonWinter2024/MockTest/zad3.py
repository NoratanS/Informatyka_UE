import os


def count_words_aux(filename, word_count):
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            for word in str.lower(line).split():
                if word.isalnum():
                    if word not in word_count:
                        word_count[word] = 1
                    else:
                        word_count[word] += 1

    return word_count


def count_words(path):
    for cat in os.listdir(path):
        cat_path = os.path.join(path, cat)
        word_count = {}
        for filename in os.listdir(cat_path):
            file_path = os.path.join(cat_path, filename)
            word_count = count_words_aux(file_path, word_count)
        if len(word_count) != 0:
            total_words = sum(word_count.values())
            print(cat)
            for word, count in word_count.items():
                print(f"\t{word}:\t{count}\t{round(count/total_words * 100, 2)}%")


count_words('zad3_data')
