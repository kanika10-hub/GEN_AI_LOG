##basic argument
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name")

args = parser.parse_args()

print("Hello", args.name)

#to run
python app.py Kanika

#output-
Hello Kanika


#optional argument
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--age", type=int)

args = parser.parse_args()

print(args.age)
#to run
python app.py --age 20
