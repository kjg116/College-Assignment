from Song import *

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

        
