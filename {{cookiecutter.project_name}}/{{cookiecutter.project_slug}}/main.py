from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi_health import health

from {{cookiecutter.project_slug}}.routes.router import router

__version__ = "0.0.1"

app = FastAPI(
    title="{{cookiecutter.project_name}} APIs",
    description="{{cookiecutter.project_description}}",
    version=__version__,
    docs_url="/docs",
    redoc_url="/redoc",
)


app = FastAPI()


async def health_check():
    return {"status": "healthy"}


# Include routers
app.add_api_route("/health", health([health_check]), tags=["Management"], description="Management APIs")
app.include_router(router, prefix="/api/v1", tags=["Model Operations"])


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="{{cookiecutter.project_name}} APIs",
        description="{{cookiecutter.project_description}}",
        version=__version__,
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


def main():
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port={{cookiecutter.app_host_port}})


if __name__ == "__main__":
    main()
