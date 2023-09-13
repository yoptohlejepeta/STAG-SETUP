from pydantic_settings import BaseSettings, SettingsConfigDict


class RedisSettings(BaseSettings):
    host: str
    port: int
    db: int


class AppSettings(BaseSettings):
    host: str
    port: int
    reload: bool
    login_url: str


class Settings(BaseSettings):
    redis: RedisSettings
    app: AppSettings

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
        arbitrary_types_allowed=True,
        env_nested_delimiter="__",
    )
