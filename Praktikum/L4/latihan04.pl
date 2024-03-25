menikah(wati, andi).
anakKandung(wati, budi).
saudaraKembar(budi, andi).

is_saudaraKandung(X, Y) :-
    saudaraKembar(X, Y).

is_keponakan(Z, Y) :-
    anakKandung(Z, X), saudaraKembar(X, Y).


not(sah(menikah(Z, Y))) :- is_keponakan(Z, Y).
