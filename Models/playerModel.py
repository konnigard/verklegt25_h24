class Player:
    # Hér geymum við upplýsingarnar upp úr playerUIClass sem við spurjum playerinn um
    def __init__(
        self,
        name: str,
        dob: str,
        address: str,
        phone_number: str,
        email: str,
        link: str,
        username: str,
    ) -> None:
        self.name = name
        self.dob = dob
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.link = link
        self.username = username