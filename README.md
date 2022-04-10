# NLP-clickbait-detection-using-bert

Click baiting involves encouraging the reading by using sensationalized headlines that often exaggerate facts, to entice readers to click on them. Click baits dissatisfy users because the article content does not match their expectations and violates journalistic codes of ethics. Therefore, detecting clickbait is of importance to provide the reader with more honest content on the web that does not waste their time.

Traditional clickbait-detection methods rely heavily on feature engineering and fail to distinguish clickbait from normal headlines precisely because of the limited information in headlines. This paper focuses on models that encapsulate the core ideas behind semantic understanding through contextual embeddings and provides an analysis of its effectiveness by comparing it against conventional hand-engineered feature settings.

To train and evaluate used models we used the [Webis clickbait Corpus 2017](https://webis.de/data/webis-clickbait-17.html). This corpus was intended to be used as a clickbait detection challenge in 2017 and comprises of a total of 38,517 Twitter posts from 27 major United States new publishers. In addition to the posts, information about the articles linked in the posts are included. The posts had been published between November 2016 and June 2017. To avoid publisher and topical biases, a maximum of ten posts per day and publisher were sampled. All posts were annotated on a 4-point scale.

# BERT
[BERT](https://arxiv.org/abs/1810.04805)’s model architecture is a multi-layer bidirectional transformer and tries to address the major limitation of standard language models that were originally undirected (left-to-right or right-to-left) [ 3]. Undirected models limit the choice of architectures that can be used during pre-training. For example, OpenAI GPT used a left-to-right architecture, where tokens can only attend to previous tokens in the self-attention layers of a Transformer. These restrictions are sup-optimal for sentence-level tasks, and even harmful when applying fine-tuning based approaches to token-level tasks such as question answering, where it is crucial to incorporate context from both directions. BERT improves fine-tuning based approaches by proposing Bidirectional Encoder Representations from Transformers. BERT alleviates the former undirected models by using a Masked **Language Model (MLM)** and **Next Sentence Prediction (NSP)**:
- MLM teaches BERT to understand relationships between words. MLM’s objective enables the representation
to fuse the left and the right context, which allows us to pre-train a deep bidirectional Transformer. In other
words, it tries to understand relationships between words.
- NSP teaches BERT to understand longer-term dependencies across sentences. The models concatenates two
masked sentences as inputs during pretraining. Sometimes they correspond to sentences that were next to each
other in the original text, sometimes not. The model then has to predict if the two sentences were following
each other or not sentences.

# Conclusion
When using BERT only on Tweet contents we achieve the following results:

|   |   |
|---|---|
| Precision | 0.920 |
| Recall | 0.489 |
| Accuracy | 0.870 |
| F1-score | 0.639 |


BERT is pre-trained on a massive corpus and is thus superior when it comes to context understanding.
