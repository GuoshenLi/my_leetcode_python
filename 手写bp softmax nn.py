import numpy as np
from tensorflow.keras.datasets.mnist import load_data
import matplotlib.pylab as plt
from sklearn.preprocessing import OneHotEncoder


class ANN:
    def __init__(self, hidden_dim):
        self.layers_dim = hidden_dim
        self.parameters = {}
        self.n = 0
        self.costs = []

    def sigmoid(self, Z):
        return 1 / (1 + np.exp(-Z))


    def softmax(self, Z):
        return np.exp(Z) / np.sum(np.exp(Z), axis=1, keepdims=True)

    def initialize_parameters(self):
        np.random.seed(1)

        for l in range(1, len(self.layers_dim)):
            self.parameters["W" + str(l)] = np.random.uniform(-1, 1, size=[self.layers_dim[l - 1], self.layers_dim[l]])
            self.parameters["b" + str(l)] = np.zeros((self.layers_dim[l],))

    def forward(self, X):
        store = {}

        A = X
        for l in range(1, self.L - 1):
            Z = A @ self.parameters["W" + str(l)] + self.parameters["b" + str(l)]
            A = self.sigmoid(Z)
            store["A" + str(l)] = A
            store["W" + str(l)] = self.parameters["W" + str(l)]
            store["Z" + str(l)] = Z

        Z = A @ self.parameters["W" + str(self.L - 1)] + self.parameters["b" + str(self.L - 1)]
        A = self.softmax(Z)
        store["A" + str(self.L - 1)] = A
        store["W" + str(self.L - 1)] = self.parameters["W" + str(self.L - 1)]
        store["Z" + str(self.L - 1)] = Z

        return A, store

    def sigmoid_derivative(self, Z):
        Z = self.sigmoid(Z)
        return Z * (1 - Z)

    def backward(self, X, Y, store):

        derivatives = {}
        num_sample = X.shape[0]
        store["A0"] = X
        index = self.L - 1
        A = store["A" + str(index)]
        dZ = A - Y

        dW = store["A" + str(index - 1)].T @ dZ  / num_sample
        db = np.sum(dZ, axis=0) / num_sample

        derivatives["dW" + str(index)] = dW
        derivatives["db" + str(index)] = db

        for l in range(index - 1, 0, -1):
            dA = dZ @ store["W" + str(l + 1)].T
            dZ = dA * self.sigmoid_derivative(store["Z" + str(l)])
            dW = store["A" + str(l - 1)].T @ dZ / num_sample
            db = np.sum(dZ, axis=0) / num_sample


            derivatives["dW" + str(l)] = dW
            derivatives["db" + str(l)] = db

        return derivatives

    def fit(self, X, Y, test_x, test_y, learning_rate=0.01, n_iterations=2500, batch_size=32):
        np.random.seed(1)

        self.n = X.shape[0]

        self.layers_dim.insert(0, X.shape[1])
        self.layers_dim.append(Y.shape[1])
        self.L = len(self.layers_dim)
        self.initialize_parameters()

        for loop in range(n_iterations):
            shuffle = np.random.permutation(self.n)
            train_loss = 0
            train_acc = 0
            X_batches = np.array_split(X[shuffle], self.n / batch_size)
            Y_batches = np.array_split(Y[shuffle], self.n / batch_size)

            for batch_X, batch_Y in zip(X_batches, Y_batches):

                batch_A, store = self.forward(batch_X)
                train_loss += np.mean(np.sum(-np.log(batch_A) * batch_Y, axis=1))
                derivatives = self.backward(batch_X, batch_Y, store)

                for l in range(1, self.L):
                    self.parameters["W" + str(l)] = self.parameters["W" + str(l)] - learning_rate * derivatives[
                        "dW" + str(l)]
                    self.parameters["b" + str(l)] = self.parameters["b" + str(l)] - learning_rate * derivatives[
                        "db" + str(l)]

                train_acc += self.predict(batch_X, batch_Y)

            print("Epoch", loop + 1, "Cost: ", train_loss / len(X_batches), "Train Accuracy:", train_acc / len(X_batches))
            print("Epoch", loop + 1, "Test Accuracy:", self.predict(test_x, test_y))
            print("*" * 20)


    def predict(self, X, Y):
        A, cache = self.forward(X)
        y_hat = np.argmax(A, axis=1)
        Y = np.argmax(Y, axis=1)
        accuracy = (y_hat == Y).mean()
        return accuracy * 100



def pre_process_data(train_x, train_y, test_x, test_y):
    # Normalize
    train_x = np.reshape(train_x, (60000, 28 * 28))
    test_x = np.reshape(test_x, (10000, 28 * 28))
    train_x = train_x / 255.
    test_x = test_x / 255.

    enc = OneHotEncoder(sparse=False, categories='auto')
    train_y = enc.fit_transform(train_y.reshape(len(train_y), -1))

    test_y = enc.transform(test_y.reshape(len(test_y), -1))

    return train_x, train_y, test_x, test_y


if __name__ == '__main__':
    (train_x, train_y), (test_x, test_y) = load_data()

    train_x, train_y, test_x, test_y = pre_process_data(train_x, train_y, test_x, test_y)

    print("train_x's shape: " + str(train_x.shape))
    print("test_x's shape: " + str(test_x.shape))

    layers_dims = [128, 64]

    ann = ANN(layers_dims)
    ann.fit(train_x, train_y, test_x, test_y, learning_rate=0.2, n_iterations=100, batch_size=32)
    print("Train Accuracy:", ann.predict(train_x, train_y))
    print("Test Accuracy:", ann.predict(test_x, test_y))
