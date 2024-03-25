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
orangTua(mary, peter).

menikah(X, Y) :-
    orangTua(X, Z), orangTua(Y, Z).

ibu(X, Y) :-
    orangTua()
