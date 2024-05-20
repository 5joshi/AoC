:- use_module(library(dcg/basics)).
:- use_module(library(lists)).


% Solve day 7 given the filename
solve(File) :-
  % parse the pairs of hands and bids from file
  phrase_from_file(parse(Pairs), File),
  % turn the hands into values consisting of class + card values & sort them
  findall(Value - Bid, (member(Hand - Bid, Pairs), total_value(Hand, Value)), ValuedPairs),
  msort(ValuedPairs, SortedPairs),
  % calculate the winnings and sum them up to find the solution for part 1
  aggregate_all(sum(Winnings), (nth1(Idx, SortedPairs, _ - Bid), Winnings is Bid * Idx), S1),
  write("Part 1: "), write(S1),

  % turn the hands into values consisting of class + card values given that J is now a joker & sort them
  findall(Value - Bid, (member(Hand - Bid, Pairs), joker_value(Hand, Value)), JokerPairs),
  msort(JokerPairs, SortedJokerPairs),
  % calculate the winnings and sum them up to find the solution for part 2
  aggregate_all(sum(JokerWinnings), (nth1(Idx, SortedJokerPairs, _ - Bid), JokerWinnings is Bid * Idx), S2),
  write("\nPart 2: "), write(S2).

% DCG to parse the input file of hand, bid pairs
parse([]) --> (""; "\n").
parse([Hand - Bid|Xs]) --> string_without(" ", HandString), {hand_value(HandString, Hand)}, blank, number(Bid), blanks, parse(Xs).

% Create a counter of the cards in the hand in the form [Count - Card, ...]
counter(Hand, Counter) :-
  msort(Hand, Sorted),
  findall(Freq - Card, (member(Card, Sorted), aggregate_all(count, member(Card, Sorted), Freq)), Freqs),
  sort(Freqs, Counter).

% Create a counter of the optimal hand by using jokers (this is done by adding the joker count to the most occurring card)
joker_counter([5-11], [5-14]) :- !.
joker_counter(Counter, NewCounter) :-
  joker_count(Counter, JokerCount),
  exclude([_ - X] >> (X == 11), Counter, Filtered),
  last(Filtered, MaxCount - MaxCard),
  NewMaxCount is MaxCount + JokerCount,
  replace(MaxCount - MaxCard, NewMaxCount - MaxCard, Filtered, NewCounter).

% Get the number of jokers in the hand
joker_count([], 0) :- !.
joker_count([Count - 11 | _], Count) :- !.
joker_count([_ | Rest], Count) :- joker_count(Rest, Count).

% Calculate the total value of a hand by combining hand type and card values
total_value(Hand, Value) :-
  counter(Hand, Counter),
  hand_type(Counter, Type),
  append([Type], Hand, Value).

% Calculate the total value of a hand by combining hand type and card values given that J is now a joker
% The type is determined by adding the amount of jokers to the most occurring other card,
% the values of jokers are replaced by the lowest possible card value
joker_value(Hand, Value) :-
  counter(Hand, Counter),
  joker_counter(Counter, NewCounter),
  hand_type(NewCounter, Type),
  replace(11, 1, Hand, NerfedHand),
  append([Type], NerfedHand, Value).

% Get the card values of a hand
hand_value(Hand, Values) :- maplist(card_value, Hand, Values).
card_value(Card, Value) :- nth1(Value, `#23456789TJQKA`, Card), !.

% Get the hand type of a hand given the counter of the cards
hand_type([5-_], 6) :- !.
hand_type([1-_, 4-_], 5) :- !.
hand_type([2-_, 3-_], 4) :- !.
hand_type([1-_, 1-_, 3-_], 3) :- !.
hand_type([1-_, 2-_, 2-_], 2) :- !.
hand_type([1-_, 1-_, 1-_, 2-_], 1) :- !.
hand_type(_, 0).

% Replace all occurrences of O with R in a list
replace(_, _, [], []).
replace(O, R, [O|T], [R|T2]) :- replace(O, R, T, T2).
replace(O, R, [H|T], [H|T2]) :- H \= O, replace(O, R, T, T2).

:- solve("day07.txt").