import pandas as pd                                                                             #read and manipulate files
import numpy as np                                                                              #do mathematical operations
import torch                                                                                    #for tensors
import torch.nn as nn                                                                           #prebuilt structures
import torch.optim as optim                                                                     #SGD
from tourch.utils.data import TensorDataset, DataLoader                                         #create object of data and split the oject
from sklearn.model_selection import train_test_split                                            #split data for better training of AI
from sklearn.preprocessing import StandardScaler                                                #standardise numerical values 

df = pd.read_csv("diabetes_data.csv")                                                           #loading data into panda df

df = df.dropna()                                                                                #delete blank or missing data

x_df = df.drop(columns=['target_data'])                                                         #table containing input
y_df = df['target_data']                                                                        #table we want to use

x_train_raw, x_test_raw, y_train_raw, y_test_raw = train_test_split (
    x_df, y_df, test_size = 0.3, random_state = 100
)                                                                                               #30% of the data = test the data, 70% of the data = train the data, test and train data shuffled 100 times 

scaler = StandardScaler()
x_train_scale = scaler.fit_transform(x_train_raw)                                               #calculates avg of train data and standardises it in a small range
x_test_scale = scaler.transform(x_test_raw)                                                     #calculates avg of test data and standardises it in a small range

x_train_tensor = torch.tensor(x_train_scale, dtype = torch.float32)                             #convert numpy array into pytorch tensor (decimal)

y_train_tensor = torch.tensor(y_train_raw.values, dtype = torch.float32.unsqueeze(1))           #convert numpy array into pytorch tensor and convert list into a matrix of [100, 1]

train_dataset = TensorDataset(x_train_tensor, y_train_tensor)                                   #keep the data together for easy navigation
train_loader = DataLoader(train_dataset, batch_size = 32, shuffle = True)                       #organize data into 30 rows and shuffle

num_features = x_df.shape[1]                                                                    #expected input signal

class diabetes(nn.Module):

    def __init__(self, input_dim):
        super(diabetes, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, 32),                                                           #make 32 nodes
            nn.ReLu(),                                                                          #replace negative numbers with 0
            nn.Linear(32, 16), 
            nn.ReLu(),
            nn.Linear(16, 1),                                                                   #convert values to single node
            nn.Sigmoid()                                                                        #probability percentage
        )

def forward(self, x):
    return self.network(x)                                                                      #only move forward through the data

model = diabetes(input_dim=num_features)                                                        #object of the class and expected input
criterion = nn.BCEloss()                                                                        #teaches to guess the correct answer
optimizer = optim.Adam(model.parameters(), lr = 0.005)                                          #change rate in data (learning rate)

epoch = 15                                                                                     #pass the date through 15 times
for epoch in range(epoch):
    model.train()
    total_loss = 0.0                                                                            #resets model and calculates errors

for batch_x, batch_y in train_loader:
    predictions = model(batch_x)                                                                #feed batch to get predictions
    loss = criterion(predictions, batch_y)                                                      #compare predictions against real answers and give error score
    optimizer.zero_grad()                                                                       #clear prev result to prevent corruption
    loss.backward()                                                                             #find which code line is causing most error
    optimizer.step()                                                                            #adam used to make model more accurate with each batch
    total_loss += loss.item()                                                                   #quantify loss and add to the total

    print(f"Epoch {epoch+1:02d}/{epoch} , Average loss: {total_loss/len(train_loader):.4f}")    #final output telling the accuracy of the model