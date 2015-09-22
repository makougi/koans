class AboutMethods():
    class Dog:
        def name(self):
            return "Fido"

        def _tail(self):
            # Prefixing a method with an underscore implies private scope
            return "wagging"

        def __password(self):
            return 'password' # Genius!

    def metodi():
        password = Dog().__password()
    metodi()

    def test_calling_methods_in_other_objects(self):
        rover = self.Dog()
        self.assertEqual("Fido", rover.name())

    def test_private_access_is_implied_but_not_enforced(self):
        rover = self.Dog()

        # This is a little rude, but legal
        self.assertEqual("wagging", rover._tail())

    def test_attributes_with_double_underscore_prefixes_are_subject_to_name_mangling(self):
        rover = self.Dog()
        with self.assertRaises(): password = rover.__password()

        # But this still is!
        self.assertEqual(__, rover._Dog__password())

        # Name mangling exists to avoid name clash issues when subclassing.
        # It is not for providing effective access protection

