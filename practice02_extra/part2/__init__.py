# Преобразование Барроуза-Уилера
def burrows_wheeler(src):
    curr_idx = 0
    tmp = tmp_str = response = []

    for i in range(len(src)):
        tmp.append(src)
        src = src[1:] + src[0]
    tmp.sort()

    for i in range(len(src)):
        if tmp[i] == src:
            curr_idx = i
            break

    for i in range(len(src)):
        response.append(tmp[i][-1])
        tmp_str += tmp[i][-1]
    response.sort()

    for i in range(len(src) - 1):
        for j in range(len(src)):
            response[j] = tmp_str[j] + response[j]
        response.sort()

    return response[curr_idx]


if __name__ == '__main__':
    print(burrows_wheeler('12345'))
    print(burrows_wheeler('941'))
