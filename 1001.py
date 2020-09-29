if __name__ == "__main__":
    a,b = [int(tmp) for tmp in input().split(" ")]
    summary = list(str(a + b))
    L = len(summary)
    result = []
    
    for i in range(L):
        result.insert(0,summary[-i-1])
        if (i-2) % 3 == 0:
            result.insert(0,",")

    if result[0] == ',':
        result.remove(',')
    elif result[0] == '-' and result[1] == ',':
        result.remove(',')

    print("".join(tmp for tmp in result))
