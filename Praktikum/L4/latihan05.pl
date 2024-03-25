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

% % X adalah saudara perempuan dari Y
% saudaraPerempuan(X, Y) :-
%     orangTua(Z, X), orangTua(Z, Y), perempuan(X).

% % X adalah saudara laki-laki dari Y
% saudaraLakilaki(X, Y) :-
%     orangTua(Z, X), orangTua(Z, Y), lakiLaki(X).

% X adalah kakek dari Y
kakek(X, Y) :-
    orangTua(Z, Y), orangTua(X, Z), lakiLaki(X).

% X adalah nenek dari Y
nenek(X, Y) :-
    orangTua(Z, Y), orangTua(X, Z), perempuan(X).