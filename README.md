# Persian-Transliterator
A code transliterating the Persian script into the Roman Alphabet. Work in progress.

I would like the code to do this:


Input: هَر یه ساعَت یه قَطار به شَهر هَست.

Output: har ye sâ`at ye qatâr be šahr hast.


Right now it does this:


Input: هَر یه ساعَت یه قَطار به شَهر هَست

Output: hَr yeh sâ'َt yeh qَtâr bh šَhr hَst.


Eventually I would love the code to transliterate Persian text without vowel markers like this:


Input: هر یه ساعت یه قطار به شهر هست

Output: har ye sâ`at ye qatâr be šahr hast.


I'm guessing the way this could be done is:

1) First convert the non-vowel marked text to a vowel marked text:


Input: هر یه ساعت یه قطار به شهر هست

Output: هَر یه ساعَت یه قَطار به شَهر هَست


2) Convert the vowel marked text into Roman letters:

Input: هَر یه ساعَت یه قَطار به شَهر هَست

Output: har ye sâ`at ye qatâr be šahr hast

Currently, the code only does simple substitution, iterating over a list using a for loop.
It's faulty and complicated to make it work so In the future I would like to try to code a neural network to do the same.
