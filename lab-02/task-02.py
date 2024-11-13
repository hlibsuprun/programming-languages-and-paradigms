import re


def dodaj_macierze(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mnoz_macierze(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def transponuj_macierz(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def walidacja_operacji(A, B, operacja):
    if operacja == 'dodaj' and len(A) == len(B) and len(A[0]) == len(B[0]):
        return True
    if operacja == 'mnoz' and len(A[0]) == len(B):
        return True
    if operacja == 'transponuj':
        return True
    return False


def wykonaj_operacje(operacja_string, A, B=None):
    operacja_match = re.match(r'(\w+)\(([^,]+)(?:,\s*([^,]+))?\)', operacja_string)
    if not operacja_match:
        print("Niepoprawny format operacji.")
        return None

    nazwa_operacji = operacja_match.group(1)
    macierz_a = operacja_match.group(2)
    macierz_b = operacja_match.group(3) if operacja_match.group(3) else None

    if macierz_a != 'A' or (macierz_b and macierz_b != 'B'):
        print("Macierze muszą być przekazane jako 'A' i 'B'.")
        return None

    if not walidacja_operacji(A, B, nazwa_operacji):
        print(f"Operacja '{nazwa_operacji}' nie może być wykonana z powodu niezgodności wymiarów macierzy.")
        return None

    if nazwa_operacji == 'dodaj':
        return eval("dodaj_macierze(A, B)")
    elif nazwa_operacji == 'mnoz':
        return eval("mnoz_macierze(A, B)")
    elif nazwa_operacji == 'transponuj':
        return eval("transponuj_macierz(A)")
    else:
        print("Niepoprawna operacja.")
        return None


A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

operacje = [
    "dodaj(A, B)",
    "mnoz(A, B)",
    "transponuj(A)"
]

for op in operacje:
    wynik = wykonaj_operacje(op, A, B)
    print(f"Wynik operacji '{op}':\n{wynik}")
