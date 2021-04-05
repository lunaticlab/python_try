{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n",
      "[25, 73, 117, 157, 193, 225, 253, 277, 297, 313]\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import random\n",
    "import matplotlib.pyplot as plt\n",
    "yhead=[]\n",
    "x=[]\n",
    "for i in range(0,10):\n",
    "    yhead.append((-2*i**2)+50*i+25)\n",
    "    x.append(i)\n",
    "print(x)\n",
    "print(yhead)\n",
    "plt.plot(x,yhead,'r--')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_predict=[0]*len(x)\n",
    "\n",
    "w=[0]*3\n",
    "generation=0\n",
    "r=0.00006 #learning rate 很重要依實測 1次方適合小於3/1000 2次方適合小於等於6/100000\n",
    "def differential(w,x,yhead,feature):\n",
    "    global y_predict\n",
    "    \n",
    "    diff_value=0\n",
    "    if feature==0:\n",
    "        for i in range(0,10):\n",
    "            diff_value+=2*(yhead[i]-(y_predict[i]))*(-1)\n",
    "            \n",
    "       \n",
    "    if feature==1:\n",
    "        for i in range(0,10):\n",
    "            diff_value+=2*(yhead[i]-(y_predict[i]))*(-1)*(x[i])\n",
    "    if feature==2:\n",
    "        for i in range(0,10):\n",
    "            diff_value+=2*(yhead[i]-(y_predict[i]))*(-1)*(x[i])**2\n",
    "    return diff_value       \n",
    "def gradient():\n",
    "    global w,x,yhead\n",
    "    for i in range(0,len(w)):\n",
    "        w[i]=w[i]-r*(differential(w,x,yhead,i))\n",
    "        \n",
    "while generation<=1000:\n",
    "    \n",
    "    for i in range(0,10):\n",
    "        y=w[2]*x[i]**2+w[1]*x[i]+w[0] #function\n",
    "        y_predict[i]=y\n",
    "    #print(y_predict)\n",
    "    gradient()\n",
    "    generation+=1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[-0.024715050823690857, 0.022885793693048204, 0.997434978060611]\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(x,yhead,'r--')\n",
    "plt.plot(x,y_predict,'b--')\n",
    "print(w)\n",
    "plt.show()"
   ]
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
