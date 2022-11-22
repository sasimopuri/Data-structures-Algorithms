def linearsearch(arr,key):
    for i in range(len(arr)):
        if(arr[i]==key):
            return i


def main():
    arr=list(map(int,input().split()))
    k=int(input())
    ans=linearsearch(arr,k)
    print(k,'is found at ',ans)

if __name__ == '__main__':
    main()