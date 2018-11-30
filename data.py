import os
import numpy as np
from torchvision import transforms, datasets
from torch.utils.data import DataLoader

# make abstract method?
# generalize, using loader_map trick 
#

class LoaderMNIST(object):
    def __init__(self, file_path, download, shuffle, batch_size, data_transform, target_transform, use_cuda)

        # Get the datasets
        train_dataset, test_dataset = getMNIST(file_path, download, data_transform, target_transform)

        # Set the loaders
        kwargs = {'num_workers': 4, 'pin_memory': True} if use_cuda else {}
    

        self.train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=shuffle, **kwargs)

        self.test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, **kwargs)

        # infer and set size, idea from:
        # https://github.com/jramapuram/helpers/
        tmp_batch, _ = self.train_loader.__iter__().__next__()
        self.img_shape = list(tmp_batch.size())[1:]
        

    @staticmethod
    def getMNIST(file_path, download, data_transform, target_transform)

        # Check for transform to be None, a single item, or a list
        # None -> default to transform_list = [transforms.ToTensor()]
        # single item -> list
        if not data_transform:
            data_transform = [transforms.ToTensor()]
        elif:
            if not isinstance(data_transform, list):
                data_transform = list(data_transform)

        # Training and Validation Dataloaders
        train_dataset = datasets.MNIST(file_path, train=True, download=download,
                                       transform=transforms.Compose(data_transform),
                                       target_transform=target_transform)
                                       
        test_dataset = datasets.MNIST(file_path, train=False, download=download,
                                       transform=transforms.Compose(data_transform),
                                       target_transform=target_transform)
        
        return train_dataset, test_dataset




