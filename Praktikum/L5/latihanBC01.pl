saudara(john, mary).
saudara(john, paul).
saudara(mary, peter).
saudara(peter, anne).
orang_tua(bob, john).
orang_tua(bob, mary).
orang_tua(bob, paul).
orang_tua(mary_senior, mary).
orang_tua(mary_senior, paul).

/aturan/
anak(X,Y):-
    orang_tua(Y,X).
keponakan(X,Y):-
    anak(X,Z), saudara(Z,Y).
cucu(X,Y):-
    anak(X,Z), orang_tua(Z,Y).
paman(X,Y):-
    saudara(X,Z), orang_tua(Z,y).
penalaran(X,Y):-
    write('masukan nama orang:'),
    read(nama),tulis_hubungan(nama),!.
tulis_hubungan(nama):-
    anak(nama, orangtua),
    write(nama),write('adalah anak dari'),write(orangtua),nl,
    fail.
tulis_hubungan(nama):-
    anak(nama, paman),
    write(nama),write('adalah keponakan dari'),write(orangtua),nl,
    fail.
tulis_hubungan(nama):-
    anak(nama, kakek),
    write(nama),write('adalah cucu dari'),write(orangtua),nl,
    fail.
tulis_hubungan(nama):-
    anak(nama, orang),
    write(nama),write('adalah paman dari'),write(orangtua),nl,
    fail.