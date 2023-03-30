from slp_tfplan.slp_tfplan.parse.tfplan_parser import TfplanParser
from slp_tfplan.slp_tfplan.validate.tfplan_mapping_file_validator import TFPlanMappingFileValidator
from slp_tfplan.slp_tfplan.load.tfplan_loader import TfplanLoader, get_tfplan, get_tfgraph
from slp_tfplan.slp_tfplan.map.tfplan_mapping_file_loader import TfplanMappingFileLoader
from slp_tfplan.slp_tfplan.validate.tfplan_validator import TFPlanValidator
from slp_base.slp_base import MappingLoader, MappingValidator
from slp_base.slp_base import OTMProcessor
from slp_base.slp_base import ProviderValidator
from slp_base.slp_base.provider_loader import ProviderLoader
from slp_base.slp_base.provider_parser import ProviderParser


class TFPlanProcessor(OTMProcessor):
    """
    Terraform implementation of OTMProcessor
    """

    def __init__(self, project_id: str, project_name: str, sources: [bytes], mappings: [bytes]):
        self.project_id = project_id
        self.project_name = project_name
        self.mappings = mappings
        self.sources = sources

        self.tfplan_source: bytes = get_tfplan(sources)
        self.tfgraph_source: bytes = get_tfgraph(sources)

        self.terraform_loader = None
        self.mapping_loader = None

    def get_provider_validator(self) -> ProviderValidator:
        return TFPlanValidator(self.sources)

    def get_provider_loader(self) -> ProviderLoader:
        self.terraform_loader = TfplanLoader(self.tfplan_source, self.tfgraph_source)
        return self.terraform_loader

    def get_mapping_validator(self) -> MappingValidator:
        return TFPlanMappingFileValidator(self.mappings)

    def get_mapping_loader(self) -> MappingLoader:
        self.mapping_loader = TfplanMappingFileLoader(self.mappings)
        return self.mapping_loader

    def get_provider_parser(self) -> ProviderParser:
        return TfplanParser(
                self.project_id,
                self.project_name,
                self.terraform_loader.get_terraform(),
                self.terraform_loader.get_tfgraph(),
                self.mapping_loader.get_mappings())
