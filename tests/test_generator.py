from pypassword.pypassword import password_generator


class test_simple_password:
    password = password_generator()


class test_special_password:
    password = password_generator(special=True)