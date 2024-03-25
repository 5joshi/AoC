import Data.Char (isAlphaNum)
import Data.List (words)

-- Takes string from input to solve, can use piping to pipe from input file
main = interact $ solve . lines

-- Takes input lines and prints out the results of part 1 and part 2
solve :: [String] -> String
solve xs = "Part 1: " ++ show s1 ++ "\nPart 2: " ++ show s2
  where
    s1 = sum $ map part1 xs
    s2 = sum $ map part2 xs

-- Parse a list of strings into pairs of number and string, this represents the count and ball color
pairs :: [String] -> [(Int, String)]
pairs [] = []
pairs [x] = error "Unreachable"
pairs (x : y : xs) = (read x, y) : pairs xs

-- Find the maximum number of balls of a given color that was drawn from the given list of draws
balls :: String -> [(Int, String)] -> Int
balls color = maximum . map fst . filter ((== color) . snd)

-- Solve part 1 by summing up the ids where the maximum ball counts for each color are under the limit
part1 :: String -> Int
part1 line
  | balls "red" draws <= 12 && balls "green" draws <= 13 && balls "blue" draws <= 14 = read id
  | otherwise = 0
  where
    id = head $ parse line
    draws = pairs $ tail $ parse line
    parse = drop 1 . words . filter (\c -> isAlphaNum c || c == ' ')

-- Solve part 2 by multiplying the maximum ball counts for each color that was drawn
part2 :: String -> Int
part2 line = balls "red" draws * balls "green" draws * balls "blue" draws
  where
    draws = pairs $ parse line
    parse = drop 2 . words . filter (\c -> isAlphaNum c || c == ' ')
