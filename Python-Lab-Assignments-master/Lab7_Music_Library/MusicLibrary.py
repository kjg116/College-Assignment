import random

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


class MusicLibrary:
    """Class creates a library and Generates a random Playlist"""

    def __init__(self, cd_list = []):
        self.cd_list = cd_list

    def add_item(self, cd_object):
        self.cd_list.append(cd_object)

    def remove_item(self, cd_object):
        self.cd_list.remove(cd_object)

    def get_list(self):
        return self.cd_list

    def generateList(self, number_of_songs):
        #empty list for for song_list
        song_list = []

        #while loop to check if songs were picked randomly and if it was picked or not
        while len(song_list) != number_of_songs:
            random_CD = random.choice(self.cd_list)
            songs_in_album = random_CD.get_songs()
            length_of_album = len(songs_in_album)
            random_pick = random.randrange(0, length_of_album)
            if songs_in_album[random_pick] not in song_list:
                song_list.append(songs_in_album[random_pick])

        return song_list


def main():

    album_one = open("X.txt", "r")
    album_two = open("Hysteria.txt", "r")

    album_list = []
    song_list = []

    for line in album_one:
        album_list.append(line)

    for each in album_list[2:]:
        song = Song(each, album_list[1], album_list[0])
        song_list.append(song)

    hysteria = CD(album_list[1], album_list[0], song_list)

    song_list = []
    album_list = []

    for line in album_two:
        album_list.append(line)

    for each in album_list[2:]:
        song = Song(each, album_list[1], album_list[0])
        song_list.append(song)

    X = CD(album_list[1], album_list[0], song_list)

    library = MusicLibrary([hysteria, X])

    playlist = library.generateList(5)

    cd_list = library.get_list()
    for each in cd_list:
        print(each)
        songlist = each.get_songs()
        for each in song_list:
            print("\t" + each.get_title())

    print("My playlist: ")

    for each in playlist:
        print(each)

    album_one.close()
    album_two.close()

main()