from http import HTTPStatus

from fast_zero.schemas import UserPublic


def test_post_user(client):
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


def test_get_users(client):
    response = client.get(
        '/users/'
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [],
    }


def test_get_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get(
        '/users/'
    )
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user, token):
    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'id': user.id,
            'username': 'testusername2',
            'email': 'teste@test2.com',
            'password': '123',
        },
    )

    assert response.json() == {
        'id': user.id,
        'username': 'testusername2',
        'email': 'teste@test2.com',
    }


def test_delete_user(client, token):
    response = client.delete(
        '/users/1', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.json() == {'message': 'User deletado'}


def test_delete_user_fornidden(client, user, token):
    response = client.delete(
        f'/users/{user.id + 1}', headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {
        'detail': 'Sem permisao para excluir esse usuario'
    }
