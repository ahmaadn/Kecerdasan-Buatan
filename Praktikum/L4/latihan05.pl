lakiLaki(david).
lakiLaki(jack).
lakiLaki(john).
lakiLaki(ray).
lakiLaki(peter).

perempuan(amy).
perempuan(karen).
perempuan(liza).
perempuan(susan).
perempuan(mary).

% X adalah orang tua Y
orangTua(david, liza).
orangTua(amy, liza).
orangTua(david, john).
orangTua(amy, john).
orangTua(jack, susan).
orangTua(karen, susan).
orangTua(jack, ray).
orangTua(karen, ray).
orangTua(john, peter).
orangTua(susan, peter).
orangTua(john, mary).
orangTua(susan, mary).

menikah(X, Y) :-
    orangTua(X, Z), orangTua(Y, Z).

% X adalah ibu dari Y
ibu(X, Y) :-
    orangTua(X, Y), perempuan(X).

% X adalah ayah dari Y
ayah(X, Y) :-
    orangTua(X, Y), lakiLaki(X).

memilikiAnak(X) :-
    orangTua(X, _).

saudaraPerempuan(X, Y) :-