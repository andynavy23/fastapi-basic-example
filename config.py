from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AWFU API"
    admin_email: str = "andynavy23@gmail.com"


settings = Settings()