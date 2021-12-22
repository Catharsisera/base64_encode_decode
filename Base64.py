BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

class Base64(object):

    def __init__(self):
        pass

    def encode(alphabet, sequenceBytes):
        def Symb(x, op=8):
            t = ''
            if len(x) % op != 0:
                for i in range(op - len(x) % op):
                    t = t + '0'
            return t + x

        bitsCount = 6 # Число бит на символ в алгоритме
        TextBits = "".join([Symb(bin(i)[2:]) for i in sequenceBytes])
        sizeText = len(TextBits)

        while ((sizeText) % bitsCount) != 0:
            TextBits += '00000000'
            sizeText += 8

        TextBits = list(map(int, [i for i in TextBits]))
        TextBits = [TextBits[i] * 2 ** (bitsCount - i % bitsCount - 1) for i in range(len(TextBits))] #перевод из 2 в 10 (1)
        TextBits = [sum(TextBits[i * bitsCount:i * bitsCount + bitsCount]) for i in range(len(TextBits) // bitsCount)] #(2)

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

    def decode(alphabet, sequenceBytes, code='UTF-8'):
        bitsCount = 6
        TextBits = ["".join(['0' for k in range(bitsCount - len(bin(alphabet.index(i))[2:]))]) + bin(alphabet.index(i))[2:]
                    if i != '=' else "".join(['0' for l in range(bitsCount)]) for i in sequenceBytes]
        TextBits = "".join(TextBits)
        sizeText = len(TextBits)

        while '00000000' in TextBits[sizeText - 8:sizeText]:
            TextBits = TextBits[:sizeText - 8]
            sizeText -= 8

        finalSequence = [int('0b' + TextBits[i * 8:i * 8 + 8], 2) for i in range(sizeText // 8)]
        return finalSequence