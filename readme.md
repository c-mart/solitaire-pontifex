This readme file assumes familiarity with Bruce Schnier's [description of Solitaire](https://www.schneier.com/cryptography/solitaire/)

## Card string representation
Cards can be represented as a list of numeric values (1 to 54 inclusive), or as a list of human-friendly string values. These string values contain two characters:
1. First letter of suit of card (e.g. C for clubs)
2. Rank of card (A for ace, number of numeric card, or first letter of face card e.g. Q for queen)

Jokers are represented as "JA" or "JB".

## Card unicode representation