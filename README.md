# Rules
1. Max 2 players
3. Each deck has total 60 cards
4. Each player has 1 deck
5. Each turn player draws 2 cards from their deck

## Decks
1. Main deck: 60
2. Counter deck: 30

## Classes
1. Pyromancer (unbeatable, you lose if you don't pick this)
- Concept
  - Produces "Ember" secondary resource by lighting things on fire. Building up enough Ember unlocks power breakpoints:
    - 0 Ember: No effect
    - 5 Ember: All spells do +2 damage to targets
    - 10 Ember: Single target spells may choose one an additional target
    - 20 Ember: The mana cost of all spells is reduced by half, rounding down.
  - Very weak early game before Ember producing engine is set up. Must balance spending Ember on abilities to avoid losing outright while trying to build up a large enough amount to combo off and win the game.

- Stats
  - Secondary Resource: Ember
  - Minion Commands: 0
  - HP: 100
  - Mana/Turn: 3

2. Necromancer (decidely less cool then Pyromancer)
- Concept
  - Class focuses on Minion summoning and control, as well as "on death" effects. Minions can be ressurected as zombies or sacrificed for other effects. Has cards that allow additional Minion attacks outside of the Minion Phase.

- Stats
  - Minion Commands: 3
  - HP: 100
  - Mana/Turn: 3

3. Arcanist (like, seriously?)
  - No spawns, draws a lot cards
4. Blood Mage (Nancy's class)
  - Trades enemy health for own health
5. Druid cuck
  - Health fountain

## Gameplay

### Board
Each player has a board consisting three zones: Minion, Structure, and Environment

1. Minion Zone:
Summoned minions are added to the Minion Zone. Minions are destroyed if they take damage equal to their hit point total. Damage persists across turns. This zone can hold an unlimited amount of minions. To save space, multiple copies of a minion can be placing a dice onto a representative card.

2. Structure Zone:
The structure zone can hold up to 6 structures. Structures are destroyed if they take damage equal to their hit point total.

3. Environment Zone:
Environment cards are added to that player's Environment Zone until their effects are completed.

### Turn
A turn consists of 3 phases: Resource, Minion, and Play

1. Resource Phase:
At the begining of the resource phase the player increases their total mana count by their Mana/Turn stat and draw 2 cards. Then, any secondary resources (such as Ember) gained from active spells or minions are calculated. When resolving secondary resource effects in this phase, use the state of the board at the start of the Resource Phase (i.e. resolving order does not matter).

2. Minion Phase:
During the Minion phase the player can command a number of minions equal to their Minion Command value to attack. Minions must attack opposing minions first, with targets chosen by the attacker. If the opposing player has no minions, attacks may be directed at either the opposing player directly or the opposing player's structures.

3. Play Phase:
During the play phase players can pay resource costs to play spell, structure, or environment cards any number of times.

### Win Conditions

A player loses the game when one of the following conditions is met:

1. The player loses all their hit points
2. The player must draw a card, but their deck is empty
3. The player resolves a spell or effect stating "This player loses the game."
4. The player's opponent resolves a spell or effect stating "Your opponent loses the game."