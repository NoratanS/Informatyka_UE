import os


def analyze_reviews_aux(filename, word_count, min_word_size):
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        for word in str.lower(line).strip().split():
            if word.isalpha() and len(word) >= min_word_size:
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1

    return word_count


def analyze_reviews(path, min_word_size=3):
    for cat in os.listdir(path):
        cat_path = os.path.join(path, cat)
        word_count = {}
        for filename in os.listdir(cat_path):
            file_path = os.path.join(cat_path, filename)
            word_count = analyze_reviews_aux(file_path, word_count, min_word_size)
        print("Category:", cat)
        print("     Number of reviews:", len(os.listdir(cat_path)))
        print("     Average words per review:", sum(word_count.values()) / len(os.listdir(cat_path)))
        print("     Most popular word:", max((list(word_count.items())), key=lambda x: x[1])[0])


analyze_reviews('zad2_data')
analyze_reviews('mini_newsgroups')
