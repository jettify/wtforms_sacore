import sqlalchemy as sa
from unittest import TestCase
from wtforms_sqcore.core import model_form


meta = sa.MetaData()

user = sa.Table(
    "user", meta,
    sa.Column('id', sa.Integer, nullable=False),
    sa.Column('login', sa.String(64), nullable=False),
    sa.Column('passwd', sa.String(256), nullable=False),
    sa.Column('salt', sa.String(256), nullable=False),
    sa.Column('is_superuser', sa.Boolean, nullable=False,
              server_default='FALSE'),
    sa.Column('firstname', sa.String(256), nullable=False),
    sa.Column('lastname', sa.String(256), nullable=False),
    sa.Column('disabled', sa.Boolean, nullable=False,
              server_default='FALSE'),

    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('login', name='user_login_key'),
    )

class TestBase(TestCase):


    def test_column_default_callable(self):
        user_form = model_form(site)()
        expected = {'salt': None, 'passwd': None,
                    'is_superuser': False,
                    'firstname': None,
                    'lastname': None,
                    'login': None,
                    'disabled': False}
        self.assertEqual(user_form.data, expected)
