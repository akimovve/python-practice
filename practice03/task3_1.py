from struct import unpack

from source import Source


# Задача 1
def f31(binary_data):
    start_from = [int(i) for i in [0x45, 0x4a, 0x46, 0x50, 0x46]]
    # Получение id, с которого необходимо начать обработку
    idx = [
        (i, i + len(start_from)) for i in range(len(binary_data))
        if [int(i) for i in binary_data[i:i + len(start_from)]] == start_from
    ][0][1]

    def struct_a(index):
        response = {}
        # Структура B
        response['A1'], index = struct_b(index)

        # uint16
        [a2] = unpack('>H', binary_data[index:index + 2])
        index += 2
        response['A2'] = a2

        # Массив структур D, размер 2
        d_size = 2
        a3_tmp = [struct_d(index + i * 12) for i in range(d_size)]
        response['A3'] = [i[0] for i in a3_tmp]
        index = [i[1] for i in a3_tmp][d_size - 1]

        # Структура E
        response['A4'], index = struct_e(index)

        # float, int8
        a5, a6 = unpack('>fb', binary_data[index:index + 5])
        index += 5
        response['A5'] = a5
        response['A6'] = a6

        return response

    def struct_b(index):
        response = {}
        # int16, int32
        b1, b2 = unpack('>hi', binary_data[index:index + 6])
        index += 6
        response['B1'] = b1
        response['B2'] = b2

        # Размер (uint32) и адрес (uint16) массива char
        size, address = unpack('>IH', binary_data[index:index + 6])
        b3 = ''.join([chr(i) for i in binary_data[address:address + size]])
        index += 6
        response['B3'] = b3

        # Структура C
        response['B4'], index = struct_c(index)

        # int8, int32
        b5, b6 = unpack('>bi', binary_data[index:index + 5])
        index += 5
        response['B5'] = b5
        response['B6'] = b6

        return response, index

    def struct_c(index):
        response = {}
        # Размер (uint32) и адрес (uint32) массива int64
        size, address = unpack('>II', binary_data[index:index + 8])
        c1 = list(unpack('>{}q'.format(size),
                         binary_data[address:address + 8 * size]))
        index += 8
        response['C1'] = c1

        # uint16, int64
        c2, c3 = unpack('>Hq', binary_data[index:index + 10])
        index += 10
        response['C2'] = c2
        response['C3'] = c3

        return response, index

    def struct_d(index):
        response = {}
        # uint64, float
        d1, d2 = unpack('>Qf', binary_data[index:index + 12])
        index += 12
        response['D1'] = d1
        response['D2'] = d2

        return response, index

    def struct_e(index):
        response = {}
        # int32
        [e1] = unpack('>i', binary_data[index:index + 4])
        index += 4
        response['E1'] = e1

        # Размер (uint16) и адрес (uint32) массива int32
        size, address = unpack('>HI', binary_data[index:index + 6])
        e2 = list(unpack('>{}i'.format(size),
                         binary_data[address:address + 4 * size]))
        index += 6
        response['E2'] = e2

        # int8, uint16, int64
        e3, e4, e5 = unpack('>bHq', binary_data[index:index + 11])
        index += 11
        response['E3'] = e3
        response['E4'] = e4
        response['E5'] = e5

        return response, index

    return struct_a(idx)


if __name__ == '__main__':
    assert f31(Source.BINARY_1.value) == Source.RESULT_1.value
    assert f31(Source.BINARY_2.value) == Source.RESULT_2.value
