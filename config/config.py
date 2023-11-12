from pydantic_settings import BaseSettings


class Config(BaseSettings):
    DATABASE_URL: str
    ALEMBIC_DATABASE_URL: str

    class Config:
        env_file = ".env"
        from_attribute = True


settings = Config()
