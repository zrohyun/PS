def solution(numbers):

    answer = []
    for n in numbers:
        # 제일 마지막 비트가 비었다면 마지막 비트를 바꾼 수 푸시
        if 1 & n == 0:
            answer.append(n + 1)
        else:

            binary = list("0" * (52 - len(bin(n))) + bin(n)[2:])
            for i in range(len(binary) - 1, 0, -1):
                if binary[i] == "0":
                    break

            binary[i] = "1"
            binary[i + 1] = str(int(binary[i + 1]) ^ 1)
            answer.append(int("".join(binary), 2))

    return answer
