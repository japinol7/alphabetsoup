"""Module utils."""
__author__ = 'Joan A. Pinol  (japinol)'

from unicodedata import normalize, combining

def remove_diacritics_from_str(input_str, preserve_char_set=None):
    """Removes diacritics from a string, for the unicode characters that are tagged as diacritic.
       Returns a string with diacritics removed.
       Example 1: If you want to remove all diacritics from "Hóla cañaçö cano CAÑAÇ CANAC":
            remove_diacritics_from_str("Hóla cañaçö cano CAÑAÇ CANAC")
        It will return "Hola canaco cano CANAC CANAC".
       Example 2: If you want to remove all diacritics except for 'ñ' and 'ç' from "Hóla cañaçö cano": 
            remove_diacritics_from_str("Hóla cañaçö cano CAÑAÇ CANAC", preserve_char_set=('ñ','ç'))
        It will return "Hola cañaço cano CAÑAÇ CANAC".
    """
    norm_str = input_str
    if preserve_char_set:
        # Preserve characters in their both lower and upper versions
        preserve_chars = [(ch.lower(), normalize_str(ch.lower())) for ch in preserve_char_set]
        preserve_chars.extend([(ch.upper(), normalize_str(ch.upper())) for ch in preserve_char_set])
        for ch in preserve_chars:
            norm_str = norm_str.replace(ch[0], "<&&%s&&>" % ch[1])
    norm_str = normalize('NFKD', norm_str)
    norm_str = u"".join([c for c in norm_str if not combining(c)])
    if preserve_char_set:
        for ch in preserve_chars:
            norm_str = norm_str.replace("<&&%s&&>" % ch[1], ch[0])
    return norm_str

def normalize_str(input_str):
    """Normalizes a string removing all diacritics.
       Returns a string with diacritics removed.
    """
    res = normalize('NFKD', input_str)
    return u"".join([c for c in res if not combining(c)])
