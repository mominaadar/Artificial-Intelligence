
/** Momina Atif Dar - p18-0030 */

male(atif).
female(aliya).
female(momina).
female(farwa).
female(bushra).

parent(atif,momina).
parent(atif,farwa).
parent(atif,bushra).
parent(aliya,momina).
parent(aliya,farwa).
parent(aliya,bushra).
sibling(momina,farwa).
sibling(momina,bushra).
sibling(farwa,momina).
sibling(farwa,bushra).
sibling(bushra,momina).
sibling(bushra,farwa).

mother(X, Y) :- parent(X, Y), female(X).
father(X, Y) :- parent(X, Y), male(X).
daughter(X, Y) :- parent(Y, X), female(X).
sister(X, Y) :- parent(Z,X), parent(Z,Y), female(X), female(Y).
