class playlist:
    def __init__(self,name,genre):
        self.name = name
        self.genre = genre
        self.song = []
        print(f"playlist '{self.name}' ({self.genre}) is ready!")

    def add_song(self,song):
        self.song.append(song) 
        print(f"'{song}' is added to {self.name}.")

    def remove_song (self,song):
        if song in self.song:
            self.song.remove(song)
            print(f"'{song}' is removed.")
        else:
            print(f"'{song}' is not in the playlist.")   

    def display(self):
        print(f"\n---{self.name} ({self.genre})---")
        if self.song:
            for i in enumerate(self.song,1):
               print(f" {i}.{song} ")
        else:
            print("add some songs")

    def __del__(self):
        print(f"playlist '{self.name}' has been removed.")

my_playlist = playlist("honeybee","pop")
while True:
    print("\n1.add song 2.remove song 3.view playlist 4.delete and quit")
    choice = input("Enter your choice:")

    if choice == "1":
        song = input("Enter song name:")
        my_playlist.add_song(song)
    elif choice == "2":
        song = input("Enter a song to remove:")
        my_playlist.remove_song(song)
    elif choice == "3":
        my_playlist.display()
    elif choice == "4":
        del my_playlist
        break
    else:    
        print("Invalid choice.Enter 1,2,3 or 4.")