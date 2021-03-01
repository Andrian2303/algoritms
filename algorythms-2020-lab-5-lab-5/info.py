from rabin_karp_algorithm import search_pattern

if __name__ == "__main__":
    prime_number = 893
    digits_amount = 256

    with open('exmp/in', 'r+') as fileIn:
        text = fileIn.readline()
        pattern = fileIn.readline()

    with open('exmp/out', 'w') as fileOut:
        fileOut.write('\n'.join('%s %s' % x for x in search_pattern(pattern, text, prime_number, digits_amount)))