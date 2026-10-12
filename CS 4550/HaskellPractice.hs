module Main where

addAndPrint :: Int -> Int -> IO ()
addAndPrint x y = putStrLn (show x ++ " + " ++ show y ++ " = " ++ show (x + y))

function1 :: Int -> Int
function1 x = (x * 3) + 1

maxMin :: Ord a => a -> a -> (a, a)
maxMin x y
  | x >= y    = (x, y)
  | otherwise = (y, x)

areStringsEqual :: String -> String -> Bool
areStringsEqual str1 str2 = str1 == str2

main :: IO ()
main = do
    putStrLn "=== Problem 1: Integer Addition ==="
    addAndPrint 10 15
    addAndPrint 7 32

    putStrLn "\n=== Problem 2: function1 ==="
    putStrLn $ "Positive (5):  " ++ show (function1 5)
    putStrLn $ "Zero (0):      " ++ show (function1 0)
    putStrLn $ "Negative (-4): " ++ show (function1 (-4))

    putStrLn "\n=== Problem 3: maxMin ==="
    putStrLn $ "maxMin 8 3   = " ++ show (maxMin (8 :: Int) 3)
    putStrLn $ "maxMin 4 11  = " ++ show (maxMin (4 :: Int) 11)
    putStrLn $ "maxMin 5 5   = " ++ show (maxMin (5 :: Int) 5)

    putStrLn "\n=== Problem 4: areStringsEqual ==="
    putStrLn $ "areStringsEqual \"Haskell\" \"Haskell\" = " ++ show (areStringsEqual "Haskell" "Haskell")
    putStrLn $ "areStringsEqual \"Haskell\" \"Python\"  = " ++ show (areStringsEqual "Haskell" "Python")
    putStrLn $ "areStringsEqual \"Haskell\" \"haskell\" = " ++ show (areStringsEqual "Haskell" "haskell")