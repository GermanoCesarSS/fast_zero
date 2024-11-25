from http import HTTPStatus


def test_get_users__exercicio(client, user):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': user.username,
        'email': user.email,
        'id': user.id,
    }


def test_get_user_not_found__exercicio(client):
    response = client.get('users/666')

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


def test_put_user_not_found__exercicio(client):
    response = client.put(
        '/users/666',
        json={
            'id': 666,
            'username': 'testusername10',
            'email': 'test@test.com',
            'password': '123',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_put_user_conflict__exercicio(client, user2):
    response = client.put(
        'users/1',
        json={
            'id': '1',
            'username': 'Teste2',
            'email': 'teste2@test.com',
            'password': 'testtest',
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Username ou Email ja existe'}


def test_delete_user_not_found__exercicio(client):
    response = client.delete('/users/666')

    assert response.status_code == HTTPStatus.NOT_FOUND
