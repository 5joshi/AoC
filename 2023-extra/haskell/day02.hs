import Data.Char (isAlphaNum)
import Data.List (words)

main = interact $ solve . lines

solve :: [String] -> String
solve xs = "Part 1: " ++ show s1 ++ "\nPart 2: " ++ show s2
  where
    s1 = sum $ map part1 xs
    s2 = sum $ map part2 xs

balls :: String -> [String] -> Int
balls color [] = 0
balls color [x] = error "Unreachable"
balls color (x : y : xs)
  | read x > balls color xs && y == color = read x
  | otherwise = balls color xs

part1 :: String -> Int
part1 line
  | balls "red" info <= 12 && balls "green" info <= 13 && balls "blue" info <= 14 = id
  | otherwise = 0
  where
    id = read $ head $ parse line
    info = tail $ parse line
    parse = drop 1 . words . filter (\c -> isAlphaNum c || c == ' ')

part2 :: String -> Int
part2 line = balls "red" info * balls "green" info * balls "blue" info
  where
    info = parse line
    parse = drop 2 . words . filter (\c -> isAlphaNum c || c == ' ')
