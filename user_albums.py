def make_album(artist_name, album_title, number_songs=None):
	album = {'artist_name': artist_name.title(), 'album_title': album_title.title()}
	if number_songs:
		album['number_songs'] = number_songs 
	return album 

while True:
	artist_name = input("Pleae enter an album name: ")
	if artist_name == 'q':
		break
	
	album_title = input("Please enter the artist name: ")
	if album_title == 'q':
		break
	album = make_album(artist_name, album_title, number_songs=12)
	print(album)