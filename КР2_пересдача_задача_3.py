def count_triples(sequence):
    max_3 = max(
        (x for x in sequence if 10000 <= abs(x) <= 99999 and abs(x) % 10 == 3),
        default=None
    )
    if max_3 is None:
        return 0  

    count = 0
    for i in range(len(sequence) - 2):
        triple = sequence[i:i+3]
        if any(abs(x) % 10 == 3 for x in triple) and sum(triple) <= max_3:
            count += 1

    return count

sequence = [123, 10003, 23, -100023, 5, 13, 33]
print("Количество подходящих троек:", count_triples(sequence))
