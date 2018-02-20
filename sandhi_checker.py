## This Python file uses the following encoding: utf-8
#/usr/bin/python3
#
# Copyright (C) 2018 Nithya Duraisamy <nithyadurai87@gmail.com>
# Tamil sandhi checker - validate and fix list of Sandhi errors in Tamil text

import tamil
import collections

#http://www.tamilvu.org/courses/degree/c021/c0214/html/c0214661.htm

a =u"அங்குக் கண்டான் அந்த பையன். எத்தனை பழங்கள்?  கண்டவாறு சொன்னான், ஐந்து சிறுவர்கள், கத்தியோடு  நின்றான்," \
   u"கத்திகொண்டு குத்தினான், வீட்டிலிருந்து  சென்றான், கை குழந்தை,  கற்று கொடுத்தான், குரங்கு குட்டி, விறகு கடை, பொது பணி,  தேர்வு  கட்டணம், கனியை தின்றான்," \
   u"எனக்கு கொடு, வீட்டினின்று வெளியேறினான், வர சொன்னான், என்னுடைய புத்தகம், எனது புத்தகம், குறிஞ்சி தலைவன், தேங்காய் சட்னி,  தயிர் குடம், தீரா சிக்கல், மரம் தலைவன்."
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
suttu_vina_not=[u'அது',u'இது',u'எது',u'அவை',u'இவை',u'எவை',u'அன்று',u'இன்று',u'என்று',u'அத்தனை',u'இத்தனை',u'எத்தனை',u'அவ்வளவு',u'இவ்வளவு',u'எவ்வளவு',u'அவ்வாறு',u'இவ்வாறு',u'எவ்வாறு']
numerals=[u'ஒன்று',u'இரண்டு',u'மூன்று',u'நான்கு',u'ஐந்து',u'ஆறு',u'நூறு',u'ஏழு',u'ஒன்பது',u'ஒரு',u'இரு',u'அறு',u'எழு']

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
    for counter,word in enumerate(words):
    # வல்லினம் மிகா இடங்கள்
        if tamil.utf8.get_letters(word)[-1] in special_chars:
            fixed_list.append(word)
            print(u"மிகா - விதி 1 - " + word)
            result.add(word,u'விதி 1',u'மிகா')
            continue

    # வல்லினம் மிகா சுட்டு, வினா அடியாகத் தோன்றிய சொற்கள் - எத்தனை பழங்கள்?
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
                first_char_of_next_word = (words[counter + 1][0])
                mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                fixed_list.append(word + mei_of_first_char_of_next_word)
                print(u"மிகும் - விதி 1 - " + word + mei_of_first_char_of_next_word)
                result.add(word,u'விதி 1',u'மிகும்')
                continue

    # வல்லினம் மிகா ஒடு & ஓடு என உயிர் ஈறு கொண்டவை - கத்தியோடு நின்றான்
        if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) in [u'ஒ',u'ஓ']:
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
        if ''.join(tamil.utf8.get_letters(word)[-4:]) == u'லிருந்து':
            fixed_list.append(word)
            print(u"மிகா - விதி 7 - " + word)
            result.add(word,u'விதி 7',u"மிகா")
            continue

    # வல்லினம் மிகா இன் என்பதோடு நின்று என்னும் சொல்லுருபு - வீட்டினின்று வெளியேறினான்
        if ''.join(tamil.utf8.get_letters(word)[-3:]) == u'னின்று':
            fixed_list.append(word)
            print(u"மிகா - விதி 8 - " + word)
            result.add(word,u'விதி 8',u"மிகா")
            continue

    # வல்லினம் மிகா ஆறாம் வேற்றுமைக்கு உரிய அது - எனது புத்தகம்
        if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) == u'அ':
            if (tamil.utf8.get_letters(word)[-1]) == u'து':
                fixed_list.append(word)
                print(u"மிகா - விதி 9 - " + word)
                result.add(word,u'விதி 9',u'மிகா')
                continue

    # வல்லினம் மிகா ‘உடைய’ என்னும் சொல்லுருபு- என்னுடைய புத்தகம்
        if ''.join(tamil.utf8.get_letters(word)[-2:]) == u'டைய':
            if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-3])[1]) == u'உ':
                fixed_list.append(word)
                print(u"மிகா - விதி 10 - " + word)
                result.add(word,u'விதி 10',u'மிகா')
                continue

    # சுட்டு, வினா அடியாகத் தோன்றிய சொற்கள் முன் வல்லினம் மிகல்
    # 6.1.1 - அந்த பையன்

        if (tamil.utf8.get_letters(word)[0]) in suttu_vina:
            if (tamil.utf8.get_letters(word)[-1]) not in mei_letters:
                if u''.join(tamil.utf8.get_letters(word)[-2:]) != u'டைய':
                    first_char_of_next_word = (words[counter + 1][0])
                    mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                    fixed_list.append(word + mei_of_first_char_of_next_word)
                    print(u"மிகும் - விதி 2 - " + word + mei_of_first_char_of_next_word)
                    result.add(word,u'விதி 2',u'மிகும்')
                    continue

    # வன்தொடர்க் குற்றியலுகரம் முன் வல்லினம் மிகல் - கற்று கொடுத்தான்
    # 6.1.3 - 1

        if (tamil.utf8.get_letters(word)[-2]) in vallinam_letters:
            uyir_of_last_char = tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]

            if uyir_of_last_char == u'உ':

                first_char_of_next_word = (words[counter + 1][0])
                mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                fixed_list.append(word + mei_of_first_char_of_next_word)
                print(u"மிகும் - விதி 3 - " + word + mei_of_first_char_of_next_word)
                result.add(word,u'விதி 3',u'மிகும்')
                continue

    # மென்தொடர்க் குற்றியலுகரம் முன் வல்லினம் மிகல் - குரங்கு குட்டி
    # 6.1.3 - 2
        if (tamil.utf8.get_letters(word)[-2]) in mellinam_letters:
            uyir_of_last_char = tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]

            if uyir_of_last_char == u'உ':

                if not ( u''.join(tamil.utf8.get_letters(word)[-3:]).endswith( u'கொண்டு') ):
                    first_char_of_next_word = (words[counter + 1][0])
                    mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                    fixed_list.append(word + mei_of_first_char_of_next_word)
                    print(u"மிகும் - விதி 4 - " + word + mei_of_first_char_of_next_word)
                    result.add(word,u'விதி 4',u'மிகா')
                    continue

    # முற்றியலுகரச் சொற்கள் முன் வல்லினம் மிகல்
    # 6.1.4 - 1 - தனிக் குறில் அடுத்து வரும் உகரம்  - பொது பணி
        if len(tamil.utf8.get_letters(word)) == 2:
            if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) in kuril_letters:
                uyir_of_last_char = tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]
                if uyir_of_last_char == u'உ':
                    first_char_of_next_word = (words[counter + 1][0])
                    mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                    fixed_list.append(word + mei_of_first_char_of_next_word)
                    print(u"மிகும் - விதி 5 - " + word + mei_of_first_char_of_next_word)
                    result.add(word,u'விதி 5',u'மிகும்')
                    continue

    # உயிர்த்தொடர்க் குற்றியலுகரம் முன் வல்லினம் மிகல் - விறகு கடை
    # 6.1.3 - 3
        if tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1] in uyir_letters:
            uyir_of_last_char = tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]

            if uyir_of_last_char == u'உ':
                first_char_of_next_word = (words[counter + 1][0])
                mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                fixed_list.append(word + mei_of_first_char_of_next_word)
                print(u"மிகும் - விதி 6 - " + word + mei_of_first_char_of_next_word)
                result.add(word,u'விதி 6',u'மிகா')
                continue

    # 6.1.4 - 1 - வல்லினமெய் அல்லாத பிற மெய்களின் மேல் ஏறி வருகின்ற உகரம் - தேர்வு கட்டணம்
        if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[0]) not in [u'க்',u'ச்',u'ட்',u'த்',u'ப்',u'ற்']:
            if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == u'உ':
                first_char_of_next_word = (words[counter + 1][0])
                mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                fixed_list.append(word + mei_of_first_char_of_next_word)
                print(u"மிகும் - விதி 7 - " + word + mei_of_first_char_of_next_word)
                result.add(word,u'விதி 7',u'மிகும்')
                continue

    # 6.1.5 - 1 - இரண்டாம் வேற்றுமை விரி - கனியை  தின்றான்
        if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == u'ஐ':
            first_char_of_next_word = (words[counter + 1][0])
            mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
            fixed_list.append(word + mei_of_first_char_of_next_word)
            print(u"மிகும் - விதி 8 - " + word + mei_of_first_char_of_next_word)
            result.add(word,u'விதி 8',u'மிகும்')
            continue

    # 6.1.5 - 2 -  நான்காம் வேற்றுமை விரி - எனக்கு  கொடு
        if tamil.utf8.get_letters(word)[-1] == u'கு':
            first_char_of_next_word = (words[counter + 1][0])
            mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
            fixed_list.append(word + mei_of_first_char_of_next_word)
            print(u"மிகும் - விதி 9 - " + word + mei_of_first_char_of_next_word)
            result.add(word,u'விதி 9',u'மிகும்')
            continue

    # 6.1.6 - 1 - அ இ ய் ர் - அகர, இகர, யகர மெய் ஈற்று வினையெச்சம்; ஈறுகெட்ட எதிர்மறைப் பெயரெச்சம் ்
    # வர சொன்னான் குறிஞ்சி தலைவன்  தேங்காய் சட்னி  தயிர் குடம் தீரா சிக்கல்
        if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == u'அ':
            if not u''.join(tamil.utf8.get_letters(word)[-2:]).endswith(u'டைய'):
                first_char_of_next_word = (words[counter + 1][0])
                mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                fixed_list.append(word + mei_of_first_char_of_next_word)
                print(u"மிகும் - விதி 10 - " + word + mei_of_first_char_of_next_word)
                result.add(word,u'விதி 10',u'மிகும்')
                continue

        if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == u'இ':
            first_char_of_next_word = (words[counter + 1][0])
            mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
            fixed_list.append(word + mei_of_first_char_of_next_word)
            print(u"மிகும் - விதி 11 - " + word + mei_of_first_char_of_next_word)
            result.add(word,u'விதி 11',u'மிகும்')
            continue

        if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])) == u'ய்':
            first_char_of_next_word = (words[counter + 1][0])
            mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
            fixed_list.append(word + mei_of_first_char_of_next_word)
            print(u"மிகும் - விதி 12 - " + word + mei_of_first_char_of_next_word)
            result.add(word,u'விதி 12',u'மிகும்')
            continue

        if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])) == u'ர்':
            first_char_of_next_word = (words[counter + 1][0])
            mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
            fixed_list.append(word + mei_of_first_char_of_next_word)
            print(u"மிகும் - விதி 13 - " + word + mei_of_first_char_of_next_word)
            result.add(word,u'விதி 13',u'மிகும்')
            continue

        if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == u'ஆ':
            first_char_of_next_word = (words[counter + 1][0])
            mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
            fixed_list.append(word + mei_of_first_char_of_next_word)
            print(u"மிகும் - விதி 14 - " + word + mei_of_first_char_of_next_word)
            result.add(word,u'விதி 14',u'மிகும்')
            continue

    # 6.1.7 - மகர இறுதி கெட்டு உயிர் ஈறாய் நிற்கும் சொற்கள் - மரம் கிளை
        if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])) == u'ம்':
            if tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1] in uyir_letters:
                first_char_of_next_word = (words[counter + 1][0])
                mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                fixed_list.append(word[:-2] + mei_of_first_char_of_next_word)
                print(u"மிகும் - விதி 15 - " + word[:-2] + mei_of_first_char_of_next_word)
                result.add(word,u'விதி 15',u'மிகும்')
                continue

        fixed_list.append(word)
        print(u"விதி " + word)
    return fixed_list,result

if __name__ == u"__main__":
    words=tamil.utf8.get_words(a)    
    fixed_list,result = check_sandhi(words)
    print(u' '.join(fixed_list))
    print(u"%s"%result)
