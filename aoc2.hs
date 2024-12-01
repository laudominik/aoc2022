import System.IO
import Control.Monad
import Data.List.Split
import Data.List

solve1 :: String -> Int
solve1 s = (sum . (map evaluate2).(splitOn "\n")) s
    where
        evaluate :: String -> Int
        evaluate s = case s of 
            "A X" -> 4
            "A Y" -> 8 
            "A Z" -> 3
            "B X" -> 1
            "B Y" -> 5
            "B Z" -> 9
            "C X" -> 7
            "C Y" -> 2
            "C Z" -> 6
            _-> 0 
        evaluate2 :: String -> Int
        evaluate2 s = case s of 
            "A X" -> 3
            "A Y" -> 4
            "A Z" -> 8
            "B X" -> 1
            "B Y" -> 5
            "B Z" -> 9
            "C X" -> 2
            "C Y" -> 6
            "C Z" -> 7
            _-> 0

main :: IO()
main = do   
    handle <- openFile "input2.txt" ReadMode
    contents <- hGetContents handle
    putStrLn $ show (solve1 contents)
    hClose handle