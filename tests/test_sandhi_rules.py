# -*- coding: utf-8 -*-
# Test for sandhi rules
#
# This file is part of 'tamil-sandhi-rules' package tests
#

# setup the paths
from sandhitests import PYTHON3, unittest
from tamilsandhi.sandhi_checker import safe_splitMeiUyir, check_sandhi, sandhi_checker_file_IO, Results
import tamil.utf8 as utf8
import codecs
import os


if PYTHON3:
    class long(int):
        pass

class SandhiTest(unittest.TestCase):
    def test_integration(self):
        golden = u"அங்குக் கண்டான் அந்த பையன். எத்தனைப் பழங்கள்? கண்டவாறு சொன்னான், ஐந்து சிறுவர்கள், கத்தியோடு நின்றான்,கத்திகொண்டு குத்தினான், வீட்டிலிருந்து சென்றான், கைக் குழந்தை, கற்று கொடுத்தான், குரங்கு குட்டி, விறகு கடை, பொது பணி, தேர்வு கட்டணம், கனியைத் தின்றான்,எனக்கு கொடு, வீட்டினின்று வெளியேறினான், வர சொன்னான், என்னுடைய புத்தகம், எனது புத்தகம், குறிஞ்சி தலைவன், தேங்காய் சட்னி, தயிர் குடம், தீராச் சிக்கல், மரம் தலைவன்."
        source =u"அங்குக் கண்டான் அந்த பையன். எத்தனை பழங்கள்?  கண்டவாறு சொன்னான், ஐந்து சிறுவர்கள், கத்தியோடு  நின்றான்," \
                 u"கத்திகொண்டு குத்தினான், வீட்டிலிருந்து  சென்றான், கை குழந்தை,  கற்று கொடுத்தான், குரங்கு குட்டி, விறகு கடை, பொது பணி,  தேர்வு  கட்டணம், கனியை தின்றான்," \
                 u"எனக்கு கொடு, வீட்டினின்று வெளியேறினான், வர சொன்னான், என்னுடைய புத்தகம், எனது புத்தகம், குறிஞ்சி தலைவன், தேங்காய் சட்னி,  தயிர் குடம், தீரா சிக்கல், மரம் தலைவன்."
        fixed,res = check_sandhi(source)
        fixed_string = u" ".join(fixed)
        #import pprint
        #pprint.pprint(u"%s"%fixed_string)
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

class APITest(unittest.TestCase):
    def test_integ_file_IO(self):
        BASEDIR = os.path.split(__file__)[0]
        ip = os.path.join(BASEDIR,u"test_in.txt")
        op = os.path.join(BASEDIR,u"test_op.txt")
        gold_op = codecs.open(os.path.join(BASEDIR,u"test_gold.txt"),"r","UTF-8").read()
        sandhi_checker_file_IO(ip , op )
        with codecs.open(op,"r","UTF-8") as op_handle:
            op_text = op_handle.read()
        os.unlink( op )
        self.assertEqual( op_text+u"\n", gold_op)
        
    def test_split_mei_uyir(self):
        #from pprint import pprint
        ip=[u"அ",u"க்",u"க",u"கோ",u"கப்பல்","fubar","f"]
        gold = [(u'', u'\u0b85'),(u'\u0b95\u0bcd', u''),(u'\u0b95\u0bcd', u'\u0b85'),(u'\u0b95\u0bcd', u'\u0b93'),(u'', u''),(u'', u''),(u'', u'')]
        op = []
        for l in ip:
            r=safe_splitMeiUyir(l)
            #print(u"%s"%l)
            op.append(r)
            
        self.assertEqual( op, gold )
        return

if __name__ == u'__main__':
    unittest.main()
