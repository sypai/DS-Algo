Although all languages have a builtin pow function that computes powers of a number, you can write a similar function recursively, and it can be very efficient. The only hitch is that the exponent has to be an integer.

* Suppose you want to compute _x^n_, where x is any real number and n is any integer. It's easy if n is 0, since x^0=1 
no matter what x is. That's a good base case.

* So now let's see what happens when n is positive. Let's start by recalling that when you multiply powers of x, you add the exponents: 

        x^a x^b = x^{a+b}
    for any base x and any exponents a and b.
 
    Therefore, if n is positive and even, then 
          
       x^n = x^{n/2} x^{n/2}
    If you were to compute y = x^{n/2}
  recursively, then you could compute _x^n_
  as y⋅y.
   
 *   What if n is positive and odd?
    
          x^n = x^{n-1}. x  
        
        where n−1 either is 0 or is positive and even. 
        We just saw how to compute powers of x when the exponent either is 0 or is positive and even.
        
        Therefore, you could compute x^{n-1} 
  recursively, and then use this result to compute _x^n_ = x^{n-1} x.

*   What about when n is negative?
    
        x^n = 1 / x^{-n} x 
    and the exponent −n is positive, since it's the negation of a negative number. So you can compute x^{-n} 
 recursively and take its reciprocal.

#### Putting these observations together, we get the following recursive algorithm for computing _x^n_
 *  The base case is when n = 0 and x^0 = 1
 *  If n is positive and even, recursively compute y = x^{n/2} 
 , and then _x^n_=y⋅y. Notice that you can get away with making just one recursive call in this case, computing x^{n/2}
 just once, and then you multiply the result of this recursive call by itself.

*   If n is positive and odd, recursively compute x^{n-1}, so that the exponent either is 0 or is positive and even. Then, _x^n_ = x^{n-1}.x 

*   If n is negative, recursively compute x^{-n}, so that the exponent becomes positive. Then, _x^n_ = 1 / x^{-n}.
