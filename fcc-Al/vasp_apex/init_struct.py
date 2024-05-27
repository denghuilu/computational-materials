from ase.io import read, write
from pathlib import Path
from pymatgen.ext.matproj import MPRester

# Replace with your Materials Project API key
API_KEY = "wCN1U16O5jIs0byffczBICP2D7S79HYq"

# Replace with the material ID you are interested in
material_id = "mp-134"  # Example: Silicon has the material ID "mp-149"

with MPRester(API_KEY) as m:
    # Get CIF file
    structure = m.get_structure_by_material_id(material_id, conventional_unit_cell=True)
    poscar_str = structure.to(fmt="poscar")

    # Save the CIF file to the local directory
    with open(f"{material_id}.POSCAR", "w") as f:
        f.write(poscar_str)

print(f"POSCAR file for {material_id} has been saved.")