% fakta
orangtua(ahmad, budi).
orangtua(ahmad, candra).
orangtua(budi, cindy).
orangtua(budi, david).
orangtua(candra, emily).
orangtua(candra, fahri).
orangtua(david, grace).

% Aturan
kakek(Kakek, Cucu) :-
    orangtua(Kakek, Anak),
    orangtua(Anak, Cucu).

saudara(Saudara1, Saudara2) :-
    orangtua(Orangtua, Saudara1),
    orangtua(Orangtua, Saudara2),
    Saudara1 \== Saudara2.

paman(Paman, Keponakan) :-
    saudara(Paman, Orangtua),
    saudara(Orangtua, Keponakan).

cucu(Cucu, Kakek) :-
    kakek(Kakek, Cucu).
cucu(Cucu, Kakek) :-
    orangtua(Orangtua, Cucu),
    cucu(Orangtua, Kakek).