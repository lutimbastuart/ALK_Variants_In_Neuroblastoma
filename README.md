# ALK_Variants_In_Neuroblastoma
Neuroblastoma-associated ALK variants have distinct cellular and biochemical activities 

# Repository Contents
raw_data – Unprocessed data from molecular dynamics (MD) simulations and structural modeling.
simulation_inputs: – Input coordinate and parameter files (PDB, topology, force field, docking files, etc.).
simulation_outputs: – Processed MD trajectories, RMSD/RMSF analyses, radius of gyration values, and other derived metrics.
figures_data: – Data underlying figures shown in the main manuscript and supporting information.
movies: – Molecular dynamics trajectory movies (Supplementary Movies S2 & S3).
notebooks: – Example analysis Jupyter notebooks for reproducing figures and plots.
docs: – Supporting documentation and supplementary methods.

# Methods Summary (Computational)
## Structural modeling:
ALK kinase domain (residues 1105–1377) modeled with GSK3 isoforms (α: 82–457; β: 1–403).
Initial models built using AlphaFold and HADDOCK for protein–protein docking.
Mutations (F1174L, R1275Q, I1250T) introduced via UCSF Chimera.
Molecular dynamics simulations:
All-atom simulations run for 50 ns per complex.

## Analyses performed:
Root Mean Square Deviation (RMSD)
Root Mean Square Fluctuation (RMSF)
Radius of gyration (Rg)
Interaction residue mapping

## Visualization:
Structural interfaces analyzed in PyMOL/Chimera.
Movies rendered at 0.2 ns/frame.
For complete protocols, see the Supporting Information (SI) included with the manuscript.


## How to Use This Repository
## Clone the repo:
git clone https://github.com/lutimbastuart/ALK_Variants_In_Neuroblastoma.git
cd ALK_Variants_In_Neuroblastoma

## Explore data:
Simulation trajectories (simulation_outputs/) can be loaded into VMD, PyMOL, ChimeraX, or MDAnalysis.


## Cite this work:
If you use these datasets, please cite:
Wulf AM, Lutimba S, Cameron D, Desjardins J, Shaw T, Rossetti L, Mansour MA, Liu KJ. Neuroblastoma-associated ALK variants have distinct cellular and biochemical activities. (2025).
