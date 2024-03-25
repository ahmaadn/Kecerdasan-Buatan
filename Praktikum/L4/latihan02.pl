lebihBesar(gajah, kuda).
lebihBesar(kuda, keledei).
lebihBesar(keledei, anjing).
lebihBesar(keledei, monyet).

apakahLebihBesar(X, Y) :-
    lebihBesar(X, Y).
apakahLebihBesar(X, Z) :-
    lebihBesar(X, Y),
    lebihBesar(X, Z).
