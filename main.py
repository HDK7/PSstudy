# 코딩테스트
#
# - 문자열 내에서 반복되지 않는 문자를 찾기 (대소문자 구분 안함)
# - 문자는 알파벳으로만 이루어져 있음
# - input : abcdefgadfkjhaeigfkasndccjoperhqwienfeiahbukascdbzabcdfg
# - output : opqruwz

def main(input):
    m = dict()

    for cha in input:
        if not cha in m:
            m[cha] = 1
        else:
            m[cha] = m[cha] + 1

    result = []
    for cha in m:
        if m[cha] == 1:
            result.append(cha)

    return result

returnArray = main("abcdefgadfkjhaeigfkasndccjoperhqwienfeiahbukascdbzabcdfg")
print(returnArray)





