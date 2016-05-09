From https://www.schneier.com/cryptography/solitaire/

## Todo
- Build verbose output
- Refactor joker rotation to use a circular data structure rather than hard-coding special cases
- Use unicode representations of cards? https://en.wikipedia.org/wiki/Standard_52-card_deck#Text
- Every public function checks valid input? Or make functions not public?
- Accept key phrase

## Implementation notes
Deck has state, should be an object
We can represent state of deck as a list of numbers (using numbering system below) or as a list of short strings per card ("KH" king of hearts, "JB" is joker B)

Internally represent deck as numbers, but can print (output) as cards

Instantiate new deck, pass either numbers or cards

Cipher is keystream-based - this is a stream cipher

- Keystream is generated to match length of plaintext, keystream is letters or numbers representing same
- A keystream can be re-generated from a particular arrangement of a deck of cards
- Plaintext is added to keystream modulo 26 to encrypt
- Keystream is subtracted from ciphertext modulo 26 to decrypt

How does a deck of 54 cards generate a keystream with 26 elements?

## Key
The key is just a deck of cards in a given position
Create new key by shuffling?

## Cards to numbers
Assign numerical value for each card: 1 (Ace) through 13 (King)
For steps 4 and 5 below, both jokers are worth 53
Bridge order of suits:

- Clubs (face value)
- Diamonds (+13)
- Hearts (+26)
- Spades (+39)

## Generating Keystream
54-card deck is 54-element permutation
Jokers must be distinguishable from each other (designate them A and B)

Deck is circular array: first card follows the last card. So, moving a card past the end of the deck moves it back to the beginning.
IS the bottom the top?

Initialize deck to generate known key by arranging cards in key configuration

To produce one character of keystream:

1. Find A joker, advance it one position (move to card beneath it)
2. Find B joker, advance it two positions (move forward two cards)
3. Triple cut
  - Swap the cards above first joker in the deck, with the cards below second joker in the deck
  - If there are no cards above first joker or below second joker, treat as empty set and 'move' it anyway
4. Count cut
  - Observe bottom card, convert it to number n as described above
  - Count n cards down from top of the deck
  - Cut after the nth card but before the bottom card
  - Move cut cards to top of deck, leaving bottom card in place
5. Record output
  - Observe top card, convert it to number p as described above
  - Count down p cards from top of deck
  - Card *after* the pth card is the key output if it is not a joker, record its value
  - If key output is a joker, disregard and start over from step 1

Continue repeating these steps to generate a keystream the same length as the plaintext/ciphertext

## Keying the Deck
A key is a deck with cards in a particular order

## Opsec considerations
- Don't ever encrypt two messages with the same key, treat it as a one-time pad
- Solitaire is reversible so a deck that has been used to encrypt/decrypt a message allows for recovery of keystream