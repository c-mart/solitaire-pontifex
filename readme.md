This readme file assumes familiarity with Bruce Schnier's [Solitaire cipher](https://www.schneier.com/cryptography/solitaire/). Go learn about Solitaire there, then 

## Key representation
Key can be represented as a list of numeric card values (1 to 54 inclusive), or as a list of human-friendly string values. These string values contain two characters:
1. First letter of suit of card (e.g. C for clubs)
2. Rank of card (A for ace, number of numeric card, or first letter of face card e.g. Q for queen)

Jokers are represented as "JA" or "JB".

### Example Key Representations
Numeric:
`[17, 6, 7, 28, 27, 24, 42, 43, 15, 3, 29, 20, 11, 1, 13, 49, 22, 14, 52, 53, 10, 34, 30, 51, 23, 32, 46, 48, 40, 44, 25, 54, 39, 4, 37, 45, 50, 12, 5, 8, 18, 31, 9, 35, 47, 19, 38, 36, 21, 2, 26, 33, 16, 41]`

String:
`['H3', 'DK', 'S9', 'C10', 'C8', 'D6', 'C7', 'C6', 'S4', 'S3', 'D2', 'S2', 'SK', 'S7', 'CJ', 'JB', 'DA', 'D9', 'HA', 'CA', 'H7', 'HQ', 'D7', 'HJ', 'SQ', 'D4', 'C5', 'CK', 'D3', 'S10', 'S5', 'C2', 'H8', 'SA', 'S6', 'H6', 'H10', 'DJ', 'H5', 'JA', 'H4', 'CQ', 'DQ', 'S8', 'H2', 'C3', 'D10', 'D5', 'H9', 'C4', 'SJ', 'D8', 'HK', 'C9']`

## Card unicode representation
????