# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from authentik_client.api.admin_api import AdminApi
    from authentik_client.api.authenticators_api import AuthenticatorsApi
    from authentik_client.api.core_api import CoreApi
    from authentik_client.api.crypto_api import CryptoApi
    from authentik_client.api.enterprise_api import EnterpriseApi
    from authentik_client.api.events_api import EventsApi
    from authentik_client.api.flows_api import FlowsApi
    from authentik_client.api.managed_api import ManagedApi
    from authentik_client.api.oauth2_api import Oauth2Api
    from authentik_client.api.outposts_api import OutpostsApi
    from authentik_client.api.policies_api import PoliciesApi
    from authentik_client.api.propertymappings_api import PropertymappingsApi
    from authentik_client.api.providers_api import ProvidersApi
    from authentik_client.api.rac_api import RacApi
    from authentik_client.api.rbac_api import RbacApi
    from authentik_client.api.root_api import RootApi
    from authentik_client.api.schema_api import SchemaApi
    from authentik_client.api.sources_api import SourcesApi
    from authentik_client.api.ssf_api import SsfApi
    from authentik_client.api.stages_api import StagesApi
    from authentik_client.api.tasks_api import TasksApi
    from authentik_client.api.tenants_api import TenantsApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from authentik_client.api.admin_api import AdminApi
from authentik_client.api.authenticators_api import AuthenticatorsApi
from authentik_client.api.core_api import CoreApi
from authentik_client.api.crypto_api import CryptoApi
from authentik_client.api.enterprise_api import EnterpriseApi
from authentik_client.api.events_api import EventsApi
from authentik_client.api.flows_api import FlowsApi
from authentik_client.api.managed_api import ManagedApi
from authentik_client.api.oauth2_api import Oauth2Api
from authentik_client.api.outposts_api import OutpostsApi
from authentik_client.api.policies_api import PoliciesApi
from authentik_client.api.propertymappings_api import PropertymappingsApi
from authentik_client.api.providers_api import ProvidersApi
from authentik_client.api.rac_api import RacApi
from authentik_client.api.rbac_api import RbacApi
from authentik_client.api.root_api import RootApi
from authentik_client.api.schema_api import SchemaApi
from authentik_client.api.sources_api import SourcesApi
from authentik_client.api.ssf_api import SsfApi
from authentik_client.api.stages_api import StagesApi
from authentik_client.api.tasks_api import TasksApi
from authentik_client.api.tenants_api import TenantsApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
