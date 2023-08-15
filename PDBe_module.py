import urllib.request
import urllib.error
import json

class PyPDBe:
    """
    Python binding to the European Protein Data Bank (PDBe) search functions.
    """

    def perform_action(self, action, pdbid, chain_id=None, resultpath=None):
        """
        Performs action defined by given url
        :param action: action name
        :param pdbid: string - 4-character PDB id code.
        :param chain_id: chain identifier
        :param resultpath: path to the file where results are stored (if the file exists, will be overwritten)
        :return:
        """
        url = f'http://www.ebi.ac.uk/pdbe/api/pdb/entry/{action}/{pdbid}'
        if chain_id:
            url += f"chain/{chain_id}"
        print(url)
        try:
            request = urllib.request.Request(url)
            temp = urllib.request.urlopen(request)
            result = temp.read()
            result = result.decode('unicode_escape')
            # assert result
            result = json.loads(result)
            result = json.dumps(result, indent=4)
            if resultpath:
                with open(resultpath, 'w') as file:
                    file.write(result)
            return result
        except urllib.error.HTTPError as err:
            if err.code == 404:
                print(f'Structure {pdbid} not found')
            else:
                print('Invalid Input')

    def get_summary(self, pdbid):
        """"
        Provides a summary of properties of a PDB entry, such as the title of the entry, list of depositors,
        date of deposition, date of release, date of latest revision, experimental method,
        list of related entries in case split entries, etc.

        :param pdbid:  String - 4-character PDB id code.
        :return: entry_authors, number_of_entities, title, processing_site, deposition_date, split_entry, revision_date,
        assemblies, experimental_method, related_structures, deposition_site, release_date, experimental_method_class
        """
        return self.perform_action('summary', pdbid)

    def get_molecules(self, pdbid):
        """
        Provides the details of molecules (or entities in mmCif-speak) modelled in the entry, such as entity pdb id,
        description, type, polymer-type (if applicable), number of copies in the entry, sample preparation method,
        source organism(s) (if applicable), etc.

        :param pdbid: String - 4-character PDB id code.
        :return: molecule_name, chem_comp_ids,molecule_type, in_chains, number_of_copies, ca_p_only,
            in_struct_asyms, mutation_flag, entity_id, weight, sample_preparation, gene_name, molecule_type, sequence,
            source, entity_id, weight, synonym, number_of_copies, length, in_struct_asyms, sample_preparation,
            pdb_sequence_indices_with_multiple_residues, pdb_sequence, chem_comp_ids
        """
        # TODO: check weight, entity_id, sample_preparation (twice mentioned in the return section)
        return self.perform_action('molecules', pdbid)

    def get_publications(self, pdbid):
        """
        This call provides details of publications associated with an entry, such as title of the article, journal name,
        year of publication, volume, pages, doi, pubmed_id, etc.
        Primary citation is listed first.

        :param pdbid: String - 4-character PDB id code.
        :return: pubmed_id, publication, authors, pub_id, title, doi, pubmed_id, type, journal_info, pages, issue, year,
        volume, pdb_abbreviation, ISO_abbreviation, abstract, author_list
        """
        # TODO: check pubmed_id (twice mentioned in the return section)
        return self.perform_action('publications', pdbid)

    # TODO function get_related_publications is missing

    def get_experiment(self, pdbid):
        """
        Provides details of experiment(s) carried out in determining the structure of the entry.
        Each experiment is described in a separate dictionary.
        For X-ray diffraction, the description consists of resolution, space group, cell dimensions, R and Rfree,
            refinement program, etc.
        For NMR, details of spectrometer, sample, spectra, refinement, etc. are included.
        For EM, details of specimen, imaging, acquisition, reconstruction, fitting etc. are included.

        :param pdbid: String - 4-character PDB id code.
        :return: experimental_method_class, resolution, r_factor, spacegroup, starting_model, refinement_software,
        phasing_method, r_free, structure_determination_method, resolution_low, r_free_selection_details,
        r_free_percent_reflections, expression_host_scientific_name, resolution_high, diffraction_experiment,
        experiment_data_available, num_reflections, experimental_method, percent_reflections_observed, cell,
        completeness, crystal_growth, r_work
        """
        return self.perform_action('experiment', pdbid)


    def get_NMR_resources(self, pdbid):
        """
        Provides URLs of available additional resources for NMR entries.
        E.g., mapping between structure (PDB) and chemical shift (BMRB) entries.

        :param pdbid: String - 4-character PDB id code.
        :return: vivaldi_link_restraints, vivaldi_link_olderado, casd_nmr_link, uniquely_linked_bmrb_entries,
            vivaldi_link_default, vivaldi_link_score, vivaldi_link_vasco, related_bmrb_entries, olderado_link,
            nrg_link
        """
        return self.perform_action('nmr_resources', pdbid)

    def get_ligands(self, pdbid):
        """
        Provides a a list of modelled instances of ligands, i.e. 'bound' molecules that are not waters.

        :param pdbid: String - 4-character PDB id code.
        :return: entity_id, author_residue_number, chem_comp_id, residue_number, alternate_conformers, chem_comp_name,
            chain_id, struct_asym_id, author_insertion_code
        """
        return self.perform_action('ligand_monomers', pdbid)

    def get_modified_residues(self, pdbid):
        """
        Provides a list of modelled instances of modified amino acids or nucleotides in protein,
        DNA or RNA chains.

        :param pdbid: String - 4-character PDB id code.
        :return:entity_id, author_residue_number, chem_comp_id, residue_number, alternate_conformers, chem_comp_name,
            chain_id, struct_asym_id, author_insertion_code
        """
        return self.perform_action('modified_AA_or_NA', pdbid)

    def get_mutated_residues(self, pdbid):
        """
        Provides a list of modelled instances of mutated amino acids in proteins in an entry.
        (Note that at present it does not provide information about mutated nucleotides in RNA or DNA chains,
        but it would do so in near future.)

        :param pdbid: String - 4-character PDB id code.
        :return:entity_id, author_residue_number, chem_comp_id, residue_number, chem_comp_name, chain_id, struct_asym_id,
            author_insertion_code, mutation_details
        """
        return self.perform_action('mutated_AA_or_NA', pdbid)


    def get_release_status(self, pdbid):
        """
        Provides status of a PDB entry (released, obsoleted, on-hold etc) along with some other information such as
        authors, title, experimental method, etc.

        :param pdbid: String - 4-character PDB id code.
        :return: experimental_method, since, obsoletes, superceded_by, entry_authors,experimental_method_class,
        status_code, title
        """
        return self.perform_action('status', pdbid)

    def get_observed_ranges(self, pdbid, chain=None):
        """
        Provides observed ranges, i.e. segments of structural coverage, of polymeric molecules that are modelled
        fully or partly.

        If chain is specified, returns data for a particular chain

        :param pdbid: String - 4-character PDB id code.
        :param chain: String - PDB chain pdbid.
        :return: struct_asym_id, author_residue_number, residue_number, author_insertion_code
        """
        return self.perform_action('polymer_coverage', pdbid, chain_id=chain)

    def get_secondary_structure(self, pdbid):
        """
        Provides details about residue ranges of regular secondary structure (alpha helices and beta strands)
        found in protein chains of the entry. For strands, sheet pdb id can be used to identify a beta sheet.

        :param pdbid: String - 4 -character PDB id code.
        :return: struct_asym_id, author_residue_number, residue_number, author_insertion_code, strands, helices, sheet_id
        """
        return self.perform_action('secondary_structure', pdbid)

    def get_residues(self, pdbid, chain=None):
        """
        Lists all residues (modelled or otherwise) in the entry, except waters,
        along with details of the fraction of expected atoms modelled for the residue and any alternate conformers.

        :param pdbid: String - 4 -character PDB id code.
        :param chain: String - PDB chain id.
        :return: struct_asym_id, author_residue_number, residue_number, author_insertion_code, observed_ratio
        """
        return self.perform_action('residue_listing', pdbid, chain_id=chain)

    def get_binding_sites(self, pdbid):
        """
        Provides details on binding sites in the entry as per STRUCT_SITE records in PDB files (or mmCif equivalent
        thereof), such as ligand, residues in the site, description of the site, etc.

        :param pdbid: String - 4-character PDB pdbid code.
        :return: struct_asym_id, author_residue_number, residue_number, author_insertion_code,
        chain_id, entity_id, evidence_code, details, site_id, site_residues, symmetry_symbol
        """
        return self.perform_action('binding_sites', pdbid)

    def get_files(self, pdbid):
        """
        Provides URLs and brief descriptions (labels) for PDB and mmCif files, biological assembly files,
        FASTA file for sequences, SIFTS cross reference XML files, validation XML files, X-ray structure factor file,
        NMR experimental constraints files, etc. Please note that these files are also available on https.

        :param pdbid: String - 4-character PDB id code.
        :return: label, url, downloads, views, SIFTS, assembly
        """
        return self.perform_action('files', pdbid)

    def get_observed_residues_ratio(self, pdbid):
        """
        Provides the ratio of observed residues for each chain in each molecule (or entity in mmCif-speak) of a pdb entry.
        The list of chains within an entity is sorted by observed_ratio (descending order), partial_ratio (ascending order),
        and number_residues (descending order).

        :param pdbid: String - 4-character PDB id code.
        :return: struct_asym_id, number_residues, chain_id, observed_ratio
        """
        return self.perform_action('observed_residues_ratio', pdbid)

    def get_assembly(self, pdbid):
        """
        Provides information for each assembly of a given PDB ID. This information is broken down at the entity level for
        each assembly. The information given includes the molecule name, type and class, the chains where the molecule
        occur, and the number of copies of each entity in the assembly.

        :param pdbid: String - 4-character PDB id code.
        :return
        """
        return self.perform_action('assembly', pdbid)