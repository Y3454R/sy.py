import torch
import torch.nn as nn

def conv_block(in_f, out_f, activation='relu', *args, **kwargs):
    activations = nn.ModuleDict([
                ['lrelu', nn.LeakyReLU()],
                ['relu', nn.ReLU()]
    ])
    
    return nn.Sequential(
        nn.Conv2d(in_f, out_f, *args, **kwargs),
        nn.BatchNorm2d(out_f),
        activations[activation]
    )

def dec_block(in_f, out_f):
    return nn.Sequential(
        nn.Linear(in_f, out_f),
        nn.Sigmoid()
    )

class MyEncoder(nn.Module):
    def __init__(self, enc_sizes, *args, **kwargs):
        super().__init__()
        self.conv_blocks = nn.Sequential(*[conv_block(in_f, out_f, kernel_size=3, padding=1, *args, **kwargs) 
                       for in_f, out_f in zip(enc_sizes, enc_sizes[1:])])
        
        def forward(self, x):
            return self.conv_blocks(x)
        
class MyDecoder(nn.Module):
    def __init__(self, dec_sizes, n_classes):
        super().__init__()
        self.dec_blocks = nn.Sequential(*[dec_block(in_f, out_f) 
                       for in_f, out_f in zip(dec_sizes, dec_sizes[1:])])
        self.last = nn.Linear(dec_sizes[-1], n_classes)

    def forward(self, x):
        return self.dec_blocks()
    
    
class MyCNNClassifier(nn.Module):
    def __init__(self, in_c, enc_sizes, dec_sizes,  n_classes, activation='relu'):
        super().__init__()
        self.enc_sizes = [in_c, *enc_sizes]
        self.dec_sizes = [32 * 28 * 28, *dec_sizes]

        self.encoder = MyEncoder(self.enc_sizes, activation=activation)
        
        self.decoder = MyDecoder(dec_sizes, n_classes)
        
    def forward(self, x):
        x = self.encoder(x)
        
        x = x.flatten(1) # flat
        
        x = self.decoder(x)
        
        return x

model = MyCNNClassifier(1, [32,64], [1024, 512], 10, activation='lrelu')
print(model)
