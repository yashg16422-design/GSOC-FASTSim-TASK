import numpy as np
import matplotlib.pyplot as plt

data = np.load("point_cloud_dataset.npy", allow_pickle=True)
data1 = [data[0]]


# r_all = []
# E_all = []

# for event in data:

#     x = event[:,0]
#     z = event[:,2]
#     E = event[:,3]

#     # shower centroid
#     x0 = np.mean(x)
#     z0 = np.mean(z)

#     # radial distance from shower core
#     r = np.sqrt((x - x0)**2 + (z - z0)**2)

#     r_all.extend(r)
#     E_all.extend(E)

# r_all = np.array(r_all)
# E_all = np.array(E_all)

# # restrict to useful region
# max_radius = 200  # mm

# bins = np.linspace(0, max_radius, 40)

# energy_radial, edges = np.histogram(r_all, bins=bins, weights=E_all)

# r_centers = 0.5 * (edges[1:] + edges[:-1])

# plt.figure(figsize=(6,4))
# plt.plot(r_centers, energy_radial, marker='o')

# plt.xlabel("Radial Distance from Shower Core (mm)")
# plt.ylabel("Deposited Energy")
# plt.title("Transverse Shower Profile")
# print(sum(E_all))
# plt.grid(True)

# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt    ####corrrrrecttttt

# data = np.load("point_cloud_dataset.npy", allow_pickle=True)

# beam_dir = np.array([0,1,0])

# depth_all = []
# E_all = []

# for event in data:

#     pos = event[:,0:3]
#     E = event[:,3]

#     depth = pos @ beam_dir

#     depth = depth - np.mean(depth)

#     depth_all.extend(depth)
#     E_all.extend(E)

# depth_all = np.array(depth_all)
# E_all = np.array(E_all)

# bins = np.linspace(-100, 100, 40)

# energy_per_layer, edges = np.histogram(depth_all, bins=bins, weights=E_all)

# centers = 0.5*(edges[1:] + edges[:-1])

# plt.plot(centers, energy_per_layer, marker='o')
# print(len(depth_all))
# plt.xlabel("Relative Shower Depth (mm)")
# plt.ylabel("Deposited Energy")
# plt.title("Average Longitudinal Shower Profile")
# plt.grid(True)
# plt.show()
# import uproot
# f = uproot.open("newfile.root")
# tree = f["events"]
# # Print all ECalBarrel branches
# ecal_branches = [k for k in tree.keys() if "ECalBarrel" in k]
# if "ECalBarrelCollection/ECalBarrelCollection.type" in ecal_branches:
#     print(True)

# import uproot
# import numpy as np

# f = uproot.open("newfile.root")
# tree = f["events"]


# py = tree["MCParticles.momentum.y"].array(library="np")
# pz = tree["MCParticles.momentum.z"].array(library="np")

# for i in range(10):  # first 10 events
#     # take first particle (index 0) — your primary photon
#     px_i = px[i][0]
#     py_i = py[i][0]
#     pz_i = pz[i][0]
#     px = tree["MCParticles.momentum.x"].array(library="np")
#     p_mag = np.sqrt(px_i**2 + py_i**2 + pz_i**2)
#     # Polar angle theta (from Z  axis)
#     theta = np.degrees(np.arccos(pz_i / p_mag))
    
#     # Azimuthal angle phi (in X-Y plane)
#     phi = np.degrees(np.arctan2(px_i, py_i))
    
#     # Pseudorapidity eta (most common in particle physics)
#     eta = -np.log(np.tan(theta/2 * np.pi/180))
    
#     print(f"Event {i}: theta={theta:.2f}°  phi={phi:.2f}°  eta={eta:.3f}")
'''

---

**What you expect to see:**

Since your gun direction is exactly `(0,1,0)`:
- `theta` ≈ **90°** — perpendicular to beam axis ✓
- `phi` ≈ **0°** — pointing along Y ✓  
- `eta` ≈ **0.0** — midpoint of detector ✓

If all events show the same angles, it confirms your test dataset is a **single fixed-angle sample** — which is fine for now but means for the full dataset you'll need to vary the angle to cover the full detector.

---

**Why angles matter for your project:**

This directly connects to your **detector coverage study** milestone. For a production ML dataset you need showers at many different eta values:
```
η = 0.0  → barrel centre     (your current test)
η = 0.5  → mid barrel
η = 1.0  → barrel edge
η = 1.5+ → endcap region'''
# r_hit   = np.sqrt(x**2 + y**2)
# depth   = r_hit - r_hit.min()        # detector-independent depth
# phi     = np.arctan2(z, x)           # azimuthal symmetry preserved
# E_norm  = E / E.sum()                # scale-independent energy

import numpy as np
import matplotlib.pyplot as plt

# Loading MC particle info
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
plt.title("Detector Coverage — Test Dataset\n(Single point confirms fixed-angle simulation)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()