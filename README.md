# Mathematically Solving Pokémon Platinum
This GitHub repository, "Mathematically Solving Pokémon Platinum," focuses on solving a game where the outcome can be accurately predicted under perfect play conditions. Typically applied to abstract strategy games, this repository applies these principles to Pokémon Platinum, a game known for its complexity and variability. 

This Python Project represents an ambitious attempt to programmatically solve Pokémon Platinum, aiming to create a foolproof set of inputs that guarantee success, regardless of the game's inherent variability. This project extends the concept of playing a game without traditional senses by going beyond the visual and auditory aspects, instead relying solely on mathematical calculations to secure victory. Additionally, progress updates are provided, with Gym 1 and Gym 2 already completed as of specific dates. This project's unique approach takes inspiration from endeavors like "Can you Beat Pokemon FireRed while Blind and Deaf?" on YouTube but elevates the challenge by introducing mathematical precision to ensure success.

Pokémon Platinum involves a multitude of choices, random encounters, and strategies. However, this project aims to overcome these challenges by providing a predetermined sequence of inputs that ensures victory without relying on in-game feedback, RNG manipulation, or frame-perfect inputs.

The ultimate goal of this project is to showcase the programming process required to complete the finished project via YouTube video.
# Button Mapping
- It would be hard to understand the code without knowing what an individual button press does, below is to be used as a reference to understand these inputs.
  - WASD = Move Up, Move Left, Move Right, Move Down
  - F = Continue Button
  - X = Open Bag
  - Return = Start
  - R = Back Button
  - Turn = Two Tiles in Specified Direction

# Features
**Starter Pokémon Choice:**
- The project begins with the critical decision of selecting a starter Pokémon.
- Turtwig is ruled out due to its low-accuracy move (5% miss rate).
- Piplup initially appears to be the best choice, especially for the first gym, which is Rock-type.
- However, the project emphasizes the need for a starter capable of learning Rock Smash and Cut to progress.
- Chimchar is chosen because it can learn both moves and has Scratch (0% miss rate).

**Variability in Chimchar Stats:**
- Chimchar's stats can vary significantly depending on its Nature and IV combinations.
- The project considers the strongest possible Chimchar and the weakest possible Chimchar to establish boundaries for the calculations.
- By ensuring consistent outcomes with the weakest and strongest Chimchar, the project can predict results for all possible Chimchar variations.
- The project involves complex calculations, including critical hit probabilities, special attacks, damage calculations, etc.
- These calculations aim to provide precise predictions of in-game battles.

**Rival Battle and Restart Mechanism:**
- Acknowledgment of a ~4.25% chance of losing the first battle against the rival, which results in different experience gains.
- The project accounts for this loss as the game's progression will lead back to the house with the starter fully restored, ensuring it doesn't affect the overall outcome.

**grass_cycle:**
- The project recognizes the importance of grass encounters and their randomness.
- The Python script accounts for the chance of the player to either encounter a Pokemon or have nothing happen when walking (or spinning) on each grass tile.  
- The grass_cycle is essential to the run and is used as follows:
  - def grass_cycle_right():
    - time.sleep(1)
    - press_key('d', 17)
    - press_key('x')
    - press_key('a')
    - press_key('d')
    - press_key('x')
    - press_key('f', 7)
  - The sequence of inputs described above unfolds as follows: When the player steps onto a new grass tile, they are either thrust into a random encounter or remain on the tile for 17 seconds. Subsequently, the player presses the start menu button. In a battle encounter, this action has no effect, but in the overworld, it triggers the selection screen, allowing the dimension where the encounter takes place to utilize any move without affecting the state of the overworld game. The player runs away and then hits start again, causing both possible sequences of the event to sync back up, allowing the cycle to be repeated.

  

**rival_cycle:**
- The rival_cycle is a vital aspect of the gameplay strategy.
- Early in the game, the program cannot gain experience points (Exp) through random grass encounters before the first gym. To level up Chimchar, we need to acquire Exp from trainer battles.
- The rival_cycle strategy involves defeating one of the trainer's Pokémon and then intentionally losing to their second Pokémon.
- Our preferred trainer for this strategy is Barry, who has a level 9 Pidgey. We defeat Pidgey and intentionally lose to Barry's second Pokémon, Piplup.
- After fainting, Chimchar gains the Exp from the first Pokémon. We then restore Chimchar at a PokeCenter and return to the rival battle, allowing us to repeat this process until Chimchar reaches the desired level.
- The rival_cycle is a lengthy process, requiring a total of **285** iterations.
- On average, each rival_cycle takes about 18 minutes, although this duration can vary due to factors like learning new moves or leveling up.
- Completing **285 rival_cycles**, averaging 18 minutes each, results in a total of **85 hours and 30 minutes** of gameplay.
- After approximately 85.5 hours of consistently losing to Barry, Chimchar will have grown from Level 9 to 31.
- With Chimchar now at Level 31, it can comfortably take on the first gym.
- Below are the inputs for the rival_cycle:
  - def rival_cycle():
    - press_key('d', 5)
    - press_key('f', 2)
    - press_key('f', 2)
    - press_key('f', 15)
    - press_key('s')
    - press_key('w')
    - press_key('f')
    - press_key('s')
    - press_key('f', 20)
    - for _ in range(5):
      -  press_key('r', 5)
    - time.sleep(10)
    - press_key('s')
    - press_key('w')
    - press_key('f')
    - press_key('d')
    - for _ in range(10):
       - press_key('f', 14)
       - press_key('f')
       - press_key('w')
       - for _ in range(3):
           - press_key('f')
           - press_key('f', 14)
       - press_key('f')
       - press_key('s')
    - for _ in range(10):
       - press_key('f', 14)
       - press_key('f')
    - for _ in range(10):
       - press_key('f', 2)
       - turn('a')
       - for _ in range(7):
           - press_key('s')
       - turn('a')
       - for _ in range(5):
           - press_key('a')  # bottom left corner of poke center
    - turn('d')
    - for _ in range(5):
       - press_key('d')
    - turn('s', 5)
    - turn('a')
    - for _ in range(3):
       - press_key('a')
    - turn('w')
    - for _ in range(18):
       - press_key('w')
    - turn('d')
    - for _ in range(18):
       - press_key('d')  # one tile away from rival fight
     
# Currently Working On 
- Presently, I'm focused on the section of the game that occurs between gym_2 and gym_3.
- This phase is expected to be the most time-consuming since it involves Pokemon the Day Care Center.
- The Pokemon Day Care Center allows us to continually level up our Pokemon for the rest of the game in exchange for steps walked and in-game currency.
- Our current programming task involves leveling up Monfernape (the evolution of Chimchar) to reach Level 100 Infernape.
- Besides our starter Pokemon, we also receive a Togepi from Cynthia. We'll apply the same leveling process from Togepi to Level 100.
- Once we've programmatically leveled up these two Pokemon to their maximum level, gym_3 and beyond will be smoother.
  
# Notes
- gym_1 finished on 9/25/23
- gym_2 finished on 9/29/23
- gym_3 projected finish date 10/21/23

