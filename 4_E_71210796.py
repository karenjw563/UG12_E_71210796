def score_x(deret_bilangan):
    score_big = deret_bilangan[0]
    for score in deret_bilangan:
        if score > score_big:
            score_big = score
    return score_big
def score_y(deret_bilangan):
    score_small = deret_bilangan[0]
    for score in deret_bilangan:
        if score < score_small:
            score_small = score
    return score_small

x=[3, 20, 100, -35, 50]
print (x)
print('Nilai terbesar: ', score_x(x))
print('Nilai terkecil: ', score_y(x))

y=[3, 20, 90, 35, 75]
print (y)
print('Nilai terbesar: ', score_x(y))
print('Nilai terkecil: ', score_y(y))