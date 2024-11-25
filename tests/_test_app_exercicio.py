from http import HTTPStatus

from fast_zero.security import create_access_token


def test_get_users__exercicio(client, user):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': user.username,
        'email': user.email,
        'id': user.id,
    }


def test_get_user_not_found__exercicio(client):
    response = client.get('/users/666')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User nao encontrado'}


def test_create_user_conflict_username__exercicio(client, user):
    response = client.post(
        '/users/',
        json={
            'username': user.username,
            'email': 'teste@test.com',
            'password': '123',
        },
    )

    # VAlidar o status code correto?
    assert response.status_code == HTTPStatus.CONFLICT
    # Validar UserPublic
    assert response.json() == {'detail': 'Username ja existe'}


def test_create_user_conflict_email__exercicio(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'Teste1',
            'email': user.email,
            'password': '123',
        },
    )

    # VAlidar o status code correto?
    assert response.status_code == HTTPStatus.CONFLICT
    # Validar UserPublic
    assert response.json() == {'detail': 'Email ja existe'}


def test_put_user_not_found__exercicio(client, user, token):
    response = client.put(
        '/users/666',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'id': user.id,
            'username': 'testusername10',
            'email': 'test@test.com',
            'password': '123',
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_jwt_credentials_exception_email__exercicio(client):
    token = create_access_token({})

    response = client.delete(
        '/users/1', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_jwt_credentials_exception_user__exercicio(client):
    data = {'sub': '666@test.com'}
    token = create_access_token(data)

    response = client.delete(
        '/users/1', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}