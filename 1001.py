if __name__ == "__main__":
    a,b = [int(tmp) for tmp in input().split(" ")]

    summary = list(str(a + b))
    L = len(summary)

    for i in range(L-3,0,-3):
        summary[i] = ',' + summary[i]
    if summary[0] == '-' and summary[1][0] == ',':
        summary[1] = summary[1][1]
    
    print("".join(tmp for tmp in summary))
