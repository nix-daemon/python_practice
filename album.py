def make_album(artist_name, album_title, number_songs=None):
	album = {'artist_name': artist_name.title(), 'album_title': album_title.title()}
	if number_songs:
		album['number_songs'] = number_songs 
	return album 



for num in range(0,3):
	artist_name = input("Pleae enter an album name: ")
	album_title = input("Please enter the artist name: ")
	album = make_album(artist_name, album_title, number_songs=12)
	print(album)