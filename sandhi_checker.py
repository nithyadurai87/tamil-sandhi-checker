# This Python file uses the following encoding: utf-8
#/usr/bin/python3
#
# Copyright (C) 2018 Nithya Duraisamy <nithyadurai87@gmail.com>
# Tamil sandhi checker - validate and fix list of Sandhi errors in Tamil text

import tamil
import collections
import codecs
import os
import sys

#http://www.tamilvu.org/courses/degree/c021/c0214/html/c0214661.htm
BASE_DIRECTORY = os.path.split(__file__)[0]

tamil_path = os.path.join(BASE_DIRECTORY,"all-tamil-nouns.txt")
noun_file = codecs.open(tamil_path,"r","UTF-8")
noun_list = noun_file.read().strip().split()

#a =u"அங்குக் கண்டான் அந்த பையன். எத்தனை பழங்கள்?  கண்டவாறு சொன்னான், ஐந்து சிறுவர்கள், கத்தியோடு  நின்றான்," \
#   u"கத்திகொண்டு குத்தினான், வீட்டிலிருந்து  சென்றான், கை குழந்தை,  கற்று கொடுத்தான், குரங்கு குட்டி, விறகு கடை, பொது பணி,  தேர்வு  கட்டணம், கனியை தின்றான்," \
#   u"எனக்கு கொடு, வீட்டினின்று வெளியேறினான், வர சொன்னான், என்னுடைய புத்தகம், எனது புத்தகம், குறிஞ்சி தலைவன், தேங்காய் சட்னி,  தயிர் குடம், தீரா சிக்கல், மரம் தலைவன்."
mei_letters = tamil.utf8.mei_letters
uyir_letters = tamil.utf8.uyir_letters
kuril_letters = tamil.utf8.kuril_letters
nedil_letters = tamil.utf8.nedil_letters
agaram_letters = tamil.utf8.agaram_letters
uyirmei_letters = tamil.utf8.uyirmei_letters
vallinam_letters = tamil.utf8.vallinam_letters
mellinam_letters = tamil.utf8.mellinam_letters
special_chars=[u'.',u';',u',',u':',u'?']
one_letter_words=[u'கை',u'தீ',u'தை',u'பூ',u'மை']
suttu_vina=[u'அ',u'ஆ',u'இ',u'ஈ',u'எ',u'யா']
suttu_vina_not=[u'அது',u'இது',u'எது',u'யாது',u'அவை',u'இவை',u'எவை',u'அன்று',u'இன்று',u'என்று',u'அத்தனை',u'இத்தனை',u'எத்தனை',u'அவ்வளவு',u'இவ்வளவு',u'எவ்வளவு',u'அவ்வாறு',u'இவ்வாறு',u'எவ்வாறு']
numerals=[u'ஒன்று',u'இரண்டு',u'மூன்று',u'நான்கு',u'ஐந்து',u'ஆறு',u'நூறு',u'ஏழு',u'ஒன்பது',u'ஒரு',u'இரு',u'அறு',u'எழு']
viyankol=[u'கற்க',u'நில்',u'கவனி',u'செல்',u'செல்க',u'மன்னிய',u'வெல்க',u'செப்பும்',u'வினாவும்',u'வாழ்க',u'ஓம்பல்',u'அஞ்சாமை',u'வாழி',u'வீழ்க',u'ஒழிக',u'வருக',u'உண்க',u'அருள்க',u'கருணைபுரிக',u'வருக',u'வாழிய',
u'வாழியர்',u'வாரற்க',u'கூறற்க',u'செல்லற்க',u'வாரல்',u'செல்லல்',u'பகரேல்']

def safe_splitMeiUyir(arg):
    try:
        # when uyir letters are passed to splitMeiUyir function it will throw an IndexError
        rval = tamil.utf8.splitMeiUyir(arg)
        if len(rval) == 1:
            return (rval,u'')
        return rval
    except IndexError as idxerr:
        pass
    except ValueError as valerr:
        # non tamil letters cannot be split - e.g. '26வது'
        pass
    return (u'',u'')

class Results:
    # class contains results of 'check_sandhi' method
    ErrorLog = collections.namedtuple('ErrorLog',['rule','description','word']) #description of error
    def __init__(self):
        self.errors = [] #list of ErrorLog object

    def add(self,word,rule,descr):
        elog = Results.ErrorLog( rule, descr, word )
        self.errors.append(elog)

    @property
    def counter(self):
        return len(self.errors)

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        summary_list = [u"%s -> (%s, %s),\n"%(err.word,err.rule,err.description) for err in self.errors]
        return u"".join(summary_list)

def check_sandhi(words):
    if not isinstance(words,list):
        words = tamil.utf8.get_words(words)

    result = Results()
    fixed_list=[]
    prev_word_stack = [u'']
    for counter,word in enumerate(words):
        prev_word = prev_word_stack.pop()
        prev_word_stack.append(word)
        next_word = (counter+1) < len(words) and words[counter+1] or u' '
    # வல்லினம் மிகா இடங்கள்
        if tamil.utf8.get_letters(word)[-1] in special_chars:
            fixed_list.append(word)
            print(u"மிகா - விதி 1 - " + word)
            result.add(word,u'விதி 1',u'மிகா')
            continue

    # வல்லினம் மிகா சுட்டு, வினா அடியாகத் தோன்றிய சொற்கள் - எத்தனை பழங்கள்?
    # ‘அஃறிணைப் பன்மை’ - பல பசு
        if word in suttu_vina_not:
            fixed_list.append(word)
            print(u"மிகா - விதி 2 - " + word)
            result.add(word,u'விதி 2',u'மிகா')
            continue

    # வல்லினம் மிகா வந்த, கண்ட, சொன்ன, வரும் என்பன  போன்ற பெயரெச்சங்களோடு படி, ஆறு என்னும் சொற்கள்- கண்டவாறு சொன்னான்
        if (tamil.utf8.get_letters(word)[0]) in [u'வ',u'க',u'சொ']:
            if (tamil.utf8.get_letters(word)[-1]) in [u'டி',u'று']:
                fixed_list.append(word)
                print(u"மிகா - விதி 3 - " + word)
                result.add(word,u'விதி 3',u'மிகா')
                continue

    # வல்லினம் மிகா எண்ணுப்பெயர்கள் - ஐந்து சிறுவர்கள்
        if word in numerals:
            fixed_list.append(word)
            print(u"மிகா - விதி 4 - " + word)
            result.add(word,u'விதி 4',u'மிகா')
            continue

    # ஓர் எழுத்துச் சொற்கள் முன் வல்லினம் மிகல்
    # 6.1.2 - கை குழந்தை

        if len(tamil.utf8.get_letters(word)) == 1:
            if  word in one_letter_words:
                first_char_of_next_word = (next_word[0])
                mei_of_first_char_of_next_word = safe_splitMeiUyir(first_char_of_next_word)[0]
                fixed_list.append(word + mei_of_first_char_of_next_word)
                print(u"மிகும் - விதி 1 - " + word + mei_of_first_char_of_next_word)
                result.add(word,u'விதி 1',u'மிகும்')
                continue

        # வல்லினம் மிகா ஒடு & ஓடு என உயிர் ஈறு கொண்டவை - கத்தியோடு நின்றான்
        if (safe_splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) in [u'ஒ',u'ஓ']:
            if (tamil.utf8.get_letters(word)[-1]) == u'டு':
                fixed_list.append(word)
                print(u"மிகா - விதி 5 - " + word)
                result.add(word,u'விதி 5',u'மிகா')
                continue

    # வல்லினம் மிகா ‘கொண்டு’ என்னும் சொல்லுருபு -கத்திகொண்டு குத்தினான்
        if u''.join(tamil.utf8.get_letters(word)[-3:]) ==  u'கொண்டு':
            fixed_list.append(word)
            print(u"மிகா - விதி 6 - " + word)
            result.add(word,u'விதி 6',u"மிகா")
            continue

    # வல்லினம் மிகா இல் என்பதோடு இருந்து என்னும்  சொல்லுருபு - வீட்டிலிருந்து சென்றான்
        if u''.join(tamil.utf8.get_letters(word)[-4:]) == u'லிருந்து':
            fixed_list.append(word)
            print(u"மிகா - விதி 7 - " + word)
            result.add(word,u'விதி 7',u"மிகா")
            continue

    # வல்லினம் மிகா இன் என்பதோடு நின்று என்னும் சொல்லுருபு - வீட்டினின்று வெளியேறினான்
        if u''.join(tamil.utf8.get_letters(word)[-3:]) == u'னின்று':
            fixed_list.append(word)
            print(u"மிகா - விதி 8 - " + word)
            result.add(word,u'விதி 8',u"மிகா")
            continue

    # வல்லினம் மிகா ஆறாம் வேற்றுமைக்கு உரிய அது - எனது புத்தகம்
        if (safe_splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) == u'அ':
            if (tamil.utf8.get_letters(word)[-1]) == u'து':
                fixed_list.append(word)
                print(u"மிகா - விதி 9 - " + word)
                result.add(word,u'விதி 9',u'மிகா')
                continue

    # வல்லினம் மிகா ‘உடைய’ என்னும் சொல்லுருபு- என்னுடைய புத்தகம்
        if u''.join(tamil.utf8.get_letters(word)[-2:]) == u'டைய':
            if (safe_splitMeiUyir(tamil.utf8.get_letters(word)[-3])[1]) == u'உ':
                fixed_list.append(word)
                print(u"மிகா - விதி 10 - " + word)
                result.add(word,u'விதி 10',u'மிகா')
                continue
        # வல்லினம் மிகா மென்தொடர்க் குற்றியலுகர  வினையெச்சங்கள் - ண்டு, ந்து, ன்று என முடியும்
        # கண்டு பேசினார்
        if u''.join(tamil.utf8.get_letters(word)[-2:]) == u'ண்டு':
            fixed_list.append(word)
            print(u"மிகா - Rule11 - " + word)
            counter = counter+1
            result.add(word,u'விதி 11',u'மிகா')
            continue

        # வந்து சென்றான்
        if ''.join(tamil.utf8.get_letters(word)[-2:]) == u'ந்து':
            fixed_list.append(word)
            print(u"மிகா - Rule12 - " + word)
            counter = counter+1
            result.add(word,u'விதி 12',u'மிகா')
            continue

        # கொன்று குவித்தான்
        if u''.join(tamil.utf8.get_letters(word)[-2:]) == u'ன்று':
            fixed_list.append(word)
            print(u"மிகா - Rule13 - " + word)
            counter = counter+1
            result.add(word,u'விதி 13',u'மிகா')
            continue

        # வல்லினம் மிகா இடைத்தொடர்க் குற்றியலுகர  வினையெச்சங்கள் - ய்து என முடியும்
        # செய்து தந்தான்
        if u''.join(tamil.utf8.get_letters(word)[-2:]) == u'ய்து':
            fixed_list.append(word)
            print(u"மிகா - Rule14 - " + word)
            result.add(word,u'விதி 14',u'மிகா')
            counter = counter+1
            continue

        # வல்லினம் மிகா மற்ற பெயரெச்சங்கள் - ஆத, இய, ஐய,ற்ற,ல்ல, ட்ட கின்ற, உம் ஆகிய விகுதிகள் பெற்று முடியும்
        # அழியாத கல்வி
        if u''.join(tamil.utf8.get_letters(word)[-1:]) == u'த':
            if (safe_splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) == u'ஆ':
                fixed_list.append(word)
                print(u"மிகா - Rule15 - " + word)
                result.add(word,u'விதி 15',u'மிகா')
                counter = counter+1
                continue

        # பெரிய பெண்
        if u''.join(tamil.utf8.get_letters(word)[-1:]) == u'ய':
            if (safe_splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) == u'இ':
                fixed_list.append(word)
                print(u"மிகா - Rule16 - " + word)
                counter = counter+1
                result.add(word,u'விதி 16',u'மிகா')
                continue

        # இன்றைய செய்தி
        if u''.join(tamil.utf8.get_letters(word)[-1:]) == u'ய':
            if (safe_splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) == u'ஐ':
                fixed_list.append(word)
                print(u"மிகா - Rule17 - " + word)
                result.add(word,u'விதி 17',u'மிகா')
                counter = counter+1
                continue

        # கற்ற சிறுவன்
        if u''.join(tamil.utf8.get_letters(word)[-2:]) == u'ற்ற':
            fixed_list.append(word)
            print(u"மிகா - Rule18 - " + word)
            result.add(word,u'விதி 18',u'மிகா')
            counter = counter+1
            continue

        # நல்ல பையன்
        if u''.join(tamil.utf8.get_letters(word)[-2:]) == u'ல்ல':
            fixed_list.append(word)
            print(u"மிகா - Rule19 - " + word)
            result.add(word,u'விதி 19',u'மிகா')
            counter = counter+1
            continue

        # கேட்ட  பாட்டு
        if u''.join(tamil.utf8.get_letters(word)[-2:]) == u'ட்ட':
            fixed_list.append(word)
            print(u"மிகா - Rule20 - " + word)
            result.add(word,u'விதி 20',u'மிகா')
            counter = counter+1
            continue

        # கேட்கின்ற பாட்டு
        if u''.join(tamil.utf8.get_letters(word)[-3:]) == u'கின்ற':
            fixed_list.append(word)
            print(u"மிகா - Rule21 - " + word)
            result.add(word,u'விதி 21',u'மிகா')
            counter = counter+1
            continue

        # கேட்கும் பாட்டு
        if u''.join(tamil.utf8.get_letters(word)[-1:]) == u'ம்':
            if (safe_splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) == u'உ':
                fixed_list.append(word)
                print(u"மிகா - Rule22 - " + word)
                result.add(word,u'விதி 22',u'மிகா')
                counter = counter+1
                continue

        # வல்லினம் மிகா வியங்கோள் வினைமுற்று - வருக புலவரே
        if word in viyankol:
            fixed_list.append(word)
            print(u"மிகா - Rule23 - " + word)
            result.add(word,u'விதி 23',u'மிகா')
            counter = counter+1
            continue

        # print(word)
        # print(next_word)
        # வல்லினம் மிகா இரட்டைக் கிளவி, அடுக்குத்தொடர்கள் - கல கல
        if word == next_word:
            fixed_list.append(word)
            print(u"மிகா - Rule24 - " + word)
            result.add(word,u'விதி 24',u'மிகா')
            counter = counter+1
            continue

        # # வல்லினம் மிகா கள், தல் விகுதிகள் - வாக்கு கள்
        #     if next_word in ['கள்','தல்']:
        #         fixed_list.append(word)
        #         print(u"மிகா - Rule25 - " + word)
        #         counter = counter+1
        #         continue

        # வல்லினம் மிகா பல, சில, ஏவல் வினை - வா கலையரசி
        if word in [u'கல',u'பல',u'சில',u'வா',u'எழு',u'போ',u'பார்'] :
            fixed_list.append(word)
            print(u"மிகா - Rule26 - " + word)
            counter = counter+1
            result.add(word,u'விதி 26',u'மிகா')
            continue

        # வல்லினம் மிகா பொதுப்பெயர்கள்,உயர்திணைப் பெயர்கள்,வடமொழி சொற்கள்  - மகளிர் கல்லூரி
        if word in noun_list :
            fixed_list.append(word)
            print(u"மிகா - விதி 28 - " + word)
            counter = counter+1
            result.add(word,u'விதி 28',u'மிகா')
            continue

        # 6.1.1 சுட்டு, வினா அடியாகத் தோன்றிய சொற்கள் முன் வல்லினம் மிகல் - அந்த பையன்
        if (tamil.utf8.get_letters(word)) in suttu_vina:
            if (tamil.utf8.get_letters(word)[-1]) not in mei_letters:
                if u''.join(tamil.utf8.get_letters(word)[1:3]) == 'வ்வா':
                    fixed_list.append(word)
                    print(u"மிகா - Rule29 - " + word)
                    result.add(word,u'விதி 29',u'மிகா')
                    counter = counter+1
                    continue
                if u''.join(tamil.utf8.get_letters(word)[-2:]) != u'டைய':
                    first_char_of_next_word = (next_word[0])
                    if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                        mei_of_first_char_of_next_word = safe_splitMeiUyir(first_char_of_next_word)[0]
                        if mei_of_first_char_of_next_word in vallinam_letters:
                            fixed_list.append(word + mei_of_first_char_of_next_word)
                            print(u"மிகும் - Rule2 - " + word + mei_of_first_char_of_next_word)
                            result.add(word,u'விதி 2',u'மிகும்')
                            counter = counter+1
                            continue

        # வன்தொடர்க் குற்றியலுகரம் முன் வல்லினம் மிகல் - கற்று கொடுத்தான்
        # 6.1.3 - 1

        if (tamil.utf8.get_letters(word)[-2]) in vallinam_letters:
            uyir_of_last_char = safe_splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]

            if uyir_of_last_char == u'உ':

                first_char_of_next_word = (next_word[0])
                mei_of_first_char_of_next_word = safe_splitMeiUyir(first_char_of_next_word)[0]
                fixed_list.append(word + mei_of_first_char_of_next_word)
                print(u"மிகும் - விதி 3 - " + word + mei_of_first_char_of_next_word)
                result.add(word,u'விதி 3',u'மிகும்')
                continue

        # மென்தொடர்க் குற்றியலுகரம் முன் வல்லினம் மிகல் - குரங்கு குட்டி
        # 6.1.3 - 2
        if (tamil.utf8.get_letters(word)[-2]) in mellinam_letters:
            uyir_of_last_char = safe_splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]

            if uyir_of_last_char == u'உ':

                if not ( u''.join(tamil.utf8.get_letters(word)[-3:]).endswith( u'கொண்டு') ):
                    first_char_of_next_word = (next_word[0])
                    mei_of_first_char_of_next_word = safe_splitMeiUyir(first_char_of_next_word)[0]
                    fixed_list.append(word + mei_of_first_char_of_next_word)
                    print(u"மிகும் - விதி 4 - " + word + mei_of_first_char_of_next_word)
                    result.add(word,u'விதி 4',u'மிகா')
                    continue

    # முற்றியலுகரச் சொற்கள் முன் வல்லினம் மிகல்
    # 6.1.4 - 1 - தனிக் குறில் அடுத்து வரும் உகரம்  - பொது பணி
        if len(tamil.utf8.get_letters(word)) == 2:
            if (safe_splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) in kuril_letters:
                uyir_of_last_char = safe_splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]
                if uyir_of_last_char == u'உ':
                    first_char_of_next_word = (next_word[0])
                    mei_of_first_char_of_next_word = safe_splitMeiUyir(first_char_of_next_word)[0]
                    fixed_list.append(word + mei_of_first_char_of_next_word)
                    print(u"மிகும் - விதி 5 - " + word + mei_of_first_char_of_next_word)
                    result.add(word,u'விதி 5',u'மிகும்')
                    continue

    # உயிர்த்தொடர்க் குற்றியலுகரம் முன் வல்லினம் மிகல் - விறகு கடை
    # 6.1.3 - 3
        if safe_splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1] in uyir_letters:
            uyir_of_last_char = safe_splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]

            if uyir_of_last_char == u'உ':
                first_char_of_next_word = (next_word[0])
                mei_of_first_char_of_next_word = safe_splitMeiUyir(first_char_of_next_word)[0]
                fixed_list.append(word + mei_of_first_char_of_next_word)
                print(u"மிகும் - விதி 6 - " + word + mei_of_first_char_of_next_word)
                result.add(word,u'விதி 6',u'மிகா')
                continue

    # 6.1.4 - 1 - வல்லினமெய் அல்லாத பிற மெய்களின் மேல் ஏறி வருகின்ற உகரம் - தேர்வு கட்டணம்
        if (safe_splitMeiUyir(tamil.utf8.get_letters(word)[-1])[0]) not in [u'க்',u'ச்',u'ட்',u'த்',u'ப்',u'ற்']:
            if (safe_splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == u'உ':
                first_char_of_next_word = (next_word[0])
                mei_of_first_char_of_next_word = safe_splitMeiUyir(first_char_of_next_word)[0]
                fixed_list.append(word + mei_of_first_char_of_next_word)
                print(u"மிகும் - விதி 7 - " + word + mei_of_first_char_of_next_word)
                result.add(word,u'விதி 7',u'மிகும்')
                continue

    # 6.1.5 - 1 - இரண்டாம் வேற்றுமை விரி - கனியை  தின்றான்
        if (safe_splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == u'ஐ':
            first_char_of_next_word = (next_word[0])
            mei_of_first_char_of_next_word = safe_splitMeiUyir(first_char_of_next_word)[0]
            fixed_list.append(word + mei_of_first_char_of_next_word)
            print(u"மிகும் - விதி 8 - " + word + mei_of_first_char_of_next_word)
            result.add(word,u'விதி 8',u'மிகும்')
            continue

    # 6.1.5 - 2 -  நான்காம் வேற்றுமை விரி - எனக்கு  கொடு
        if tamil.utf8.get_letters(word)[-1] == u'கு':
            first_char_of_next_word = (next_word[0])
            mei_of_first_char_of_next_word = safe_splitMeiUyir(first_char_of_next_word)[0]
            fixed_list.append(word + mei_of_first_char_of_next_word)
            print(u"மிகும் - விதி 9 - " + word + mei_of_first_char_of_next_word)
            result.add(word,u'விதி 9',u'மிகும்')
            continue

    # 6.1.6 - 1 - அ இ ய் ர் - அகர, இகர, யகர மெய் ஈற்று வினையெச்சம்; ஈறுகெட்ட எதிர்மறைப் பெயரெச்சம் ்
    # வர சொன்னான் குறிஞ்சி தலைவன்  தேங்காய் சட்னி  தயிர் குடம் தீரா சிக்கல்
        if (safe_splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == u'அ':
            if not u''.join(tamil.utf8.get_letters(word)[-2:]).endswith(u'டைய'):
                first_char_of_next_word = (next_word[0])
                mei_of_first_char_of_next_word = safe_splitMeiUyir(first_char_of_next_word)[0]
                fixed_list.append(word + mei_of_first_char_of_next_word)
                print(u"மிகும் - விதி 10 - " + word + mei_of_first_char_of_next_word)
                result.add(word,u'விதி 10',u'மிகும்')
                continue

        if (safe_splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == u'இ':
            first_char_of_next_word = (next_word[0])
            mei_of_first_char_of_next_word = safe_splitMeiUyir(first_char_of_next_word)[0]
            fixed_list.append(word + mei_of_first_char_of_next_word)
            print(u"மிகும் - விதி 11 - " + word + mei_of_first_char_of_next_word)
            result.add(word,u'விதி 11',u'மிகும்')
            continue

        if (safe_splitMeiUyir(tamil.utf8.get_letters(word)[-1])) == u'ய்':
            first_char_of_next_word = (next_word[0])
            mei_of_first_char_of_next_word = safe_splitMeiUyir(first_char_of_next_word)[0]
            fixed_list.append(word + mei_of_first_char_of_next_word)
            print(u"மிகும் - விதி 12 - " + word + mei_of_first_char_of_next_word)
            result.add(word,u'விதி 12',u'மிகும்')
            continue

        if (safe_splitMeiUyir(tamil.utf8.get_letters(word)[-1])) == u'ர்':
            first_char_of_next_word = (next_word[0])
            mei_of_first_char_of_next_word = safe_splitMeiUyir(first_char_of_next_word)[0]
            fixed_list.append(word + mei_of_first_char_of_next_word)
            print(u"மிகும் - விதி 13 - " + word + mei_of_first_char_of_next_word)
            result.add(word,u'விதி 13',u'மிகும்')
            continue

        if (safe_splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == u'ஆ':
            first_char_of_next_word = (next_word[0])
            mei_of_first_char_of_next_word = safe_splitMeiUyir(first_char_of_next_word)[0]
            fixed_list.append(word + mei_of_first_char_of_next_word)
            print(u"மிகும் - விதி 14 - " + word + mei_of_first_char_of_next_word)
            result.add(word,u'விதி 14',u'மிகும்')
            continue

        rule15_letter = safe_splitMeiUyir(tamil.utf8.get_letters(word)[-1])
        # 6.1.7 - மகர இறுதி கெட்டு உயிர் ஈறாய் நிற்கும் சொற்கள் - மரம் கிளை
        if (rule15_letter == u'ம்'):
            if safe_splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1] in uyir_letters:
                first_char_of_next_word = (next_word[0])
                mei_of_first_char_of_next_word = safe_splitMeiUyir(first_char_of_next_word)[0]
                fixed_list.append(word[:-2] + mei_of_first_char_of_next_word)
                print(u"மிகும் - விதி 15 - " + word[:-2] + mei_of_first_char_of_next_word)
                result.add(word,u'விதி 15',u'மிகும்')
                continue

        fixed_list.append(word)
        print(u"விதி " + word)
    return fixed_list,result

def run_sandhi_checker_command_line():
    if len(sys.argv) == 1:
        try:
            in_path = os.path.join(BASE_DIRECTORY,'Input_text.txt') #default
        except Exception as ioe:
            print(u"Usage: sandhi_checker.py <filename>")
            print(u"Output will also be sent to file 'Output_text.txt'")
            sys.exit(-1)
    else:
        in_path = sys.argv[1]
    file_inp = codecs.open(in_path,'r','UTF-8')
    a = file_inp.read()
    file_inp.close()

    new_path = os.path.join(BASE_DIRECTORY,'Output_text.txt')
    file_opt = codecs.open(new_path,'w','UTF-8')

    words=tamil.utf8.get_words(a)
    fixed_list,result = check_sandhi(words)
    print(u' '.join(fixed_list))
    print(u"%s"%result)

if __name__ == u"__main__":
    run_sandhi_checker_command_line()

