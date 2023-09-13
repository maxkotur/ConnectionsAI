# ConnectionsAI
AI/ML Project to solve the Connections NYT Game
https://www.nytimes.com/games/connections

The games gives 16 words which must be grouped into 4 groups.
Each group would be related with a title which will be given once you get
that specific group.

For example:
🟡 FACIAL FEATURES: CHEEK, EYE, MOUTH, NOSE

🟢 SYNONYMS FOR EAT: CHOW, GOBBLE, SCARF, WOLF

🔵 DOG BREEDS, INFORMALLY: LAB, PEKE, PIT, POM

🟣 MEMBERS OF A TRIO: AMIGO, KING, STOOGE, TENOR

Implementation:
I will be making an ML model to first understand and tokenize the 16 words using either HUgging Face or another type of transformer.
Then, once tokenized, I will be able to create a dataset which will include every word tokenized and predict from here.

Still have some doubts about giving the model the titles or if it should guess the titles.

The overall implementation is still a work in progress...
Will post if updated.
