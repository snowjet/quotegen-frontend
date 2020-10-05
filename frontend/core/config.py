from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Quotegen Frontend"
    url_quote_backend: str = "http://backend:8080"
    image_backend_api: str = "http://backend:8080/quote/image"
    log_level: str = "INFO"

    class Config:
        env_file = ".env"


settings = Settings()
