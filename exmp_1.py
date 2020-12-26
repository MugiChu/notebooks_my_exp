w = 0.1


def neural_work(input, w):
    p = input * w
    return p


number_of_toes = [8.5, 9.5, 10, 9]
input = number_of_toes[0]
pred = neural_work(input, w)
print(pred)