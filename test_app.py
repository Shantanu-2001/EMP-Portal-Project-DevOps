"""
Module for testing the application.
"""

import pytest
from models import models
from app import app, db


@pytest.fixture
def client():
    """
    Fixture for setting up and tearing down the test environment.
    """
    app_context = app.app_context()
    app_context.push()
    init_db()
    yield app.test_client()
    truncate_db()
    app_context.pop()


def init_db():
    """
    Initialize the test database.
    """
    database = 'test_emp_db.db'
    app.config.update(
        SQLALCHEMY_DATABASE_URI='sqlite:///' + database
    )


def truncate_db():
    """
    Truncate the test database.
    """
    with app.app_context():
        models.Employee.query.delete()
        db.session.commit()


def test_index():
    """
    Test case for the index route.
    """
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200


def test_add(client):
    """
    Test case for adding an employee.
    """
    test_data = {
        'name': 'Mickey Test',
        'gender': 'male',
        'address': 'IN',
        'phone': '0123456789',
        'salary': '2000',
        'department': 'Sales'
    }
    client.post('/add', data=test_data)
    with app.app_context():
        assert models.Employee.query.count() == 1


def test_edit():
    """
    Test case for editing an employee.
    """
    client = app.test_client()
    response = client.post('/edit/0')
    assert response.status_code == 200
    assert b"Sorry, the employee does not exist." in response.data


def test_delete(client):
    """
    Test case for deleting an employee.
    """
    test_data = {'emp_id': 0}
    response = client.post('/delete', data=test_data)
    assert response.status_code == 200
    assert b"Sorry, the employee does not exist." in response.data
