// Problem Name : Append and Delete

import Foundation

func appendAndDelete(s: String, t: String, k: Int) -> String {
    var sArr = Array(s)
    var tArr = Array(t)
    var c = 0
    let minA = min(s.count, t.count)
    for i in 0..<minA{
        if sArr[i] != tArr[i]{
            break
        }
        c += 1
    }
    var stepNeeded = s.count + t.count - c*2;
    return ((stepNeeded <= k && stepNeeded%2 == k%2) || s.count + t.count < k ? "Yes" : "No")
}

appendAndDelete(s:"hackerrank",t:"hackerhappy",k:9)
