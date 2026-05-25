# MD-Simulation-of-radiation-hardness-and-self-healing-of-GaN
Molecular dynamics simulation of a 5 keV Ga PKA displacement cascade in bulk wurtzite GaN using LAMMPS. Tracks radiation damage and room-temperature self-healing at the atomic level.


Requirements
LAMMPS (any recent version with hybrid/overlay pair style support)
GaN.tersoff potential file (place in the same directory as the input scripts)
Python 3 with pandas and matplotlib (for the analysis scripts)
OVITO (for Wigner-Seitz defect analysis and trajectory visualization)


Steps to Reproduce
Step 1: Clone the repository

git clone https://github.com/Tej36asvi/GaN-Radiation-Damage-MD.git

cd GaN-Radiation-Damage-MD

Step 2: Place the potential file

Copy GaN.tersoff into the potentials/ folder. Make sure the path in the input scripts matches.

Step 3: Run the equilibration

This builds the 55,296-atom wurtzite GaN supercell, equilibrates it at 300 K using NVT and anisotropic NPT, and generates two output files: GaN_equilibrated.data (the starting point for the cascade) and GaN_0K_reference.data (the perfect reference for defect counting).

mpirun -np 4 lmp -in input_scripts/in_01_equilibrate.lmp

Runtime: approximately 19 to 20 hours on 4 cores.

Step 4: Run the cascade

Loads GaN_equilibrated.data, fires a 5 keV Ga PKA from the box center, runs the ballistic cascade with adaptive timestepping, 20 ps of dynamic recovery at 300 K, and a final quench. Outputs the trajectory dump and GaN_post_cascade.data.

mpirun -np 4 lmp -in input_scripts/in_02_cascade.lmp

Runtime: approximately 40 minutes on 4 cores.

Step 5: Plot the thermodynamic dashboard

Reads the LAMMPS log and produces a 4-panel plot of temperature, potential energy, pressure, and adaptive timestep.

cd analysis

python3 impgraphs.py

Edit the log_file path inside impgraphs.py to point to your log file before running.

Step 6: Run the Wigner-Seitz defect analysis in OVITO

Open OVITO and load dump/dump.cascade.lammpstrj
Add modifier: Wigner-Seitz Defect Analysis
Set reference to External File and load data/GaN_0K_reference.data
Enable Distinguish atom types
Export the per-frame defect counts to a text file and save as results/defect_counts

Step 7: Plot the defect count evolution

cd analysis

python3 defecgraph.py


Expected Results
Quantity
Value
Peak Frenkel pairs
494 (frame 24)
Surviving Frenkel pairs
~113 (frame 140)
Defect recovery fraction
~77 %
Peak cascade pressure
~26,800 bar
Peak effective temperature
~1000 K



Notes
The dump file (dump.cascade.lammpstrj) is large. Git LFS is recommended for tracking it.
The GaN_0K_reference.data file in data/ was generated from the same NPT-relaxed box as the cascade. Do not substitute a separately minimized reference or the Wigner-Seitz cell boundaries will not align.
This is a single cascade. Results reflect one random PKA direction and should not be treated as statistically averaged material properties.

