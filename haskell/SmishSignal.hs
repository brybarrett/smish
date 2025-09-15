module SmishSignal where

broadcast :: String -> IO ()
broadcast msg = putStrLn ("[Smish] broadcasting: " ++ msg)

probe :: String -> Float
probe signal = fromIntegral (length signal) * 0.01

main :: IO ()
main = broadcast "hello future mesh"
