from settings import Settings


def test_settings() -> None:
    settings = Settings()

    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "test-app"
    assert settings.API_KEY == "fake-api-key-test"
