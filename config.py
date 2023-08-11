from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    TOKEN_MINUTES_LIFESPAN: int
    TOKEN_SECRET_KEY: str
    TOKEN_ALGORITHM: str

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
