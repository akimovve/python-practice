# Задача 2.1
def f21(arr):
    tree = {
        "yacc": 11,
        "x10": 12,
        "volt": {
            2010: 10,
            1986: {
                "roff": 6,
                "svg": {
                    1969: 7,
                    2006: 8,
                    1994: 9
                }
            },
            2007: {
                "roff": {
                    1969: 0,
                    2006: 1,
                    1994: 2
                },
                "svg": {
                    "rebol": 3,
                    "grace": 4,
                    "idl": 5
                }
            }
        }
    }
    resolve = tree[arr[1]]
    if type(resolve) is not dict:
        return resolve
    resolve = resolve[arr[2]]
    if type(resolve) is not dict:
        return resolve
    resolve = resolve[arr[3]]
    prev = arr[2]
    if type(resolve) is not dict:
        return resolve
    el = arr[3]
    if prev == 2007 and el == "svg":
        return resolve[arr[4]]
    return resolve[arr[0]]


print(f21([1994, "yacc", 2007, "roff", "grace"]))
print(f21([1969, "volt", 2007, "roff", "idl"]))
print(f21([1994, "volt", 1986, "svg", "idl"]))
