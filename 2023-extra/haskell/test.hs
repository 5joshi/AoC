import Data.List (groupBy)

main = interact $ solve . paragraphs

paragraphs :: String -> [[String]]
paragraphs input = filter (/= [""]) . groupBy (\a b -> a /= "" && b /= "") $ lines input

solve :: [[String]] -> String
solve s = "Test:" ++ show s