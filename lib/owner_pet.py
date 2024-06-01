class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner 
        Pet.all.append(self)
        if owner:
            owner.add_pet(self)

        if pet_type not in Pet.PET_TYPES:
            raise Exception("invalid pet type")
        
        @property
        def owner(self):
            return self._owner
        
        @owner.setter
        def owner(self, owner):
            if owner is not None and not isinstance(owner, Owner):
                raise Exception("Owner has to be an instance of owner class")
            self._owner = owner 

class Owner:
    def __init__(self, name):
        self.name = name 
        self._pets = []

    def pets(self):
        return Pet.all  

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
             raise Exception("invalid pet")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)