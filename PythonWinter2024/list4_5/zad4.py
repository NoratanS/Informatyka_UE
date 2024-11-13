"""Napisz program, który umożliwia szyfrowanie podanego ciągu znaków przy użyciu szyfru Cezara, który jest szczególnym przypadkiem szyfru podstawieniowego
monoalfabetycznego.
Użytkownik program podaje tekst do zaszyfrowania oraz liczbę n, o którą przesunięty jest alfabet za pomocą którego szyfrujemy tekst. Dla uproszczenia można
przyjąć, że łańcuch wejściowy składa się tylko z małych liter alfabetu angielskiego,
tj. ’a’ – ’z’ (26 znaków) oraz spacji.
Przykład 1.
Podaj łańcuch znaków do zaszyfrowania: abrakadabraz
Podaj przesunięcie: 2
Zaszyfrowany tekst: cdtcmcfcdtcb
Przykład 2.
8
Podaj łańcuch znaków do zaszyfrowania: cdtcmcfcdtcb
Podaj przesunięcie: -2
Zaszyfrowany tekst: abrakadabraz"""


def caesar(s: str, n: int) -> str:
    print(f"before cypher: {s}")
    res = ""
    # cycle management
    n = n % (ord('z') - ord('a') + 1)

    for i in range(len(s)):
        # if we're in range then no problem
        if ord('a') <= ord(s[i]) + n <= ord('z'):
            res += chr(ord(s[i]) + n)
        # if we go over we need to cycle back to the start
        elif ord(s[i]) + n > ord('z'):
            res += chr(ord(s[i]) + n - (ord('z') - ord('a') + 1))
        else:
            # if we go under we need to cycle to the end
            res += chr(ord(s[i]) + n + (ord('z') - ord('a') + 1))
    print(f"after cypher: {res}")
    return res


caesar(caesar("abrakadabraz", 2000), -2000)
