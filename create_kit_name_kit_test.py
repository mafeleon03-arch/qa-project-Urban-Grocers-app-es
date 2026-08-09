import sender_stand_request
import data

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(name):
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()

    kit_response = sender_stand_request.post_new_client_kit(
        kit_body,
        auth_token
    )

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()

    kit_response = sender_stand_request.post_new_client_kit(
        kit_body,
        auth_token
    )

    assert kit_response.status_code == 400

# PRUEBA 1
# Número permitido de caracteres: 1
def test_create_kit_1_character_in_name_get_success_response():
    positive_assert("a")


# PRUEBA 2
# Número permitido de caracteres: 511
def test_create_kit_511_characters_in_name_get_success_response():
    positive_assert("a" * 511)


# PRUEBA 3
# Número de caracteres menor que el permitido: 0
def test_create_kit_0_characters_in_name_get_error_response():
    negative_assert_code_400("")


# PRUEBA 4
# Número de caracteres mayor que el permitido: 512
def test_create_kit_512_characters_in_name_get_error_response():
    negative_assert_code_400("a" * 512)


# PRUEBA 5
# Se permiten caracteres especiales
def test_create_kit_special_characters_in_name_get_success_response():
    positive_assert("№%@,")


# PRUEBA 6
# Se permiten espacios
def test_create_kit_spaces_in_name_get_success_response():
    positive_assert(" A Aaa ")


# PRUEBA 7
# Se permiten números dentro de un string
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert("123")


# PRUEBA 8
# El parámetro name no se pasa en la solicitud
def test_create_kit_without_name_get_error_response():
    kit_body = {}
    auth_token = get_new_user_token()

    kit_response = sender_stand_request.post_new_client_kit(
        kit_body,
        auth_token
    )

    assert kit_response.status_code == 400


# PRUEBA 9
# Se pasa un tipo diferente: número entero
def test_create_kit_number_type_in_name_get_error_response():
    negative_assert_code_400(123)