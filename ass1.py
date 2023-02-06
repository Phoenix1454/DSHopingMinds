{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "ba293fbc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the Sentense: the quick brown fox jumps over the lazy dog\n",
      "The String is a Pangram String.\n"
     ]
    }
   ],
   "source": [
    "import string \n",
    "def check_pangram(str1): \n",
    "    alphabet = \"abcdefghijklmnopqrstuvwxyz\"\n",
    "    for char in alphabet: \n",
    "        if char not in str1.lower(): \n",
    "            return False\n",
    "    return True\n",
    "# Driver code \n",
    "str1 = input(\"Enter the Sentense: \")\n",
    "if(check_pangram(str1) == True): \n",
    "    print(\"The String is a Pangram String.\") \n",
    "else: \n",
    "    print(\"The String is not a Pangram String.\") "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4d2b953e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
