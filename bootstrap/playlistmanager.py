class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print("Song added successfully!")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print("Song removed successfully!")
        else:
            print("Song Not Found!")

    def display(self):
        print("\nPlaylist Name:", self.name)
        print("Genre:", self.genre)
        if len(self.songs) == 0:
            print("Playlist is Empty!")
        else:
            print("\nSongs:")
            for i, song in enumerate(self.songs, start=1):
                print(i, ".", song)

    def __del__(self):
        print("\nPlaylist Deleted Successfully!")


name = input("Enter Playlist Name : ")
genre = input("Enter Genre : ")
playlist = Playlist(name, genre)

while True:
    print("\n1. Add Song")
    print("2. Remove Song")
    print("3. Display Playlist")
    print("4. Exit")
    
    choice = input("Enter Choice: ")

    if choice == "1":
        song = input("Enter Song Name : ")
        playlist.add_song(song)
    elif choice == "2":
        song = input("Enter Song Name to Remove : ")
        playlist.remove_song(song)
    elif choice == "3":
        playlist.display()
    elif choice == "4":
        print("Thank You!")
        del playlist
        break
    else:
        print("Invalid Choice")