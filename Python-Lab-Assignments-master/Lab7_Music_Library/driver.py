import random
class CD:
    def __init__(self, album, artist, song_list = []):
        self.set_album(album)
        self.set_artist(artist)
        self.set_song_list(song_list)
        return

    #Removes beginning and trailing whitespace characters in album and
    #stores the attribute
    def set_album(self, album):
        self._album = album.strip()
        return

    #Removes beginning and trailing whitespace characters, capitalizes
    #the first letter of each name or initial, and stores the attribute
    def set_artist(self, artist):
        artist = artist.strip()
        names = artist.split()
        artist = ''
        for each_name in names:
            artist += each_name.capitalize()
            artist += ' '
        artist.strip()
        self._artist = artist
        return

    #Adds each song in the list, but checks to see that the album information
    #is the same first
    def set_song_list(self, song_list):
        self._songs = []
        for each_song in song_list:
            self.add_song(each_song)
        return

    def add_song(self, a_song):
        #if a_song is an instance of the Song class, just append it to the
        #list
        if isinstance(a_song, Song):
            #The song should have the name of the CD as the name of the album
            if a_song.get_album() == self._album:
                self._songs.append(a_song)
            #If the song doesn't have the same title, it doesn't belong
            else:
                raise Exception (a_song.get_title() + " is not on " + self._album + " album.")
        #if a_song is just a song title, create an instance of the Song
        #class and set the title.  Leave the other fields blank
        else:
            new_song = Song()
            new_song.set_title(a_song)
        return

    #Removes the first instance of a_song from the list of songs
    def remove_song(self, a_song):
        self._songs.remove(a_song)

    def get_songs(self):
        return self._songs

    def __str__(self):
        return '\"' + self._album + '\" by ' + self._artist
class Song:
    def __init__(self, title = None, album = None, artist = None, category = None):
        self.set_title(title)
        self.set_album(album)
        self.set_artist(artist)
        self.set_category(category)
        return

    #Removes beginning and trailing whitespace characters in title and
    #stores the attribute
    def set_title(self, title):
        if title != None:
            title = title.strip()
        self._title = title
        return

    #Removes beginning and trailing whitespace characters in album and
    #stores the attribute
    def set_album(self, album):
        if album != None:
            album = album.strip()
        self._album = album
        return

    #Removes beginning and trailing whitespace characters, capitalizes
    #the first letter of each name or initial, and stores the attribute
    def set_artist(self, artist):
        if artist != None:
            artist = artist.strip()
            names = artist.split()
            artist = ''
            for each_name in names:
                artist += each_name.capitalize()
                artist += ' '
            artist = artist.strip()
        self._artist = artist
        return

    #Removes beginning and trailing whitespace characters and
    #stores attribute
    def set_category(self, category):
        if category != None:
            category = category.strip()
        self._category = category
        return

    #Each getter returns the desired attribute
    def get_title(self):
        return self._title

    def get_album(self):
        return self._album

    def get_artist(self):
        return self._artist

    def get_category(self):
        return self._category

    #Determines if two songs are the same song (have all of the same information)
    def __eq__(self, other):
        same = True
        if self._title != other._title:
            same = False
        elif self._artist != other._artist:
            same = False
        elif self._album != other._album:
            same = False
        #Not checking category since some songs could fall in more than one
        return same

    def __str__(self):
        return '\"' + self._title + '\" by ' + self._artist + ' from \"' + self._album + '\"'
class MusicLibrary:
    """Class creates a library and Generates a random Playlist"""

    def __init__(self):
        self.item = []
        return

    def add_item(self, item):
        self.item.append(item)
        return

    def remove_item(self, item):
        self.item.remove(item)
        return

    def get_list(self):
        return self.item

    def generate_playlist(self, number_songs):
         #empty list for for song_list
        list = []

        #For loop to choose random songs for playlist
        for each in range(number_songs):
            num = random.randint(0, len(self.item) - 1)
            num2 = random.randint(0, len(self.item[num].get_songs()) - 1)
            rand_song = self.item[num].get_songs()[num2]
            list.append(rand_song)

        return list

#Kelcy Gooch and Clayton Hudspeth
#kjg116 and ch1518
#Class Section 01

def main():

    list1 = []
    album1 = open("X.txt", "r")
    album2 = open("Hysteria.txt", "r")

#Creates first CD
    counter = 0
    for each in album1:
        counter += 1
        each = each.strip()
        if counter == 1:
            artist = each
        elif counter == 2:
            album = each
        else:
           list1.append(Song(each, album, artist))

    X = CD(album, artist, list1)

#Creates second CD
    list2 =[]
    count = 0
    for each in album2:
        count += 1
        each = each.strip()
        if count == 1:
            artist2 = each
        elif count == 2:
            album2 = each
        else:
           list2.append(Song(each, album2, artist2))

    Hysteria = CD(album2, artist2, list2)

#Puts CD into MusicLibrary
    library = MusicLibrary()
    library.add_item(X)
    library.add_item(Hysteria)
    rand_list = library.generate_playlist(5)

    for all in library.get_list():
        print(all)
        for each in all.get_songs():
            print('\t', each.get_title())

#Creates random Playlist
    print("My Playlist:")
    choice = 0
    for i in rand_list:
        choice += 1
        print(rand_list[choice-1])



main()


