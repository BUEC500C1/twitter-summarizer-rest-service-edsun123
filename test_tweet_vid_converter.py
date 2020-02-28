from pathlib import Path
#from flask import Flask
#import pytest
#app = Flask(__name__)
#
def test_random_test():
    assert 1==1
    
def test_does_keys_exist():
    assert Path('keys.py').is_file()
    
def test_does_mergedfile_exist():
    assert Path('mergedfile.mp4').is_file()
     
def test_does_requirements_exist():
    assert Path('requirements.txt').is_file()

def test_does_list_exist():
    assert Path('list.txt').is_file()
    
def test_does_list_exist():
    assert Path('tweet_vid_converter.py').is_file()
