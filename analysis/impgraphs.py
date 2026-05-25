import pandas as pd
import matplotlib.pyplot as plt

def parse_lammps_log(filepath):
    """Parses a LAMMPS log file and extracts the thermo data across all runs."""
    data = []
    reading_thermo = False
    
    # errors='ignore' safely bypasses the non-ASCII warning LAMMPS generated
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
                
            parts = line.split()
            
            # Robust header detection: checks the exact words regardless of spacing
            if parts == ['Step', 'Dt', 'Temp', 'PotEng', 'KinEng', 'TotEng', 'Press']:
                reading_thermo = True
                continue
            
            # Stop reading when the loop finishes
            if line.startswith("Loop time"):
                reading_thermo = False
                continue
                
            # If we are in a thermo block, parse the numbers
            if reading_thermo:
                if len(parts) == 7:
                    try:
                        step = int(parts[0])
                        dt = float(parts[1])
                        temp = float(parts[2])
                        pe = float(parts[3])
                        ke = float(parts[4])
                        etotal = float(parts[5])
                        press = float(parts[6])
                        data.append([step, dt, temp, pe, ke, etotal, press])
                    except ValueError:
                        pass # Skip malformed lines or non-numeric rows

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=['Step', 'Dt', 'Temp', 'PotEng', 'KinEng', 'TotEng', 'Press'])
    
    # Drop duplicates in case of overlapping run steps
    df = df.drop_duplicates(subset=['Step']).sort_values(by='Step').reset_index(drop=True)
    return df

# --- Execution ---
# Set this to the exact name/path of the file you just uploaded
log_file = '/Users/tejasvikaranth/Desktop/NEWLAMMPS/log.lammps.txt' 
df = parse_lammps_log(log_file)

if not df.empty:
    # Create a 2x2 grid of plots
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('LAMMPS Cascade Simulation Dashboard', fontsize=16, fontweight='bold')

    # 1. Temperature vs Step
    axs[0, 0].plot(df['Step'], df['Temp'], color='red')
    axs[0, 0].set_title('Thermal Spike & Quench')
    axs[0, 0].set_xlabel('Step')
    axs[0, 0].set_ylabel('Temperature (K)')
    axs[0, 0].grid(True, linestyle=':', alpha=0.6)
    axs[0, 0].axvline(x=5000, color='gray', linestyle='--', label='Phase 2 Start')
    axs[0, 0].axvline(x=25000, color='gray', linestyle='-.', label='Phase 3 Start')
    axs[0, 0].legend()

    # 2. Energies vs Step
    axs[0, 1].plot(df['Step'], df['PotEng'], label='Potential Energy', color='blue')
    axs[0, 1].plot(df['Step'], df['TotEng'], label='Total Energy', color='green')
    axs[0, 1].set_title('Energy Evolution')
    axs[0, 1].set_xlabel('Step')
    axs[0, 1].set_ylabel('Energy (eV)')
    axs[0, 1].grid(True, linestyle=':', alpha=0.6)
    axs[0, 1].legend()

    # 3. Pressure vs Step
    axs[1, 0].plot(df['Step'], df['Press'], color='purple')
    axs[1, 0].set_title('Shockwave Dissipation (Pressure)')
    axs[1, 0].set_xlabel('Step')
    axs[1, 0].set_ylabel('Pressure (bar)')
    axs[1, 0].grid(True, linestyle=':', alpha=0.6)

    # 4. Timestep (Dt) vs Step (Focusing on Phase 1)
    # Masking to show only the adaptive dt phase
    phase1_df = df[df['Step'] <= 5000]
    axs[1, 1].plot(phase1_df['Step'], phase1_df['Dt'], color='orange', marker='o', markersize=3)
    axs[1, 1].set_title('Adaptive Timestep (Phase 1)')
    axs[1, 1].set_xlabel('Step')
    axs[1, 1].set_ylabel('Timestep Size (ps)')
    axs[1, 1].grid(True, linestyle=':', alpha=0.6)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
else:
    print("Could not parse data. Ensure the filepath is correct and formatted properly.")