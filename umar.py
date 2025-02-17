{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "fullstack developer\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "General case represents that developer working on \n",
    "frontend cannot work backend development unless he/she is fullstack dev.\n",
    "\n",
    "Write a method named verifier () that checks this condition.\n",
    "\n",
    "The method should check that if frontend is True and backend is True,\n",
    "the method returns Fullstack as string. If one of them is True, it should return\n",
    "the respective desgination, and if none of them are true, it returns,\n",
    "not a developer respetively.\n",
    "'''\n",
    "\n",
    "class Employee:\n",
    "    def __init__ (\n",
    "            self,\n",
    "            designation : str = 'Developer',\n",
    "            frontend : bool = False,\n",
    "            backend : bool = False\n",
    "    ):\n",
    "        self.designation = designation\n",
    "        self.frontend = frontend\n",
    "        self.backend = backend\n",
    "\n",
    "    def __repr__ (self):\n",
    "        return '{} (Frontend: {}, Backend: {})'.format(self.designation, self.frontend, self.backend)\n",
    "    \n",
    "    ### Write the your method over here.\n",
    "    def verifier (self, frontend, backend):\n",
    "        if frontend and backend:\n",
    "            return 'fullstack developer'\n",
    "        elif frontend :\n",
    "            return 'frontend developer'\n",
    "        elif backend :\n",
    "            return 'backend developer'\n",
    "        else: \n",
    "            return 'not a developer'\n",
    "if __name__ == '__main__':\n",
    "    firstEmployee = Employee ()\n",
    "    frontend_input = input(\"Are you a frontend developer? (yes=1/ no=0): \")\n",
    "    backend_input = input(\"Are you a backend developer? (yes=1/ no=0): \")\n",
    "    frontend = frontend_input == '1'\n",
    "    backend = backend_input == '1'\n",
    "\n",
    "    print(firstEmployee.verifier (frontend,backend))\n",
    "\n",
    "\n",
    "    # Call the method here to display output.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
