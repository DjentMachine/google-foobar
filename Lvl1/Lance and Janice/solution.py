def solution(text):
    alpha ="abcdefghijklmnopqrstuvwxyz"
    beta = alpha[::-1]
    decoded = [i for i in text]

    for i in range(len(decoded)):
        if alpha.find(decoded[i]) >= 0:
            decoded[i] = beta[alpha.index(decoded[i])]
    decoded2= "".join([i for i in decoded])
    return decoded2