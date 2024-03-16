import sender_stand_request
import data


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def test_kit_creation_1():
    # Comprobación 1: El número permitido de caracteres (1)
    name = "a"
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name


def test_kit_creation_2():
    # Comprobación 2: El número permitido de caracteres (511)
    name = ("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
            "dabcdabcdabcdabcdabcdabcdabcdabcdabC")
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name


def test_kit_creation_3():
    # Comprobación 3: El número de caracteres es menor que la cantidad permitida (0)
    name = ""
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400


def test_kit_creation_4():
    # Comprobación 4: El número de caracteres es mayor que la cantidad permitida (512)
    name = ("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
            "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
            "dabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcd"
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
            "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
            "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400


def test_kit_creation_5():
    # Comprobación 5: Se permiten caracteres especiales
    name = '"№%@",'
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name


def test_kit_creation_6():
    # Comprobación 6: Se permiten espacios
    name = " A Aaa "
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name


def test_kit_creation_7():
    # Comprobación 7: Se permiten números
    name = "123"
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name


def test_kit_creation_8():
    # Comprobación 8: El parámetro no se pasa en la solicitud
    kit_body = {}
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400


def test_kit_creation_9():
    # Comprobación 9: Se ha pasado un tipo de parámetro diferente (número)
    name = 123
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400


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
