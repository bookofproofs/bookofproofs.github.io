class BopLicense:
    def __init__(self, license_source):
        self.license_source = license_source
        self.references = dict()

    def add_reference(self, reference_id: str, reference_body: str):
        if reference_id in self.references:
            raise AssertionError("Duplicate reference " + reference_id + " listed in _sources/_references/index.md")
        self.references[reference_id] = reference_body


class BopReferences:
    def __init__(self, source_references, license_list: list):
        if source_references is None:
            raise AssertionError("Missing _sources/_references/index.md")
        if len(license_list) == 0:
            raise AssertionError("Missing _sources/_licenses/*")
        self._license_list = license_list
        self._licenses = dict()
        self._read_references(source_references)

    def _read_references(self, source_references):
        reference_lines = source_references.get_content_of_node().splitlines()
        for line in reference_lines:
            line = line.strip()
            if line != "":
                line_split = line.split("|")
                if len(line_split) != 3:
                    raise AssertionError("Malformed _sources/_references/index.md, each line must contain 3 columns.")
                license_id = line_split[0].strip()
                reference_id = line_split[1].strip()
                reference_body = line_split[2].strip()
                if "$" in reference_id and "$" in license_id:
                    if license_id not in self._licenses:
                        self._licenses[license_id] = BopLicense(self._get_license_by_id(license_id))
                    self._licenses[license_id].add_reference(reference_id, reference_body)

    def _get_license_by_id(self, license_id):
        for license_source in self._license_list:
            if license_source.nodeid == license_id:
                return license_source
        raise AssertionError("The license with the nodeid " + license_id + " is not defined in _sources/licenses")

    def get_cc_by_sa(self):
        for license_source in self._license_list:
            if license_source.nodeid == "bookofproofs$6919":
                return license_source
        raise AssertionError("The license CC BY_SA 4.0 is not defined in _sources/licenses")

    def get_licenses_for_bop_source(self, bop_source):
        """
        Creates a dictionary of licenses for a specific BoP source
        :param bop_source: a BopSource object
        :return: dictionary of BopLicense objects for the BoP source
        """
        licenses = dict()
        for reference_id in bop_source.references:
            found = False
            for license_id in self._licenses:
                bop_license = self._licenses[license_id]
                if reference_id in bop_license.references:
                    found = True
                    break
            if not found:
                raise AssertionError(
                    "No license found for reference " + reference_id + " in " + bop_source.get_file_name())
            if bop_license.license_source.nodeid not in licenses:
                new_bop_license = BopLicense(bop_license.license_source)
                reference_body = bop_license.references[reference_id]
                new_bop_license.add_reference(reference_id, reference_body)
                licenses[bop_license.license_source.nodeid] = new_bop_license
            else:
                reference_body = bop_license.references[reference_id]
                licenses[bop_license.license_source.nodeid].add_reference(reference_id, reference_body)
        return licenses
