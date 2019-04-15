"""Module __main__. Entry point."""
__author__ = 'Joan A. Pinol  (japinol)'
__version__ = '1.0.2'

from argparse import ArgumentParser

from alphabetsoup.alphabet_soup import AlphabetSoup

def main():
    """Main Program."""
    # Parse optional arguments from the command line
    parser = ArgumentParser(description="Alphabet Soup Solver.",
                            prog="alphabetsoup",
                            usage="%(prog)s [-h] [-i INFILE] [-o OUTFILE] [-d DICT] [-n NAME] [-m] [-r]")
    parser.add_argument('-i', '--infile', default=None,
                        help='input file where there is the soup to solve.')
    parser.add_argument('-o', '--outfile', default=None,
                        help='output file where there will be written the results.')
    parser.add_argument('-d', '--dict', default=None,
                        help='input dictionary file to be used for the the words to find.')
    parser.add_argument('-n', '--name', default=None,
                        help='name of te soup.')
    parser.add_argument('-m', '--moreinfo', default=None, action='store_true',
                        help="adds more summary info to the output file, such as the lists of words found and not found.")
    parser.add_argument('-r', '--rmdiacritics', default=None, action='store_true',
                        help="normalizes data removing diacritics from the words to find. "
                             "The characters ñ and ç will not be changed for compatibility with Spanish and Catalan soups. "
                             "Example: 'ànim' and 'mäñanúç' will be changed to 'anim' and 'mañanuç'.")
    args = parser.parse_args()

    # Solve the alphabet soup
    alphabet_soup = AlphabetSoup(name=args.name, in_file=args.infile, out_file=args.outfile, 
                                 external_dict_file=args.dict, more_info=args.moreinfo,
                                 remove_diacritics=args.rmdiacritics)
    alphabet_soup.read_data()
    alphabet_soup.search_words_in_the_soup()
    print()


if __name__ == '__main__':
    main()
