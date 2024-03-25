anakIbu(andi).
anakIbu(budi).
anakIbu(cika).
anakIbu(emil).
not(anakIbu(fadil)).

sukaPermen(andi).
sukaPermen(budi).
sukaPermen(cika).
not(sukaPermen(dani)).
not(sukaPermen(emil)).

apakahAnakIbu(X) :- anakIbu(X).

anakIbuDapatPermen(X, Y) :-
    anakIbu(X), sukaPermen(Y).
