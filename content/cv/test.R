# Definition of vectors
student_id <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
student_name <- c('John', 'Hari', 'Ali', 'Jenny', 'Lisa', 'Priya', 'Wong', 'Julius', 'Alonso', 'Noor')
student_city <- c('Atlanta', 'Mumbai', 'Dubai', 'Berlin', 'Berlin', 'Delhi', 'Beijing', 'Rome', 'Atlanta', 'London')
student_country <- c('USA', 'India', 'UAE', 'Germany', 'Germany', 'India', 'China', 'Italy', 'USA', 'UK')

# Create a data frame from the vectors
students <- data.frame(student_id, student_name, student_city, student_country)

# Definition of vectors
degree_id <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
student_id <- c(1, 2, 2, 2, 3, 4, 4, 7, 7, 7, 10, 6, 6)
degree_name <- c('B. Arts', 'B. Tech', 'MS', 'PhD', 'B. Sc.', 'B. Sc.', 'M. Sc.', 'BS', 'MS', 'PhD', 'BE', 'BE', 'ME')
degree_country <- c('USA', 'India', 'USA', 'USA', 'Germany', 'Switzerland', 'Germany', 'China', 'Australia', 'USA', 'UK', 'India', 'India')
degree_length <- c(3, 4, 2, 5, 4, 4, 3, 3, 1, 3, 4, 4, 2)

# Create a data frame from the vectors
degree <- data.frame(degree_id, student_id, degree_name, degree_country, degree_length)

require("microbenchmark")

foobar <- function(students) {
  dim(students)[1]
}

microbenchmark(foobar(students), times = 1000)
