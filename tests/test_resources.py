from .utils import spin_up, tear_down


def test_Entry_post():

	client = spin_up()

	response = client.post(
		"/entry", 
		json={
			"title": "test title", 
			"description": "test description"
		}
	)

	response_data = response.json()

	assert response.status_code == 200
	assert response_data['title'] == "test title"
	assert response_data['description'] == "test description"

	tear_down()