from slp_base.slp_base.mapping_file_loader import MappingFileLoader
from slp_abacus.slp_abacus.map.mapping import Mapping


class AbacusMappingFileLoader(MappingFileLoader):

    def __init__(self, mapping_files_data: [bytes]):
        super().__init__(mapping_files_data)
        self.mapping = None

    def load(self):
        super().load()
        self.mapping: Mapping = Mapping(self.map)

    def get_mappings(self) -> Mapping:
        return self.mapping
