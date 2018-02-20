# -*- coding: utf-8 -*-
# Test for sandhi rules
# 
# This file is part of 'tamil-sandhi-rules' package tests
# 

# setup the paths
from sandhitests import *
import tamil.utf8 as utf8 
import codecs

if PYTHON3:
    class long(int):
        pass

class SandhiTest(unittest.TestCase):
    def test_integration(self):
        golden = u"அங்குக் கண்டான் அந்தப் பையன். எத்தனை பழங்கள்? கண்டவாறு சொன்னான், ஐந்து சிறுவர்கள், கத்தியோடு நின்றான்,கத்திகொண்டு குத்தினான், வீட்டிலிருந்து சென்றான், கைக் குழந்தை, கற்று கொடுத்தான், குரங்குக் குட்டி, விறகுக் கடை, பொதுப் பணி, தேர்வுக் கட்டணம், கனியைத் தின்றான்,எனக்குக் கொடு, வீட்டினின்று வெளியேறினான், வரச் சொன்னான், என்னுடைய புத்தகம், எனது புத்தகம், குறிஞ்சித் தலைவன், தேங்காய்ச் சட்னி, தயிர்க் குடம், தீராச் சிக்கல், மரத் தலைவன்."
        source =u"அங்குக் கண்டான் அந்த பையன். எத்தனை பழங்கள்?  கண்டவாறு சொன்னான், ஐந்து சிறுவர்கள், கத்தியோடு  நின்றான்," \
                 u"கத்திகொண்டு குத்தினான், வீட்டிலிருந்து  சென்றான், கை குழந்தை,  கற்று கொடுத்தான், குரங்கு குட்டி, விறகு கடை, பொது பணி,  தேர்வு  கட்டணம், கனியை தின்றான்," \
                 u"எனக்கு கொடு, வீட்டினின்று வெளியேறினான், வர சொன்னான், என்னுடைய புத்தகம், எனது புத்தகம், குறிஞ்சி தலைவன், தேங்காய் சட்னி,  தயிர் குடம், தீரா சிக்கல், மரம் தலைவன்."
        fixed,res = check_sandhi(source)
        fixed_string = u" ".join(fixed)
        self.assertEqual(fixed_string,golden)
        self.assertTrue(isinstance(res,Results))
        self.assertEqual(res.counter,46)

#TBD: to be added
class SandhiRuleTest(unittest.TestCase):
    def test_rule1(self):
        pass
    def test_rule2(self):
        pass
    def test_rule3(self):
        pass
    def test_rule4(self):
        pass
    def test_rule5(self):
        pass
    def test_rule6(self):
        pass
    def test_rule7(self):
        pass
    def test_rule8(self):
        pass
    def test_rule9(self):
        pass
    def test_rule10(self):
        pass
    def test_rule11(self):
        pass
    def test_rule12(self):
        pass
    def test_rule13(self):
        pass
    def test_rule14(self):
        pass
    def test_rule15(self):
        pass

if __name__ == u'__main__':
    unittest.main()
