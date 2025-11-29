# tab=[18,2,15,1,22,13,27,12,29,16,21,19,26,24,23,28,17,25,14,30]
# def select(tab):
#     for i in range(len(tab)):
#         min_idx = i
#         for j in range(i+1, len(tab)):
#             if tab[j] < tab[min_idx]:
#                 min_idx = j
#         tab[i], tab[min_idx] = tab[min_idx], tab[i]
#     return tab
# print(select(tab))

T = [18, 2, 15, 1, 22, 13, 27, 12, 29, 16, 21, 19, 26, 24, 23, 28, 17, 25, 14, 30]

def select(tab):
    for i in range(len(tab)):
        indmin = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[indmin]:
                indmin = j
        
        temp = tab[i]
        tab[i] = tab[indmin]
        tab[indmin] = temp
    return tab

print(select(T))