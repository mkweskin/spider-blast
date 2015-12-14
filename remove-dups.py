'''
Removes sequences from a larger fasta file. The sequences listed in exclude are already represented in the fasta file with
another sample
'''

from Bio import SeqIO

exclude=["Pardosa_amentata_GBCH5703-13", "Micrommata_virescens_AGB014-11", "Philodromus_dispar_AGB027-11", "Segestria_senoculata_AGB034-11", "Tetragnatha_pinicola_GBCH11143-13", "Parasteatoda_tepidariorum_RBCH051-04", "Hypsosinga_pygmaea_RBCH069-04", "Xysticus_audax_AGB029-11", "Misumena_vatia_RBCH153-04", "Thanatus_formicinus_RBCH033-04", "Theridion_varians_ARONT231-09", "Neottiura_bimaculata_PWSH005-13", "Platnickina_tincta_ARONT108-09", "Phylloneta_impressa_SPIRU977-11", "Salticus_scenicus_ARONT009-09", "Micaria_pulicaria_SPICH216-09", "Micaria_aenea_SPICH157-09", "Steatoda_triangulosa_ERSPI293-09", "Steatoda_bipunctata_ERSPI376-09", "Pocadicnemis_pumila_SPIAL118-10", "Mermessus_trilobatus_ARONT726-10", "Tiso_aestivus_SPICH384-09", "Neriene_radiata_ERSPI397-09", "Linyphia_triangularis_GACAC389-12", "Neriene_clathrata_ARONT637-10", "Lepthyphantes_leprosus_ARONT220-09", "Larinioides_sclopetarius_ARONT335-09", "Pardosa_agrestis_SPIEU666-10", "Pardosa_proxima_TURAR740-10", "Pardosa_hortensis_SPIEU543-10", "Philodromus_cespitum_ARONT619-10", "Tetragnatha_extensa_GBADC036-10", "Philodromus_aureolus_GBCH11037-13", "Neoscona_adianta_GBCH11118-13", "Tmarus_piger_GBCH11023-13", "Synema_globosum_GBCH11025-13", "Pirata_piraticus_SPICH113-09", "Microlinyphia_pusilla_SPICH281-09", "Tenuiphantes_tenuis_GBCH12480-13", "Metellina_mengei_GBCH5715-13", "Pardosa_palustris_GBCH5702-13", "Araneus_angulatus_GBCH11132-13", "Agelena_labyrinthica_GBCH11071-13", "Clubiona_terrestris_AGB028-11", "Cyclosa_conica_RBCH053-04", "Anyphaena_accentuata_AGB030-11", "Heliophanus_flavipes_GACAC388-12", "Cheiracanthium_mildei_ARONT150-09", "Amaurobius_ferox_TDWGB732-10", "Enoplognatha_ovata_ARONT269-09", "Diplostyla_concolor_ARONT481-10", "Erigone_atra_ARONT639-10", "Araneus_diadematus_ARONT327-09", "Agyneta_rurestris_SPICH856-09", "Ebrechtella_tricuspidata_GBCH11031-13", "Argiope_bruennichi_GBCH10410-13"]

handle = open("barcode-08-gap-rem-name-clean-no-gaps.fasta", "rU")
output_handle = open("barcode-08-gap-rem-name-clean-no-gaps-dup-rem.fasta", "w")
for record in SeqIO.parse(handle, "fasta"):
    if record.id not in exclude:
        SeqIO.write(record, output_handle, "fasta")
handle.close()
output_handle.close()
