# imports 
import torch # core library 
from torch import nn # handles neural net built-ins such as layers, loss functions...   
from torch.utils.data import DataLoader # batches and shuffles the dataset 
from torchvision import datasets # a collection of datasets, we are using the fashion one for this example 
from torchvision.transforms import v2 # tools for preprocessing the images. saves a ton of time, in the last project this took ages


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
)

# take a batch size of 64 labels and images, same as in the previious project I looked at, except I used 1000

batch_size = 64 

# create data loaders 
train_dataloader = DataLoader(training_data, batch_size=batch_size)