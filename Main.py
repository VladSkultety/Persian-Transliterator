#coding: utf-8 -*-

PersianText = open("PersianText.txt", "r")

InternalText = PersianText.read()

MyList = [

#Diacritical marks
('َ', 'a'),
('ِ', 'e'),
('ُ', 'o'),
('ّ', 'e'),
('اً','ân'),
#Farsi letters to latin transcription
('ء','\''),
('أ','\''),
('ئ','\''),
('ؤ','\''),
('ا','â'),('آ','â'),('اَ','a'),('اَِ','e'),('اُ','o'),#problem
('ب','b'),
('پ','p'),
('ت','t'),
('ث','s'),
('ج','dž'),
('چ','č'),
('ح','h'),
('خ','kh'),
('د','d'),
('ذ','z'),
('ر','r'),
('ز','z'),
('ژ','ž'),
('س','s'),
('ش','š'),
('ص','s'),
('ض','z'),
('ط','t'),
('ظ','z'),
('ع','\''),
('عَ','\'a'),#problem
('غ','g'),
('ف','f'),
('ق','q'),
('ک','k'),
('گ','g'),
('ل','l'),
('م','m'),
('ن','n'),
('و','w'),
('ه','h'),
('ی','ye'),
('ي','i'),
#numbers
('۰','0'),('۱','1'),('۲','2'),('۳','3'),('۴','4'),
('۵','5'),('۶','6'),('۷','7'),('۸','8'),('۹','9'),
#Interpunction marks
('؟','?'),
('،',','),
('—','-'),
#Post-Persian to Latin conversion initial modifications
('thâm','tâm'),
('âw','u'),
('yeâ','iyâ'),
('âye','ây'),
(' i ',' ye '),('ye','i'),
('ow','ō'),
('rw','ru'),
('ruâ','rvâ'),
#Words ending with 'h'
#'h' before a fullstop
('mh.','me.'),
('rh.','re.'),
('bh.','be.'),
('dh.','de.'),
('gh.','ge.'),
('zh.','ze.'),
('th.','te.'),
('nh.','ne.'),
('kh.','ke.'),
('čh.','če.'),
('šh.','še.'),
('ah.','ae.'),
('eh.','e.'),
('yeh.','ye.'),
('\'h.','\'e.'),
#'h' at the end of a word
('mh ','me '),
('rh ','re '),
('bh ','be '),
('dh ','de '),
('gh ','ge '),
('zh ','ze '),
('th ','te '),
('nh ','ne '),
('kh ','ke '),
('čh ','če '),
('šh ','še '),
('ah ','ae '),
('eh ','e '),
('yeh ','ye '),
('\'h ','\'e '),
#'h' before a comma
('mh,','me,'),
('rh,','re,'),
('bh,','be,'),
('dh,','de,'),
('gh,','ge,'),
('zh,','ze,'),
('th,','te,'),
('nh,','ne,'),
('kh,','ke,'),
('čh,','če,'),
('šh,','še,'),
('ah,','ae,'),
('eh,','e,'),
('yeh,','ye,'),
('\'h,','\'e,'),
#'h' before a question mark
('mh?','me?'),
('rh?','re?'),
('bh?','be?'),
('dh?','de?'),
('gh?','ge?'),
('zh?','ze?'),
('th?','te?'),
('nh?','ne?'),
('kh?','ke?'),
('čh?','če?'),
('šh?','še?'),
('ah?','ae?'),
('eh?','e?'),
('yeh?','ye?'),
('\'h?','\'e?'),
#'h' before a exclamation mark
('mh!','me!'),
('rh!','re!'),
('bh!','be!'),
('dh!','de!'),
('gh!','ge!'),
('zh!','ze!'),
('th!','te!'),
('nh!','ne!'),
('kh!','ke!'),
('čh!','če!'),
('šh!','še!'),
('ah!','ae!'),
('eh!','e!'),
('yeh!','ye!'),
('\'h!','\'e!'),
#mix improvements
('awâ','avâ'),
('kew','khu'),('kea','kha'),('key','khiy'),('khwâ','khâ'),
('âa','a'),
('âe','e'),
('âi','i'),('‌khi','‌khâi'),
('âo','o'),
('iâ','yâ'),
('ie','âye'),
('ii','iye'),
('w','u'),
#'u' conversion into 'va'
(' u ',' va '),
('u ','va '),
(',u ',',va '),
#further improvements
('uie','uye'),
('uâ','u'),
('khuh','khâh'),
('ee','e'),
('ae','e'),
('eui','evi'),
('iue','ive'),
('iye','iyâi'),
('iye','iyâi'),
(' ua',' va'),
('ى','y'),
#Full words
('keili','kheili'),(' sobe ',' sobh '),(' čye',' čiye')
]

for k,v in MyList:
    InternalText = InternalText.replace(k, v)

PersianText.close()

#Write PersianText.txt file with transliterated Persian. #Need to close and open
#PersianText again.

WriteFile = open("PersianText.txt", "w")
WriteFile.write(InternalText)
WriteFile.close()
