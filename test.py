import sender_stand_request

def positive_assert(track_id): # Позитивная проверка
    order_response = sender_stand_request.get_order_track(track_id)
    assert order_response.status_code == 200

def test_get_order_track_success_response():
    positive_assert(sender_stand_request.track_id)