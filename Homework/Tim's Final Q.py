'''Make a class, you must use two of the data structures. 
Make a playlist that stores all the songs, 
and plays them in the order they were put in. 
Use a hashmap to make the playlist, then put every song into the queue.
'''
from ArrayQueue import *

class Song:

    def __init__(self):
        self.dict = {}
        self.q = ArrayQueue()

    def add_song(self,song):
        if song not in self.dict:
            self.dict[song] = (song, 1)
            self.q.enqueue(song)

        else:
            self.dict[song] = (song, self.dict[song][1] + 1)
            self.q.enqueue(song)


    def play_song(self):
        self.dict[self.q.first()] = (self.dict[self.q.first()][0],self.dict[self.q.first()][1] - 1 )

        return self.q.dequeue()





