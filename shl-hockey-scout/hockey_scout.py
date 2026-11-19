class SHLhockeyscout:
    def __init__(self, data):
        self.data = data


    def get_players(self,):
        return self.data[0]["stats"]
    

    def find_player(self, player_name):
        for player in self.get_players():
            if player_name == player["info"]["fullname"]:

            

        
