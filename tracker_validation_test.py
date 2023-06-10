import functions


# This function uses 2 other funcs to create an order, check that the order actually exists in the
# database and then makes sure that the response code from that check == 200
def test_track_check():
    track = functions.create_order()
    response = functions.check_track(track)
    assert response.status_code == 200


# Дарчиашвили Кирилл, 5-я когорта — Финальный проект. Инженер по тестированию плюс
