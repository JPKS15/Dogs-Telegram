from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    SLEEP_TIME: list[int] = [3000, 3600]
    AUTO_TASK: bool = True
    RANDOM_CARD: bool = True
    CARD_NUMBER: int = 1
    USE_REF: bool = True

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()
