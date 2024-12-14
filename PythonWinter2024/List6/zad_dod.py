"""Połącz macierz błędów
Zaimplementować funkcję def confusion_matrix(path), która jako parametr otrzymuje ścieżkę
do katalogu, w którym znajdują się pliki tekstowe. Wszystkie te pliki zawierają rzeczywiste wyniki
klasyfikacji przeprowadzone przez program WEKA (można to założyć i nie trzeba dokonywać żadnych
sprawdzeń). W wyniku działania należy stworzyć plik o nazwie „zad_dod_result.txt”, w którym zapisana będzie
suma wszystkich macierzy błędów z plików.
Każdy plik ma tę samą strukturę – w pewnym momencie pojawia się linia:
‘=== Confusion Matrix ===\n’
Po niej (w pewnej strukturze) pojawia się macierz błędu. Można założyć, że w każdym pliku ta macierz
będzie dokładnie tej samej wielkości – w wyniku działania programu należy połączyć (dodać) wartości
macierzy z każdego pliku. Dla przykładowej macierzy:
Plik 1: Plik 2:
=== Confusion Matrix === === Confusion Matrix ===
a b c d <-- classified as a b c d <-- classified as
2 3 0 1 | a = 1 2 4 0 0 | a = 1
5 12 12 2 | b = 2 1 8 10 0 | b = 2
0 3 39 23 | c = 3 0 0 1 0 | c = 3
0 1 18 81 | d = 4 1 1 42 2 | d = 4
Plik wyjściowy powinien zawierać:
4 7 0 1
6 20 22 2
0 3 40 23
1 2 60 83"""
import os


# finds the confusion matrix in a file and returns it as a list of lists of ints
def extract_confusion_matrix(file_path: str, key="=== Confusion Matrix ===\n") -> list[list[int]]:
    file = open(file_path, "r")
    lines = file.readlines()
    file.close()

    # find confusion matrix location in the file
    key_pos = 0
    for i in range(len(lines) - 1, 0, -1):  # search from the back for a small optimization
        if lines[i] == key:
            key_pos = i
            break

    # extract the confusion matrix from the file
    mat = []
    for i in range(key_pos + 3, len(lines)):  # +3 skips unnecessary lines to get to the numbers
        row = lines[i]
        if row != '\n':
            row_end = row.find('|')
            mat.append([int(num) for num in row[:row_end].strip().split()])
        else:
            break

    return mat


# adds all n x n matrices in a list together and returns one matrix as a result
def add_matrices(mats: list[list[list[int]]]) -> list[list[int]]:
    mats_len = len(mats)
    if mats_len == 0:
        raise ValueError("matrix list is empty")

    res_mat = mats[0]  # we take the first matrix to store the result
    mat_size = len(mats[0])
    for i in range(1, mats_len):  # here we add the remaining matrices
        for row in range(mat_size):
            for col in range(mat_size):
                res_mat[row][col] += mats[i][row][col]

    return res_mat


# saves the confusion matrix to a specified file,
# num_len defines the amount of characters that the numbers will be written on
def save_result_matrix(file_path: str, res_mat: list[list[int]], num_len=6) -> None:
    file = open(file_path, "w")
    for i in range(len(res_mat)):
        row = ""
        for num in res_mat[i]:
            row += f"{num:{num_len}}"
        file.write(f"{row}\n")
    file.close()


# finds and adds confusion matrices in a specified directory and saves the result to a specified file
def combine_confusion_matrix(data_dir_path="zad_dod_data", result_file_path="zad_dod_result.txt") -> None:
    data_files_paths = [os.path.join(data_dir_path, file_path) for file_path in os.listdir(data_dir_path)]
    matrix_list = [extract_confusion_matrix(file_path) for file_path in data_files_paths]
    res_mat = add_matrices(matrix_list)
    save_result_matrix(result_file_path, res_mat)


combine_confusion_matrix()
