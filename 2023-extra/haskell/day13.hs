import Data.Char (isAlphaNum)
import Data.List (words)

main = interact $ solve . lines

solve :: [String] -> String
solve xs = "Part 1: " ++ show s1 ++ "\nPart 2: " ++ show s2
  where
    s1 = sum $ map part1 xs
    s2 = sum $ map part2 xs

pairs :: [String] -> [(Int, String)]
pairs [] = []
pairs [x] = error "Unreachable"
pairs (x : y : xs) = (read x, y) : pairs xs

balls :: String -> [(Int, String)] -> Int
balls color = maximum . map fst . filter ((== color) . snd)

part1 :: String -> Int
part1 line
  | balls "red" draws <= 12 && balls "green" draws <= 13 && balls "blue" draws <= 14 = read id
  | otherwise = 0
  where
    id = head $ parse line
    draws = pairs $ tail $ parse line
    parse = drop 1 . words . filter (\c -> isAlphaNum c || c == ' ')

part2 :: String -> Int
part2 line = balls "red" draws * balls "green" draws * balls "blue" draws
  where
    draws = pairs $ parse line
    parse = drop 2 . words . filter (\c -> isAlphaNum c || c == ' ')
