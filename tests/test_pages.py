import pytest

from app import create_app

# One literal, so the notice stays greppable and matches the issue verbatim.
ARCHIVE_NOTICE = "Archivo: este análisis se publicó antes de la elección del 1 de junio de 2025."  # noqa: E501


@pytest.fixture
def client():
    return create_app().test_client()


def get_page(client, path):
    response = client.get(path)
    assert response.status_code == 200
    return response.get_data(as_text=True)


@pytest.mark.parametrize(
    "path",
    ["/", "/boleta-verde", "/boleta-azul", "/lista-negra", "/acerca"],
)
def test_every_page_carries_the_archive_notice(client, path):
    assert ARCHIVE_NOTICE in get_page(client, path)
