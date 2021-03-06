NagBody_pkg
===========

Numerical Algorithms for General Body Dynamics and data analysis

MathematicaMCMC code

Author:
Mario A. Rodríguez-Meza
Instituto Nacional de Investigaciones Nucleares
marioalberto.rodriguez@inin.gob.mx
Ciudad de México. January 1st, 2019
Updated: 2020-11-5


Acknowledgements: Tula Bernal, Lizbeth M. Fernández-Hernández and Ariadna Montiel 

Based in a Mathematica code shared by Tula Bernal

Paper reference: 
If you use this code, please cite the reference: L. M. Fernández-Hernández, A. Montiel and Mario A. Rodríguez-Meza, MNRAS 488, 5127–5144 (2019). arXiv:1809.06875. (See the bibtex file format: citation_paper.bibtex)

First clone it:
git clone https://github.com/rodriguezmeza/MathematicaMCMC-1.0.0.git

RUN:  

This is a Mathematica notebook: go to directory 

Mathematica/mcmc/MathematicaMCMC

and open the notebook there with Mathematica.

(For a more detailed explanition see at the begining of the Mathematica notebook and in the Readme section i.0.
)

shift-enter on the biggest right bracket ->
It runs in about one minute.

Case study: 
rotation curve galaxy IC 2574; 
data from SPARC catalog, F. Lelli et al., Astron. J. 152, 157 (2016); 
implemented model Pseudo isothermal dark matter density profile;
two parameters: Subscript[\[Rho], s] and Subscript[r, s].

For a different two parameter density profile model make the appropriate changes in subsubsubsection 30.a. Model definitios Equations Rotation curve dark matter model.

For a different rotation curve data, change the line:

RCTable = Import["IC2574_rotmod.txt", "Data"];

in the subsubsection 30.b.1 Input galaxy rotation curve data. Make sure the column types correspond to:

(* From de header of the data file: IC2574_rotmod_header.txt :
# Distance=3.91 Mpc
# Rad Vobs errV Vgas Vdisk Vbul SBdisk SBbul
# kpc km/s km/s km/s km/s km/s L/pc^2 L/pc^2
*)

Columns in the chain extended file (to process using GetDist)
(* 
col1: weights, 
col2: -2LogLike, 
col3: \[Rho]s (fit parameter),
col4: rs (fit parameter),
col5: muDM (derived parameter),
col6: m300 (derived parameter),
col7: mTot (DM) (derived parameter),
col8: %mTot (DM) (derived parameter)
*)

Output:
Folder Results
Folder Results/Chains
Folder Results/LaTeX
Folder Results/PDF
Folder Results/TXT

Changes only in section or subsections with "(adapt to your needs)"

For more details see at the begining of the Mathematica notebook and in the Readme section i.0.
