from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='nome',
        email='email@email.com',
        password='minha_senha-legal',
    )
    session.add(user)
    session.commit()
    session.scalar(select(User).where(User.email == 'email@email.com'))

    assert user.username == 'nome'
