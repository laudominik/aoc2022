import System.IO
import Control.Monad
import Data.List.Split
import Data.List


solve :: String -> Char
solve s = (parse . (splitOn "\n")) s
    where
    
        parse (x:xs) = 
            if "$ cd" `isPrefixOf` x
                then 'A'
            else if "$ ls" `isPrefixOf` x
                then 'B'
            else 'C'
            
        
    


main :: IO()
main = do   
    handle <- openFile "input7.txt" ReadMode
    contents <- hGetContents handle
    putStrLn $ show (solve contents)
    hClose handle