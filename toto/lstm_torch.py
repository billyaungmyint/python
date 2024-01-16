import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import pandas as pd
import random

# get the past winning numbers from the web
url = 'https://en.lottolyzer.com/history-export-csv/singapore/toto/ToTo.csv'
# read the url
data_csv = pd.read_csv(url)

def rnn(isize , hsize , osize, lsize):
    # from the data , choose the specific columns from there , winning numbers + additional number
    # winning_number = data_csv[['Winning Number 1', '2', '3', '4', '5', '6', 'Additional Number ']]
    # from the data , choose the specific columns from there , winning numbers 
    winning_number = data_csv[['Winning Number 1', '2', '3', '4', '5', '6']]
    # rename the winning number and additional number columns to 1 and 7 respectively
    # winning_number = winning_number.rename({'Winning Number 1': '1', 'Additional Number ': '7'}, axis=1)
    # rename the winning number 
    winning_number = winning_number.rename({'Winning Number 1': '1'}, axis=1)

    # make a new list of winning numbers of the most recent 10 winning numbers 
    winning_list = winning_number.iloc[0:lsize].values.tolist()


    # Convert data to a numpy array
    data = np.array(winning_list, dtype=np.float32)

    # Prepare input and output data
    X = data[:-1]  # Input sequences
    y = data[1:]   # Output sequences

    # Convert data to PyTorch tensors
    X = torch.tensor(X)
    y = torch.tensor(y)

    # Define the RNN model
    class RNN(nn.Module):
        def __init__(self, input_size, hidden_size, output_size):
            super(RNN, self).__init__()
            self.hidden_size = hidden_size
            self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
            self.fc = nn.Linear(hidden_size, output_size)

        def forward(self, x):
            out, _ = self.rnn(x)
            out = self.fc(out)
            return out

    input_size = isize # input size either with additional number then 7 or without then 6
    hidden_size = hsize  # You can adjust this as needed
    output_size = osize

    model = RNN(input_size, hidden_size, output_size)

    # Define loss function and optimizer
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Training loop
    num_epochs = 1000

    for epoch in range(num_epochs):
        optimizer.zero_grad()
        outputs = model(X.unsqueeze(0))  # Add a batch dimension
        loss = criterion(outputs, y.unsqueeze(0))  # Add a batch dimension
        loss.backward()
        optimizer.step()

        # if (epoch + 1) % 100 == 0:
        #     print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

    # Predict the next list
    with torch.no_grad():
        last_sequence = X[-1].unsqueeze(0).unsqueeze(0)  # Add batch and sequence dimensions
        next_list = model(last_sequence)
        next_list = next_list.squeeze().numpy()

    print(f"Predicted Next List according to RNN based on hidden size {hsize} :")
    print([int(x) for x in next_list])

def lstm(isize , hsize , osize , lsize):
    
    # from the data , choose the specific columns from there , winning numbers + additional number
    # winning_number = data_csv[['Winning Number 1', '2', '3', '4', '5', '6', 'Additional Number ']]
    # from the data , choose the specific columns from there , winning numbers 
    winning_number = data_csv[['Winning Number 1', '2', '3', '4', '5', '6']]
    # rename the winning number and additional number columns to 1 and 7 respectively
    # winning_number = winning_number.rename({'Winning Number 1': '1', 'Additional Number ': '7'}, axis=1)
    # rename the winning number 
    winning_number = winning_number.rename({'Winning Number 1': '1'}, axis=1)

    # make a new list of winning numbers of the most recent 10 winning numbers 
    winning_list = winning_number.iloc[0:lsize].values.tolist()


    # Convert data to a numpy array
    data = np.array(winning_list, dtype=np.float32)
    
    # Prepare input and output data
    X = data[:-1]  # Input sequences
    y = data[1:]   # Output sequences

    # Convert data to PyTorch tensors
    X = torch.tensor(X)
    y = torch.tensor(y)

    # Define the LSTM model
    class LSTM(nn.Module):
        def __init__(self, input_size, hidden_size, output_size):
            super(LSTM, self).__init__()
            self.hidden_size = hidden_size
            self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
            self.fc = nn.Linear(hidden_size, output_size)

        def forward(self, x):
            out, _ = self.lstm(x)
            out = self.fc(out)
            return out

    input_size = isize
    hidden_size = hsize # You can adjust this as needed
    output_size = osize

    model = LSTM(input_size, hidden_size, output_size)

    # Define loss function and optimizer
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Training loop
    num_epochs = 1000

    for epoch in range(num_epochs):
        optimizer.zero_grad()
        outputs = model(X.unsqueeze(0))  # Add a batch dimension
        loss = criterion(outputs, y.unsqueeze(0))  # Add a batch dimension
        loss.backward()
        optimizer.step()

        # if (epoch + 1) % 100 == 0:
        #     print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

    # Predict the next list
    with torch.no_grad():
        last_sequence = X[-1].unsqueeze(0).unsqueeze(0)  # Add batch and sequence dimensions
        next_list = model(last_sequence)
        next_list = next_list.squeeze().numpy()

    print(f"Predicted Next List according to LSTM based on hidden size {hsize} : ")
    print([int(x) for x in next_list])

print("most recent 3 numbers")
lstm(6,50,6,3)
#lstm(6,100,6,3)
rnn(6,50,6,3)
#rnn(6,100,6,3)
print("most recent 6 numbers")
lstm(6,50,6,6)
#lstm(6,100,6,6)
rnn(6,50,6,6)
#rnn(6,100,6,6)
print("most recent 10 numbers")
lstm(6,50,6,10)
#lstm(6,100,6,10)
rnn(6,50,6,10)
#rnn(6,100,6,10)