def test_get_activities_returns_seeded_data(client):
    # Arrange

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_get_activities_items_have_expected_fields(client):
    # Arrange

    # Act
    response = client.get("/activities")

    # Assert
    data = response.json()
    required_fields = {"description", "schedule", "max_participants", "participants"}

    for _, activity in data.items():
        assert required_fields.issubset(activity.keys())
        assert isinstance(activity["participants"], list)
        assert isinstance(activity["max_participants"], int)
