from fastapi import FastAPI
from .routes_cases import router as cases
from .routes_alerts import router as alerts
from .routes_stats import router as stats
from .routes_soar import router as soar
from .routes_wifi import router as wifi

#route registration
app = FastAPI(title="Network Security Analysis API")

app.include_router(cases)
app.include_router(alerts)
app.include_router(stats)
app.include_router(soar)
app.include_router(wifi)
