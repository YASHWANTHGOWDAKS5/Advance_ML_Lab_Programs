import pandas as pd 
import numpy as np 
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler, OneHotEncoder

class NeuralNetwork:
    def __init__(self,input_size,hidden_size,output_size,learning_rate=0.1):
        self.w1 =np.random.randn(input_size,hidden_size)*0.1
        self.b1 = np.zeros((1,hidden_size))
        self.w2 = np.random.randn(hidden_size,output_size)*0.1
        self.b2=np.zeros((1,output_size))
        self.lr = learning_rate

    def sigmoid(self,x):
        return 1/(1+np.exp(-np.clip(x,-250,250)))

    def sigmoid_derivative(self,a):
        return a*(1-a)

    def softmax(self,x):
        exp_x=np.exp(x-np.max(x,axis=1,keepdims=True))
        return exp_x/np.sum(exp_x,axis=1,keepdims=True)

    def forward(self,X):
        self.a1 = self.sigmoid(np.dot(X, self.w1)+self.b1)
        self.a2 = self.softmax(np.dot(self.a1,self.w2)+self.b2)
        return self.a2

    def backword(self,X,y,output):
        m = X.shape[0]
        dz2 = output-y
        dz1=np.dot(dz2,self.w2.T)*self.sigmoid_derivative(self.a1)
        self.w2 -= self.lr*(np.dot(self.a1.T,dz2)/m)
        self.w1 -= self.lr*(np.dot(X.T,dz1)/m)

    def compute_loss(self, y, output):
        m = y.shape[0]
        loss = -np.sum(y * np.log(output + 1e-8)) / m
        return loss

    def train(self,X,y,epochs=500):
        for i in range(epochs):
            out = self.forward(X)
            if i/100 in [1,2,3,4,5,6,7,8,9]:
                print(f"Epoch : {i} and loss: {self.compute_loss(y,out)}")
            self.backword(X,y,out)

print("Backpropagation running")

iris=load_iris()
X = StandardScaler().fit_transform(iris.data)
y=OneHotEncoder(sparse_output=False).fit_transform(iris.target.reshape(-1,1))

model = NeuralNetwork(4,5,3)
model.train(X,y,epochs=1000)

predictions = np.argmax(model.forward(X),axis=1)
accuracy = np.mean(predictions == iris.target)
print(f"Final accuracy: {accuracy*100:.3f}")

# Output:
# Backpropagation running
# Epoch : 100 and loss: 0.8982528501291213
# Epoch : 200 and loss: 0.5762266448877993
# Epoch : 300 and loss: 0.4544555894657925
# Epoch : 400 and loss: 0.38644322264659925
# Epoch : 500 and loss: 0.33943576420294397
# Epoch : 600 and loss: 0.30428110653902585
# Epoch : 700 and loss: 0.27654244479354456
# Epoch : 800 and loss: 0.25369896937891906
# Epoch : 900 and loss: 0.23436006926377786
# Final accuracy: 96.000