# Create a list of songs
# Select one at random
# Print the song

import random

def randSong():
  titles = ["4th Breaker", "Neverita", "Heartless", "In the End", "Ride", "Get Into It"]
  
  randIndex = random.randint(0, len(titles) - 1) # prints based on index
  
  print(titles[randIndex])
  
  # print(random.choice(songs)) This Works

songs = [] 

def appendSong():
  # Create a program that repeatedly asks a user for a song title and adds it to a list.
  # Prompt the user for a song title
  # Get the user's input
  # Add song into a list
  # Print that list
  # Terminate?
  print("When you are done adding songs, type Quit")
  while True:
    song = input("Enter a song title: ")
    if song.title() == "Quit":
      print("This is your final song list:")
      print(songs)
      break
    if song.title() in songs: #repeat song; title=proper method
      #default last
      print("The song is already in the list!")
    else:
      songs.append(song.title())
      print(songs)

appendSong()