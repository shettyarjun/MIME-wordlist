# MIME Wordlist

A collection of MIME types and their corresponding parsers/extensions for security research and testing.

## Files

- `mime_types.txt` - List of MIME types (UTF-16BE encoded)
- `mime_parsers.txt` - Corresponding parsers/extensions (UTF-16BE encoded)

## Testing

To validate the integrity of the wordlists:

```bash
# Run all tests
make test

# Or run directly with Python
python3 test_wordlists.py
```

The test suite validates:
- File existence
- UTF-16BE encoding format
- Matching line counts between files
- Basic content format

## Usage

The wordlists are paired - each line in `mime_types.txt` corresponds to the same line number in `mime_parsers.txt`.
