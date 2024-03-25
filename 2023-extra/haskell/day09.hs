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

-- Creates a list of differences between the consecutive numbers in the given list
listDiff :: [Int] -> [Int]
listDiff list = zipWith (-) (tail list) list

-- Find the next number in the list by summing the last elements of the recursive list differences until all elements are 0
nextNum :: [Int] -> Int
nextNum list
  | all (== 0) list = 0
  | otherwise = last list + nextNum (listDiff list)

-- Solve part 1 by finding the next number in the list
part1 :: String -> Int
part1 line = nextNum . map read $ words line

-- Solve part 2 by simply applying part1 to the reversed list
part2 :: String -> Int
part2 line = nextNum . reverse . map read $ words line
