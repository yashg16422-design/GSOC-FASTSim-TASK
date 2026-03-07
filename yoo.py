import uproot

import awkward as ak
file = uproot.open("newfile.root")
tree = file["events"]
num_events = tree.num_entries


energies_per_event = tree["ECalBarrelCollection.energy"].array()

print("Type:", type(energies_per_event))
print("Hits in event 0:", len(energies_per_event[0]))
print("First 10 hit energies in event 0:", energies_per_event[0])
print(sum(energies_per_event[0]))
print("Number of events:", num_events)
for i in range(5):  # first 5 events
    hits = energies_per_event[i]
    print(f"Event {i}: number of ECal barrel hits = {len(hits)}")

for i in range(num_events):
    hits = energies_per_event[i]
    total_energy = ak.sum(hits)
    print(f"Event {i}: hits={len(hits)}, total ECal energy={total_energy:.3f} GeV")

import numpy as np
import matplotlib.pyplot as plt


tree = file["events"]

# Get the ECalBarrel hit energies

branch_name = "ECalBarrelCollection/ECalBarrelCollection.energy"
try:
    # Load the energy data as a numpy array
    # We use .flatten() because each event contains a list of hits
    energies = tree[branch_name].array(library="np")
    all_hits = np.concatenate(energies)
    event_totals = [np.sum(e) for e in energies]
    mean_val2 = np.mean(event_totals)
    # 4. Calculate Statistics
    entries = len(all_hits)
    mean_val = np.mean(all_hits)
    std_val = np.std(all_hits)
    std_dev2 = np.std([sum(e) for e in energies])
    print(f"--- Analysis Results ---")
    print(f"Total Entries (Hits): {entries}")
    print(f"Mean Energy:          {mean_val:.6f} GeV")
    print(f"Mean Energy of One Event:  {mean_val2:.6f} GeV")

    print(f"Standard Deviation:   {std_val:.6f} GeV")
    print(f"Standard Deviation wrt events:   {std_dev2:.6f} GeV")

    # Count events where the energy array is empty
    zero_hit_events = sum(1 for e in energies if len(e) == 0)
    print(f"Events with zero hits: {zero_hit_events} out of 100")
    vtx_x = tree["MCParticles/MCParticles.vertex.x"].array(library="np")
    vtx_y = tree["MCParticles/MCParticles.vertex.y"].array(library="np")
    vtx_z = tree["MCParticles/MCParticles.vertex.z"].array(library="np")
    p_x = tree["MCParticles/MCParticles.momentum.x"].array(library="np")[0][0]
    p_y = tree["MCParticles/MCParticles.momentum.y"].array(library="np")[0][0]
    p_z = tree["MCParticles/MCParticles.momentum.z"].array(library="np")[0][0]
    print(f"Momentum (Px, Py, Pz): ({p_x:.2f}, {p_y:.2f}, {p_z:.2f})")

# Print the starting position of the first particle in the first event
    print(f"Gun Position (X, Y, Z): ({vtx_x[0][0]}, {vtx_y[0][0]}, {vtx_z[0][0]})")
    print(file.keys()) 

    
    plt.figure(figsize=(8, 6))
    plt.hist(all_hits, bins=100, color='skyblue', edgecolor='black', histtype='stepfilled')
    
    plt.title("Hit Energy Distribution in ECalBarrel (10 GeV Photons)")
    plt.xlabel("Hit Energy [GeV]")
    plt.ylabel("Number of Hits")
    plt.grid(axis='y', alpha=0.3)
    
    # Add stats box to the plot
    stats_text = f"Entries: {entries}\nMean: {mean_val:.4f}\nStd Dev: {std_val:.4f}"
    plt.text(0.95, 0.95, stats_text, transform=plt.gca().transAxes, 
             verticalalignment='top', horizontalalignment='right', 
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))

    plt.show()

except KeyError:
    print(f"Error: Could not find branch '{branch_name}'.")
    print("Available branches are:")
    print(tree.keys())
# print(file.keys())
import uproot
import awkward as ak

file = uproot.open("newfilee.root")
tree = file["events"]

# Load MCParticle PDG IDs
pdg_ids = tree["MCParticles/MCParticles.PDG"].array()

all_pdgs = ak.flatten(pdg_ids)

# Print unique PDG codes
print("Unique PDG IDs in file:", set(all_pdgs.tolist()))
status = tree["MCParticles/MCParticles.generatorStatus"].array()
pdg_ids = tree["MCParticles/MCParticles.PDG"].array()

primary_pdgs = []

for s, p in zip(status, pdg_ids):
    primary_pdgs.extend(p[s == 1])  # generatorStatus == 1 means primary

print("Primary particle PDGs:", set(primary_pdgs))
