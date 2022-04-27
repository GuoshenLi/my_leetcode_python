def KNN_classify(k,X_train,y_train,x):
    """
      k:表示knn的中k的值
      X_train: 训练集的features
      y_train: 训练集的labels
      x: 新的数据
    """

    
    # 计算新来的数据x与整个训练数据中每个样本数据的距离
    distances = [sqrt(np.sum((x_train-x)**2)) for x_train in X_train]
    nearest = np.argsort(distances) # 对距离排序并返回对应的索引

    topK_y = [y_train[i] for i in nearest] # 返回最近的k个距离对应的分类
    votes = Counter(topK_y) # 统计属于每个分类的样本数

    return votes.most_common(1)[0][0] # 返回属于样本数最多的分类结果