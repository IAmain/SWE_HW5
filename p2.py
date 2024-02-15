import random

treasure_items = ['gold coins', 'diamond', 'sword', 'scroll', 'dagger', 'emerald']
treasure_chest = random.sample(treasure_items, k=len(treasure_items)) 

bank_account = 500

wager = 50

print("Welcome to Jack the Pirate's Chest! Your starting bank account is", bank_account)

while bank_account > 0:
  print("\nRound starting...")
  print("Current bank account:", bank_account)

  # Player's wagers 
  bank_account -= wager

  # Randomly draw the treasure
  prize = random.choice(treasure_chest)
  print("You drew:", prize)

  # 30% chance to win the wager back
  if random.random() <= 0.3:
    bank_account += wager
    print("Lucky draw! You've won your wager back.")

  # 10% chance to win double
  if random.random() <= 0.1: 
    bank_account += 2 * wager
    print("Jackpot! You've won double your wager.")

print("\nGame over, your bank account is now", bank_account)