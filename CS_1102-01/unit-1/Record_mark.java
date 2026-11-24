import java.util.Scanner;

/**
 * Records student marks for five subjects, calculates the total and average,
 * and displays the corresponding letter grade and performance summary.
 */
public class Record_mark {

    /**
     * {@code main} - Entry point of the application.
     * Prompts the user to enter marks for five subjects.
     * validates the input, computes the total,
     * average, grade, and prints a formatted summary table.
     *
     * <p>Program terminates if any inputs mark is invalid (returns {@code -1}).
     *
     * @param args - command-line arguments (not used)
     */
    public static void main(String args[])
    {
        double[] marks = new double[5];
        double total = 0;
        int arrayLength = marks.length;
        char grade;
        Scanner input = new Scanner(System.in);

        System.out.println("Please, enter mark");
			for (int i = 0; i < arrayLength; i++)
            {
                System.out.printf("mark_subject_%d: ", i + 1);
                    // Read and Check if input is double and save it in 'mark[i]'
                    if (input.hasNextDouble())
                    {
                        marks[i] = input.nextDouble();
                        // Check if marks[i] is in range 0 - 100
                        if (marks[i] >= 0 && marks[i] <= 100)
                            continue;
                    }
                    // Print message if not double or in range
                    System.out.print("Invalid input - ");
                    System.out.println("Marks must be between 0 and 100 (inclusive)");
                    input.close();
                        return;
            }
            input.close();
            // Calculate total marks
            for (int i = 0; i < arrayLength; total += marks[i], i++);
            // Call calculateGrade() method to compute and return grade
            grade = calculateGrade(total, arrayLength);

            printPerformance(grade);
            System.out.printf("   Total  |  Average  |  Grade\n %6.02f   | %6.02f    | %4c\n", total, total/arrayLength, grade);
    }

    /**
     * Prints  a performance message to the console
     *          based on the grade letter.
     *
     * @param grade: the letter grade ({@code 'A'}, {@code 'B'}, {@code 'C'}, or {@code 'F'})
     */
    static void printPerformance(char grade)
    {
        switch (grade) {
            case 'A':
                System.out.println("\n-----[Excellent Performance!]-----");
                break;
            case 'B':
                System.out.println("\n-----[Very good Performance!]-----");
                break;
            case 'C':
                System.out.println("\n-----[Satisfactory Performance!]-----");
                break;
            default:
                System.out.println("\n-----[Unsatisfactory Performance!]-----");
        }
    }

    /**
     * Computes the average mark, updates {@link #average}, and determines the
     * corresponding letter grade.
     *
     * <p>Grading scale:
     * <ul>
     *   <li>90 to 100: {@code 'A'}</li>
     *   <li>80 to 89.99: {@code 'B'}</li>
     *   <li>70 to 79.99: {@code 'C'}</li>
     *   <li>Below 70: {@code 'F'}</li>
     * </ul>
     *
     * @param totalMarks - the sum of marks obtained across all subjects
     * @param noSubjects - the number of subjects
     * @return - the calculated letter grade ({@code 'A'}, {@code 'B'}, {@code 'C'}, or {@code 'F'})
     */
    static char calculateGrade(double totalMarks, int noSubjects)
    {
        double average = totalMarks/noSubjects;

        if (average >= 90 && average <= 100)
            return ('A');
        if (average >= 80 && average < 90)
            return ('B');
        if (average >= 70 && average < 80)
            return ('C');
        return ('F');
    }
}
