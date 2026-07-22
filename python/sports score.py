class Cricket:
    def __init__(self,player,score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Cricket - player:{self.__player}, score:{self.__score}")

    def play(self):
        print(f"{self.__player} hits a six!") 

    def get_score(self):
        return self.__score
    
    def set_score(self,new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"score updated to {self.__score}")
        else:
            print("score can not be negative")    

class Football:
    def __init__(self,player,score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Football - player:{self.__player}, score:{self.__score}")

    def play(self):
        print(f"{self.__player} scores a goal!") 

    def get_score(self):
        return self.__score

    def set_score(self,new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"score is updated to {self.__score}")
        else:
            print("score can not be negative")

cricket = Cricket("Babar Azam",78)
football = Football("neymar",1)

print("=== Sports Scoreboard ===\n")

for sports in (cricket , football):
    sports.info()
    sports.play()
    print()

print("--- Direct Change Attempt ---")
cricket.__score = 676
print(f"get_score() still shows: {cricket.get_score()}") 

print("\n--- Updating Scores ---")
cricket.set_score(120)
football.set_score(2)