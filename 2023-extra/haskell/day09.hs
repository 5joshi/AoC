import Data.Char (isAlphaNum)
import Data.List (words)

main = interact $ solve . lines

solve :: [String] -> String
solve xs = "Part 1: " ++ show s1 ++ "\nPart 2: " ++ show s2
  where
    s1 = sum $ map part1 xs
    s2 = sum $ map part2 xs

listDiff :: [Int] -> [Int]
listDiff list = zipWith (-) (tail list) list

nextNum :: [Int] -> Int
nextNum list
  | all (== 0) list = 0
  | otherwise = last list + nextNum (listDiff list)

part1 :: String -> Int
part1 line = nextNum . map read $ words line

part2 :: String -> Int
part2 line = nextNum . reverse . map read $ words line
