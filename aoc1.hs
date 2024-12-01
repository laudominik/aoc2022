import System.IO
import Control.Monad
import Data.List.Split
import Data.List

solve :: String -> Int
solve s =  (
            sum .
            (take 3) .
            reverse . 
            sort .
            map (sum . (map (read)) . (filter (/= "")) . (splitOn "\n")) . 
            (splitOn "\n\n")
           ) s

main :: IO()
main = do   
    handle <- openFile "input1.txt" ReadMode
    contents <- hGetContents handle
    putStrLn $ show (solve contents)
    hClose handle