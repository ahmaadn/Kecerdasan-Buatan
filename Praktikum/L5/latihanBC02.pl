:- dynamic user_fact/1.
:- dynamic infered_fact/1.

% Predikat untuk menghapus semua fakta sebelum program dijalankan
clear_facts :-
    retractall(user_fact(_)),
    retractall(infered_fact(_)).

% predikat untuk meminta input fakta dari pengguna
ask_for_facts :-
    write('Masukan fakta-fakta awal (ketik "Sunny."/"Dry."/"Wet."/"Rainy."/"Selesai." untuk berhenti): '), nl,
    read(Fact),
    (
        Fact \= selesai ->
            (
                assert(user_fact(Fact)),
                ask_for_facts
            );
        true
    ).

% rules
rule(play) :- user_fact(sunny), user_fact(dry).
rule(not_play) :- user_fact(sunny), user_fact(wet).
rule(not_play) :- user_fact(rainy).

% inference engine
infer :-
    rule(X),
    \+ infered_fact(X),
    assert(infered_fact(X)),
    fail.
infer.

% print
print_facts :-
    write('Facts: '), nl,
    user_fact(X),
    write('- '), write(X), nl,
    fail.
print_facts :-
    write('Infered Facts: '), nl,
    infered_fact(X),
    write('- '), write(X), nl,
    fail.
print_facts.

% start
start :-
    clear_facts, %clear fact
    ask_for_facts,
    infer,
    print_facts.
