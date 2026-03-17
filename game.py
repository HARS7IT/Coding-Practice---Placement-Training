import random 

print("⚔  WELCOME TO THE PYTHON DUNGEON ⚔")


player_name = input("Enter Hero Name: ")
player_hp = 100
player_potions = 3

boss_name = "Shadow King"
boss_hp = 150

print(f"\nA wild {boss_name} appears! Get ready, {player_name}!")


while True:
    print("\n" + "="*30)
    print(f"❤  {player_name}: {player_hp} HP | 🧪 Potions: {player_potions}")
    print(f"👹 {boss_name}: {boss_hp} HP")
    print("="*30)

    print("ACTIONS: 1. Attack  2. Heal  3. Run")
    choice = input("Choose your move (1-3): ")


    if choice == '1':

        dmg = random.randint(10, 25)


        crit_chance = random.randint(1, 10)
        if crit_chance > 8: # 20% chance
            dmg *= 2 # Day 1 Operator (Multiply Assign)
            print(f"🔥 CRITICAL HIT! You dealt {dmg} damage!")
        else:
            print(f"⚔ You hit the boss for {dmg} damage.")

        boss_hp -= dmg # Update variable

    elif choice == '2':
        # Player Heals
        if player_potions > 0:
            heal_amount = random.randint(15, 30)
            player_hp += heal_amount
            player_potions -= 1
            print(f"✨ You drank a potion and recovered {heal_amount} HP.")
        else:
            print("❌ You are out of potions! You wasted a turn looking for one.")

    elif choice == '3':

        print("🏃 You ran away safely... Coward!")
        break # Exits the loop immediately

    else:

        print("Invalid move! You stumbled and lost your turn.")
        continue # Skips the rest of the loop and restarts


    if boss_hp <= 0:
        print(f"\n🏆 VICTORY! {boss_name} has been defeated!")
        break # Game Over - Win


    boss_dmg = random.randint(5, 20)
    player_hp -= boss_dmg
    print(f"💀 {boss_name} attacks you for {boss_dmg} damage!")

    # Check if Player Died
    if player_hp <= 0:
        print(f"\n🪦 GAME OVER... {player_name} has fallen.")
        break # Game Over - Loss