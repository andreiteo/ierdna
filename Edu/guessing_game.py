#!/usr/local/bin/python3
import sys
print(sys.version)


secret_word = "girafa"
raspuns = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

#cat timp raspunsul nu e egal cu secret_word se va rula din nou
while raspuns != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        raspuns = input("Animal cu gatul lung: ")
        guess_count += 1
    else:
        out_of_guesses = True



if out_of_guesses:
    print("You are a weakling!")
else:
    print("You my sir are a champion!")
