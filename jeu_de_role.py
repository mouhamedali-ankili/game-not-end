from random import randint
player_life_point = enemy_life_point = 50
portion = 3
lose = False
choose_potion = False
print("🎮 !!! DEBUT DU JEU !!! Amusez vous bien 🎮")
while True:
    if choose_potion == False:
        player_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
        if player_choice == "1":
            player_damage_point = randint(5,10)
            enemy_life_point -= player_damage_point
            print(f"Vous avez infligé {player_damage_point} points de dégats à l'ennemi ⚔")
        elif player_choice == "2":
            if portion > 0:
                choose_potion = True
                life_point = randint(15,50)
                player_life_point += life_point
                portion -= 1
                print(f"Vous avez recuperé {life_point} points de vie 💚 ({portion} 🧪 restants)")
            else:
                print("Il ne vous reste plus de potion 🧪")
                continue
        else:
            print("Choix innexistant")
            continue
    else:
        print("Vous passez votre tour...")
        choose_potion = False
    if enemy_life_point > 0:
            enemy_damage_point = randint(5,15)
            player_life_point -= enemy_damage_point
            if player_life_point > 0:
                print(f"L'ennemi vous a infligé {enemy_damage_point} points de dégats ⚔💘")
                print(f"Il vous reste {player_life_point} points de vie 💚")
                print(f"Il reste {enemy_life_point} points de vie 💚  à l'ennemi") 
            else:
                lose = True
                break
    else:
        break
    print("-"*100)
if lose:
    print(f"Il ne vous reste plus de points de vie contrairement à votre adversaire ({enemy_life_point} point{'s' if enemy_life_point > 1 else ''})")
    print("Gamme Over!!! Vous avez peru😓")
else:
    print(f"Vous avez GAGNE !!! 💪 avec {player_life_point} point{'s' if enemy_life_point > 1 else ''} de vie restants ")
print("🎮!!! FIN DU JEU !!!🎮")
