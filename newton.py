{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ad5cd2d9-7986-41a0-9c74-5bd96091d763",
   "metadata": {},
   "source": [
    "## Newton's method\n",
    "\n",
    "accept a starting value x0, and the function f(') to optimize\n",
    "implement the iterative algorithm\n",
    "implement the stopping criterion (feel free to keep this simple)\n",
    "\n",
    "calculate the first and second derivatives using a basic finite difference approach to estimating the derivative based on the definition of a derivative as a limit\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "25b96823-c4b1-4ff9-9821-622663845e3c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#8/22 \n",
    "\n",
    "def newton(f, Df, x0, epsilon, max_iter):\n",
    "\n",
    "    xn = x0\n",
    "    for x in range(0, max_iter):\n",
    "        fxn = f(xn)\n",
    "        if abs(fxn) < epsilon:\n",
    "            print(n)\n",
    "            return xn\n",
    "        Dfxn = Df(xn)\n",
    "        if Dfxn == 0:\n",
    "            print('Zero derivative, no solution found')\n",
    "            return \n",
    "        xn = xn - fxn/Dfxn\n",
    "    print('Exceeded maximum iterations, no solution found')\n",
    "    retrun "
   ]
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
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
