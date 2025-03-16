def merge(arr, ini, meio, fim):
    n1 = meio - ini + 1
    n2 = fim - meio

    # Criando subarrays temporários
    L = arr[ini:ini + n1]
    R = arr[meio + 1:meio + 1 + n2]

    i, j, k = 0, 0, ini

    # Intercala os subarrays
    while i < n1 and j < n2:
        if L[i] <= R[j]:  # Preserva estabilidade
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copia os elementos restantes de L[], se houver
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copia os elementos restantes de R[], se houver
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, ini, fim):
    if ini < fim:
        meio = (ini + fim) // 2
        merge_sort(arr, ini, meio)
        merge_sort(arr, meio + 1, fim)
        merge(arr, ini, meio, fim)


# Exemplo de uso
data = [38, 27, 43, 200, 9, 82, 10]
merge_sort(data, 0, len(data) - 1)
print("Array ordenado:", data)
