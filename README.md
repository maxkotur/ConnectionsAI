# ConnectionsAI
AI/ML Project to solve the Connections NYT Game
https://www.nytimes.com/games/connections

The aim of the game is that, given 16 words, the player must find 4 groups of 4 that are somehow connected.
Guess the connection right and the category is revealed!

For example:

🟡 FACIAL FEATURES: CHEEK, EYE, MOUTH, NOSE

🟢 SYNONYMS FOR EAT: CHOW, GOBBLE, SCARF, WOLF

🔵 DOG BREEDS, INFORMALLY: LAB, PEKE, PIT, POM

🟣 MEMBERS OF A TRIO: AMIGO, KING, STOOGE, TENOR

Implementation:

I will be making an ML model to first understand and tokenize the 16 words using either Hugging Face or another type of transformer.
Then, once tokenized, I will be able to create a dataset which will include every word tokenized and predict from here.

Still have some doubts about giving the model the titles or if it should guess the titles.

The overall implementation is still a work in progress...

Will post if updated.

Here is how my initial implementation will be:

BERT or Transformer-based Models:

Fine-tune a pre-trained transformer model like BERT on the classification task.

Convert the input sentence or list of words into embeddings using the fine-tuned model.

Apply clustering algorithms or custom logic to group the embeddings into four clusters.
This would be K-Means where K=4. Once the groups have been connected correctly, try to find the
theme for bonus points.


