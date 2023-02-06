{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "7d002322",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number: 5\n",
      "           1 \n",
      "          1      1 \n",
      "         1      2      1 \n",
      "        1      3      3      1 \n",
      "       1      4      6      4      1 \n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter the number: \"))  \n",
    "list1 = []   \n",
    "for i in range(num):  \n",
    "  list1.append([])  \n",
    "  list1[i].append(1)  \n",
    "  for j in range(1, i):  \n",
    "    list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j])  \n",
    "  if(num != 0):  \n",
    "    list1[i].append(1)  \n",
    "for i in range(num):  \n",
    "  print(\" \" * (num - i), end = \" \", sep = \" \")  \n",
    "  for j in range(0, i + 1):  \n",
    "    print('{0:6}'.format(list1[i][j]), end = \" \", sep = \" \")  \n",
    "  print() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4337fb77",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bdf9c7b9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0173ec83",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "855211d1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa630356",
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
