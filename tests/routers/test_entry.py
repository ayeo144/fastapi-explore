from ..utils import spin_up, tear_down


def test_Entry_post():
    """
    Test adding a new entry record to the database via
    the API.
    """
    client = spin_up()

    response = client.post(
        "/entry", json={"title": "test title", "description": "test description"}
    )

    response_data = response.json()

    assert response.status_code == 200
    assert response_data["title"] == "test title"
    assert response_data["description"] == "test description"

    tear_down()


def test_Entry_post_exists():
    """
    Test adding an entry to the database via the API that already
    exists.
    """
    client = spin_up()

    entry = {"title": "test title", "description": "test description"}

    response_1 = client.post("/entry", json=entry)

    assert response_1.status_code == 200

    response_2 = client.post("/entry", json=entry)

    assert response_2.status_code == 400

    tear_down()
