//Problem name :- Cut The Sticks
//Description :- Swift built in functions makes it easier to find minimum and filter the zeroes so we can count the remaining elements in the array


import Foundation

func cutTheSticks(arr: [Int]) -> [Int] {
    var arr2 = arr
    var remaining : [Int] = []
    repeat{
        remaining.append(arr2.count)
        var mini = arr2.min()
        arr2 = arr2.map {$0 - mini!}
        arr2 = arr2.filter {$0 != 0}
    }while arr2.count > 0

    return(remaining)
}