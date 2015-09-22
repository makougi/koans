class Dog:
        def name(self):
            return "Fido"

        def _tail(self):
            # Prefixing a method with an underscore implies private scope
            return "wagging"

        def __password(self):
            return 'password' # Genius!

def test_attributes_with_double_underscore_prefixes_are_subject_to_name_mangling():
	rover = Dog()
	password = rover.__password()
	print(Dog.__password())
	
test_attributes_with_double_underscore_prefixes_are_subject_to_name_mangling()
