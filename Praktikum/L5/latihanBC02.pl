:- dynamic user_fact/1.
:- dynamic inferred_fact/1.

clear_facts :-
    retractall(user_fact(_)),
    retractall(inferred_fact(_)).

% Predikat untuk meminta input fakta dari pengguna
ask_for_facts :-
    write('Masukan fakta fakta awal (ketik "sunny."/"dry."/"wet."/"rainy."/"selesai." untuk berhenti): '), nl,
    read(Fact),
    (
        Fact \= selesai ->
        (
            assert(user_fact(Fact)),
            ask_for_facts
        );
        true
    ).

% RUles
%  fakta play dapat dibuktikan jika sunny dan dry terpenuhi
can_prove(play) :- user_fact(sunny), user_fact(dry).
% fakta no_play dapat dibuktikan jika sunny dan wet terpenuhi
can_prove(not_play) :- user_fact(sunny), user_fact(wet).
% fakta no_play dapat dibuktikan jika rainy terpenuhi
can_prove(not_play) :- user_fact(rainy).

infer(Fact) :-
    can_prove(Fact),
    assert(inferred_fact(Fact)),!.
infer(_).

print_facts :-
    write('Facts:'), nl,
    user_fact(X),
    write('- '),
    write(X), nl,
    fail.
print_facts :-
    write('Inferred Facts:'), nl,
    inferred_fact(X),
    write('- '),
    write(X), nl,
    fail.
print_facts.

start :-
    clear_facts,
    ask_for_facts,
    infer(play),
    infer(not_play),
    print_facts.