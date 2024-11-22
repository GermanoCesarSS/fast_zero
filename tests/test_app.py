from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


@app.get('/')
def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # asseert
    assert response.json() == {'message': 'Olar mundo!!'}
