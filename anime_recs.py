import random
anime = open("Animes to Watch.txt")
anime_list= anime.readlines()
anime_list = list(map(lambda s: s.strip(), anime_list))
anime_list = anime_list[2:]
anime_boolean = True
while anime_boolean == True:
    rec = input("Would you like an anime recommended to you? (Enter Y/N): ")
    if rec == 'Y' or rec == 'y':
        anime_rec = random.choice(anime_list)
        print(anime_rec)
    elif rec == 'N' or rec =='n':
        print("ok, good bye")
        anime_boolean = False
    else: 
        print("enter Y or N")