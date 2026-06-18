func hasDuplicate(nums []int) bool {
    database := make(map[int]bool)
    for _, num := range nums {
        if database[num] {
            return true
        } else {
            database[num] = true
        }
    }
    return false
}
