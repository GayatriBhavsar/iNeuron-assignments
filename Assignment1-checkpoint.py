{
 "cells": [
  {
   "cell_type": "raw",
   "id": "4a8a4a77",
   "metadata": {},
   "source": [
    "Q1 ans:\n",
    "    \n",
    "* : expression\n",
    "'hello' : value\n",
    "-87.8 : value\n",
    "-  : expression\n",
    "/ : expression\n",
    "+ : expression\n",
    "6 : value"
   ]
  },
  {
   "cell_type": "raw",
   "id": "ef69fbd7",
   "metadata": {},
   "source": [
    "Q2 ans:\n",
    "    The difference between string and variable is as below:\n",
    "        Variable is used to store a value and the value which is stored in variable can be integer,string ,list and so on. \n",
    "Value can be access in future with the help of variable. \n",
    "String is the oneof the datatype of value which is stored in variable."
   ]
  },
  {
   "cell_type": "raw",
   "id": "1679a434",
   "metadata": {},
   "source": [
    "# Q3 ans:\n",
    "    three differenData types are as follows:\n",
    "1. Numerical Datatypes:\n",
    "    Numerical datatypes holds the numerical values such as\n",
    "    i. int : it holds siged integers with non limited length\n",
    "        eg : a = 10\n",
    "            \n",
    "    ii. float : holds floating precision numbers and it’s accurate up to 15 decimal places.\n",
    "        eg:  b = 34.56\n",
    "            \n",
    "    iii. complex- holds complex numbers\n",
    "        eg : c = 3+6j\n",
    "            \n",
    "2. String datatype:\n",
    "    The string is a sequence of characters.\n",
    "    Generally, strings are represented by either single or double-quotes \n",
    "    and also sometimes with tripple quotes.\n",
    "    \n",
    "    eg: s : \"This is my first assigment of datascience class\"\n",
    "            \n",
    "3. Sequence datatype:\n",
    "    Sequence datatype contains list, tuple and range.\n",
    "    i.list : \n",
    "        list is a interesting datatype in python. \n",
    "        It is same as array but it can hold different type of data in the same list.\n",
    "       It is written with the squre brackets ([]) and the values are separated with the help of commas (,).\n",
    "       \n",
    "        eg : a = [1,2,3,'python']\n",
    "    ii.tuple :\n",
    "        The tuple is another data type which is a sequence of data similar to a list. \n",
    "        But it is immutable.\n",
    "        Data in a tuple is written using parenthesis () and commas.\n",
    "        \n",
    "        eg : d = (1,3,4,6,'python')\n",
    "    \n",
    "     "
   ]
  },
  {
   "cell_type": "raw",
   "id": "7d782856",
   "metadata": {},
   "source": [
    "Q4. What is an expression made up of? What do all expressions do?\n",
    "ans:\n",
    "    Expression is made of operands and operators.\n",
    "    with the help of the expressions we are able get result using values.\n",
    "    These expressions are interpreted by interpreter."
   ]
  },
  {
   "cell_type": "raw",
   "id": "685d07ce",
   "metadata": {},
   "source": [
    "Q5. This assignment statements, like spam = 10. What is the difference between an\n",
    "expression and a statement?\n",
    "ans:\n",
    "    Expression in python is evaluated for some result.\n",
    "    statements in pythonis not evaluate for results \n",
    "    Execution of statement changes the state of the variable\n",
    "    The expresstion evaluation does not result in any state change.\n",
    "    \n",
    "    eg : spam = 10\n",
    "        a = 20\n",
    "        c = a + spam\n",
    "        if we execute c expression then we get\n",
    "             c = 20 + 10\n",
    "             c = 30 \n",
    "        and if we assign 40 to spam then \n",
    "            spam = 40\n",
    "            c = 20 + 40\n",
    "            c= 60\n",
    "        \n"
   ]
  },
  {
   "cell_type": "raw",
   "id": "6ca0e144",
   "metadata": {},
   "source": [
    "Q6. After running the following code, what does the variable bacon contain?\n",
    "bacon = 22\n",
    "bacon + 1\n",
    "\n",
    "ans:\n",
    "    bacon = 23"
   ]
  },
  {
   "cell_type": "raw",
   "id": "d1c02894",
   "metadata": {},
   "source": [
    "Q7. What should the values of the following two terms be?\n",
    "\n",
    "'spam' + 'spamspam'\n",
    "'spam' * 3\n",
    "\n",
    "ANS:\n",
    "    'spam' + 'spamspam' = 'spamspamspam'\n",
    "'spam' * 3 = 'spamspamspam'"
   ]
  },
  {
   "cell_type": "raw",
   "id": "e3258c94",
   "metadata": {},
   "source": [
    "Q8. Why is eggs a valid variable name while 100 is invalid?\n",
    "Ans:\n",
    " A variable name must start with a letter or the underscore character. A variable name cannot start with a number. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )\n",
    " so eggs is valid variable name and 100 is invalid name"
   ]
  },
  {
   "cell_type": "raw",
   "id": "fa63a0dc",
   "metadata": {},
   "source": [
    "Q9. What three functions can be used to get the integer, floating-point number, or string\n",
    "version of a value?\n",
    "\n",
    "ans :\n",
    "    to get integer version of value int() funtion is used\n",
    "     to get floating-point number version of value float() funtion is used\n",
    "     to get string version of value str() funtion is used"
   ]
  },
  {
   "cell_type": "raw",
   "id": "899c1b0a",
   "metadata": {},
   "source": [
    "Q10. Why does this expression cause an error? How can you fix it?\n",
    "'I have eaten ' + 99 + ' burritos.'\n",
    "Ans:\n",
    "    The above expression cause an error because in the above expression there is concatenation of string and the integer thats why it is giving error.\n",
    "    As we can concatenate string with string only if we want to concat string with integer first we have convert integer in string format with str() function.\n",
    " 'I have eaten ' + 99 + ' burritos.'\n",
    "above expression error can befixed as follows\n",
    "\n",
    "'I have eaten ' + str(99) + ' burritos.'\n",
    "   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "5417a4f1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I have eaten 99 burritos\n"
     ]
    }
   ],
   "source": [
    "print('I have eaten ' + str(99) + ' burritos')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a5f39322",
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
