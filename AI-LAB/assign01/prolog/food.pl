
/** Momina Atif Dar - p18-0030 */

food(eggs).
food(toast).
food(oatmeal).
food(beans).
food(pulses).
food(chapati).
food(chicken).
food(steak).
food(soup).
food(smoothie).

breakfast(eggs).
breakfast(toast).
breakfast(oatmeal).
breakfast(smoothie).

lunch(beans).
lunch(eggs).
lunch(pulses).
lunch(chapati).
lunch(smoothie).

dinner(chicken).
dinner(steak).
dinner(soup).
dinner(chapati).

/** checking if breakfast and lunch have an item in both */
breakfast_lunch(X) :- breakfast(X), lunch(X).

/** checking if dinner and lunch have an item in both */
lunch_dinner(X) :- lunch(X), dinner(X).

/** checking if breakfast and dinner have an item in both */
breakfast_dinner(X) :- breakfast(X), dinner(X).



