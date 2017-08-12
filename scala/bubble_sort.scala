def bubble_sort(input: Array[Int]): Array[Int] = {
    val limit = input.size - 1
    for (a <- 1 to limit) {
      for (b <- limit to a by -1) {
        if (input(b) < input(b - 1)) {
          val x = input(b)
          input(b) = input(b - 1)
          input(b - 1) = x
        }
      }
    }
    input
}