import System.IO
import Control.Monad
import Data.List.Split
import Data.List
import Data.Char (ord)

toCode :: Char -> Int
toCode c = 
    if (ord c) >= (ord 'a') 
        then (ord c) - (ord 'a') + 1
        else (ord c) - (ord 'A') + 27

solve1 :: String -> Int
solve1 s =( 
        sum .
        (map (\l -> (sum . (map toCode)) l )) .
        (map (\l -> (map head . group . sort) l)) .
        (map (\l -> intersect (fst l) (snd l))) .
        (map (\l -> splitAt (div (length l) 2) l)) .
        (splitOn "\n")
    ) s 

solve2 :: String -> Int
solve2 s = ( 
    sum .
    (map (\l -> (sum . (map toCode)) l )) .
    (map (\l -> (map head . group . sort) l)) .
    (map (\l -> foldr1 intersect l)).
    (chunksOf 3) .
    (splitOn "\n")) s

main :: IO()
main = do   
    handle <- openFile "input3.txt" ReadMode
    contents <- hGetContents handle
    putStrLn $ show (solve2 contents)
    hClose handle