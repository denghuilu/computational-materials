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
    cif_str = structure.to(fmt="cif")

    # Save the CIF file to the local directory
    with open(f"{material_id}.cif", "w") as f:
        f.write(cif_str)

print(f"CIF file for {material_id} has been saved.")

cs_dir = './'
cs_cif = Path(cs_dir, 'mp-134.cif')
cs_atoms = read(cs_cif, format='cif')
cs_stru = Path(cs_dir, 'STRU')
pp = {'Al':'Al_ONCV_PBE-1.0.upf'}
basis = {'Al':'Al_gga_9au_100Ry_4s4p1d.orb'}
write(cs_stru, cs_atoms, format='abacus', pp=pp, basis=basis)