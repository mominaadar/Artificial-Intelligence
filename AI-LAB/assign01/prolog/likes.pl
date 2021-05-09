
/** Momina Atif Dar - p18-0030 */

female(mary).
male(john).
male(adam).
likes(mary,pasta).
likes(mary,lasagna).
likes(mary,smoothies).
likes(adam,biryani).
likes(adam,pasta).
likes(john,apples).
likes(john,smoothies).

/** checking if mary and some other male has similar likes */
similar_with_mary(X,Y) :- likes(Y,Z),likes(X,Z),female(X),male(Y).

/** checking if adam and john or any two males have similar likes */
similar_adam_john(X,Y) :- likes(X,Z),likes(Y,Z),male(X),male(Y).

