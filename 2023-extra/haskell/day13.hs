import Data.Char (isAlphaNum)
import Data.List (groupBy, transpose)

main = interact $ solve . paragraphs

solve :: [[String]] -> String
solve xs = "Part 1: " ++ show s1 ++ "\nPart 2: " ++ show s2
  where
    s1 = sum $ map part1 xs
    s2 = sum $ map part2 xs

paragraphs :: String -> [[String]]
paragraphs input = filter (/= [""]) . groupBy (\a b -> a /= "" && b /= "") $ lines input

listDiffs :: [Char] -> [Char] -> Int
listDiffs l1 l2 = sum $ zipWith (\a b -> fromEnum (a /= b)) l1 l2

gridDiffs :: [String] -> Int -> Int
gridDiffs grid idx = sum $ zipWith listDiffs (reverse (take idx grid)) (drop idx grid)

part1 :: [String] -> Int
part1 grid
  | not (null rows) = 100 * head rows
  | otherwise = head cols
  where
    lines grid = filter ((== 0) . gridDiffs grid) [1 .. length grid - 1]
    rows = lines grid
    cols = lines $ transpose grid

part2 :: [String] -> Int
part2 grid
  | not (null rows) = 100 * head rows
  | otherwise = head cols
  where
    lines grid = filter ((== 1) . gridDiffs grid) [1 .. length grid - 1]
    rows = lines grid
    cols = lines $ transpose grid
