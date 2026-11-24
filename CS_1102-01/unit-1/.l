/**
 * LOOP and CONDITIONAL STATEMENT
 * READ: User inputs | Validate | Display
 * IF: USER-INPUT is out of the range
 * 		DISPLAY: "Invalid input - Marks must be between 0 and 100 (inclusive)"
 */

import java.util.Scanner;

public class Record_mark {
    public static void main(String args[])
    {
        double[] marks = new double[5];
        double total = 0, average = 0;
        char grade;

        System.out.println("Please, enter mark");
			for (int i = 0; i < 5; i++)
            {
                System.out.printf("mark_subject_%d: ", i + 1);
                // Call input() method to read keyboard inputs
                marks[i] = input();
                if (marks[i] < 0)
                    return;
            }
            // Calculate total marks
            for (int i = 0; i < marks.length; total += marks[i], i++);
            // Grade
            grade = calculateGrade(total, 5);

            System.out.printf("Average mark: %.02f [Grade: '%c']: ", average, grade);
    }
    // Check perfomance based on grade
    switch (grade)
    {
        case 'A':
            System.out.println("Excellent Performance");
            break;
        case 'B':
            System.out.println("Very good Performance");
            break;
        case 'C':
            System.out.println("Satisfactory Performance");
            break;
        default:
            System.out.println("Unsatisfactory Performance");
            break;
    }

    // Method to calculate average and get Grade
    static char calculateGrade(double totalMarks, int noSubjects)
    {
        average = totalMarks / noSubjects;

        if (average >= 90 && average <= 100)
            return ('A');
        if (average >= 80 && average < 90)
            return ('B');
        if (average >= 70 && average < 80)
            return ('C');
        return ('F');
    }

    // Method to read and verify keyboard input
    static double input()
    {
        Scanner input = new Scanner(System.in);

        // Check if input is double and save it in 'entry'
        if (input.hasNextDouble())
        {
            double entry = input.nextDouble();
            // Check if entry is in range 0 - 100
            if (entry >= 0 && entry <= 100)
                return (entry);
        }
        // Print message if not double or in range
        System.out.print("Invalid input - ");
        System.out.println("Marks must be between 0 and 100 (inclusive)");
        input.close();
        return (-1);

    }
}

/**
 * Calculator - Calculate total and average value of a data (double array)
 * total() - Method to Calculate the total value of data
 * average - Method that calculate the average value of data
 */

/*
class Calculate {
    static double total(double[] data)
    {
        double total = 0;
        for (int i = 0; i < data.length; total += data[i], i++);
        return (total);
    }

    static double average(double[] data)
    {
        double len = 0;
        for (int i = 0; i < data.length; len++, i++);
        return (total(data) / len);
    }
}
*/

