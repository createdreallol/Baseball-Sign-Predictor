import argparse
import init
import train
import predict

# NEED TO SEE HOW WELL THIS THIS WOULD DO WITH A DIFFERENT SEQ PROBLEM,
# LIKE INSTEAD OF 'GF' MAYBE SOMETHING LIKE
# 'GAF' 'GEF' 'GSF' 'GDF' WHERE THE CORRECT ANSWER IS G, ANY ELEMENT, THEN F

parser = argparse.ArgumentParser(
                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-mn','--model_name', type=str, default='model',
                    help='the name you want your model to be saved as')
parser.add_argument('-df','--data_file', type=str, default='data/train.txt',
                    help='the name you want your model to be saved as')
parser.add_argument('-md','--models_dir', type=str, default='models',
                    help='the location you want your models to be saved in')
parser.add_argument('-e','--epochs',type=int, default=100,
                    help='use -e to set the number of epochs for training')
parser.add_argument('-b','--batches',type=int, default=2048,
                    help='use -b to set the number to batch for training')
parser.add_argument('-res','--resolution',type=int, nargs='+', default=[2,3],
                    help='use -res to set the resolution')
parser.add_argument('-t', "--train", action='store_true',
                    help='add -t if you want to train')
parser.add_argument('-i', "--init", action='store_true',
                    help='add -i if you want to initilize from some data')
parser.add_argument('-p', "--predict", action='store_true',
                    help='add -p if you want to predict')
parser.add_argument('-lm', "--load_model", action='store_true',
                    help='add -lm if you want to load the model for further training')
args = parser.parse_args()

# Initilize
if args.init:
    init.init(args.data_file, args.resolution)

# Train
if args.train:
    train.train(args.data_file, args.models_dir, args.model_name, args.load_model, args.epochs, args.batches)

# Predict
if args.predict:
    check = args.data_file.split(' ')

    for p in check:
        predict.predict(p, args.models_dir, args.model_name)
