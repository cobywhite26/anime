import random
anime = open("Animes to Watch.txt")
anime_list= anime.readlines()
anime_list = list(map(lambda s: s.strip(), anime_list))
del anime_list[0]
anime_list.remove('')
anime_rec = random.choice(anime_list)
print(anime_rec)