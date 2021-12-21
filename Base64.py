BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def encode(alphabet, sequenceBytes):
    def Symb(x, op=8):
        t = ''
        if len(x) % op != 0:
            for i in range(op - len(x) % op):
                t = t + '0'
        return t + x

    bitsCount = 6  # Число бит на символ в алгоритме
    TextBits = "".join([Symb(bin(i)[2:]) for i in sequenceBytes])
    sizeText = len(TextBits)

    while ((sizeText) % bitsCount) != 0:
        TextBits += '00000000'
        sizeText += 8

    TextBits = list(map(int, [i for i in TextBits]))
    TextBits = [TextBits[i] * 2 ** (bitsCount - i % bitsCount - 1) for i in range(len(TextBits))]  # перевод из 2 в 10
    TextBits = [sum(TextBits[i * bitsCount:i * bitsCount + bitsCount]) for i in range(len(TextBits) // bitsCount)]
    zeroBytes = 1  # Флаг работы с добавленными нулевыми битами
    lastPos = -1
    countBytes = []
    finalSequence = []

    while zeroBytes:
        if (TextBits[lastPos - 1] != 0) and (TextBits[lastPos] == 0):
            zeroBytes = 0
        else:
            TextBits.pop()
            countBytes.append("=")

    finalSequence = [alphabet[i] for i in TextBits]
    finalSequence.extend(countBytes)
    finalSequence = "".join(finalSequence)
    return finalSequence

print(encode(BASE64,bytes("ПРОДАМ ДУШУ ЗА ХОРОШУЮ ОЦЕНКУ","CP1251")))