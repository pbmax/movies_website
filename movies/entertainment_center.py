import fresh_tomatoes
import media

rushmore = media.Movie("Rushmore","A story about a precocious boy named Max", "https://upload.wikimedia.org/wikipedia/en/4/42/Rushmoreposter.png", "https://www.youtube.com/watch?v=GxCNDpvGyss", "Wes Anderson","1998", "Sardonic Comedy")

american_history_x = media.Movie("American History X", "A neo-nazi youth comes of age", "https://upload.wikimedia.org/wikipedia/en/0/0a/American_history_x_poster.jpg","https://www.youtube.com/watch?v=JsPW6Fj3BUI","Tony Kaye","1998","Drama")

captain_ron = media.Movie("Captain Ron","A family sails in the Carribean with Kurt Russell","https://upload.wikimedia.org/wikipedia/en/1/18/Captain_ron_poster.jpg","https://www.youtube.com/watch?v=VaTCVWnjcK8", "Thom Eberhardt","1992","Silly Comedy")

hackers = media.Movie("Hackers","A group of young hackers takes on the man in NYC", "https://upload.wikimedia.org/wikipedia/en/6/67/Hackersposter.jpg","https://www.youtube.com/watch?v=Rn2cf_wJ4f4","Iain Softley","1995","Thriller")

when_we_were_kings = media.Movie("When We Were Kings","A documentary about the Rumble In the Jungle boxing match between Muhammad Ali and George Formman","https://upload.wikimedia.org/wikipedia/en/0/0d/When_We_Were_Kings_DVD_Cover_art.jpg","https://www.youtube.com/watch?v=IfUHYUpmTFs","Leon Gast","1996","Documentary")

casablanca = media.Movie("Casablanca","Class story of Rick and Ilsa","https://upload.wikimedia.org/wikipedia/commons/b/b3/CasablancaPoster-Gold.jpg","https://www.youtube.com/watch?v=jQTWfGOv1JY","Michael Curtiz","1942","Drama")

movies = [rushmore,captain_ron,hackers,american_history_x,when_we_were_kings,casablanca]

fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.__doc__)
