from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # asseert
    assert response.json() == {'message': 'Olá Mundo!!!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'test@test.com',
        },
    )

    # VAlidar o status code correto?
    assert response.status_code == HTTPStatus.CREATED
    # Validar UserPublic
    assert response.json() == {
        'id': 1,
        'username': 'testusername',
        'email': 'test@test.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'testusername',
                'email': 'test@test.com',
            }
        ]
    }


def test_updatee_user(client):
    response = client.put(
        '/users/1',
        json={
            'id': 1,
            'username': 'testusername2',
            'email': 'test@test.com',
            'password': '123',
        },
    )

    assert response.json() == {
        'id': 1,
        'username': 'testusername2',
        'email': 'test@test.com',
    }


def teste_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}
