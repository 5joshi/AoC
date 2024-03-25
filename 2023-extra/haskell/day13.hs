import Data.Char (isAlphaNum)
import Data.List (groupBy, transpose)

-- Takes string from input to solve, can use piping to pipe from input file
main = interact $ solve . paragraphs

-- Takes input lines and prints out the results of part 1 and part 2
solve :: [[String]] -> String
solve xs = "Part 1: " ++ show s1 ++ "\nPart 2: " ++ show s2
  where
    s1 = sum $ map part1 xs
    s2 = sum $ map part2 xs

-- Parse the input into a list of matrices, basically splits on double newlines
paragraphs :: String -> [[String]]
paragraphs input = filter (/= [""]) . groupBy (\a b -> a /= "" && b /= "") $ lines input

-- Find the number of differences between two strings
listDiffs :: [Char] -> [Char] -> Int
listDiffs l1 l2 = sum $ zipWith (\a b -> fromEnum (a /= b)) l1 l2

-- Find the number of differences along a given reflection line within the given grid
gridDiffs :: [String] -> Int -> Int
gridDiffs grid idx = sum $ zipWith listDiffs (reverse (take idx grid)) (drop idx grid)

-- Solve part 1 by finding the indices of the reflection lines where the differences are 0
part1 :: [String] -> Int
part1 grid
  | not (null rows) = 100 * head rows
  | otherwise = head cols
  where
    lines grid = filter ((== 0) . gridDiffs grid) [1 .. length grid - 1]
    rows = lines grid
    cols = lines $ transpose grid

-- Solve part 2 by finding the indices of the reflection lines where the differences are 1
part2 :: [String] -> Int
part2 grid
  | not (null rows) = 100 * head rows
  | otherwise = head cols
  where
    lines grid = filter ((== 1) . gridDiffs grid) [1 .. length grid - 1]
    rows = lines grid
    cols = lines $ transpose grid
