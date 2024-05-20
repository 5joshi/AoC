:- use_module(library(dcg/basics)).
:- use_module(library(clpfd)).

% Solve day 6 given the filename
solve(File) :-
  % parse the times and dists and determine amount of solutions for each pair
  phrase_from_file(parse_file(Time, Dist), File),
  maplist(valid, Time, Dist, Ns),
  % determine the product of the # of solutions to solve part 1
  foldl([X, Y, Z] >> (Z #= X * Y), Ns, 1, S1),
  write("Part 1: "), write(S1),

  % combine the times and distances into one big number
  merge_nums(Time, T),
  merge_nums(Dist, D),
  % find the # of solutions for the combined numbers to solve part 2
  valid(T, D, S2),
  write("\nPart 2: "), write(S2).

% DCG to parse the input file which is mostly lines of numbers
parse([]) --> (""; "\n").
parse([X|Xs]) --> blanks, number(X), parse(Xs).
parse_file(Time, Dist) --> "Time: ", parse(Time), "Distance: ", parse(Dist).

% Merge a list of numbers into one big number
merge_nums(Xs, Y) :-
  maplist(number_chars, Xs, Chars),
  flatten(Chars, String),
  number_chars(Y, String).

% Determine the amount of solutions for a given time and distance
% This is the amount of possible wait times, 
% given that wait is between 0 and the total time, 
% and the calculated distance is above the given minimum distance
valid(Time, MinDist, N) :-
  Wait #> 0, Wait #< Time,
  Dist #= Wait * (Time - Wait),
  Dist #> MinDist,
  fd_size(Wait, N).

:- solve("day06.txt").