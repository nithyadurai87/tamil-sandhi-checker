#/usr/bin/python3
import tamil

#http://www.tamilvu.org/courses/degree/c021/c0214/html/c0214661.htm
path = 'Input_text.txt'
file_inp = open(path,'r')
a = file_inp.read()
file_inp.close()

new_path = 'Output_text.txt'
file_opt = open(new_path,'w')

words=tamil.utf8.get_words(a)
noun_file = open("all-tamil-nouns.txt")
noun_list = noun_file.read().strip().split()
mei_letters = tamil.utf8.mei_letters
uyir_letters = tamil.utf8.uyir_letters
ayudha_letter = ['ஃ']
kuril_letters = tamil.utf8.kuril_letters
nedil_letters = tamil.utf8.nedil_letters
agaram_letters = tamil.utf8.agaram_letters
uyirmei_letters = tamil.utf8.uyirmei_letters
vallinam_letters = tamil.utf8.vallinam_letters
mellinam_letters = tamil.utf8.mellinam_letters
tamil_letters = tamil.utf8.tamil_letters
sanskrit_letters = tamil.utf8.sanskrit_letters 
sanskrit_mei_letters = tamil.utf8.sanskrit_mei_letters 
special_chars=['.','\'',';',',',':','?','(',')','_','-','"','%','±','#','@','!','!','$','%','^','&','*','+','/','–','\\','>','<','|','}','{',']','[']
one_letter_words=['கை','தீ','தை','பூ','மை']
numbers=['0','1','2','3','4','5','6','7','8','9','½']
granda = [u"ஜ்",u"ஷ்", u"ஸ்",u"ஹ்"
,u"ஶ", 	u"ஶா", 	u"ஶி", 	u"ஶீ", u"ஶு", u"ஶூ", u"ஶெ", u"ஶே", u"ஶை", u"ஶொ", u"ஶோ", u"ஶௌ"
,u"ஜ"  ,u"ஜா"  ,u"ஜி"  ,u"ஜீ"  ,u"ஜு"  ,u"ஜூ"  ,u"ஜெ"  ,u"ஜே"  ,u"ஜை"  ,u"ஜொ"  ,u"ஜோ"  ,u"ஜௌ"
,u"ஷ"  ,u"ஷா"  ,u"ஷி"  ,u"ஷீ"  ,u"ஷு"  ,u"ஷூ"  ,u"ஷெ"  ,u"ஷே"  ,u"ஷை"  ,u"ஷொ"  ,u"ஷோ"  ,u"ஷௌ"
,u"ஸ"  ,u"ஸா"  ,u"ஸி"  ,u"ஸீ"  ,u"ஸு"  ,u"ஸூ"  ,u"ஸெ"  ,u"ஸே"  ,u"ஸை"  ,u"ஸொ"  ,u"ஸோ"  ,u"ஸௌ"
,u"ஹ"  ,u"ஹா"  ,u"ஹி"  ,u"ஹீ"  ,u"ஹு"  ,u"ஹூ"  ,u"ஹெ"  ,u"ஹே"  ,u"ஹை"  ,u"ஹொ"  ,u"ஹோ"  ,u"ஹௌ"
,u"க்ஷ" ,u"க்ஷா" ,u"க்ஷி" ,u"க்ஷீ" ,u"க்ஷு" ,u"க்ஷூ" ,u"க்ஷெ" ,u"க்ஷே" ,u"க்ஷை" ,u"க்ஷொ" ,u"க்ஷோ" ,u"க்ஷௌ" ]
english = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
suttu_vina=['அ','இ','எ','யா','அந்த','இந்த','எந்த','அங்கு','இங்கு','எங்கு','ஆங்கு','ஈங்கு','யாங்கு','அப்படி','இப்படி','எப்படி','ஆண்டு','ஈண்டு','யாண்டு','அவ்வகை','இவ்வகை','எவ்வகை','அத்துணை','இத்துணை']
suttu_vina_not=['அது','இது','எது','யாது','அவை','இவை','எவை','அன்று','இன்று','என்று','அத்தனை','இத்தனை','எத்தனை','அவ்வளவு','இவ்வளவு','எவ்வளவு','அவ்வாறு','இவ்வாறு','எவ்வாறு']
numerals=['ஒன்று','இரண்டு','மூன்று','நான்கு','ஐந்து','ஆறு','நூறு','ஏழு','ஒன்பது','ஒரு','இரு','அறு','எழு']
viyankol=['கற்க','நில்','கவனி','செல்','செல்க','மன்னிய','வெல்க','செப்பும்','வினாவும்','வாழ்க','ஓம்பல்','அஞ்சாமை','வாழி','வீழ்க','ஒழிக','வருக','உண்க','அருள்க','கருணைபுரிக','வருக','வாழிய','வாழியர்','வாரற்க','கூறற்க','செல்லற்க','வாரல்','செல்லல்','பகரேல்']
common_names=['மகளிர்','தாய்','அவள்','அவர்','கண்ணகி','கோழி','பல்லவர்','ஆராய்ச்சி','பேராசிரியர்']
fixed_list=[]

def check_sandhi(words):
    counter = 0

    for word in words:
        letters = tamil.utf8.get_letters(word)

        # வல்லினம் மிகா - கடைசி வார்த்தை
        if counter == len(words)-1:
            print("மிகா - Rule1 - " + word)
            fixed_list.append(word)
            break
        # வல்லினம் மிகா - வடமொழி எழுத்துக்கள் 
        if (any(i in letters for i in granda)) == True:
            fixed_list.append(word)
            print("மிகா - Rule2.1 - " + word)
            counter = counter+1
            continue
        if (any(i in letters for i in english)) == True:
            fixed_list.append(word)
            print("மிகா - Rule2.2 - " + word)
            counter = counter+1
            continue
        # வல்லினம் மிகா - எண்கள்  
        if (any(i in letters for i in numbers)) == True:
            fixed_list.append(word)
            print("மிகா - Rule3 - " + word)
            counter = counter+1
            continue

        # வல்லினம் மிகா இடங்கள்           
        if (tamil.utf8.get_letters(word)[-1]) in special_chars:
            fixed_list.append(word)
            print("மிகா - Rule4 - " + word)
            counter = counter+1
            continue

        # வல்லினம் மிகா சுட்டு, வினா அடியாகத் தோன்றிய சொற்கள் - எத்தனை பழங்கள்?  
        # ‘அஃறிணைப் பன்மை’ - பல பசு
        if word in suttu_vina_not:
            fixed_list.append(word)
            print("மிகா - Rule5 - " + word)
            counter = counter+1
            continue

        # வல்லினம் மிகா வந்த, கண்ட, சொன்ன, வரும் என்பன  போன்ற பெயரெச்சங்களோடு படி, ஆறு என்னும் சொற்கள்- கண்டவாறு சொன்னான்  
        if (tamil.utf8.get_letters(word)[0]) in ['வ','க','சொ']:
            if (tamil.utf8.get_letters(word)[-1]) in ['டி','று']:
                fixed_list.append(word)
                print("மிகா - Rule6 - " + word)
                counter = counter+1
                continue

        # வல்லினம் மிகா எண்ணுப்பெயர்கள் - ஐந்து சிறுவர்கள் 
        if word in numerals:
            fixed_list.append(word)
            print("மிகா - Rule7 - " + word)
            counter = counter+1
            continue

        # 6.1.2 - ஓர் எழுத்துச் சொற்கள் முன் வல்லினம்  மிகல் - கை  குழந்தை
        if len(tamil.utf8.get_letters(word)) == 1:
            if  word in one_letter_words:
                first_char_of_next_word = (words[counter + 1][0])
                if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                    mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                    if mei_of_first_char_of_next_word in vallinam_letters:                    
                        fixed_list.append(word + mei_of_first_char_of_next_word)
                        print("மிகும் - Rule1 - " + word + mei_of_first_char_of_next_word)
                        counter = counter+1
                        continue    

        # வல்லினம் மிகா ஒடு & ஓடு என உயிர் ஈறு கொண்டவை - கத்தியோடு நின்றான் 
        if len(tamil.utf8.get_letters(word)) > 1:
            if tamil.utf8.get_letters(word)[-2] not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) in ['ஒ','ஓ']:
                    if (tamil.utf8.get_letters(word)[-1]) == 'டு':
                        fixed_list.append(word)
                        print("மிகா - Rule8 - " + word)
                        counter = counter+1
                        continue

        # வல்லினம் மிகா ‘கொண்டு’ என்னும் சொல்லுருபு -கத்திகொண்டு குத்தினான்
        if ''.join(tamil.utf8.get_letters(word)[-3:]) ==  'கொண்டு':
            fixed_list.append(word)
            print("மிகா - Rule9 - " + word)
            counter = counter+1
            continue

        # வல்லினம் மிகா இல் என்பதோடு இருந்து என்னும்  சொல்லுருபு - வீட்டிலிருந்து சென்றான்  
        if ''.join(tamil.utf8.get_letters(word)[-4:]) == 'லிருந்து':
            fixed_list.append(word)
            print("மிகா - Rule10 - " + word)
            counter = counter+1
            continue

        # வல்லினம் மிகா இன் என்பதோடு நின்று என்னும் சொல்லுருபு - வீட்டினின்று வெளியேறினான் 
        if ''.join(tamil.utf8.get_letters(word)[-3:]) == 'னின்று':
            fixed_list.append(word)
            print("மிகா - Rule11 - " + word)
            counter = counter+1
            continue

        # வல்லினம் மிகா ஆறாம் வேற்றுமைக்கு உரிய அது - எனது புத்தகம்
        if len(tamil.utf8.get_letters(word)) > 1:
            if tamil.utf8.get_letters(word)[-2] not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) == 'அ':
                    if (tamil.utf8.get_letters(word)[-1]) == 'து':
                        fixed_list.append(word)
                        print("மிகா - Rule12 - " + word)
                        counter = counter+1
                        continue

        # வல்லினம் மிகா ‘உடைய’ என்னும் சொல்லுருபு- என்னுடைய புத்தகம்
        if ''.join(tamil.utf8.get_letters(word)[-2:]) == 'டைய':  
            if ''.join(tamil.utf8.get_letters(word)[-3]) not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):           
                if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-3])[1]) == 'உ':
                    fixed_list.append(word)
                    print("மிகா - Rule13 - " + word)
                    counter = counter+1
                    continue

        # வல்லினம் மிகா மென்தொடர்க் குற்றியலுகர  வினையெச்சங்கள் - ண்டு, ந்து, ன்று என முடியும் -கண்டு பேசினார்
        # இடைத்தொடர்க் குற்றியலுகர  வினையெச்சங்கள் - ய்து என முடியும் - செய்து தந்தான்
        if ''.join(tamil.utf8.get_letters(word)[-2:]) in ['ண்டு','ந்து','ன்று','ய்து','ன்கு']:            
            fixed_list.append(word)
            print("மிகா - Rule14 - " + word)
            counter = counter+1
            continue

        # வல்லினம் மிகா மற்ற பெயரெச்சங்கள் - இன்றி, ஆத, இய, ஐய,ற்ற,ல்ல, ட்ட ன்ற, ந்த, த்து உம் ஆகிய  விகுதிகள் பெற்று முடியும்  
        # அழியாத கல்வி 
        if len(tamil.utf8.get_letters(word)) > 1:
            if ''.join(tamil.utf8.get_letters(word)[-1]) == 'த':  
                if ''.join(tamil.utf8.get_letters(word)[-2]) not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):           
                    if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) == 'ஆ':
                        fixed_list.append(word)
                        print("மிகா - Rule15 - " + word)
                        counter = counter+1
                        continue

        # பெரிய பெண் 
        if len(tamil.utf8.get_letters(word)) > 1:
            if ''.join(tamil.utf8.get_letters(word)[-1]) == 'ய':  
                if ''.join(tamil.utf8.get_letters(word)[-2]) not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):           
                    if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) == 'இ':
                        fixed_list.append(word)
                        print("மிகா - Rule16 - " + word)
                        counter = counter+1
                        continue

        # இன்றைய செய்தி 
        if len(tamil.utf8.get_letters(word)) > 1:
            if ''.join(tamil.utf8.get_letters(word)[-1]) == 'ய':   
                if ''.join(tamil.utf8.get_letters(word)[-2]) not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):          
                    if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) == 'ஐ':
                        fixed_list.append(word)
                        print("மிகா - Rule17 - " + word)
                        counter = counter+1
                        continue

        # கேட்கும் பாட்டு
        if len(tamil.utf8.get_letters(word)) > 1:
            if ''.join(tamil.utf8.get_letters(word)[-1]) == 'ம்':  
                if ''.join(tamil.utf8.get_letters(word)[-2]) not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):         
                    if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) == 'உ':
                        fixed_list.append(word)
                        print("மிகா - Rule18 - " + word)
                        counter = counter+1
                        continue

        if ''.join(tamil.utf8.get_letters(word)[-2:]) == 'ன்றி':  
            if ''.join(tamil.utf8.get_letters(word)[-3]) not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):            
                if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-3])[1]) == 'இ':
                    fixed_list.append(word)
                    print("மிகா - Rule19 - " + word)
                    counter = counter+1
                    continue

        # கற்ற சிறுவன் 
        if ''.join(tamil.utf8.get_letters(word)[-2:]) in ['ற்ற','ல்ல','ட்ட','ன்ற','ந்த','த்து','இனி']:            
            fixed_list.append(word)
            print("மிகா - Rule20 - " + word)
            counter = counter+1
            continue

        # வல்லினம் மிகா மற்ற வினையெச்சங்கள் - ஆக, அன, யுற,றகு,க்கு ஆகிய  விகுதிகள் பெற்று முடியும்  
        # அழியாத கல்வி 
        if ''.join(tamil.utf8.get_letters(word)[-1:]) == 'க': 
            if ''.join(tamil.utf8.get_letters(word)[-2]) not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):             
                if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) == 'ஆ':
                    fixed_list.append(word)
                    print("மிகா - Rule21 - " + word)
                    counter = counter+1
                    continue

        if ''.join(tamil.utf8.get_letters(word)[-1]) == 'ன':  
            if ''.join(tamil.utf8.get_letters(word)[-2]) not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):               
                if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) == 'அ':
                    fixed_list.append(word)
                    print("மிகா - Rule22 - " + word)
                    counter = counter+1
                    continue

        if ''.join(tamil.utf8.get_letters(word)[-2:]) in ['யுற','றகு','ற்கு','க்கு','போது']:            
                fixed_list.append(word)
                print("மிகா - Rule23 - " + word)
                counter = counter+1
                continue

        # வல்லினம் மிகா வியங்கோள் வினைமுற்று - வருக புலவரே
        if word in viyankol:
            fixed_list.append(word)
            print("மிகா - Rule24 - " + word)
            counter = counter+1
            continue
        

        # வல்லினம் மிகா இரட்டைக் கிளவி, அடுக்குத்தொடர்கள் - கல கல
        if word == words[counter + 1]:
            fixed_list.append(word)
            print("மிகா - Rule25 - " + word)
            counter = counter+1
            continue

        # வல்லினம் மிகா கள், தல் விகுதிகள் - வாக்குகள்  வித்தியாசம் 
        if ''.join(tamil.utf8.get_letters(word)[-2:]) in ['கள்','தல்']:
            fixed_list.append(word)
            print("மிகா - Rule26 - " + word)
            counter = counter+1
            continue

        # வல்லினம் மிகா பல, சில, ஏவல் வினை - வா கலையரசி
        if word in ['கல', 'பல','சில','வா','எழு','போ','பார்'] :
            fixed_list.append(word)
            print("மிகா - Rule27 - " + word)
            counter = counter+1
            continue

        # வல்லினம் மிகா பொதுப்பெயர்கள்,உயர்திணைப் பெயர்கள்,வடமொழி சொற்கள்  - மகளிர் கல்லூரி 
        if word in noun_list :   
            fixed_list.append(word)
            print("மிகா - Rule28 - " + word)
            counter = counter+1
            continue

        # 6.1.1 சுட்டு, வினா அடியாகத் தோன்றிய சொற்கள் முன் வல்லினம் மிகல் - அந்த பையன்          
        if (tamil.utf8.get_letters(word)) in suttu_vina:
            if (tamil.utf8.get_letters(word)[-1]) not in mei_letters:
                if ''.join(tamil.utf8.get_letters(word)[1:3]) == 'வ்வா':
                    fixed_list.append(word)
                    print("மிகா - Rule29 - " + word)
                    counter = counter+1
                    continue  
                if ''.join(tamil.utf8.get_letters(word)[-2:]) != 'டைய':
                    first_char_of_next_word = (words[counter + 1][0])
                    if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                        mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                        if mei_of_first_char_of_next_word in vallinam_letters:
                            fixed_list.append(word + mei_of_first_char_of_next_word)
                            print("மிகும் - Rule2 - " + word + mei_of_first_char_of_next_word)
                            counter = counter+1
                            continue  

        # 6.1.3 - 1 வன்தொடர்க் குற்றியலுகரம் முன் வல்லினம் மிகல் - கற்று கொடுத்தான் 
        if len(tamil.utf8.get_letters(word)) > 1:        
            if (tamil.utf8.get_letters(word)[-2]) in vallinam_letters:
                uyir_of_last_char = tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]
                if uyir_of_last_char == 'உ':                
                    first_char_of_next_word = (words[counter + 1][0])
                    if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                        mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                        if mei_of_first_char_of_next_word in vallinam_letters:                    
                            fixed_list.append(word + mei_of_first_char_of_next_word)   
                            print("மிகும் - Rule3 - " + word + mei_of_first_char_of_next_word)
                            counter = counter+1
                            continue

        # 6.1.3 - 2 மென்தொடர்க் குற்றியலுகரம் முன்  வல்லினம் மிகல் - குரங்கு குட்டி 
        if len(tamil.utf8.get_letters(word)) > 1:     
            if (tamil.utf8.get_letters(word)[-2]) in mellinam_letters:
                uyir_of_last_char = tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]
                if uyir_of_last_char == 'உ':
                    if ''.join(tamil.utf8.get_letters(word)[-3:]) != 'கொண்டு':
                        first_char_of_next_word = (words[counter + 1][0])
                        if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                            mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                            if mei_of_first_char_of_next_word in vallinam_letters:
                                fixed_list.append(word + mei_of_first_char_of_next_word)            
                                print("மிகும் - Rule4 - " + word + mei_of_first_char_of_next_word)
                                counter = counter+1
                                continue

        # 6.1.4 முற்றியலுகரச் சொற்கள் முன் வல்லினம் மிகல் - 1 - தனிக் குறில் அடுத்து வரும் உகரம்  - பொது பணி   
        if len(tamil.utf8.get_letters(word)) == 2:
            if tamil.utf8.get_letters(word)[-2] not in uyir_letters:
                if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) in kuril_letters:                
                    uyir_of_last_char = tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]
                    if uyir_of_last_char == 'உ':
                        first_char_of_next_word = (words[counter + 1][0])
                        if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                            mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                            if mei_of_first_char_of_next_word in vallinam_letters:                            
                                fixed_list.append(word + mei_of_first_char_of_next_word)              
                                print("மிகும் - Rule5 - " + word + mei_of_first_char_of_next_word)
                                counter = counter+1
                                continue

        # 6.1.3 - 3   உயிர்த்தொடர்க் குற்றியலுகரம் முன் வல்லினம் மிகல் - விறகு கடை
        if len(tamil.utf8.get_letters(word)) > 1:  
            if tamil.utf8.get_letters(word)[-2] not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english + english):    
                if tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1] in uyir_letters:
                    uyir_of_last_char = tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]
                    if uyir_of_last_char == 'உ':
                        first_char_of_next_word = (words[counter + 1][0])
                        if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                            mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                            if mei_of_first_char_of_next_word in vallinam_letters:                        
                                fixed_list.append(word + mei_of_first_char_of_next_word)              
                                print("மிகும் - Rule6 - " + word + mei_of_first_char_of_next_word)
                                counter = counter+1
                                continue

        # 6.1.4 - 1 - வல்லினமெய் அல்லாத பிற மெய்களின் மேல் ஏறி வருகின்ற உகரம் - தேர்வு கட்டணம்      
        if len(tamil.utf8.get_letters(word)) > 1:
            if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[0]) not in ['க்','ச்','ட்','த்','ப்','ற்']:
                if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == 'உ':
                    first_char_of_next_word = (words[counter + 1][0])
                    if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                        mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                        if mei_of_first_char_of_next_word in vallinam_letters:                    
                            fixed_list.append(word + mei_of_first_char_of_next_word)              
                            print("மிகும் - Rule7 - " + word + mei_of_first_char_of_next_word)
                            counter = counter+1
                            continue

        # 6.1.5 - 1 - இரண்டாம் வேற்றுமை விரி - கனியை  தின்றான்    
        if len(tamil.utf8.get_letters(word)) > 1: 
            if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == 'ஐ':
                first_char_of_next_word = (words[counter + 1][0])
                if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                    mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                    if mei_of_first_char_of_next_word in vallinam_letters:                
                        fixed_list.append(word + mei_of_first_char_of_next_word)              
                        print("மிகும் - Rule8 - " + word + mei_of_first_char_of_next_word)
                        counter = counter+1
                        continue

        # 6.1.5 - 2 -  நான்காம் வேற்றுமை விரி - எனக்கு  கொடு
        if len(tamil.utf8.get_letters(word)) > 1:     
            if tamil.utf8.get_letters(word)[-1] == 'கு':
                first_char_of_next_word = (words[counter + 1][0])
                if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                    mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                    if mei_of_first_char_of_next_word in vallinam_letters:                
                        fixed_list.append(word + mei_of_first_char_of_next_word)              
                        print("மிகும் - Rule9 - " + word + mei_of_first_char_of_next_word)
                        counter = counter+1
                        continue

        # 6.1.6 - 1 - அ இ ய் ர் - அகர, இகர, யகர மெய் ஈற்று வினையெச்சம்; ஈறுகெட்ட எதிர்மறைப் பெயரெச்சம் ்
        # வர சொன்னான் குறிஞ்சி தலைவன்  தேங்காய் சட்னி  தயிர் குடம் தீரா சிக்கல் 
        if len(tamil.utf8.get_letters(word)) > 1:
            if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == 'அ':
                if ''.join(tamil.utf8.get_letters(word)[-2:]) != 'டைய':
                    first_char_of_next_word = (words[counter + 1][0])
                    if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                        mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                        if mei_of_first_char_of_next_word in vallinam_letters:                    
                            fixed_list.append(word + mei_of_first_char_of_next_word)              
                            print("மிகும் - Rule10 - " + word + mei_of_first_char_of_next_word)
                            counter = counter+1
                            continue
        if len(tamil.utf8.get_letters(word)) > 1:
            if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == 'இ':
                first_char_of_next_word = (words[counter + 1][0])
                if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                    mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                    if mei_of_first_char_of_next_word in vallinam_letters:                
                        fixed_list.append(word + mei_of_first_char_of_next_word)              
                        print("மிகும் - Rule11 - " + word + mei_of_first_char_of_next_word)
                        counter = counter+1
                        continue        
    
        if len(tamil.utf8.get_letters(word)) > 1:
            if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])) == 'ய்':
                first_char_of_next_word = (words[counter + 1][0])
                if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                    mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                    if mei_of_first_char_of_next_word in vallinam_letters:                
                        fixed_list.append(word + mei_of_first_char_of_next_word)              
                        print("மிகும் - Rule12 - " + word + mei_of_first_char_of_next_word)
                        counter = counter+1
                        continue

        if len(tamil.utf8.get_letters(word)) > 1:
            if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])) == 'ர்':            
                first_char_of_next_word = (words[counter + 1][0])
                if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                    mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                    if first_char_of_next_word in special_chars:
                        fixed_list.append(word)
                        print("மிகா - Rule13 - " + word)
                        counter = counter+1
                        continue
                    if mei_of_first_char_of_next_word in vallinam_letters:                    
                        fixed_list.append(word + mei_of_first_char_of_next_word)              
                        print("மிகும் - Rule14 - " + word + mei_of_first_char_of_next_word)
                        counter = counter+1
                        continue 

        if len(tamil.utf8.get_letters(word)) > 1:
            if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == 'ஆ':
                first_char_of_next_word = (words[counter + 1][0])
                if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                    mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                    if mei_of_first_char_of_next_word in vallinam_letters:                
                        fixed_list.append(word + mei_of_first_char_of_next_word)              
                        print("மிகும் - Rule15 - " + word + mei_of_first_char_of_next_word)
                        counter = counter+1
                        continue  

        # 6.1.7 - மகர இறுதி கெட்டு உயிர் ஈறாய் நிற்கும் சொற்கள் - மரம் கிளை
        # But this logic tot working for - உலகப்படம்  பார்த்து,  எடுப்பதெல்லாம் பெரிய
        # if len(tamil.utf8.get_letters(word)) > 1:
            # if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])) == 'ம்':
            #     if ''.join(tamil.utf8.get_letters(word)[-2]) not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
            #         if tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1] in uyir_letters:
            #             first_char_of_next_word = (words[counter + 1][0])
            #             if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda):
            #                 if first_char_of_next_word not in ayudha_letter:
            #                     mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
            #                     if mei_of_first_char_of_next_word in vallinam_letters:                    
            #                         fixed_list.append(word[:-2] + mei_of_first_char_of_next_word)            
            #                         print("மிகும் - Rule16 - " + word[:-2] + mei_of_first_char_of_next_word)
            #                         counter = counter+1
            #                         continue     

        fixed_list.append(word)        
        print("Rules" + word)
        counter = counter+1

check_sandhi(words)
file_opt.write(' '.join(fixed_list))
file_opt.close()
print (set(words).difference(fixed_list))



    
