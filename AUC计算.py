from sklearn.metrics import roc_auc_score, roc_curve
import numpy as np
from collections import Counter

def calc_auc(y_score, y_true):

    length = len(y_true)
    pos_num = sum(y_true)
    neg_num = length - pos_num

    arr = [[y_score[i], y_true[i]] for i in range(length)]

    arr = sorted(arr, key = lambda d:d[0])

    table = np.zeros((length, 3))

    for i in range(length):
        table[i, 0] = arr[i][0]
        table[i, 1] = arr[i][1]
        table[i, 2] = i + 1

    # first column is score, second column is label, third column is rank

    count = Counter(y_pred)
    for k, v in count.items():
        if v != 1:
            # numpy bool切片 可以选行 再选列
            table[table[:, 0] == k, 2] = np.mean(table[table[:, 0] == k, 2])

    pos_rank_sum = 0
    for i in range(length):
        if table[i, 1] == 1:
            pos_rank_sum += table[i, 2]


    return (pos_rank_sum - pos_num * (pos_num + 1) / 2) / (pos_num * neg_num)


def calc_auc_2(y_score, y_true):

    arr = [[y_score[i], y_true[i]] for i in range(len(y_score))]

    neg_list = list(filter(lambda x:x[1] == 0, arr))
    pos_list = list(filter(lambda x:x[1] == 1, arr))

    num_pos = len(pos_list)
    num_neg = len(neg_list)
    sum_ = 0
    for i in range(num_pos):
        for j in range(num_neg):
            if pos_list[i][0] > neg_list[j][0]:
                sum_ += 1
            elif pos_list[i][0] == neg_list[j][0]:
                sum_ += 0.5

    return sum_ / (num_neg * num_pos)

# y_pred = [0.9,0.9,0.8,0.7,0.6,0.3,0.2,0.1]
# y_true = [1,0,1,1,0,0,0,0]

# 腾讯面试题目
y_pred = list(np.random.uniform(0.4, 0.6, 2000)) + list(np.random.uniform(0.5,0.7,8000))
y_true = [0] * 2000 + [1] * 8000

print(calc_auc_2(y_score = y_pred, y_true = y_true))
print(roc_auc_score(y_score = y_pred, y_true = y_true))

fpr, tpr,_ = roc_curve(y_true=y_true, y_score=y_pred)
import matplotlib.pyplot as plt
plt.plot(fpr, tpr, 'r--')
plt.title('ROC_Curve')
plt.show()
