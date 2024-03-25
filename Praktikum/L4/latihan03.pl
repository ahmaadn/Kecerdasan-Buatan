anakIbu(andi).
anakIbu(budi).
anakIbu(cika).
anakIbu(emil).
anakIbu(dani).
not(anakIbu(fadil)).

sukaPermen(andi).
sukaPermen(budi).
sukaPermen(cika).
not(sukaPermen(dani)).
not(sukaPermen(emil)).


anakIbuDapatPermen(X) :-
    anakIbu(X), sukaPermen(X).

anakIbuDapatUang(X) :-
    anakIbu(X), not(sukaPermen(X)).
