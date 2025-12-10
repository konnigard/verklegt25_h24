class Player:
    #Hér geymum við upplýsingarnar upp úr playerUIClass sem við spurjum playerinn um
    def __init__(self, name: str, dob: str, address: str, phone_number: str, email: str, link: str, username: str, teamName: str) -> None:
        self.name: str = name
        self.dob: str = dob
        self.address: str = address
        self.phone_number: str = phone_number
        self.email: str = email
        self.link: str = link
        self.username: str = username
        self.teamName: str = teamName

    def __repr__(self):
        return f"Player: {self.name} (@{self.username}) - Team: {self.teamName}"
