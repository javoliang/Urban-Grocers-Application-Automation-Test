headers = {
    "Content-Type": "application/json"
}

user_body = {
            "firstName": "Max",
            "phone": "+10005553535",
            "address": "8042 Lancaster Ave.Hamburg, NY"
}

def get_kit_body(name):
    return kit_bodies[name].copy()

kit_bodies = {
    "one_character": {"name": "a"},
    "maximum_characters": {"name": ("Abcdabcdabcdabcdabcdabcdabcdabcdab"
                                    "cdabcdabcdabcdabcdabcdabcdabcdabcd"
                                    "abcdabcdabcdabcdabcdabcdabcdabcdab"
                                    "cdabcdabcdabcdabcdabcdabcdabcdabcd"
                                    "abcdabcdabcdabcdabcdabcdabcdabcdab"
                                    "cdabcdabcdabcdabcdabcdabcdabcdabcd"
                                    "abcdabcdabcdabcdabcdabcdabcdabcdab"
                                    "cdabcdabcdabcdabcdAbcdabcdabcdabcd"
                                    "abcdabcdabcdabcdabcdabcdabcdabcdab"
                                    "cdabcdabcdabcdabcdabcdabcdabcdabcd"
                                    "abcdabcdabcdabcdabcdabcdabcdabcdab"
                                    "cdabcdabcdabcdabcdabcdabcdabcdabcd"
                                    "abcdabcdabcdabcdabcdabcdabcdabcdab"
                                    "cdabcdabcdabcdabcdabcdabcdabcdabcd"
                                    "abcdabcdabcdabcdabcdabcdabcdabcdabC")},
    "empty_string": {"name": ""},
    "maximum_plus_one_characters": {"name": ("Abcdabcdabcdabcdabcdabcdab"
                                             "cdabcdabcdabcdabcdabcdabcd"
                                             "abcdabcdabcdabcdabcdabcdab"
                                             "cdabcdabcdabcdabcdabcdabcd"
                                             "abcdabcdabcdabcdabcdabcdab"
                                             "cdabcdabcdabcdabcdabcdabcd"
                                             "abcdabcdabcdabcdabcdabcdab"
                                             "cdabcdabcdabcdabcdabcdabcd"
                                             "abcdabcdabcdabcdabcdabcdab"
                                             "cdabcdabcdabcdabcdabcdAbcd"
                                             "abcdabcdabcdabcdabcdabcdab"
                                             "cdabcdabcdabcdabcdabcdabcd"
                                             "abcdabcdabcdabcdabcdabcdab"
                                             "cdabcdabcdabcdabcdabcdabcd"
                                             "abcdabcdabcdabcdabcdabcdab"
                                             "cdabcdabcdabcdabcdabcdabcd"
                                             "abcdabcdabcdabcdabcdabcdab"
                                             "cdabcdabcdabcdabcdabcdabcd"
                                             "abcdabcdabcdabcdabcdabcdab"
                                             "cdabcdabcdabcdabC")},
    "special_characters": {"name": '"№%@"'},
    "spaces": {"name": " A Aaa "},
    "numbers": {"name": "123"},
    "empty_kit_body": {},
    "number_name": {"name": 123}
}
