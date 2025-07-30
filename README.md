# FastAPI Azure MCP

A secure FastAPI application integrated with Model Context Protocol (MCP) and Azure Active Directory authentication.

## Overview

This project provides a FastAPI web service that:
- Implements Azure AD authentication using OAuth2 Authorization Code flow with PKCE
- Integrates with the Model Context Protocol (MCP) framework
- Provides secure API endpoints with automatic token validation
- Includes Swagger UI with OAuth2 integration for testing

## Features

- **Azure AD Authentication**: Single-tenant Azure authentication with OAuth2
- **FastAPI**: Modern, fast web framework with automatic API documentation
- **MCP Integration**: Model Context Protocol support for AI tool interactions
- **Interactive Documentation**: Swagger UI with OAuth2 login support
- **Security First**: All endpoints protected by default with Azure AD tokens

## Prerequisites

- Python 3.10.6 or higher
- Azure AD application registration
- Environment variables configured (see Configuration section)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fastapi-azure-mcp
```

2. Install dependencies using uv (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the root directory with the following variables:

```env
# Azure AD Configuration
CLIENT_ID=your-azure-ad-client-id
TENANT_ID=your-azure-ad-tenant-id
FRONTEND_CLIENT_ID=your-frontend-client-id
SCOPE_DESCRIPTION=user-impersonation
```

### Azure AD Setup

1. Register an application in Azure AD
2. Configure authentication:
   - Add redirect URI: `http://localhost:8000/oauth2-redirect`
3. Configure API permissions as needed
4. Note down the Client ID and Tenant ID

## Usage

### Running the Server

Start the development server:

```bash
python main.py
```

Or using uvicorn directly:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The server will start on `http://localhost:8000`

### API Documentation

Access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Authentication

1. Navigate to the Swagger UI at `http://localhost:8000/docs`
2. Click the "Authorize" button
3. Complete the OAuth2 flow with your Azure AD credentials
4. Test the secured endpoints

### Testing with MCP Client

Use the provided test script to verify MCP functionality:

1. Update the `token` variable in `test_security.py` with a valid Bearer token
2. Run the test:

```bash
python test_security.py
```

## Project Structure

```
fastapi-azure-mcp/
├── main.py              # FastAPI application with MCP integration
├── auth.py              # Azure AD authentication configuration
├── test_security.py     # MCP client test script
├── pyproject.toml       # Project dependencies and metadata
├── uv.lock             # Dependency lock file
└── README.md           # Project documentation
```

## API Endpoints

### `/` (GET)
- **Description**: Secure hello world endpoint
- **Authentication**: Required (Azure AD Bearer token)
- **Response**: `{"message": "Hello, secure world!"}`

### `/mcp` (MCP Protocol)
- **Description**: Model Context Protocol endpoint
- **Authentication**: Required (Azure AD Bearer token)
- **Usage**: For AI tool interactions and MCP clients

## Dependencies

- **fastapi**: Modern web framework for building APIs
- **fastapi-azure-auth**: Azure AD integration for FastAPI
- **fastapi-mcp**: Model Context Protocol integration
- **fastmcp**: MCP client library
- **uvicorn**: ASGI server for FastAPI
- **python-dotenv**: Environment variable management
- **requests**: HTTP library for API calls

## Development

### Code Structure

- `main.py`: Contains the FastAPI application setup, MCP integration, and endpoint definitions
- `auth.py`: Handles Azure AD authentication configuration and scheme setup
- `test_security.py`: Provides a test client for verifying MCP functionality

### Security

All endpoints are secured by default using Azure AD authentication. The application:
- Validates Bearer tokens against Azure AD
- Supports PKCE for secure authorization flows
- Integrates OAuth2 with Swagger UI for easy testing

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.