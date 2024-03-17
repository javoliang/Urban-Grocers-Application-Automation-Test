import sender_stand_request
import data

def positive_assert(kit_response, expected_status_code, expected_name):
    assert kit_response.status_code == expected_status_code
    assert kit_response.json()["name"] == expected_name

def negative_assert(kit_response, expected_status_code):
    assert kit_response.status_code == expected_status_code

def test_kit_creation_1():
    # Comprobación 1: El número permitido de caracteres (1)
    kit_body = data.kit_bodies["one_character"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, 201, kit_body['name'])

def test_kit_creation_2():
    # Comprobación 2: El número permitido de caracteres (511)
    kit_body = data.kit_bodies["maximum_characters"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, 201, kit_body['name'])

def test_kit_creation_3():
    # Comprobación 3: El número de caracteres es menor que la cantidad permitida (0)
    kit_body = data.kit_bodies["empty_string"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    negative_assert(kit_response, 400)

def test_kit_creation_4():
    # Comprobación 4: El número de caracteres es mayor que la cantidad permitida (512)
    kit_body = data.kit_bodies["maximum_plus_one_characters"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    negative_assert(kit_response, 400)

def test_kit_creation_5():
    # Comprobación 5: Se permiten caracteres especiales
    kit_body = data.kit_bodies["special_characters"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, 201, kit_body['name'])

def test_kit_creation_6():
    # Comprobación 6: Se permiten espacios
    kit_body = data.kit_bodies["spaces"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, 201, kit_body['name'])

def test_kit_creation_7():
    # Comprobación 7: Se permiten números
    kit_body = data.kit_bodies["numbers"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, 201, kit_body['name'])

def test_kit_creation_8():
    # Comprobación 8: El parámetro no se pasa en la solicitud
    kit_body = data.kit_bodies["empty_kit_body"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    negative_assert(kit_response, 400)

def test_kit_creation_9():
    # Comprobación 9: Se ha pasado un tipo de parámetro diferente (número)
    kit_body = data.kit_bodies["number_name"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    negative_assert(kit_response, 400)

if __name__ == "__main__":
    test_kit_creation_1()
    test_kit_creation_2()
    test_kit_creation_3()
    test_kit_creation_4()
    test_kit_creation_5()
    test_kit_creation_6()
    test_kit_creation_7()
    test_kit_creation_8()
    test_kit_creation_9()
