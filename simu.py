import numpy as np
import matplotlib.pyplot as plt

# Loading particle info
import uproot
f    = uproot.open("other.root")
tree = f["events"]

px = tree["MCParticles.momentum.x"].array(library="np")
py = tree["MCParticles.momentum.y"].array(library="np")
pz = tree["MCParticles.momentum.z"].array(library="np")

etas = []
phis = []

for i in range(len(px)):
    
    px_i = px[i][0]
    py_i = py[i][0]
    pz_i = pz[i][0]

    p_mag = np.sqrt(px_i**2 + py_i**2 + pz_i**2)
    theta = np.arccos(pz_i / p_mag)
    eta   = -np.log(np.tan(theta / 2))
    phi   = np.arctan2(px_i, py_i)

    etas.append(eta)
    phis.append(phi)

etas = np.array(etas)
phis = np.array(phis)

print(f"eta range: {etas.min():.3f} to {etas.max():.3f}")
print(f"phi range: {phis.min():.3f} to {phis.max():.3f}")

# Plot coverage map
plt.figure(figsize=(8, 5))
plt.scatter(etas, phis, alpha=0.5, s=10)
plt.xlabel("Pseudorapidity η")
plt.ylabel("Azimuthal angle φ (rad)")
plt.title("Detector Coverage — Test Dataset when non linear test configs\n))")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
