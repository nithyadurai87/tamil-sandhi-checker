#/usr/bin/python3
import tamil

#http://www.tamilvu.org/courses/degree/c021/c0214/html/c0214661.htm

a="அங்குக் கண்டான் அந்த பையன். எத்தனை பழங்கள்?  கண்டவாறு சொன்னான், ஐந்து சிறுவர்கள், கத்தியோடு  நின்றான், கத்திகொண்டு குத்தினான், வீட்டிலிருந்து  சென்றான், கை குழந்தை,  கற்று கொடுத்தான், குரங்கு குட்டி, விறகு கடை, பொது பணி,  தேர்வு  கட்டணம், கனியை தின்றான், "+\
"எனக்கு கொடு, வீட்டினின்று வெளியேறினான், வர சொன்னான், என்னுடைய புத்தகம், எனது புத்தகம், குறிஞ்சி தலைவன், தேங்காய் சட்னி,  தயிர் குடம், தீரா சிக்கல், மரம் தலைவன்."
words=tamil.utf8.get_words(a)
mei_letters = tamil.utf8.mei_letters
uyir_letters = tamil.utf8.uyir_letters
kuril_letters = tamil.utf8.kuril_letters
nedil_letters = tamil.utf8.nedil_letters
agaram_letters = tamil.utf8.agaram_letters
uyirmei_letters = tamil.utf8.uyirmei_letters
vallinam_letters = tamil.utf8.vallinam_letters
mellinam_letters = tamil.utf8.mellinam_letters
special_chars=['.',';',',',':','?']
one_letter_words=['கை','தீ','தை','பூ','மை']
suttu_vina=['அ','ஆ','இ','ஈ','எ','யா']
suttu_vina_not=['அது','இது','எது','அவை','இவை','எவை','அன்று','இன்று','என்று','அத்தனை','இத்தனை','எத்தனை','அவ்வளவு','இவ்வளவு','எவ்வளவு','அவ்வாறு','இவ்வாறு','எவ்வாறு']
numerals=['ஒன்று','இரண்டு','மூன்று','நான்கு','ஐந்து','ஆறு','நூறு','ஏழு','ஒன்பது','ஒரு','இரு','அறு','எழு']
fixed_list=[]


def check_sandhi(words):
    counter = 0

    for word in words:
    # வல்லினம் மிகா இடங்கள் 
        if tamil.utf8.get_letters(word)[-1] in special_chars:
            fixed_list.append(word)
            print("மிகா - Rule1 - " + word)
            counter = counter+1
            continue

    # வல்லினம் மிகா சுட்டு, வினா அடியாகத் தோன்றிய சொற்கள் - எத்தனை பழங்கள்?   
        if word in suttu_vina_not:
            fixed_list.append(word)
            print("மிகா - Rule2 - " + word)
            counter = counter+1
            continue

    # வல்லினம் மிகா வந்த, கண்ட, சொன்ன, வரும் என்பன  போன்ற பெயரெச்சங்களோடு படி, ஆறு என்னும் சொற்கள்- கண்டவாறு சொன்னான்  
        if (tamil.utf8.get_letters(word)[0]) in ['வ','க','சொ']:
            if (tamil.utf8.get_letters(word)[-1]) in ['டி','று']:
                fixed_list.append(word)
                print("மிகா - Rule3 - " + word)
                counter = counter+1
                continue

    # வல்லினம் மிகா எண்ணுப்பெயர்கள் - ஐந்து சிறுவர்கள் 
        if word in numerals:
            fixed_list.append(word)
            print("மிகா - Rule4 - " + word)
            counter = counter+1
            continue

    # ஓர் எழுத்துச் சொற்கள் முன் வல்லினம் மிகல்   
    # 6.1.2 - கை குழந்தை

        if len(tamil.utf8.get_letters(word)) == 1:
            if  word in one_letter_words:
                first_char_of_next_word = (words[counter + 1][0])
                mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                fixed_list.append(word + mei_of_first_char_of_next_word)
                print("மிகும் - Rule1 - " + word + mei_of_first_char_of_next_word)
                counter = counter+1
                continue    

    # வல்லினம் மிகா ஒடு & ஓடு என உயிர் ஈறு கொண்டவை - கத்தியோடு நின்றான் 
        if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) in ['ஒ','ஓ']:
            if (tamil.utf8.get_letters(word)[-1]) == 'டு':
                fixed_list.append(word)
                print("மிகா - Rule5 - " + word)
                counter = counter+1
                continue

    # வல்லினம் மிகா ‘கொண்டு’ என்னும் சொல்லுருபு -கத்திகொண்டு குத்தினான்
        if ''.join(tamil.utf8.get_letters(word)[-3:]) ==  'கொண்டு':
            fixed_list.append(word)
            print("மிகா - Rule6 - " + word)
            counter = counter+1
            continue

    # வல்லினம் மிகா இல் என்பதோடு இருந்து என்னும்  சொல்லுருபு - வீட்டிலிருந்து சென்றான்  
        if ''.join(tamil.utf8.get_letters(word)[-4:]) == 'லிருந்து':
            fixed_list.append(word)
            print("மிகா - Rule7 - " + word)
            counter = counter+1
            continue

    # வல்லினம் மிகா இன் என்பதோடு நின்று என்னும் சொல்லுருபு - வீட்டினின்று வெளியேறினான் 
        if ''.join(tamil.utf8.get_letters(word)[-3:]) == 'னின்று':
            fixed_list.append(word)
            print("மிகா - Rule8 - " + word)
            counter = counter+1
            continue

    # வல்லினம் மிகா ஆறாம் வேற்றுமைக்கு உரிய அது - எனது புத்தகம்
        if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) == 'அ':
            if (tamil.utf8.get_letters(word)[-1]) == 'து':
                fixed_list.append(word)
                print("மிகா - Rule9 - " + word)
                counter = counter+1
                continue

    # வல்லினம் மிகா ‘உடைய’ என்னும் சொல்லுருபு- என்னுடைய புத்தகம்
        if ''.join(tamil.utf8.get_letters(word)[-2:]) == 'டைய':            
            if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-3])[1]) == 'உ':
                fixed_list.append(word)
                print("மிகா - Rule10 - " + word)
                counter = counter+1
                continue

    # சுட்டு, வினா அடியாகத் தோன்றிய சொற்கள் முன் வல்லினம் மிகல்   
    # 6.1.1 - அந்த பையன்

        if (tamil.utf8.get_letters(word)[0]) in suttu_vina:
            if (tamil.utf8.get_letters(word)[-1]) not in mei_letters:
                if ''.join(tamil.utf8.get_letters(word)[-2:]) != 'டைய':
                    first_char_of_next_word = (words[counter + 1][0])
                    mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                    fixed_list.append(word + mei_of_first_char_of_next_word)
                    print("மிகும் - Rule2 - " + word + mei_of_first_char_of_next_word)
                    counter = counter+1
                    continue  

    # வன்தொடர்க் குற்றியலுகரம் முன் வல்லினம் மிகல் - கற்று கொடுத்தான்
    # 6.1.3 - 1 
          
        if (tamil.utf8.get_letters(word)[-2]) in vallinam_letters:
            uyir_of_last_char = tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]

            if uyir_of_last_char == 'உ':
                
                first_char_of_next_word = (words[counter + 1][0])
                mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                fixed_list.append(word + mei_of_first_char_of_next_word)   
                print("மிகும் - Rule3 - " + word + mei_of_first_char_of_next_word)
                counter = counter+1
                continue

    # மென்தொடர்க் குற்றியலுகரம் முன் வல்லினம் மிகல் - குரங்கு குட்டி
    # 6.1.3 - 2        
        if (tamil.utf8.get_letters(word)[-2]) in mellinam_letters:
            uyir_of_last_char = tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]

            if uyir_of_last_char == 'உ':

                if ''.join(tamil.utf8.get_letters(word)[-3:]) != 'கொண்டு':
                    first_char_of_next_word = (words[counter + 1][0])
                    mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                    fixed_list.append(word + mei_of_first_char_of_next_word)            
                    print("மிகும் - Rule4 - " + word + mei_of_first_char_of_next_word)
                    counter = counter+1
                    continue

    # முற்றியலுகரச் சொற்கள் முன் வல்லினம் மிகல்
    # 6.1.4 - 1 - தனிக் குறில் அடுத்து வரும் உகரம்  - பொது பணி      
        if len(tamil.utf8.get_letters(word)) == 2:
            if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) in kuril_letters:                
                uyir_of_last_char = tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]
                if uyir_of_last_char == 'உ':
                    first_char_of_next_word = (words[counter + 1][0])
                    mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                    fixed_list.append(word + mei_of_first_char_of_next_word)              
                    print("மிகும் - Rule5 - " + word + mei_of_first_char_of_next_word)
                    counter = counter+1
                    continue

    # உயிர்த்தொடர்க் குற்றியலுகரம் முன் வல்லினம் மிகல் - விறகு கடை
    # 6.1.3 - 3        
        if tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1] in uyir_letters:
            uyir_of_last_char = tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]

            if uyir_of_last_char == 'உ':
                first_char_of_next_word = (words[counter + 1][0])
                mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                fixed_list.append(word + mei_of_first_char_of_next_word)              
                print("மிகும் - Rule6 - " + word + mei_of_first_char_of_next_word)
                counter = counter+1
                continue

    # 6.1.4 - 1 - வல்லினமெய் அல்லாத பிற மெய்களின் மேல் ஏறி வருகின்ற உகரம் - தேர்வு கட்டணம்      
        if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[0]) not in ['க்','ச்','ட்','த்','ப்','ற்']:
            if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == 'உ':
                first_char_of_next_word = (words[counter + 1][0])
                mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                fixed_list.append(word + mei_of_first_char_of_next_word)              
                print("மிகும் - Rule7 - " + word + mei_of_first_char_of_next_word)
                counter = counter+1
                continue

    # 6.1.5 - 1 - இரண்டாம் வேற்றுமை விரி - கனியை  தின்றான்     
        if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == 'ஐ':
            first_char_of_next_word = (words[counter + 1][0])
            mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
            fixed_list.append(word + mei_of_first_char_of_next_word)              
            print("மிகும் - Rule8 - " + word + mei_of_first_char_of_next_word)
            counter = counter+1
            continue

    # 6.1.5 - 2 -  நான்காம் வேற்றுமை விரி - எனக்கு  கொடு     
        if tamil.utf8.get_letters(word)[-1] == 'கு':
            first_char_of_next_word = (words[counter + 1][0])
            mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
            fixed_list.append(word + mei_of_first_char_of_next_word)              
            print("மிகும் - Rule9 - " + word + mei_of_first_char_of_next_word)
            counter = counter+1
            continue

    # 6.1.6 - 1 - அ இ ய் ர் - அகர, இகர, யகர மெய் ஈற்று வினையெச்சம்; ஈறுகெட்ட எதிர்மறைப் பெயரெச்சம் ்
    # வர சொன்னான் குறிஞ்சி தலைவன்  தேங்காய் சட்னி  தயிர் குடம் தீரா சிக்கல் 
        if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == 'அ':
            if ''.join(tamil.utf8.get_letters(word)[-2:]) != 'டைய':
                first_char_of_next_word = (words[counter + 1][0])
                mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                fixed_list.append(word + mei_of_first_char_of_next_word)              
                print("மிகும் - Rule10 - " + word + mei_of_first_char_of_next_word)
                counter = counter+1
                continue
    
        if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == 'இ':
            first_char_of_next_word = (words[counter + 1][0])
            mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
            fixed_list.append(word + mei_of_first_char_of_next_word)              
            print("மிகும் - Rule11 - " + word + mei_of_first_char_of_next_word)
            counter = counter+1
            continue        
    
        if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])) == 'ய்':
            first_char_of_next_word = (words[counter + 1][0])
            mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
            fixed_list.append(word + mei_of_first_char_of_next_word)              
            print("மிகும் - Rule12 - " + word + mei_of_first_char_of_next_word)
            counter = counter+1
            continue
      
        if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])) == 'ர்':
            first_char_of_next_word = (words[counter + 1][0])
            mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
            fixed_list.append(word + mei_of_first_char_of_next_word)              
            print("மிகும் - Rule13 - " + word + mei_of_first_char_of_next_word)
            counter = counter+1
            continue 

        if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == 'ஆ':
            first_char_of_next_word = (words[counter + 1][0])
            mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
            fixed_list.append(word + mei_of_first_char_of_next_word)              
            print("மிகும் - Rule14 - " + word + mei_of_first_char_of_next_word)
            counter = counter+1
            continue  

    # 6.1.7 - மகர இறுதி கெட்டு உயிர் ஈறாய் நிற்கும் சொற்கள் - மரம் கிளை 
        if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])) == 'ம்':
            if tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1] in uyir_letters:
                first_char_of_next_word = (words[counter + 1][0])
                mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                fixed_list.append(word[:-2] + mei_of_first_char_of_next_word)            
                print("மிகும் - Rule15 - " + word[:-2] + mei_of_first_char_of_next_word)
                counter = counter+1
                continue     

        fixed_list.append(word)        
        print("Rules" + word)
        counter = counter+1

check_sandhi(words)
print(' '.join(fixed_list))



    
