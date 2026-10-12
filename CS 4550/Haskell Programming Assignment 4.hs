module MyLast where

myLast1 :: [a] -> a
myLast1 xs = xs !! (length xs - 1)

myLast2 :: [a] -> a
myLast2 = head . reverse

myLast3 :: [a] -> a
myLast3 []     = error "myLast3: empty list"
myLast3 [x]    = x
myLast3 (_:xs) = myLast3 xs

myLast4 :: [a] -> a
myLast4 xs
  | length xs == 0 = error "myLast4: empty list"
  | length xs == 1 = head xs
  | otherwise      = myLast4 (tail xs)