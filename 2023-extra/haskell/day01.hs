import Data.Char (digitToInt, isDigit)
import Data.List (isPrefixOf, isSuffixOf)

-- Takes string from input to solve, can use piping to pipe from input file
main = interact $ solve . lines

-- Takes input lines and prints out the results of part 1 and part 2
solve :: [String] -> String
solve xs = "Part 1: " ++ show s1 ++ "\nPart 2: " ++ show s2
  where
    s1 = sum $ map part1 xs
    s2 = sum $ map part2 xs

-- Solve part 1 by filtering out the numbers of the string using isDigit
part1 :: String -> Int
part1 line = 10 * nums head + nums last
  where
    nums func = digitToInt . func $ filter isDigit line

-- solve part 2 by filtering out numbers using pattern matching and isPrefixOf and isSuffixOf
-- these functions are passed so that the first and last digit can be found using the same generic function
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