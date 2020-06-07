//Problem name : Extra Long Factorials

// Description : The main objective of the problem is to handle large numbers and compute it.

// Strategy: Since there is no builtin function in swift to handle big integers so we convert it into string at each step of solvin problem

/* We will be multiplying like its shown below
            12345   ----> top
            x  23   ----> bottom
*/
import Foundation

func multiply(_ top:String, _ bottom:String)->String{
    
    let t1 = String(top.reversed())                                 // reversing the first number
    let b1 = String(bottom.reversed())                              // reversing the second number

    /*   what we do here basically is we reverse the top and bottom and store it in t1 and b1 respectively
        following is the naming convention used for different state

            54321   ---->t1
            32  x   ---->t2
            -----
            adds[0] a.k.a ans    this will be understood further
            adds[1] a.k.a ans    this too
            -------
            su su su su
            -----------
            sum

     */

    var adds : [String] = []                                        // this is going to contain the
    var carry = "0"
    for b in b1 {                                                   // looping throught the digits of b1
        var ans = ""
        carry = "0"
        for t in t1{                                                // looping through the digits of t1
            let prod2 = Int(String(b))!*Int(String(t))!
            let prod = prod2 + Int(carry)!
            if prod >= 10{                                          // to deal with the carry forward
                ans.append(String(prod%10))
                carry = String(prod/10)
            }else{
                ans.append(String(prod))
                carry = "0"
            }
        }
        
        if carry != "0"{
            ans.append(carry)
        }
        
        adds.append(ans)
    }
    
//MARK: - padding zeroes in front so that the shifting of the numbers for addition

/* we wish to achieve this :
            
            54321
            32  x
            -----
            53073
            (0)09642   ----> here zero is symbolic to shift of number to add   (step 1)
            ------
*/
    
    var sum = ""
    for i in 1...adds.count{
        for _ in 1..<i{
            adds[i-1] = "0"+adds[i-1]
        }
    }
    
//MARK: - padding zeroes at the last

/* we wish to achieve this :
            
            54321
            32  x
            -----
            53073(0)  ----> This zero in the bracket is added so the addition of the numbers can take place digit by digit
            009642
            ------

*/
    
    for i in 0..<adds.count{
        adds[i] = adds[i].padding(toLength: adds[adds.count-1].count, withPad: "0", startingAt: 0)
    }
    

    
//MARK: - adding the shifted numbers
    carry = "0"
    var flag = 0
    for i in 0..<adds[adds.count-1].count{
        var su = 0
        flag = 0
        for j in 0..<adds.count{
            if j == 0{
                su += Int(carry)! + Int(String(Array(adds[j])[i]))!
            }else{
                su += Int(String(Array(adds[j])[i]))!
            }
            if su >= 10 {
                flag = 1
            }
        }
        if flag == 1{
            carry = String(su/10)
        }else {
            carry = "0"
        }
        su %= 10
        sum.append(String(su))
    }
    if carry != "0"{
        sum.append(carry)
    }
    return String(sum.reversed())
}

//MARK: - function that finally prints the factorial

func extraLongFactorials(n: Int) -> Void {
    var fact = "1"
    if n==1 {
        print(fact)
    }else{
        for i in 2...n{
            let temp = String(i)
            fact = multiply(fact,temp)                      // calling multiply function that is the brain of the solution
        }
        print(fact)
    }
}


extraLongFactorials(n: 25)                                  // calling the function ,you can put anything in place of 25
