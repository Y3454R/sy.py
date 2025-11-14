from collections import Counter, defaultdict


def space_tokenize(text: str) -> list[str]:
    """Splits a string into a list of words (tokens).

    Splits text on space.

    Args:
        text: The input text.

    Returns:
        A list of tokens. Returns empty list if text is empty or all spaces.
    """
    tokens = text.split(" ")
    return tokens


def generate_ngrams(text: str, n: int) -> list[tuple[str]]:
    """Generates n-grams from a given text.

    Args:
        text: The input text string.
        n: The size of the n-grams (e.g., 2 for bigrams, 3 for trigrams).

    Returns:
        A list of n-grams, each represented as a list of tokens.
    """

    # Tokenize text.
    tokens = space_tokenize(text)

    # Construct the list of n-grams.
    ngrams = []

    # my code:
    for i in range(len(tokens) - n + 1):
        token = tuple(tokens[i : i + n])
        # print(token)
        ngrams.append(token)

    return ngrams


def get_ngram_counts(dataset: list[str], n: int) -> dict[str, Counter]:
    """Computes the n-gram counts from a dataset.

    This function takes a list of text strings (paragraphs or sentences) as
    input, constructs n-grams from each text, and creates a dictionary where:

    * Keys represent n-1 token long contexts `context`.
    * Values are a Counter object `counts` such that `counts[next_token]` is the
      count of `next_token` following `context`.

    Args:
        dataset: The list of text strings in the dataset.
        n: The size of the n-grams to generate (e.g., 2 for bigrams, 3 for
            trigrams).

    Returns:
        A dictionary where keys are (n-1)-token contexts and values are Counter
        objects storing the counts of each next token for that context.

    """

    # Define the dictionary as a defaultdict that is automatically initialized
    # with an empty Counter object. This allows you to access and set the value
    # of ngram_counts[context][next_token] without initializing
    # ngram_counts[context] or ngram_counts[context][next_token] first.
    # Reference
    # https://docs.python.org/3/library/collections.html#collections.Counter and
    # https://docs.python.org/3/library/collections.html#collections.defaultdict
    # for more information on how to use defaultdict and Counter types.
    ngram_counts = defaultdict(Counter)

    for paragraph in dataset:
        # print(paragraph)
        ngrams = generate_ngrams(paragraph, n)
        # print(ngrams)
        for ngram in ngrams:
            context = " ".join(ngram[:-1])
            print(f'context: "{context}"')
            next_token = ngram[-1]
            ngram_counts[context][next_token] += 1

    return dict(ngram_counts)


# Example usage of the function.
example_data = [
    "This is an example sentence.",
    # "Another example sentence.",
    # "Split a sentence.",
]
ngram_counts = get_ngram_counts(example_data, 2)

# Print the bigram counts dictionary for the dataset consisting of the
# three example sentences.
print("Bigram counts dictionary:\n")
print("{")
for context, counter in ngram_counts.items():
    print(f"  '{context}': {counter},")
print("}")
