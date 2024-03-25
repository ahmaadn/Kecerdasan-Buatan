menikah(wati, andi).
anakKandung(wati, budi).
saudaraKembar(budi, andi).

is_saudaraKandung(X, Y) :-
    saudaraKembar(X, Y).

is_keponakan(Z, Y) :-
    anakKandung(Z, X), saudaraKembar(X, Y).


tidak_sah(Y, X) :- is_keponakan(Y, X).
