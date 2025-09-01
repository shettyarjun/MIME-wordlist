# Makefile for MIME wordlist repository
# Provides simple commands to test and validate the wordlists

.PHONY: test help clean

# Default target
help:
	@echo "MIME Wordlist Repository"
	@echo "======================="
	@echo ""
	@echo "Available commands:"
	@echo "  make test    - Run wordlist validation tests"
	@echo "  make help    - Show this help message"
	@echo "  make clean   - Clean temporary files"

# Run the test suite
test:
	@echo "Running MIME wordlist tests..."
	@python3 test_wordlists.py

# Clean temporary files
clean:
	@echo "Cleaning temporary files..."
	@find . -name "*.pyc" -delete
	@find . -name "__pycache__" -type d -exec rm -rf {} +
	@echo "Done."