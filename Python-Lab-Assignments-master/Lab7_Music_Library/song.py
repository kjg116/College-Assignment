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

    

    
        
    

    
        
