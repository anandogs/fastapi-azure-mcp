import os
from dotenv import load_dotenv
from fastapi_azure_auth import SingleTenantAzureAuthorizationCodeBearer

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID", "")
TENANT_ID = os.getenv("TENANT_ID", "")
SCOPE_DESCRIPTION = os.getenv("SCOPE_DESCRIPTION", "user-impersonation")

if not CLIENT_ID or not TENANT_ID:
    raise ValueError("CLIENT_ID and TENANT_ID must be set in the environment variables.")

auth_scheme = SingleTenantAzureAuthorizationCodeBearer(
    app_client_id=CLIENT_ID,
    tenant_id=TENANT_ID,
    scopes={f'api://{CLIENT_ID}/{SCOPE_DESCRIPTION}': SCOPE_DESCRIPTION},
)