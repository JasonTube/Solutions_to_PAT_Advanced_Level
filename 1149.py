if __name__ == '__main__':
    N,M = [int(tmp) for tmp in input().split(" ")]
    dangerous_dic = {}
    
    for i in range(N):
        item1,item2 = input().split(" ")
        if item1 in dangerous_dic:
            dangerous_dic[item1].add(item2)
        else:
            temp = set()
            temp.add(item2)
            dangerous_dic[item1] = temp
    #print(dangerous_dic)
    
    for i in range(M):
        package = [tmp for tmp in input().split(" ")]
        package = set(package[1:])
        for j in package:
            if j in dangerous_dic :
                if package & dangerous_dic[j]:
                # including same elements
                    print("No")
                    break
        else:
            print("Yes")
