import hashtotable
import filecmp

testfile = "dummydata.txt"

def test_calc_sha1_file():
    sha1 = hashtotable.calc_sha1_file(testfile)
    assert sha1 == "83fc12e971e966f4716f8146e931f13fa78d91ba", "Error while calculating the checksum of the test file"


def test_listfiles():
    files = hashtotable.listfiles(".")
    assert files == ['./dummydata.txt', './requirements.txt,', './hashtotable.py', './test_hashtotable.py'], "Error while listing the files"


def test_save_list_csv():
    #hashes = hashtotable.generate_list_hash('.')
    hashes = ('dummydata','83fc12e971e966f4716f8146e931f13fa78d91ba')
    newfile = hashtotable.save_list_csv('testtable.csv', hashes)
    assert filecmp.cmp(newfile,'expectedtable.csv'),'Error while listing the hashes' 


def test_save_list_doc():
    hashes = ('dummydata','83fc12e971e966f4716f8146e931f13fa78d91ba')
    newfile = hashtotable.save_list_doc('testtable.doc', hashes)
    assert filecmp.cmp(newfile,'expectedtable.docx'),'Error while listing the hashes' 


