import os
from dotenv import load_dotenv
from fastapi import FastAPI, Security
from fastapi_mcp import FastApiMCP, AuthConfig
import uvicorn
from auth import auth_scheme

load_dotenv()
FRONTEND_CLIENT_ID = os.getenv("FRONTEND_CLIENT_ID", "")
CLIENT_ID = os.getenv("CLIENT_ID", "")
SCOPE_DESCRIPTION = os.getenv("SCOPE_DESCRIPTION", "user-impersonation")

app = FastAPI(
    swagger_ui_oauth2_redirect_url='/oauth2-redirect',
    swagger_ui_init_oauth={
        'usePkceWithAuthorizationCodeGrant': True,
        'clientId': FRONTEND_CLIENT_ID,
        'scopes': [f'api://{CLIENT_ID}/{SCOPE_DESCRIPTION}'],
    },
    dependencies=[Security(auth_scheme)],
)

@app.get("/", operation_id="get_secure_hello")
def get_secure_hello():
    return {"message": "Hello, secure world!"}

mcp = FastApiMCP(
    app,
    name="Secure MCP",
    auth_config=AuthConfig(
        dependencies=[Security(auth_scheme)],
    )
)

mcp.mount_http()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
