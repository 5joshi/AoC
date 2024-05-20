:- use_module(library(dcg/basics)).

% Solve day 8 given the filename
solve(File) :-
  % parse the route and nodes from file
  phrase_from_file(parse(Route, Nodes), File),
  % find the number of steps needed to go from AAA to ZZZ to get the solution for part 1
  step(Route, Nodes, `AAA`, [`ZZZ`], 0, S1),
  write("Part 1: "), write(S1),
  
  % get all the start and end nodes (nodes ending in A and Z respectively)
  findall([X, Y, 0'A], member([X, Y, 0'A]-_-_, Nodes), Starts), 
  findall([X, Y, 0'Z], member([X, Y, 0'Z]-_-_, Nodes), Ends),
  % find the number of steps needed to go from every start to any end
  findall(Steps, (member(Start, Starts), step(Route, Nodes, Start, Ends, 0, Steps)), Results),
  % these are all cycles, so the solution for part 2 is the LCM of the results
  lcm(Results, S2),
  write("\nPart 2: "), write(S2).

% DCG to parse the nodes from the input file
parse_nodes([]) --> [].
parse_nodes([From-`L`-Left, From-`R`-Right | Rest]) --> string(From), " = (", string(Left), ", ", string(Right), ")", blanks, parse_nodes(Rest).

% DCG to parse the route and nodes from the input file
parse(Route, Nodes) --> string(Route), "\n\n", parse_nodes(Nodes).

% Determine the number of steps needed to go from the current node to any of the end nodes
step([Dir | Rest], Nodes, Current, Ends, CurrSteps, TotalSteps) :-
  memberchk(Current-[Dir]-Next, Nodes),
  NextSteps is CurrSteps + 1,
  append(Rest, [Dir], Route),
  ( \+ member(Next, Ends) -> step(Route, Nodes, Next, Ends, NextSteps, TotalSteps); TotalSteps is NextSteps ).

% Calculate the least common multiple of a list of numbers
lcm(X, Y, Result) :- Result is abs(X * Y) // gcd(X, Y).
lcm([X | Xs], Result) :- foldl(lcm, Xs, X, Result).

:- solve("day08.txt").