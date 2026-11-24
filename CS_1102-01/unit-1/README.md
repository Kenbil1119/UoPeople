# Introduction to Java
<details align = right>
    <summary>Course Info</summary>
<p><b>Major:</b> BsCS</p>
<p><b>Course Code: </b>CS 1102-01</p>
<p><b>Instructor:</b> Amer Al-Rahayfeh</p>
<p><b>Academic Year: </b> 2026/2027</p>
</details>

## Student Marks Recording System
<details align = right>
    <summary>Program Info</summary>
<p><b>Project Name</b>: Student Marks Recording System.</p>
<p><b>Source File</b>: Record_mark.java"</p>
<p><b>Programming Language</b>: Java</p>
<p><b>Application Type</b>: Console-Based Application</p>
</details>

---
## 1. Project Overview

The Student Marks Recording System is a simple Java console-based application designed to record and process students' academic marks across five subjects. It accepts marks entered by the user, validates the inputs, calculates the student's total and average marks, and determines the corresponding letter grade based on a predefined grading scale.

The program also provides a performance summary that describes the student's academic achievement according to the calculated grade.

This project demonstrates fundamental Java programming concepts, including arrays, loops, conditional statements, methods, user input handling, data validation, and switch statements.

## 2. Program Objectives
The primary objectives of this application are to:
- Accept academic marks for five subjects.
- Validate user inputs to ensure that they are numeric values.
- Ensure that every subject mark falls within the acceptable range of 0–100 (inclusive).
- Calculate the total marks obtained across all five subjects.
- Determine the student's average mark.
- Assign an appropriate letter grade based on the calculated average.
- Display a performance description corresponding to the assigned grade.
- Present the final academic results in a formatted table.

## 3. Technologies Used

The application was developed using Java and several fundamental programming features.

| Technology / Feature | Purpose |
|:---|:---|
| Java | Primary programming language. |
| Scanner Class | Accepts user input through the console. |
| Arrays | Stores marks for five subjects. |
| For Loops | Collects and processes subject marks. |
| If-Else Statements | Validates marks and determines grades. |
| Switch Statement | Displays the corresponding performance message. |
| Methods | Separates grade calculation and performance reporting. |
| printf() | Formats the output for readability. |

## 4. System Requirements

To compile and execute this program, the following are required:

- Java Development Kit (JDK): JDK 8 or later.
- Code Editor or IDE: Visual Studio Code, IntelliJ IDEA, Eclipse, or any Java-compatible editor.
- Terminal or Command Prompt: To compile and execute the Java application.

## 5. Program Structure

The application contains three main methods:

### A. main() Method

The `main()` method serves as the entry point of the application.

Its responsibilities include:

1. Creating a double array to store five subject marks.
2. Initializing the total marks variable.
3. Creating a Scanner object to receive user input.
4. Using a for loop to collect marks for each subject.
5. Validating each input to ensure it is numeric and within the acceptable range.
6. Calculating the total marks after successful validation.
7. Calling the `calculateGrade()` method to determine the letter grade.
8. Calling the `printPerformance()` method to display the performance description.
9. Displaying the total marks, average, and letter grade.

If an invalid input is detected, the program displays an error message, closes the Scanner object, and terminates execution.

### B. calculateGrade() Method

The `calculateGrade()` method calculates the student's average mark and determines the corresponding letter grade.

It accepts two parameters:

- `totalMarks`: The sum of marks obtained across the five subjects.
- `noSubjects`: The number of subjects used to calculate the average.

The average is calculated using:

```Java
average = totalMarks / noSubjects
```

The method then evaluates the average using conditional statements and returns the appropriate letter grade.

### Grading Scale

Average Mark| Grade| Description
|:---|:---|:---|
90–100| A| Excellent Performance |
80–89.99| B| Very Good Performance | 
70–79.99| C| Satisfactory Performance |
Below 70| F| Unsatisfactory Performance |

The grading conditions also accommodate decimal averages. For example, an average of 89.5 receives a B, while an average of 90 receives an A.

### C. printPerformance() Method

The `printPerformance()` method displays a performance message based on the letter grade returned by the `calculateGrade()` method.

It uses a switch statement to evaluate the grade and display the appropriate message.

The messages are:

- __A__: Excellent Performance!
- __B__: Very Good Performance!
- __C__: Satisfactory Performance!
- __F__: Unsatisfactory Performance!

The default case handles any grade that does not match A, B, or C by displaying the unsatisfactory performance message.

## 6. Input Validation

Input validation is an important part of this application because it helps maintain the accuracy and reliability of the results.

The program implements two levels of input validation:

### 1. Data Type Validation

The `hasNextDouble()` method checks whether the user's input can be interpreted as a double value.

This prevents non-numeric inputs, such as letters and words, from being accepted as marks.

### 2. Range Validation

After confirming that the input is numeric, the program checks whether the mark falls between 0 and 100, inclusive.

The condition is:

```Java
marks[i] >= 0 && marks[i] <= 100
```

Any mark below 0 or above 100 is rejected.

If either validation fails, the program displays:

"Invalid input - Marks must be between 0 and 100 (inclusive)"

The application then terminates without calculating or displaying the student's results.

## 7. How to Run the Program

Follow these instructions to execute the application.

__Step 1__: Save the Source Code

Save the Java source code in a file named:

"__Record_mark.java__"

The filename must match the public class name, "__Record_mark__".

__Step 2__: Open the Terminal

Navigate to the directory containing the Java source file.

__Step 3__: Compile the Program

> [!TIP]
> Execute the following command:
>
> ```Java
javac Record_mark.java
```

If compilation is successful, Java generates a compiled class file named:

"__Record_mark.class__"

__Step 4__: Execute the Program

Run the application using:

```Java
java Record_mark
```

__Step 5__: Enter Subject Marks

The program will prompt you to enter marks for five subjects.

Enter a valid numeric mark between 0 and 100 for each subject.

## 8. Sample Program Execution

Example 1: Excellent Performance

Input:

Please, enter mark
_mark_subject_1: 95
mark_subject_2: 92
mark_subject_3: 88
mark_subject_4: 96
mark_subject_5: 94_

Output:

```Bash
-----[Excellent Performance!]-----
   Total  |  Average  |  Grade
 465.00   |  93.00    |    A
```

Example 2: Very Good Performance

Input:

Please, enter mark
_mark_subject_1: 85
mark_subject_2: 82
mark_subject_3: 88
mark_subject_4: 84
mark_subject_5: 86_

Output:

```Bash
-----[Very good Performance!]-----
   Total  |  Average  |  Grade
 425.00   |  85.00    |    B
```

Example 3: Satisfactory Performance

Input:

Please, enter mark
_mark_subject_1: 75
mark_subject_2: 72
mark_subject_3: 78
mark_subject_4: 74
mark_subject_5: 76_

Output:

```Bash
-----[Satisfactory Performance!]-----
   Total  |  Average  |  Grade
 375.00   |  75.00    |    C
```

Example 4: Unsatisfactory Performance

Input:

Please, enter mark
_mark_subject_1: 60
mark_subject_2: 65
mark_subject_3: 55
mark_subject_4: 68
mark_subject_5: 62_

Output:

```Bash
-----[Unsatisfactory Performance!]-----
   Total  |  Average  |  Grade
 310.00   |  62.00    |    F
```

Example 5: Invalid Input

Input:

Please, enter mark
_mark_subject_1: 85
mark_subject_2: 90
mark_subject_3: abc_

Output:

```Bash
Invalid input - Marks must be between 0 and 100 (inclusive)
```

The program terminates immediately after detecting the invalid input.

## 9. Calculation Logic

The application uses a straightforward mathematical approach to calculate academic results.

### Total Marks

The total is obtained by adding the marks stored in the array.

```Java
Total = Mark1 + Mark2 + Mark3 + Mark4 + Mark5
```

### Average Marks

The average is calculated by dividing the total marks by the number of subjects.

```Java
Average = Total Marks / 5
```

### Grade Determination

The calculated average is compared against the grading scale to determine the appropriate letter grade.

For example, if a student obtains a total of 425 marks across five subjects:

```Java
Average = 425 / 5 = 85
```

Since 85 falls within the 80–89.99 range, the student receives a B, representing Very Good Performance.

## 10. Important Program Characteristics and Limitations

The following characteristics describe the current implementation:

- The application processes exactly five subjects.
- Marks can be entered as integers or decimal numbers.
- The accepted mark range is 0–100, inclusive.
- The program terminates when an invalid input is detected.
- Results are displayed only after all five marks have passed validation.
- The program operates through a command-line interface.
- The application does not currently store student names, registration numbers, or results in an external file or database.
- The application processes one student's results per execution.

## 11. Conclusion

The Student Marks Recording System demonstrates how fundamental Java programming concepts can be combined to develop a practical academic results application.

By incorporating arrays, loops, conditional statements, methods, input validation, and formatted output, the application provides a structured approach to collecting and processing student marks.

The program also demonstrates the importance of validating user input before performing calculations, helping to ensure that the results are based on acceptable data.

Overall, this project provides a practical foundation for understanding Java programming and developing more advanced student management applications in the future.

---
Author: [Usman Saheed (kenbil)](https://www.github.com/kenbil1119)
