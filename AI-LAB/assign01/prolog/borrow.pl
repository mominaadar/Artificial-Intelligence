
/** Momina Atif Dar - p18-0030 */ 

female(mary).
male(adam).
male(john).
male(philips).
male(jack).

lent(mary,john).
lent(mary,jack).
lent(mary,philips).
lent(john,adam).
lent(john,philips).
lent(philips,adam).

/** mary lent money to a male */
mary_lent_male(X,Y) :- lent(X,Y), female(X), male(Y).

/** male lent money to anybody */
male_lent(X,Y) :- lent(X,Y), male(X).
