import System.IO
import Control.Monad
import Data.List.Split
import Data.List

import Data.Char (ord)


solve :: String -> Int
solve s = (findInt s) + 14
    where
        zipped :: String -> [String]
        zipped s = zipN 14 s
        unique :: String -> Bool
        unique s = length s == length ( (group . sort) s)
        findInt :: String -> Int
        findInt s = case (findIndex (unique) (zipped s)) of
            Just n -> n
            Nothing -> -1     
        zipN n xs = zipWith const (take n <$> tails xs) (drop (n-1) xs)



main :: IO()
main = do   
    handle <- openFile "input6.txt" ReadMode
    contents <- hGetContents handle
    putStrLn $ show (solve contents)
    hClose handle