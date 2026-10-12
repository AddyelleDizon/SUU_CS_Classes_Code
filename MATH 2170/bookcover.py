import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import io
import requests

def get_image(url):
    response = requests.get(url)
    img_bytes = io.BytesIO(response.content)
    img = Image.open(img_bytes)
    return img

url = r'https://raw.githubusercontent.com/emisseldine/OpenLinear/main/Chapter6/images/bookcover.png'
cover = np.asarray(get_image(url))[:,:,0]  # take only one channel
color = 'Blues_r'

plt.figure(figsize=(9,6))
plt.imshow(cover, cmap=color)
plt.axis('off')
plt.show()

U, s, VT = np.linalg.svd(cover, full_matrices=False)
Sigma = np.diag(s)

print(f"SVD computed: U shape = {U.shape}, Sigma shape = {Sigma.shape}, VT shape = {VT.shape}")

num_vals = [1,2,3,4,5,10,25,100,200,300,400,500,1000,1500,2000]

for k in num_vals:
    blur = U[:,:k] @ np.diag(s[:k]) @ VT[:k,:]
    
    plt.figure(figsize=(9,6))
    plt.imshow(blur, cmap=color)
    plt.title(f"k = {k}")
    plt.axis('off')
    plt.show()

total_size = cover.size
m, n = cover.shape
target_size = 0.1 * total_size 

k_90 = 1
while k_90*(m + n + 1) < target_size:
    k_90 += 1

blur_90 = U[:,:k_90] @ np.diag(s[:k_90]) @ VT[:k_90,:]

plt.figure(figsize=(9,6))
plt.imshow(blur_90, cmap=color)
plt.title(f"k = {k_90} (approx. 90% reduction)")
plt.axis('off')
plt.show()

print(f"Rank for ~90% data reduction: k = {k_90}")