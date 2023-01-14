"""Create a function called add_songs().
It receives one or many tuples.
Each tuple consists of exactly two elements - the song's title in the first position and a list in the second position.
The list can consist of one, many, or no strings - each representing a line of the lyrics of the song.
The function collects the information and concatenates the lyrics for each song (each string on a different line).
If you are given the same song more than once, add the additional lyrics (if ones are given) to the lyrics of the song.
In the end, it should return a string for each song with its lyrics in the format:
"- {song_title}"
"{first_line_of_lyrics}"
"{second_line_of_lyrics}"
…
"{nth_line_of_lyrics}"
If there are no lyrics given for a song, return just its title in the format shown above.
For more clarification, see the examples below.
Input
•	There will be no input, just tuples passed to your function.
Output
•	Return the desired result as described above.
Constraints:
•	You will always have a song's name on the first position of the tuple.
"""


def add_songs(*args):
    songs = {}
    for name, lyric in args:
        if name not in songs:
            songs[name] = []
        songs[name].extend(lyric)

    result = []
    for name, lyric in songs.items():
        result.append(f"- {name}")
        if lyric:
            result.extend(lyric)
    return "\n".join(result)


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))
print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
