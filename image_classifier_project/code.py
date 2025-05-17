import torch.nn as nn
import torchvision.models as models

class ModifiedResNet18(nn.Module):
    def __init__(self, num_classes=26):
        super(ModifiedResNet18, self).__init__()
        self.model = models.resnet18(weights=None)
        self.model.conv1 = nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1, bias=False)
        self.model.maxpool = nn.Identity()
        self.model.layer4 = nn.Sequential(
            nn.Dropout(0.3),
            self.model.layer4
        )
        self.model.fc = nn.Sequential(
            nn.Dropout(0.5),
            nn.BatchNorm1d(self.model.fc.in_features),
            nn.Linear(self.model.fc.in_features, num_classes)
        )

    def forward(self, x):
        return self.model(x)