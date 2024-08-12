from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from api.routers import api_healthcheck_router, api_v1_router
from core.middlewares.catcher import CatcherExceptionsMiddleware
from core.middlewares.log_interceptor import LoggerMiddleware
from core.settings import log, settings
from core.settings.database import init_db, validate_db_conections
from core.utils.environment import EnvironmentsTypes
from core.utils.logger import LoggerConfig
from core.utils.validations import validation_pydantic_field

app = FastAPI(
    title=settings.PROJECT_NAME,
    redirect_slashes=False,
)

LoggerConfig.load_format()


# Set all CORS enabled origins
app.add_middleware(CatcherExceptionsMiddleware)
app.add_middleware(LoggerMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_v1_router)
app.include_router(api_healthcheck_router)


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


#if EnvironmentsTypes.LOCAL.value[0] == settings.ENVIRONMENT:
#    init_db()
log.info(f"ENVIRONMENT: {settings.ENVIRONMENT}")
validate_db_conections()
validation_pydantic_field(app)
