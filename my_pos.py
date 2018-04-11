import argparse
import pos_tagging as pos
from nltk.tokenize import PunktSentenceTokenizer

# create a parser object
parser = argparse.ArgumentParser(description="A cli based program for POS tagging, training and testing")

# add argument
parser.add_argument("-i", "--intra", type=str, nargs="*",
                        metavar="sentence/filepath", default=None,
                        help="tag words interactively. \n use only -i to enter a sentence on cli else provide file path like -i [filepath]")

parser.add_argument("-t", "--train", type=str, nargs="*",
                        metavar="language(s)", default=None,
                        help="Train a model of given language(s)")

# parse the arguments from standard input
args = parser.parse_args()

if args.intra is not None:
    if len(args.intra) == 0:
        sentence = input('Enter a sentence for POS tagging: ')
        print('sent for POS tagging:  {}'.format(sentence))
        punktok = PunktSentenceTokenizer()
        tokenized = punktok.tokenize(text=sentence)
        POSGenerator = pos.POSGenerator(method='nltk')
        POSGenerator.process_content(tokenized_text=tokenized)

    else:  # file name input
        print('file path for POS tagging: {}'.format(args.intra[0]))
        try:
            f = open(args.intra[0])
            print('file read')
        except Exception as e:
            print(e)



if args.train is not None:
    if len(args.train) == 0:
        print('Please specify a language')
    else:
        languages = args.train
        print('Starting the training of {}'.format(languages))