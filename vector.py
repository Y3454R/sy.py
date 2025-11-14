import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import imageio
import os

# Create output folder for frames
os.makedirs("frames", exist_ok=True)

# Vector coordinates
x, y, z = 3, 4, 12

# Step fractions for animation (0->1)
steps = np.linspace(0, 1, 20)

frame_files = []

for i, t in enumerate(steps):
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection="3d")

    # Plot origin
    ax.scatter(0, 0, 0, color="black", s=50)

    # Step 1: show XY-plane vector growing
    ax.plot([0, x * t], [0, y * t], [0, 0], color="blue", lw=3, label="XY-plane vector")

    # Step 2: show vertical Z component growing
    ax.plot([x, x], [y, y], [0, z * t], color="red", lw=3, label="Z component")

    # Step 3: show hypotenuse gradually
    ax.plot(
        [0, x * t],
        [0, y * t],
        [0, z * t],
        color="green",
        lw=2,
        linestyle="--",
        label="3D hypotenuse",
    )

    # Labels
    ax.set_zlim(0, z + 1)
    ax.set_xlim(0, x + 1)
    ax.set_ylim(0, y + 1)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.view_init(elev=20, azim=45)  # fixed view

    # Save frame
    frame_path = f"frames/frame_{i:03d}.png"
    plt.legend()
    plt.savefig(frame_path)
    plt.close(fig)
    frame_files.append(frame_path)

# Make GIF
images = []
for filename in frame_files:
    images.append(imageio.imread(filename))

imageio.mimsave("vector_3d_pythagoras.gif", images, duration=0.2)

print("GIF saved as vector_3d_pythagoras.gif")
