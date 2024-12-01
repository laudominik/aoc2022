import System.IO
import Control.Monad
import Data.List.Split
import Data.List
import Data.Char (ord)

overlapping :: [[String]] -> Bool
overlapping a = or 
    [and [x <= z, z <= y], 
    and [z <= x, x <= t]]
    where
        x = (read ((a!!0)!!0) :: Int)
        y = (read ((a!!0)!!1) :: Int)
        z = (read ((a!!1)!!0) :: Int)
        t = (read ((a!!1)!!1) :: Int)

solve :: String -> Int
solve s = length $ (
    (filter (overlapping)).
    (map (\x -> (
        (map (\x -> splitOn "-" x)) .
        (splitOn ",")
        ) x)
    ) .
    (splitOn "\n")
    ) s
     

main :: IO()
main = do   
    handle <- openFile "input4.txt" ReadMode
    contents <- hGetContents handle
    putStrLn $ show (solve contents)
    hClose handle