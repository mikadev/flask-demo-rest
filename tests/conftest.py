import pytest

from app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture()
def client(app):
    app.config.update({
        "TESTING": True,
    })
    app.app_context().push()
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
