# 1. 코딩 테스트 단어에 나오는 모음의 순서를 바꾸는 함수를 코딩해보세요.
# ex) hello -> holle
# naver webtoon => novor webtean

def main(str):
    strSet = set(['a','e','i','o','u','y','A','E', 'I', 'O', 'U', 'Y'])
    tempArray = []
    chaArray = []

    for cha in str:
        chaArray.append(cha)
        if cha in strSet:
            tempArray.append(cha)

    for index in range(len(chaArray)):
        if chaArray[index] in strSet:
            chaArray[index] = tempArray.pop()

    return chaArray;

result = main("nAvEr wEbtOOn")
print(''.join(result))
