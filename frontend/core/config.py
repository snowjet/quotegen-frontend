from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Quotegen Frontend"
    url_quote_backend: str = "http://backend:8000"
    log_level: str = "INFO"

    class Config:
        env_file = ".env"


settings = Settings()
