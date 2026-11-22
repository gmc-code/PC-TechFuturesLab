# playlist.py
# Lists: store, add, remove and loop through songs.

playlist = ["Song A", "Song B", "Song C"]

print("Your playlist:")
for song in playlist:
    print("-", song)

new_song = input("Add a song: ")
playlist.append(new_song)

remove_song = input("Remove a song: ")
if remove_song in playlist:
    playlist.remove(remove_song)
else:
    print(f"{remove_song} is not in the playlist.")

print()
print(f"Your playlist now has {len(playlist)} songs:")
for number, song in enumerate(playlist, start=1):
    print(f"{number}. {song}")

print(f"First song: {playlist[0]}")
print(f"Last song: {playlist[-1]}")
