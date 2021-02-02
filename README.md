# Persian-Transliterator
A code transliterating the Persian script into the Roman Alphabet. Work in progress.

I would like the code to do this:


Input: هَر یه ساعَت یه قَطار به شَهر هَست.

Output: har ye sâ`at ye qatâr be šahr hast.


Right now it does this:


Input: هَر یه ساعَت یه قَطار به شَهر هَست

Output: har ih sâ'at ih qatâr be šahr hast.


Eventually I would love the code to transliterate Persian text without vowel markers like this:


Input: هر یه ساعت یه قطار به شهر هست

Output: har ye sâ`at ye qatâr be šahr hast.


Based on the following paper, it seems like building a neural net is the only way to go:

https://www.researchgate.net/publication/312564526_Persian_sentences_to_phoneme_sequences_conversion_based_on_recurrent_neural_networks

Currently, the code only does simple substitution, iterating over a list using a for loop.
It's faulty and complicated to make it work because of the many Persian reading rules and exceptions. Often a new substitution rule messes up a previous substitution rule.
