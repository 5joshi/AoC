import Data.Char (isAlphaNum)
import Data.List (words)
import Numeric (readHex)

-- Takes string from input to solve, can use piping to pipe from input file
main = interact $ solve . lines

-- Takes input lines and prints out the results of part 1 and part 2
solve :: [String] -> String
solve xs = "Part 1: " ++ show s1 ++ "\nPart 2: " ++ show s2
  where
    s1 = part1 xs
    s2 = part2 xs

-- Map direction characters to a tuple containing their coordinate change
ctd :: Char -> (Int, Int)
ctd c
  | c == 'U' = (0, 1)
  | c == 'D' = (0, -1)
  | c == 'L' = (-1, 0)
  | c == 'R' = (1, 0)
  | otherwise = error "Invalid direction"

-- Find the resulting coordinates after moving from a given coordinate in a given direction by a given amount
coord :: (Int, Int) -> (Char, Int) -> (Int, Int)
coord (x, y) (dir, amt) = (x + dx * amt, y + dy * amt)
  where
    (dx, dy) = ctd dir

-- Find the area contained by a list of given coordinates using the shoelace formula
area :: [(Int, Int)] -> Int
area [] = 0
area [x] = 0
area coords@((x1, y1) : (x2, y2) : xs) = (y1 + y2) * (x1 - x2) + area (tail coords)

-- Find the length of the border of a given route
border :: [(Char, Int)] -> Int
border route = sum $ map snd route

-- Find the actual size of the area contained by a given route using Pick's theorem with the border and area
size :: [(Char, Int)] -> Int
size route = b + (abs a - b) `div` 2 + 1
  where
    b = border route
    a = area $ scanl coord (0, 0) route

-- Solve part 1 by finding the size of the area contained by the given routes
part1 :: [String] -> Int
part1 xs = size $ map (parse . words) xs
  where
    parse [x, y, _] = (head x, read y)

-- Solve part 2 by parsing the input into new instructions and finding the size of the area contained by those
part2 :: [String] -> Int
part2 xs = size $ map (parse . words) xs
  where
    parse [_, _, color] = (dir color, amt color)
      where
        dir :: String -> Char
        dir color = "RDLU" !! read [color !! 7]
        amt :: String -> Int
        amt = fst . head . readHex . take 5 . drop 2
