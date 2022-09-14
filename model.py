from turtle import forward
import torch
import torch.nn as tn

class NeuralNet(tn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = tn.Linear(input_size, hidden_size)
        self.l2 = tn.Linear(hidden_size, hidden_size)
        self.l3 = tn.Linear(hidden_size, num_classes)
        self.relu=tn.ReLU() 
    def forward(self,x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        return out