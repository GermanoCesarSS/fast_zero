from http import HTTPStatus


def test_read_users__exercicio(client, user):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': user}


def test_update_user_not_found__exercicio(client):
    response = client.put(
        '/users/10',
        json={
            'id': 10,
            'username': 'testusername10',
            'email': 'test@test.com',
            'password': '123',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user_not_found__exercicio(client):
    response = client.delete('/users/10')

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_get_user_not_found__exercicio(client):
    response = client.get('users/666')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
