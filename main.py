# imports 
import torch # core library 
from torch import nn # handles neural net built-ins such as layers, loss functions...   
from torch.utils.data import DataLoader # batches and shuffles the dataset 
from torchvision import datasets # a collection of datasets, we are using the fashion one for this example 
from torchvision.transforms import v2 # tools for preprocessing the images. saves a ton of time, in the last project this took ages

import os


# Download training data from open datasets.
training_data = datasets.FashionMNIST(
    root="data",
    train=True, # defined training split of 6:1 is used, that is, 60,000 test images and 10,000 training images for learning 
    download=True, # download all of the images if theyre not already at root 
    transform=v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)]), # preprocessing stage
)

# Download test data from open datasets.
test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)]),
    # the transform part is responsible for chaining multiple transforms together 
    # they are - converting the image to a torch image tensor -> converting it to a 32 bit float -> rescales pixel values 
    # from 0-255 to 0-1.0
)

# take a batch size of 64 labels and images, same as in the previious project I looked at, except I used 1000

batch_size = 64 

# create data loaders 
train_dataloader = DataLoader(training_data, batch_size=batch_size)
test_dataloader = DataLoader(test_data, batch_size=batch_size)

for X, y in test_dataloader: # X = images, y = labels!
    print(f"Shape of X [N, C, H, W]: {X.shape}") # output is Shape of X [N, C, H, W]: torch.Size([64, 1, 28, 28])
                                                 # what this really means is we have a batch of 64, with 1 colour channel (greyscale)
                                                 # and the image is 28 x 28 pixels 
    print(f"Shape of y: {y.shape} {y.dtype}") 
    break

# ~~~~~~~~~~ ~~~~~~~~~~ ~~~~~~~~~~ ~~~~~~~~~~ #
# ~~~~~~~~~~ Creation of the Model ~~~~~~~~~~ #
# ~~~~~~~~~~ ~~~~~~~~~~ ~~~~~~~~~~ ~~~~~~~~~~ ~ 

device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu"
print(f"Using {device} device") # checking to see if there is a better option than using a CPU since GPUs are better suited for this
# ... sort of thing 

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(), 
            nn.Linear(512,10)
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

model = NeuralNetwork().to(device)
print(model)
