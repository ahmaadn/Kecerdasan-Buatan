saudara(john, mary).
saudara(john, paul).
saudara(mary, peter).
saudara(peter, anne).
orang_tua(bob, john).
orang_tua(bob, mary).
orang_tua(bob, paul).
orang_tua(mary_senior, mary).
orang_tua(mary_senior, paul).

/* aturan */
anak(X,Y):-
    orang_tua(Y,X).
keponakan(X,Y):-
    anak(X,Z), saudara(Z,Y).
cucu(X,Y):-
    anak(X,Z), orang_tua(Z,Y).
paman(X,Y):-
    saudara(X,Z), orang_tua(Z,Y).

penalaran:-
    write('Masukan nama orang: '),
    read(Nama),
    tulis_hubungan(Nama), !.

tulis_hubungan(Nama):-
    anak(Nama, OrangTua),
    write(Nama), write(' adalah anak dari '), write(OrangTua), nl,
    fail.
tulis_hubungan(Nama):-
    keponakan(Nama, Paman),
    write(Nama), write(' adalah keponakan dari '), write(Paman), nl,
    fail.
tulis_hubungan(Nama):-
    cucu(Nama, Kakek),
    write(Nama), write(' adalah cucu dari '), write(Kakek), nl,
    fail.
tulis_hubungan(Nama):-
    paman(Nama, Keponakan),
    write(Nama), write(' adalah paman dari '), write(Keponakan), nl,
    fail.
tulis_hubungan(_).

:- penalaran.
