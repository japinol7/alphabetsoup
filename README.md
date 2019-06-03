## Alphabet Soup

	 program: alphabet_soup
	 version: 1.0.2
	 language: English
	 author: Joan A. Pinol
	 author_nickname:  japinol
	 author_gitHub: japinol7
	 author_twitter: @japinol
	 main module: alphabet_soup.py
	 other modules: utils.py
	 Python requires: 3.6 or greater.
	 Python versions tested: 3.6.6 and 3.7.1 64bits under Windows 10.  Last minor changes tested with v. 3.7.3
	
	 Objective: To solve an alphabet soup finding a given list of words inside it.
	 Input (text file):
	    Line  1: The words to find, separated by commas.
	             > If the words are in a language that uses written accents, these written accents must be left out.
	               For Example: "ànima" (Catalan) must be written as "anima".
				 > If in the line 1 there is the word and only the word "read_from_dictionary",
	               it takes the words separated by a new line from the file: "files/soup_dictionary.txt".
	    Line  2: This line will be ignored.
	    Lines 3 - N: The rows of the table that make up the soup.
	 
	 new v. 1.0.2: 
	        > Optional arguments from the command line:
	               usage: alphabetsoup [-h] [-i INFILE] [-o OUTFILE] [-d DICT] [-n NAME] [-m] [-r]
	        > Adds the flag '-r', '--rmdiacritics'. See usage below.
	        > If the command line has the flag '-m', '--moreinfo' it will display also this information:
	            > A list with the words to find.   
	            > A list with the words found in the soup.
	            > The number of words not found in the soup.
	            > A list with the words that are not in the soup.
	 
	 Output:
	    - A row for each word found, following this structure:
	         word       posY, posX      direction


## Usage		 

	alphabetsoup [-h] [-i INFILE] [-o OUTFILE] [-d DICT] [-n NAME] [-m] [-r] [-t]

	optional arguments:
	  -h, --help            show this help message and exit
	  -i INFILE, --infile INFILE
	                        input file where there is the soup to solve.
	  -o OUTFILE, --outfile OUTFILE
	                        output file where there will be written the results.
	  -d DICT, --dict DICT  input dictionary file to be used for the the words to
	                        find.
	  -n NAME, --name NAME  name of te soup.
	  -m, --moreinfo        adds more summary info to the output file, such as
	                        the lists of words found and not found.
	  -r, --rmdiacritics    normalizes data removing diacritics from the words to
	                        find. The characters ñ and ç will not be changed for
	                        compatibility with Spanish and Catalan soups. Example:
	                        'ànim' and 'mäñanúç' will be changed to 'anim' and
	                        'mañanuç'.
	  -t, --debugtraces		show debug back traces information when something goes wrong.


**Examples of usage**

	> If alphabetsoup has been installed as an app:
		$ alphabetsoup
		$ alphabetsoup -o ./out.txt -i ./in.txt -d ./dict.txt

	> If alphabetsoup has not been installed as an app:
		$ python -m alphabetsoup
		$ python -m alphabetsoup -o ./out.txt -i ./in.txt -d ./dict.txt


**Default optional arguments**

		NAME		Alphabet Soup
		INFILE		files/input_soup.txt
		OUTFILE		output/output_soup.txt
		DICT		files/soup_dictionary.txt


**To install alphabetsoup as an app**

	Do this:
		1. Clone its repository.
		2. go to its folder in your system.
		3. $ pip install .

		
**Example of Input file "files/input_soup.txt"**

	read_from_dictionary
	----------------------------------------
	canikuufxhzpzbfkultebilhmehuphrafgtcepur
	rjngsjnrztlongarrbsmyvwaytiyojldzhaadfes
	mifeesymepiyxpvufoawwyimuqugmccutheafgax
	rettcbsvmnueplmiftpdyinghrmtwvjtaveklahc
	afwbgdjlyonfrixbzavnsnybfcevywfogcexapoh
	wcgxnposbztiewwuasrvmtrlbruvwfgatswuvics
	dqwmxeztmewgppmqdmxhanojgfcmeoclutvgelio
	rurjadsuahrsrsrcdncowvewhurtaneceipofler
	adlohdxrelxatafbseaeeoqewbfijlfcokvpcota
	wlaekqmqvbtmtzvrehtlgotsetidgrxactiyfwuc
	hfskuaueuhcdgerdjayenirpnuogasecixoceghc
	nlycfqrdwgvkicejgovvwctyvcblztortghckogr
	teyatfocjdapempumtzfwbeloandnhohnydjapzt
	xsftdunopkfgavpgcqxjaueaifixvhpzctvfcair
	gtpqvoeheohvnnecbepklecchagrmilocnkehgca
	jcfptktlaamsoopdhepfelloplxkbqleqtieactt
	qtnchxpgnbgmouwprztjmqupwlhnckaldolplear
	gwseupqourjacdfgekhwuiyaeraynxijatevirxe
	oxgkimvitowpaproliferatelvhssypmqipkciet
	kjwvloqlsijlrbowebmhshqgdkolemcedondecud
	
	
	
	
	>> Example of output file solved for the previous input file:
	
	Alphabet Soup
	-------------
	The words to find will be taken from the file: files/soup_dictionary.txt
	Number of words to find: 4829
	
	word         y ,  x  direction
	---------------------------------------------------
	anecdotal    1 ,  2  diag. top->bottom, left->right
	apocalypse  18 , 24  bottom--> top
	berate       6 ,  9  diag. top->bottom, left->right
	chalice     14 , 37  top--> bottom
	chalk        4 , 40  right--> left
	dot          5 ,  6  diag. top->bottom, left->right
	dot         14 ,  5  diag. top->bottom, left->right
	draw         7 ,  1  top--> bottom
	dreg        11 , 16  right--> left
	ego         11 , 20  diag. bottom->top left->right
	era          7 , 10  diag. top->bottom, left->right
	era         18 , 25  left--> right
	era         19 , 20  left--> right
	even         5 , 27  diag. top->bottom, left->right
	fall        14 , 26  top--> bottom
	far          1 , 33  right--> left
	far          4 , 17  diag. top->bottom, left->right
	fat          9 , 15  right--> left
	fee          3 ,  3  left--> right
	fee         14 , 36  top--> bottom
	fell        16 , 20  left--> right
	fig          5 , 12  top--> bottom
	fix          3 , 17  diag. top->bottom, right->left
	fix         14 , 26  left--> right
	fro         18 , 15  top--> bottom
	gag         12 , 10  diag. top->bottom, left->right
	gag         14 , 12  diag. bottom->top right->left
	gap          3 , 38  top--> bottom
	gap         15 , 38  bottom--> top
	gap         15 , 38  diag. top->bottom, right->left
	gape        15 , 38  diag. top->bottom, right->left
	gar          2 , 14  left--> right
	gas         11 , 28  left--> right
	gate        12 , 17  diag. bottom->top left->right
	gel          7 , 36  left--> right
	get          2 ,  4  top--> bottom
	ham          1 , 24  top--> bottom
	hem          1 , 27  right--> left
	hen         10 , 18  bottom--> top
	her         10 , 18  right--> left
	hew         20 , 20  bottom--> top
	hex          3 , 34  diag. top->bottom, left->right
	hex         16 , 17  diag. bottom->top left->right
	hoc          4 , 39  top--> bottom
	hoc         13 , 30  diag. bottom->top left->right
	hoc         15 ,  8  bottom--> top
	hoe          7 , 20  top--> bottom
	hoe         15 , 11  right--> left
	hog          1 , 30  diag. top->bottom, right->left
	hoi         12 , 35  bottom--> top
	hold         9 ,  5  right--> left
	hop          5 , 40  right--> left
	hue         11 , 10  right--> left
	hurt         8 , 25  left--> right
	hut         11 , 39  bottom--> top
	ice         11 , 33  right--> left
	ice         12 , 13  left--> right
	ice         18 , 37  top--> bottom
	imp         12 , 13  diag. top->bottom, left->right
	inch        16 , 35  diag. bottom->top right->left
	inn          6 , 12  diag. bottom->top right->left
	inner        6 , 12  diag. bottom->top right->left
	ire         19 , 38  bottom--> top
	ivy          1 , 22  top--> bottom
	ivy          8 , 34  diag. top->bottom, left->right
	jay         11 , 17  left--> right
	jet          2 ,  6  diag. top->bottom, right->left
	jot          4 , 31  diag. top->bottom, left->right
	joy          2 , 30  right--> left
	jug         12 , 16  top--> bottom
	keg         18 , 18  right--> left
	kelp        14 , 10  diag. top->bottom, right->left
	kick         9 , 34  diag. top->bottom, left->right
	kin          1 ,  5  right--> left
	kit          9 , 34  bottom--> top
	lac         13 , 24  top--> bottom
	leaf        16 , 23  diag. bottom->top right->left
	let         19 , 25  right--> left
	life        19 , 17  left--> right
	lim         15 , 31  right--> left
	lip          7 , 38  bottom--> top
	loan        13 , 24  left--> right
	long         2 , 11  left--> right
	lot         12 , 28  diag. bottom->top right->left
	love         6 , 24  diag. top->bottom, right->left
	low          8 , 38  top--> bottom
	mad          7 ,  4  diag. top->bottom, left->right
	map         17 , 12  top--> bottom
	maw          6 , 21  top--> bottom
	mew          3 ,  1  diag. top->bottom, left->right
	mew          7 ,  9  left--> right
	mew         10 ,  7  diag. top->bottom, left->right
	mop         16 , 11  diag. bottom->top right->left
	paid        16 , 25  diag. bottom->top left->right
	peanut      14 ,  9  top--> bottom
	pie          8 , 35  right--> left
	pie         13 , 12  diag. bottom->top left->right
	piece        8 , 35  right--> left
	pill         5 , 38  top--> bottom
	pillow       5 , 38  top--> bottom
	pinch       17 , 36  diag. bottom->top right->left
	pro         19 , 14  left--> right
	proliferate 19 , 14  left--> right
	rag          2 , 16  right--> left
	rat          8 , 11  diag. top->bottom, left->right
	rat          8 , 13  diag. top->bottom, right->left
	rat          8 , 15  diag. top->bottom, right->left
	rat         14 , 40  top--> bottom
	rat         18 , 38  diag. bottom->top left->right
	rat         19 , 21  left--> right
	red         18 , 38  diag. top->bottom, left->right
	rep          5 , 13  top--> bottom
	rep         11 , 15  top--> bottom
	rep         17 , 17  diag. bottom->top left->right
	rivet       18 , 38  right--> left
	rot         12 , 32  right--> left
	self        14 ,  2  bottom--> top
	spy         10 , 24  top--> bottom
	stow         5 , 21  diag. top->bottom, left->right
	stun        20 ,  9  bottom--> top
	tack        14 ,  4  bottom--> top
	tad         12 , 30  diag. bottom->top right->left
	tag          3 , 33  top--> bottom
	tag          6 , 33  right--> left
	tag         10 , 19  diag. top->bottom, right->left
	tam          4 , 18  diag. bottom->top left->right
	tan          8 , 28  left--> right
	tao          6 , 22  diag. top->bottom, right->left
	tar         10 , 11  diag. bottom->top left->right
	tar         10 , 13  diag. bottom->top left->right
	tar         10 , 13  diag. bottom->top right->left
	tar         16 , 40  bottom--> top
	tar         16 , 40  diag. top->bottom, right->left
	tar         19 , 23  right--> left
	tart        16 , 40  bottom--> top
	tax          9 , 13  right--> left
	tax         16 , 39  top--> bottom
	tea          6 , 11  diag. top->bottom, right->left
	tea         12 , 30  diag. bottom->top left->right
	tear         6 , 11  diag. top->bottom, right->left
	ted         10 , 19  diag. bottom->top right->left
	tee         10 , 13  diag. top->bottom, left->right
	tee         12 , 23  top--> bottom
	ten         16 ,  7  bottom--> top
	tenor       16 ,  7  bottom--> top
	test        10 , 26  right--> left
	the          3 , 33  left--> right
	the         10 , 19  right--> left
	tic         12 , 33  bottom--> top
	tid          8 , 28  top--> bottom
	tid         10 , 26  left--> right
	tie          2 , 10  diag. top->bottom, left->right
	tie          6 , 11  left--> right
	tie         16 , 34  left--> right
	tier         2 , 10  diag. top->bottom, left->right
	today       16 ,  7  diag. bottom->top right->left
	tog         10 , 23  right--> left
	ton         16 ,  5  diag. bottom->top left->right
	top         19 ,  9  diag. bottom->top right->left
	tor         12 , 30  left--> right
	tort        12 , 30  left--> right
	tot         16 , 34  top--> bottom
	tot         18 , 34  bottom--> top
	tow          6 , 22  diag. top->bottom, left->right
	tow         10 , 23  diag. bottom->top right->left
	tow         19 ,  9  left--> right
	tug          2 , 26  diag. top->bottom, right->left
	tun         19 ,  9  bottom--> top
	tuna        19 ,  9  bottom--> top
	villa       14 , 29  diag. top->bottom, left->right
	villain     14 , 29  diag. top->bottom, left->right
	viz          3 , 15  diag. top->bottom, left->right
	von         19 ,  7  diag. bottom->top left->right
	wale        13 , 21  top--> bottom
	war          6 ,  1  bottom--> top
	war         10 ,  1  bottom--> top
	ward        10 ,  1  bottom--> top
	warm         6 ,  1  bottom--> top
	way          2 , 23  left--> right
	web         20 , 16  left--> right
	wee          6 , 35  bottom--> top
	weld        17 , 25  top--> bottom
	wet          8 , 21  diag. top->bottom, right->left
	wet         12 , 21  diag. bottom->top right->left
	win          2 , 23  top--> bottom
	winy         2 , 23  top--> bottom
	wit         12 , 21  diag. bottom->top left->right
	yen         11 , 19  left--> right
	
	------
	Number of words found: 143
