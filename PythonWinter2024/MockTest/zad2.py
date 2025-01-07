def change_phrases(text: str, phrases: list[tuple]):
    text_copy = str.lower(text)
    for phrase in phrases:
        text_copy = text_copy.replace(phrase[0], phrase[1])

    text_lst = text.split()
    text_copy_lst = text_copy.split()
    print(text_lst)
    for i in range(len(text_lst)):
        if text_lst[i][0].isupper():
            text_copy_lst[i] = text_copy_lst[i].capitalize()

    return " ".join(text_copy_lst)


print(change_phrases("Ala ma kota, psa i dom. Kota mam też ja. Psa nie ma nikt, nawet Mama.",
                     [("kota", "szczura"), ("psa", "ogórka"), ("ma", "xyz")]))
