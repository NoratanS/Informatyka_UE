"""6. Napisać funkcję czy anagram(t1, t2) , która sprawdza, czy łańcuch t2 jest
anagramem tekstu t1 , czyli czy składa się z tych samych znaków, ale ustawionych
niekoniecznie w tej samej kolejności
Uwaga, należy sprawdzać jedynie małe i duże litery alfabetu angielskiego, jednak
bez względu na ich wielkość, tzn. zarówno małe ’a’ jak i duże ’A’ liczone są tak
samo. Pozostałe znaki nie są sprawdzane, a więc nie mają wpływu na to, czy
słowo będzie uznane za anagram innego.
Przykładowo, dla poniższego fragmentu programu:
czy_anagram("kolej", "olejk") -> true
czy_anagram("kolej", "kole") -> false
czy_anagram("kolej", "K O L E J") -> true
czy_anagram("Gregory House", "Huge ego, sorry") -> true"""


def is_anagram(t1: str, t2: str) -> bool:
    t1 = t1.lower()
    t2 = t2.lower()
    d1 = {}
    d2 = {}

    for char in t1:
        if char.isalpha():
            if char in d1:
                d1[char] += 1
            else:
                d1[char] = 1

    for char in t2:
        if char.isalpha():
            if char in d2:
                d2[char] += 1
            else:
                d2[char] = 1

    return d1 == d2


print(is_anagram("kolej", "olejk"))
print(is_anagram("kolej", "kole"))
print(is_anagram("kolej", "K O L E J"))
print(is_anagram("Gregory House", "Huge ego, sorry"))

