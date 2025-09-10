# ALK_Variants_In_Neuroblastoma
Neuroblastoma-associated ALK variants have distinct cellular and biochemical activities 
# Abstract
Mutations in anaplastic lymphoma kinase (ALK) are associated with high-risk neuroblastoma, a childhood cancer arising in trunk neural crest (NC) cells. The role of ALK in undifferentiated NC is still unknown; however, the presence of activating mutations in ALK correlates with migratory and invasive cell behaviours in neuroblastoma cell lines. Here, we show the functional consequences of ALK overexpression on neural crest cells, by comparing wildtype ALK (ALKWT) protein to ALK gain-of-function variants ALKF1174L and ALKR1275Q. Elevated ALK activity leads to increased migration velocity and loss of directionality, while ALKF1174L overexpression presents additional effects on cytoskeletal protrusions. These results correlate with increased binding of ALKF1174L to GSK3, which has previously been shown to regulate cytoskeletal dynamics in neural crest cells. Further, molecular dynamics simulations of this complex shows high flexibility, suggestive of enhanced allosteric regulation. Together, our data suggests that activating mutations in ALK drive migratory changes in trunk NC cells, potentially mediated by its novel interacting partner GSK3.

# Repository Contents
## raw_data – Unprocessed data from molecular dynamics (MD) simulations and structural modeling.
## simulation_inputs: – Input coordinate and parameter files (PDB, topology, force field, docking files, etc.).
## simulation_outputs: – Processed MD trajectories, RMSD/RMSF analyses, radius of gyration values, and other derived metrics.
## figures_data: – Data underlying figures shown in the main manuscript and supporting information.
## movies: – Molecular dynamics trajectory movies (Supplementary Movies S2 & S3).
## notebooks: – Example analysis Jupyter notebooks for reproducing figures and plots.
## docs: – Supporting documentation and supplementary methods.

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

# For complete protocols, see the Supporting Information (SI) included with the manuscript.



## How to Use This Repository

# Clone the repo:
git clone https://github.com/YOUR_USERNAME/alk-neuroblastoma-variants.git
cd alk-neuroblastoma-variants


# Explore data:
Simulation trajectories (simulation_outputs/) can be loaded into VMD, PyMOL, ChimeraX, or MDAnalysis.


# Cite this work:
If you use these datasets, please cite:

# Wulf AM, Lutimba S, Cameron D, Desjardins J, Shaw T, Rossetti L, Mansour MA, Liu KJ. Neuroblastoma-associated ALK variants have distinct cellular and biochemical activities. (2025).
