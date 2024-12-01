import System.IO
import Control.Monad
import Data.List.Split
import Data.List
import Data.Char (ord)

arrays :: [String]
arrays = ["BSJZVDG", 
        "PVGMSZ",
        "FQTWSBLC",
        "QVRMWGJH",
        "DMFNSLC",
        "DCGR",
        "QSDJRTGH",
        "VFP",
        "JTSRD"]
testArrays :: [String]
testArrays = ["JGWMRVQJDDG","LSNPVGMSZ","HGTRDMF","PFVH","C","DCGR","","","CLBSWTQFSQVZJSBJTSRD"]



replaceNth :: Int -> a -> [a] -> [a]
replaceNth _ _ [] = []
replaceNth n newVal (x:xs)
    | n == 0 = newVal:xs
    | otherwise = x:replaceNth (n-1) newVal xs

step :: Int -> Int -> Int -> [String] -> [String]
step quantity src dest li = (
    (replaceNth (dest - 1) ((fst part) ++ (li!!(dest-1)))) .
    (replaceNth (src - 1) (snd part))
    ) li
    where 
        part = (splitAt quantity (li!!(src - 1)))

--solve :: String -> String

solv s = parse s
    where 
    parse :: String -> [[String]]
    parse s = (
        (map (\a -> [a!!1,a!!3,a!!5])).
        (map (splitOn " ")).
        (splitOn "\n")
        ) s

solve s = 
    (foldl (\x y -> (step (read (y!!0)) (read (y!!1)) (read (y!!2)) x)) arrays (parse s))
    where 
    parse :: String -> [[String]]
    parse s = (
        (map (\a -> [a!!1,a!!3,a!!5])).
        (map (splitOn " ")).
        (splitOn "\n")
        ) s

main :: IO()
main = do   
    handle <- openFile "input5.txt" ReadMode
    contents <- hGetContents handle
    putStrLn $ show (solve contents)
    hClose handle