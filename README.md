# Mathematically Solving Pokémon Platinum
This GitHub repository, "Mathematically Solving Pokémon Platinum," focuses on the concept of solving a game, where the outcome can be accurately predicted under perfect play conditions. Typically applied to abstract strategy games, this repository applies these principles to Pokémon Platinum, a game known for its complexity and variability.

Pokémon Platinum involves a multitude of choices, random encounters, and strategies. However, this project aims to overcome these challenges by providing a predetermined sequence of inputs that ensures victory, all without relying on in-game feedback, RNG manipulation, or frame-perfect inputs.

This Python Project represents an ambitious attempt to programmatically solve Pokémon Platinum, aiming to create a foolproof set of inputs that guarantee success, regardless of the game's inherent variability. This project extends the concept of playing a game without traditional senses by going beyond the visual and auditory aspects, instead relying solely on mathematical calculations to secure victory. Additionally, progress updates are provided, with Gym 1 and Gym 2 already completed as of specific dates. This project's unique approach takes inspiration from endeavors like "Can you Beat Pokemon FireRed while Blind and Deaf?" on YouTube but elevates the challenge by introducing mathematical precision to ensure success.

# Features
**Starter Pokémon Choice:**
- The project begins with the critical decision of selecting a starter Pokémon.
- Turtwig is ruled out due to its low-accuracy move.
- Piplup initially appears to be the best choice, especially for the first gym, which is Rock-type.
- However, the project emphasizes the need for a starter capable of learning both Rock Smash and Cut to progress.
- Chimchar is chosen because it can learn both moves.

**Variability in Chimchar Stats:**
- Chimchar's stats can vary significantly depending on its Nature and IV combinations.
- The project considers the strongest possible Chimchar and the weakest possible Chimchar to establish boundaries for the calculations.
- By ensuring consistent outcomes with both the weakest and strongest Chimchar, the project can predict results for all possible Chimchar variations.

**Battle Calculations:**
- The project involves complex calculations, including critical hit probabilities, special attack, damage calculations, and more.
- These calculations aim to provide precise predictions of in-game battles.

**Rival Battle and Restart Mechanism:**
- Acknowledgment of a ~4.25 percent chance of losing the first battle against the rival, which results in different experience gains.
- The project accounts for this loss as the game's progression will lead back to the house with the starter fully restored, ensuring it doesn't affect the overall outcome.

**Grass Encounters:**
- The project recognizes the importance of grass encounters and the randomness associated with them.
- Presumably, the project will address strategies for dealing with these encounters and incorporate them into the overall solution.


# Notes
- gym_1 finished on 9/25/23
- gym_2 finished on 9/29/23


