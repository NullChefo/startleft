from startleft.paths import etm_mapping_schema
from startleft.processors.base.mapping import MultipleMappingFileValidator


class MtmtMappingFileValidator(MultipleMappingFileValidator):
    schema = 'etm_mapping_schema'

    def __init__(self, mapping_files: [bytes]):
        super(MtmtMappingFileValidator, self).__init__(self.schema, mapping_files)
