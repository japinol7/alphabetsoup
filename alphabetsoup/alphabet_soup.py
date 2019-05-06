"""Module alphabet_soup."""
__author__ = 'Joan A. Pinol  (japinol)'
__all__ = ["AlphabetSoup"]

from sys import exit
import logging

from alphabetsoup.utils import remove_diacritics_from_str


# Module Constants
WORDS_MIN_CHARS = 3    # Minimum characters for each word to be searched
WORDS_MIN_SEARCH = 1   # Minimum words to be searched
SOUP_MIN_ROWS = 7      # Minimum rows in the table that represents the alphabet soup
SOUP_MIN_COLS = 7      # Minimum columns in the table that represents the alphabet soup
READ_WORDS_FROM_FILE = "read_from_dictionary"      # String used to know if the words to be found will be read from a dictionary in a external file
MORE_INFO_STRING = "more_info"  # String used to know if we have to display more info
SAVE_BUFFER_EACH_N_WORDS = 90   # How many words to be found before saving the buffer to the output file
PR_DOT_EACH_N_WORDS = 4000      # How many words searched between progress dots
PR_DOT_NEW_LINE = 50            # How many words written before new line of dots
SOUP_NAME_DEFAULT = "Alphabet Soup"
DIACRITICS_PRESERVE_CHAR_SET = ('ñ', 'ç')   # When removing diacritics normalizing a string, the chars in the tuple will be preserved
# Files
IN_FILE_DEFAULT = "files/input_soup.txt"
OUT_FILE_DEFAULT = "output/output_soup.txt"
EXTERNAL_DICT_FILE_DEFAULT = "files/soup_dictionary.txt"   # External dictionary file for the words to search
# Errors
ERROR_IN_FILE = "!!! ERROR: Input file: %s. Search aborted !!!"
ERROR_IN_FILE_CONSOLE = "!!! ERROR: Input file: See the output file for more details. Search aborted !!!"
ERROR_OUT_FILE_OPEN = "!!! ERROR: Output file: %s. Search aborted !!!"
ERROR_OUT_FILE_WRITING = "!!! ERROR writing output file: %s. Some information has been lost. Search aborted !!!"
ERROR_OUT_FILE_MAX_TRIES = "!!! ERROR: Too much tries failed writing to the output file: %s. Search aborted !!!"
MAX_ERRORS_OUT_FILE = 5         # Max writing errors when trying to write the buffer to the output file


logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s: %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class AlphabetSoup:
    """Solves an alphabet soup finding a given list of words inside it."""

    def __init__(self, name=None, in_file=None, out_file=None, external_dict_file=None,
                 more_info=None, remove_diacritics=None):
        self._name = str(name) if name else SOUP_NAME_DEFAULT
        self._in_file = str(in_file) if in_file else IN_FILE_DEFAULT
        self._out_file = str(out_file) if out_file else OUT_FILE_DEFAULT
        self._external_dict_file = str(external_dict_file) if external_dict_file else EXTERNAL_DICT_FILE_DEFAULT
        self._read_words_from_file = True if external_dict_file else False
        self._more_info = True if more_info else False    # If true, calculates and displays more info, mainly in the summary
        self._remove_diacritics = True if remove_diacritics else False    # If true, removes diacritics from the words to find
        self._num_rows = 0
        self._num_cols = 0
        self._soup = []            # The alphabet soup
        self._words = []           # Words to find
        self._num_words = 0        # Number of words to find
        self._words_found = set()
        self._num_words_too_short = 0
        self._str_out = []                   # List of strings to save to the output file
        self._error_in_file = False          # If true, and error in the input file has been detected.
        self._num_errors_out_file = 0        # How many errors writing the output file
        self._progress_dots_count = 0        # How many progress dots have been displayed

        # Put soup's name to the buffer of the output file.
        self._write_line('%s\n%s' % (self._name, '-' * len(self._name)))

    def read_data(self):
        """Reads the words to find and the alphabet soup."""
        self._print_progress_dots(char_str='[')
        try:
            with open(self._in_file, "r", encoding='utf-8') as in_file:
                i = 0
                for line_in in in_file:
                    line = line_in.lower().replace('\n', '').replace(' ', '')
                    if i == 0:
                        # Read the list of words to find from the first line if the words are not to be read from a file.
                        if line != READ_WORDS_FROM_FILE and not self._read_words_from_file:
                            self._words = line.split(',')
                        else:
                            # The words to find will be read from an external file.
                            self._read_words_from_file = True
                    elif i >= 2:
                        # Read the characters in the soup until it founds an empty line.
                        if line == '':
                            break
                        self._soup.append(line)
                        # The first row will determine the number of columns.
                        if i == 2:
                            self._num_cols = len(line)
                        else:
                            if len(line) != self._num_cols:
                                break
                    i += 1
        except FileNotFoundError:
            self._error_in_file = True
            self._write_line(f"Input file not found: {self._in_file}")
        except Exception:
            self._error_in_file = True

        self._num_rows = len(self._soup)
        # Read the words to find from an external file if necessary.
        if self._read_words_from_file:
            self._read_words_to_find_from_file()
        else:
            # Discard the words to find that have too few characters.
            for word in self._words[:]:
                if len(word) < WORDS_MIN_CHARS:
                    self._num_words_too_short += 1
                    self._words.remove(word)

        # Remove diacritics from the words to find
        if self._remove_diacritics:
            self._words = [remove_diacritics_from_str(word, preserve_char_set=DIACRITICS_PRESERVE_CHAR_SET)
                           for word in self._words]

        # Remove duplicated words to find and sort the list.
        self._words = list(set(self._words))
        self._words.sort()

        self._num_words = len(self._words)
        # Check if there is something wrong with the input data.
        if not self._error_in_file:
            self._validate_input_data()

        # Check if error reading an input file.
        if self._error_in_file:
            self._write_line(ERROR_IN_FILE % self._in_file)
        self._write_data_to_file(open_method='w')

    def search_words_in_the_soup(self):
        """Searches the words in the alphabet soup."""
        self._print_progress_dots()
        if (self._error_in_file):
            logger.critical(ERROR_IN_FILE_CONSOLE)
            return

        self._write_header_of_the_search()

        # Search the words in the soup.
        self._write_line(self._format_msg_word_found_header())
        num_words_searched = 0
        num_words_found = 0
        for word in self._words:
            num_words_found += self._search_word_in_the_soup(word)
            num_words_searched += 1
            if num_words_found >= SAVE_BUFFER_EACH_N_WORDS:
                self._write_data_to_file()
                num_words_found = 0
            if num_words_searched == PR_DOT_EACH_N_WORDS:
                self._print_progress_dots()
                num_words_searched = 0
        self._print_progress_dots()

        # Write the summary of the search.
        self._write_summary_of_the_search()
        self._print_progress_dots(char_str=']')

        # Check if all the buffer has been written to the output file.
        if self._str_out and self._num_errors_out_file > 0:
            logger.critical(ERROR_OUT_FILE_WRITING % self._out_file)
            exit()

    def _read_words_to_find_from_file(self):
        """Reads the words to find from an external file. This file must have a word for line."""
        try:
            self._write_line(f"The words to find will be taken from the file: {self._external_dict_file}")
            with open(self._external_dict_file, "r", encoding='utf-8') as in_file:
                for line_in in in_file:
                    line = line_in.strip().replace("\n", "").replace(" ", "").lower()
                    if len(line) >= WORDS_MIN_CHARS:
                        self._words.append(line)
                    else:
                        self._num_words_too_short += 1
        except FileNotFoundError:
            self._error_in_file = True
            self._write_line(f"Input file not found: {self._external_dict_file}")
        except Exception:
            self._error_in_file = True

    def _validate_input_data(self):
        """Validates the input data."""
        # Check the dimensions of the soup.
        for wordSoup in self._soup:
            if len(wordSoup) != self._num_cols: 
                self._error_in_file = True
                self._write_line(f"!!! ERROR: The first row of the soup has {self._num_cols} columns. "
                                 "Every other row must have this very number of columns !!!")
                return
        # Check rows, columns and minimum words to search.
        if (self._num_rows < SOUP_MIN_ROWS or self._num_cols < SOUP_MIN_COLS
                or self._num_words < WORDS_MIN_SEARCH):
            self._error_in_file = True
            self._write_line("!!! Input data error. Some of the following rules has been violated: !!!")
            self._write_line(f"    > Minimum rows: {SOUP_MIN_ROWS}")
            self._write_line(f"    > Minimum columns: {SOUP_MIN_COLS}")
            self._write_line(f"    > Minimum words to find: {WORDS_MIN_SEARCH}")

    def _search_word_in_the_soup(self, word):
        """Searches a word in the alphabet soup."""
        word_len = len(word)
        num_words_found = 0
        for i in range(self._num_rows):     # Go through rows
            for j in range(self._num_cols):    # Go through columns
                if word[0] == self._soup[i][j]:   # Find the first char. of the current word in the soup
                    for p in range(word_len):       # Check horitz. left->right
                        if (j + p) >= self._num_cols:
                            break
                        elif word[p] != self._soup[i][j + p]:
                            break
                        if p == word_len - 1:
                            self._words_found.add(word)
                            num_words_found += 1
                            self._write_line(self._format_msg_word_found(word, i, j, "left--> right"))
                    for p in range(word_len):       # Check horitz. right->left
                        if (j - p) < 1:
                            break
                        elif word[p] != self._soup[i][j - p]:
                            break
                        if p == word_len - 1:
                            self._words_found.add(word)
                            num_words_found += 1
                            self._write_line(self._format_msg_word_found(word, i, j, "right--> left"))
                    for p in range(word_len):       # Check vertical top->bottom
                        if (i + p) >= self._num_rows:
                            break
                        elif word[p] != self._soup[i + p][j]:
                            break
                        if p == word_len - 1:
                            self._words_found.add(word)
                            num_words_found += 1
                            self._write_line(self._format_msg_word_found(word, i, j, "top--> bottom"))
                    for p in range(word_len):       # Check vertical bottom->top
                        if (i - p) < 1:
                            break
                        elif word[p] != self._soup[i - p][j]:
                            break
                        if p == word_len - 1:
                            self._words_found.add(word)
                            num_words_found += 1
                            self._write_line(self._format_msg_word_found(word, i, j, "bottom--> top"))
                    for p in range(word_len):       # Check diagonal top->bottom left->right
                        if (i + p >= self._num_rows) or (j + p >= self._num_cols):
                            break
                        elif word[p] != self._soup[i + p][j + p]:
                            break
                        if p == word_len - 1:
                            self._words_found.add(word)
                            num_words_found += 1
                            self._write_line(self._format_msg_word_found(word, i, j, "diag. top->bottom, left->right"))
                    for p in range(word_len):       # Check diagonal bottom->top left->right
                        if (i - p < 1) or (j + p >= self._num_cols):
                            break
                        elif word[p] != self._soup[i - p][j + p]:
                            break
                        if p == word_len - 1:
                            self._words_found.add(word)
                            num_words_found += 1
                            self._write_line(self._format_msg_word_found(word, i, j, "diag. bottom->top left->right"))
                    for p in range(word_len):       # Check diagonal top->bottom right->left
                        if (i + p >= self._num_rows) or (j - p < 1):
                            break
                        elif word[p] != self._soup[i + p][j - p]:
                            break
                        if p == word_len - 1:
                            self._words_found.add(word)
                            num_words_found += 1
                            self._write_line(self._format_msg_word_found(word, i, j, "diag. top->bottom, right->left"))
                    for p in range(word_len):       # Check diagonal bottom->top right->left
                        if (i - p < 1) or (j - p < 1):
                            break
                        elif word[p] != self._soup[i - p][j - p]:
                            break
                        if p == word_len - 1:
                            self._words_found.add(word)
                            num_words_found += 1
                            self._write_line(self._format_msg_word_found(word, i, j, "diag. bottom->top right->left"))
        return num_words_found

    def _write_header_of_the_search(self):
        """Writes the header of the search."""
        if self._num_words_too_short > 0:
            self._write_line(f'\nNumber of words rejected because they have less than {WORDS_MIN_CHARS} characters: '
                             f'{self._num_words_too_short}')
        self._write_line(f'Number of words to find: {self._num_words}\n')
        self._write_data_to_file()

    def _write_summary_of_the_search(self):
        """Writes the summary of the search."""
        self._write_line(f'\n------\nNumber of words found: {len(self._words_found)}')
        self._write_data_to_file()

        # Write more summary info.
        if self._more_info:
            self._words_found = list(self._words_found)
            self._words_found.sort()
            words_not_found = set()
            for word in self._words:
                if (word not in self._words_found):
                    words_not_found.add(word)
            words_not_found = list(words_not_found)
            words_not_found.sort()
            self._write_line("\n\n------- More info -------\n")
            self._write_line(f"Words found: \n{self._words_found}\n")
            self._write_line(f"Number of words not found: {len(words_not_found)}\n")
            self._write_line(f"These words are not in the soup: \n{words_not_found}")
            self._write_data_to_file()

    def _format_msg_word_found(self, word, i, j, direction_txt):
        """Formats the message for a word found. Return a string."""
        return '%s %s , %s  %s' % (word.ljust(11), str(i+1).rjust(2), str(j+1).rjust(2), direction_txt)

    def _format_msg_word_found_header(self):
        """Formats the header for the messages for words found. Return a string."""
        return '%s %s , %s  %s\n%s' % ("word".ljust(11), "y".rjust(2), "x".rjust(2), "direction", "-" * 51)

    def _write_line(self, line):
        """Writes a line to the output file."""
        self._str_out.append(f'{line}\n')

    def _write_data_to_file(self, open_method='a'):
        """Writes the data still in the buffer to the output file."""
        if not self._str_out:
            return
        try:
            with open(self._out_file, open_method, encoding='utf-8') as out_file:
                for line in self._str_out:
                    out_file.write(line)
        except Exception:
            if open_method == 'w':
                logger.critical(ERROR_OUT_FILE_OPEN % self._out_file)
                exit()
            else:
                self._num_errors_out_file += 1
                if self._num_errors_out_file >= MAX_ERRORS_OUT_FILE:
                    logger.critical(ERROR_OUT_FILE_MAX_TRIES % self._out_file)
                    exit()
            return
        self._str_out = []

    def _print_progress_dots(self, char_str='.'):
        """Displays progress dots to the console."""
        print(char_str, end='', flush=True)
        self._progress_dots_count += 1
        if self._progress_dots_count == PR_DOT_NEW_LINE:
            print()
            self._progress_dots_count = 0
