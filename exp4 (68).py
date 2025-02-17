{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Content before appending:\n",
      " This is the first line.\n",
      "This is the second line.\n",
      "\n",
      "Content after appending:\n",
      " This is the first line.\n",
      "This is the second line.\n",
      "This is the appended line.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from contextlib import contextmanager\n",
    "\n",
    "@contextmanager\n",
    "def genericFileFunction(filename, method):\n",
    " \n",
    "    file = open(filename, method)\n",
    "    try:\n",
    "\n",
    "        yield file\n",
    "    finally:\n",
    "      \n",
    "        file.close()\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    filename = 'file.txt'\n",
    "    \n",
    "\n",
    "    with genericFileFunction(filename, 'w') as file:\n",
    "        file.write(\"This is the first line.\\n\")\n",
    "        file.write(\"This is the second line.\\n\")\n",
    "    \n",
    "    \n",
    "    with genericFileFunction(filename, 'r') as file:\n",
    "        content_before_append = file.read()\n",
    "   \n",
    "    with genericFileFunction(filename, 'a') as file:\n",
    "        file.write(\"This is the appended line.\\n\")\n",
    "    \n",
    "    with genericFileFunction(filename, 'r') as file:\n",
    "        content_after_append = file.read()\n",
    "\n",
    "    print(\"Content before appending:\\n\", content_before_append)\n",
    "    print(\"Content after appending:\\n\", content_after_append)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
