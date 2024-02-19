import Data.Char (digitToInt, isDigit)
import Data.List (isPrefixOf, isSuffixOf)

main = interact $ solve . lines

solve :: [String] -> String
solve xs = "Part 1: " ++ show s1 ++ "\nPart 2: " ++ show s2
  where
    s1 = sum $ map part1 xs
    s2 = sum $ map part2 xs

part1 :: String -> Int
part1 line = 10 * nums head + nums last
  where
    nums func = digitToInt . func $ filter isDigit line

part2 :: String -> Int
part2 line = 10 * nums head tail isPrefixOf line + nums last init isSuffixOf line
  where
    nums func rest contains str
      | isDigit $ func str = digitToInt $ func str
      | contains "one" str = 1
      | contains "two" str = 2
      | contains "three" str = 3
      | contains "four" str = 4
      | contains "five" str = 5
      | contains "six" str = 6
      | contains "seven" str = 7
      | contains "eight" str = 8
      | contains "nine" str = 9
      | otherwise = nums func rest contains $ rest str