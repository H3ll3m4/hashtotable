import hashtotable
import filecmp

testfile = "dummydata.txt"

def test_calc_sha1_file():
    sha1 = hashtotable.calc_sha1_file(testfile)
    assert sha1 == "3a1852d340332de49b8b9eeb7814ca24a3e499e2", "Error while calculating the checksum of the test file"


def test_listfiles():
    files = hashtotable.listfiles(".")
    assert files == ['./dummydata.txt', './requirements.txt,', './hashtotable.py', './test_hashtotable.py'], "Error while listing the files"


def test_save_list_csv():
    hashes = ('.\dummydata.txt','3a1852d340332de49b8b9eeb7814ca24a3e499e2')
    newfile = hashtotable.save_list_csv('testtable.csv', hashes)
    assert filecmp.cmp(newfile,'expectedtable.csv'),'Error while listing the hashes' 


def test_save_list_doc():
    hashes = ('.\dummydata.txt','3a1852d340332de49b8b9eeb7814ca24a3e499e2')
    newfile = hashtotable.save_list_doc('testtable.docx', hashes)
    assert filecmp.cmp(newfile,'expectedtable.docx'),'Error while listing the hashes' 


