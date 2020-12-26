import numpy as np
# игр % побед болельщиков
ih_wgt = np.array([[0.1, 0.2, -0.1],
                   [-0.1,0.1, 0.9],
                   [0.1, 0.4, 0.1]]).T

hp_wgt = np.array([[0.3, 1.1, -0.3],
                  [0.1, 0.2, 0.0],
                   [0.0, 1.3, 0.1]]).T

ws = [ih_wgt, hp_wgt]


def neural_network(input, ws):
    hid = input.dot(ws[0])
    pred = hid.dot(ws[1])
    return pred


toes = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])
# В переменной input передается запись,
# соответствующая первой игре в сезоне.
input = np.array([toes[0], wlrec[0], nfans[0]])
pred = neural_network(input, ws)
print(pred)