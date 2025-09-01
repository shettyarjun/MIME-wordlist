#!/usr/bin/env python3
"""
Test script for MIME wordlist repository.
Validates the integrity and format of the MIME type and parser wordlists.
"""

import os
import sys
import codecs

def test_files_exist():
    """Test that required wordlist files exist."""
    print("Testing file existence...")
    
    required_files = ['mime_types.txt', 'mime_parsers.txt']
    for filename in required_files:
        if not os.path.exists(filename):
            print(f"❌ FAIL: {filename} does not exist")
            return False
        print(f"✅ PASS: {filename} exists")
    
    return True

def test_file_encoding():
    """Test that files are properly encoded in UTF-16BE."""
    print("\nTesting file encoding...")
    
    files = ['mime_types.txt', 'mime_parsers.txt']
    for filename in files:
        try:
            # Check for UTF-16BE BOM (0xFE 0xFF)
            with open(filename, 'rb') as f:
                bom = f.read(2)
                if bom != b'\xfe\xff':
                    print(f"❌ FAIL: {filename} does not have UTF-16BE BOM")
                    return False
            
            # Try to decode the file
            with codecs.open(filename, 'r', encoding='utf-16-be') as f:
                f.read()
            
            print(f"✅ PASS: {filename} has correct UTF-16BE encoding")
        except Exception as e:
            print(f"❌ FAIL: {filename} encoding error: {e}")
            return False
    
    return True

def test_line_counts():
    """Test that mime_types.txt and mime_parsers.txt have the same number of lines."""
    print("\nTesting line counts...")
    
    try:
        with codecs.open('mime_types.txt', 'r', encoding='utf-16-be') as f:
            types_lines = len(f.readlines())
        
        with codecs.open('mime_parsers.txt', 'r', encoding='utf-16-be') as f:
            parsers_lines = len(f.readlines())
        
        if types_lines != parsers_lines:
            print(f"❌ FAIL: Line count mismatch - mime_types.txt has {types_lines} lines, mime_parsers.txt has {parsers_lines} lines")
            return False
        
        print(f"✅ PASS: Both files have {types_lines} lines")
        return True
        
    except Exception as e:
        print(f"❌ FAIL: Error reading files: {e}")
        return False

def test_content_format():
    """Test that the content has reasonable format."""
    print("\nTesting content format...")
    
    try:
        with codecs.open('mime_types.txt', 'r', encoding='utf-16-be') as f:
            types_content = f.readlines()
        
        with codecs.open('mime_parsers.txt', 'r', encoding='utf-16-be') as f:
            parsers_content = f.readlines()
        
        # Check for empty lines
        empty_types = sum(1 for line in types_content if not line.strip())
        empty_parsers = sum(1 for line in parsers_content if not line.strip())
        
        if empty_types > 0:
            print(f"⚠️  WARNING: {empty_types} empty lines in mime_types.txt")
        
        if empty_parsers > 0:
            print(f"⚠️  WARNING: {empty_parsers} empty lines in mime_parsers.txt")
        
        # Check first few entries for basic format
        if len(types_content) > 0:
            print(f"📋 Sample mime type: {types_content[4].strip()}")  # Skip first few encoding entries
        
        if len(parsers_content) > 0:
            print(f"📋 Sample parser: {parsers_content[4].strip()}")
        
        print("✅ PASS: Content format appears reasonable")
        return True
        
    except Exception as e:
        print(f"❌ FAIL: Error analyzing content: {e}")
        return False

def main():
    """Run all tests."""
    print("🧪 MIME Wordlist Test Suite")
    print("=" * 40)
    
    tests = [
        test_files_exist,
        test_file_encoding,
        test_line_counts,
        test_content_format
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        else:
            print(f"\n❌ Test failed: {test.__name__}")
    
    print("\n" + "=" * 40)
    print(f"🏁 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("💥 Some tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())