//Problem name : Sherlock Square
//Description the main idea is to detect if the number is a sqare in the most efficient way
//Strategy : Through a keen observation one can deduce that the perfect squares are seperated on a number line by the gap of 2*i + 1 where i stands for the natural numbers starting from 1 from beginning

/*example :  1 and 4 are seperated by 2*(i) + 1 where i=1
             4 and 9 are seperated by 2*(i) + 1 where i=2
             9 and 16 are seperated by 2*(i) + 1 where i=3
             and so on

             so the idea is to count those numbers which comes between the range using a counter variable.
*/

import Foundation

func squares2(a: Int, b: Int) -> Int {
    var squares = 1
    var count = 0
    var i = 1
    while squares <= b{
    if (a...b).contains(squares){
        count += 1
    }
    squares += 2*i + 1
    i += 1
    }
    return count
}

let a = Int(readLine(strippingNewline: true)!)!
let b = Int(readLine(strippingNewline: true)!)!

print(squares2(a: a,b: b))