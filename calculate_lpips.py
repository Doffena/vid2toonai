import os
import lpips
import torch
import cv2
import numpy as np
from tqdm import tqdm

loss_fn = lpips.LPIPS(net='vgg')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
loss_fn = loss_fn.to(device)

input_folder = "input_images"
styled_folder = "styled_frames"

lpips_scores = []

print(f"Comparing images in '{input_folder}' and '{styled_folder}'...")

for filename in tqdm(os.listdir(input_folder)):
    input_path = os.path.join(input_folder, filename)
    styled_path = os.path.join(styled_folder, filename)

    if os.path.exists(styled_path):
        img1 = cv2.imread(input_path)
        img2 = cv2.imread(styled_path)

        img1 = cv2.resize(img1, (256, 256))
        img2 = cv2.resize(img2, (256, 256))

        img1_tensor = torch.from_numpy(img1).permute(2, 0, 1).unsqueeze(0).float() / 127.5 - 1.0
        img2_tensor = torch.from_numpy(img2).permute(2, 0, 1).unsqueeze(0).float() / 127.5 - 1.0

        img1_tensor = img1_tensor.to(device)
        img2_tensor = img2_tensor.to(device)

        dist = loss_fn(img1_tensor, img2_tensor)
        lpips_scores.append((filename, dist.item()))

print("\n🧪 LPIPS SONUÇLARI:")
for fname, score in lpips_scores:
    print(f"{fname}: {score:.4f}")

avg_score = np.mean([s for _, s in lpips_scores])
print(f"\n📊 Ortalama LPIPS Skoru: {avg_score:.4f}")
