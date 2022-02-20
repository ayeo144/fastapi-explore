from ..utils import spin_up, tear_down


def test_Entries_get():
    """
    Test the /entries endpoint get method returns the correct number
    of entries with the right contents.
    """
    client = spin_up()

    entry_1 = {"title": "title 1", "description": "contents 1"}
    entry_2 = {"title": "title 2", "description": "contents 2"}
    entry_3 = {"title": "title 3", "description": "contents 3"}

    response_1 = client.post("/entry", json=entry_1)
    response_2 = client.post("/entry", json=entry_2)
    response_3 = client.post("/entry", json=entry_3)

    response = client.get("/entries")

    response_data = response.json()

    assert response.status_code == 200

    assert len(response_data) == 3

    assert response_data[2]["title"] == "title 3"

    tear_down()