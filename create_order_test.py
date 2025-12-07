# Юлия Блинкова 38 когорта финальный проект
import sender_stand_request


# Тест на создание заказа
def test_create_order_success():
    response = sender_stand_request.post_new_order()
    assert response.status_code == 201
    assert "track" in response.json()

# Тест на получение заказа по треку
def test_get_order_by_track_success():
    # Создаем заказ
    create_response = sender_stand_request.post_new_order()
    track = create_response.json()["track"]
    
    # Получаем заказ по треку
    get_response = sender_stand_request.get_order(track)
    assert get_response.status_code == 200
    