import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

# ── GENERATOR 
class Generator(nn.Module):
    def __init__(self, noise_dim=100, img_dim=784):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(noise_dim, 256),
            nn.LeakyReLU(0.2),

            nn.Linear(256, 512),
            nn.LeakyReLU(0.2),

            nn.Linear(512, img_dim),
            nn.Tanh()
        )
    def forward(self, z):
      return self.net(z)

# ── DISCRIMINATOR
class Discriminator(nn.Module):
    def __init__(self, img_dim=784):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(img_dim, 512),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.3),

            nn.Linear(512, 256),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.3),

            nn.Linear(256, 1),
            nn.Sigmoid()
        )
    def forward(self, x):
      return self.net(x)

 # ── LOAD MNIST DATASET 
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

dataset = torchvision.datasets.MNIST(
    root="./data",
    train=True,
    transform=transform,
    download=True
)

loader = torch.utils.data.DataLoader(
    dataset,
    batch_size=32,
    shuffle=True
)

# ── CREATE MODELS 
G = Generator()
D = Discriminator()

# ── OPTIMIZERS 
opt_G = torch.optim.Adam(G.parameters(), lr=0.0002, betas=(0.5, 0.999))
opt_D = torch.optim.Adam(D.parameters(), lr=0.0002, betas=(0.5, 0.999))

criterion = nn.BCELoss()

# ── TRAINING LOOP 
epochs = 50

for epoch in range(epochs):

    for batch_idx, (real_images, _) in enumerate(loader):

        batch_size = real_images.shape[0]

        real_images = real_images.view(batch_size, 784)

        # Labels
        real_labels = torch.ones(batch_size, 1)
        fake_labels = torch.zeros(batch_size, 1)





# ── TRAIN DISCRIMINATOR 
        z = torch.randn(batch_size, 100)

        fake_images = G(z)

        real_pred = D(real_images)
        fake_pred = D(fake_images.detach())

        d_loss_real = criterion(real_pred, real_labels)
        d_loss_fake = criterion(fake_pred, fake_labels)

        d_loss = d_loss_real + d_loss_fake

        opt_D.zero_grad()
        d_loss.backward()
        opt_D.step()


# ── TRAIN GENERATOR ───────────────────────────
        fake_pred = D(fake_images)

        g_loss = criterion(fake_pred, real_labels)

        opt_G.zero_grad()
        g_loss.backward()
        opt_G.step()

        # ── PRINT LOSSES
        if batch_idx % 200 == 0:
            print(
                f"Epoch [{epoch+1}/{epochs}] "
                f"Batch {batch_idx}/{len(loader)} "
                f"D Loss: {d_loss.item():.4f} "
                f"G Loss: {g_loss.item():.4f}"
            )

# ── GENERATE FINAL IMAGES 
z = torch.randn(16, 100)

generated_images = G(z)

generated_images = generated_images.view(16, 28, 28)

# ── DISPLAY GENERATED IMAGES
fig, axes = plt.subplots(4, 4, figsize=(6, 6))

for i, ax in enumerate(axes.flat):

    img = generated_images[i].detach().numpy()
    img = (img + 1) / 2
    ax.imshow(img, cmap="gray")
    ax.axis("off")

plt.show()
