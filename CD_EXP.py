'''
---SIMPLE CALCULATOR---
#include <stdio.h>
int main() {
    char operator;
    double num1, num2, result;

    printf("Enter an operator (+, -, *, /): ");
    scanf("%c", &operator);

    printf("Enter two numbers: ");
    scanf("%lf %lf", &num1, &num2);

    switch(operator) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            if(num2 != 0) {
                result = num1 / num2;
            } else {
                printf("Error: Division by zero\n");
                return 1; // Exit the program with an error code
            }
            break;
        default:
            printf("Error: Invalid operator\n");
            return 1; // Exit the program with an error code
    }

    printf("Result: %.2lf\n", result);

    return 0;
}

'''



'''
---FLEX PROGRAMS---
---POSITIVE OR NEGATIVE NUMBER---
%{
#include <stdio.h>
%}

DIGIT       [0-9]
NUMBER      {DIGIT}+(\.{DIGIT}+)?
%%
{NUMBER}    { 
                double num = atof(yytext); // Convert matched string to double
                if(num > 0)
                    printf("%.2lf is positive\n", num);
                else if(num < 0)
                    printf("%.2lf is negative\n", num);
                else
                    printf("Number is zero\n");
            }
%%
int main() {
    yylex();
    return 0;
}



---ODD OR EVEN---
%{
#include <stdio.h>
%}

DIGIT       [0-9]
NUMBER      {DIGIT}+(\.{DIGIT}+)?
%%
{NUMBER}    { 
                int num = atoi(yytext); // Convert matched string to integer
                if(num % 2 == 0)
                    printf("%d is even\n", num);
                else
                    printf("%d is odd\n", num);
            }
%%
int main() {
    yylex();
    return 0;
}



---PRIME OR NOT---
%{
#include <stdio.h>
#include <math.h>
%}

DIGIT       [0-9]
NUMBER      {DIGIT}+(\.{DIGIT}+)?
%%
{NUMBER}    { 
                int num = atoi(yytext); // Convert matched string to integer
                int is_prime = 1; // Assume the number is prime initially

                if (num <= 1) {
                    is_prime = 0; // Numbers less than or equal to 1 are not prime
                } else {
                    int limit = sqrt(num);
                    for (int i = 2; i <= limit; ++i) {
                        if (num % i == 0) {
                            is_prime = 0; // If num is divisible by any number, it's not prime
                            break;
                        }
                    }
                }

                if (is_prime)
                    printf("%d is prime\n", num);
                else
                    printf("%d is not prime\n", num);
            }
%%
int main() {
    yylex();
    return 0;
}



---COUNT NUMBER OF WORDS---
%{
#include <stdio.h>
%}

ALPHA       [a-zA-Z]
%%
{ALPHA}+    { 
                // Increment the word count whenever a word is encountered
                ++word_count;
                ECHO; // Echo the matched word
            }

[ \t\n]     ; // Ignore whitespace characters

.           ; // Ignore any other characters

%%
int word_count = 0;

int main() {
    yylex();
    printf("Number of words: %d\n", word_count);
    return 0;
}
'''


'''
---EVEN OR ODD---
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        
        if (number % 2 == 0) {
            System.out.println(number + " is even.");
        } else {
            System.out.println(number + " is odd.");
        }
        
        scanner.close();
    }
}


---POSITIVE OR NEGATIVE NUMBER---
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a number: ");
        double number = scanner.nextDouble();
        
        if (number > 0) {
            System.out.println(number + " is positive.");
        } else if (number < 0) {
            System.out.println(number + " is negative.");
        } else {
            System.out.println("The number is zero.");
        }
        
        scanner.close();
    }
}


---ADDITION/SUBTRACTION/MULTIPLICATION/DIVISION---
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter the first number: ");
        double num1 = scanner.nextDouble();
        
        System.out.print("Enter the second number: ");
        double num2 = scanner.nextDouble();
        
        System.out.print("Enter the operator (+, -, *, /): ");
        char operator = scanner.next().charAt(0);
        
        double result = 0;
        switch (operator) {
            case '+':
                result = num1 + num2;
                break;
            case '-':
                result = num1 - num2;
                break;
            case '*':
                result = num1 * num2;
                break;
            case '/':
                if (num2 != 0) {
                    result = num1 / num2;
                } else {
                    System.out.println("Error: Division by zero");
                    return;
                }
                break;
            default:
                System.out.println("Error: Invalid operator");
                return;
        }
        
        System.out.println("Result: " + result);
        
        scanner.close();
    }
}


---PRIME OR NOT---
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        
        boolean isPrime = true;
        
        if (number <= 1) {
            isPrime = false; // Numbers less than or equal to 1 are not prime
        } else {
            int limit = (int) Math.sqrt(number);
            for (int i = 2; i <= limit; ++i) {
                if (number % i == 0) {
                    isPrime = false; // If num is divisible by any number, it's not prime
                    break;
                }
            }
        }
        
        if (isPrime) {
            System.out.println(number + " is prime.");
        } else {
            System.out.println(number + " is not prime.");
        }
        
        scanner.close();
    }
}


---REVERSE A STRING---
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a string: ");
        String input = scanner.nextLine();
        
        String reversed = reverseString(input);
        
        System.out.println("Reversed string: " + reversed);
        
        scanner.close();
    }
    
    public static String reverseString(String str) {
        // Create a StringBuilder object from the input string
        StringBuilder stringBuilder = new StringBuilder(str);
        
        // Use the reverse() method of StringBuilder to reverse the string
        stringBuilder.reverse();
        
        // Convert the reversed StringBuilder back to a String and return
        return stringBuilder.toString();
    }
}
'''


'''
---FIRST AND FOLLOW---
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_RULES 10
#define MAX_SYMBOLS 10

// Data structure to represent a production rule
struct ProductionRule {
    char nonTerminal;
    char rhs[MAX_SYMBOLS];
};

// Data structure to represent a set of symbols
struct SymbolSet {
    char symbols[MAX_SYMBOLS];
    int count;
};

// Function prototypes
void computeFirstSets(struct ProductionRule rules[], int numRules, struct SymbolSet first[]);
void computeFollowSets(struct ProductionRule rules[], int numRules, struct SymbolSet first[], struct SymbolSet follow[]);
void printSet(char symbol, struct SymbolSet set);

int main() {
    struct ProductionRule rules[MAX_RULES];
    int numRules;

    printf("Enter the number of rules: ");
    scanf("%d", &numRules);

    printf("Enter the grammar rules in the format 'nonTerminal -> RHS':\n");
    for (int i = 0; i < numRules; ++i) {
        printf("Rule %d: ", i + 1);
        scanf(" %c -> %s", &rules[i].nonTerminal, rules[i].rhs);
    }

    struct SymbolSet first[MAX_SYMBOLS];
    struct SymbolSet follow[MAX_SYMBOLS];

    computeFirstSets(rules, numRules, first);
    computeFollowSets(rules, numRules, first, follow);

    printf("\nFirst sets:\n");
    for (int i = 0; i < MAX_SYMBOLS; ++i) {
        if (first[i].count > 0) {
            printSet('A' + i, first[i]);
        }
    }

    printf("\nFollow sets:\n");
    for (int i = 0; i < MAX_SYMBOLS; ++i) {
        if (follow[i].count > 0) {
            printSet('A' + i, follow[i]);
        }
    }

    return 0;
}

void computeFirstSets(struct ProductionRule rules[], int numRules, struct SymbolSet first[]) {
    // Initialize First sets
    for (int i = 0; i < MAX_SYMBOLS; ++i) {
        first[i].count = 0;
    }

    // Iterate until no new symbols are added to any First set
    int changed;
    do {
        changed = 0;
        for (int i = 0; i < numRules; ++i) {
            char nonTerminal = rules[i].nonTerminal;
            char *rhs = rules[i].rhs;
            int rhsLen = strlen(rhs);
            int idx = nonTerminal - 'A';

            for (int j = 0; j < rhsLen; ++j) {
                char symbol = rhs[j];
                if (isupper(symbol)) { // Non-terminal
                    int symIdx = symbol - 'A';
                    for (int k = 0; k < first[symIdx].count; ++k) {
                        if (!strchr(first[idx].symbols, first[symIdx].symbols[k])) {
                            first[idx].symbols[first[idx].count++] = first[symIdx].symbols[k];
                            changed = 1;
                        }
                    }
                } else { // Terminal
                    if (!strchr(first[idx].symbols, symbol)) {
                        first[idx].symbols[first[idx].count++] = symbol;
                        changed = 1;
                    }
                    break;
                }
            }
        }
    } while (changed);
}

void computeFollowSets(struct ProductionRule rules[], int numRules, struct SymbolSet first[], struct SymbolSet follow[]) {
    // Initialize Follow sets
    for (int i = 0; i < MAX_SYMBOLS; ++i) {
        follow[i].count = 0;
    }

    // Add $ (end of input) to the follow set of the start symbol
    follow[0].symbols[follow[0].count++] = '$';

    // Iterate until no new symbols are added to any Follow set
    int changed;
    do {
        changed = 0;
        for (int i = 0; i < numRules; ++i) {
            char nonTerminal = rules[i].nonTerminal;
            char *rhs = rules[i].rhs;
            int rhsLen = strlen(rhs);

            for (int j = 0; j < rhsLen; ++j) {
                char symbol = rhs[j];
                if (isupper(symbol)) { // Non-terminal
                    int idx = symbol - 'A';
                    int nextIdx = j + 1;

                    while (nextIdx < rhsLen && isupper(rhs[nextIdx])) {
                        int nextSymIdx = rhs[nextIdx] - 'A';
                        for (int k = 0; k < first[nextSymIdx].count; ++k) {
                            if (!strchr(follow[idx].symbols, first[nextSymIdx].symbols[k])) {
                                follow[idx].symbols[follow[idx].count++] = first[nextSymIdx].symbols[k];
                                changed = 1;
                            }
                        }
                        if (!strchr(first[nextSymIdx].symbols, 'e')) {
                            break;
                        }
                        ++nextIdx;
                    }

                    if (nextIdx >= rhsLen) { // A -> ...B
                        for (int k = 0; k < follow[nonTerminal - 'A'].count; ++k) {
                            if (!strchr(follow[idx].symbols, follow[nonTerminal - 'A'].symbols[k])) {
                                follow[idx].symbols[follow[idx].count++] = follow[nonTerminal - 'A'].symbols[k];
                                changed = 1;
                            }
                        }
                    }
                }
            }
        }
    } while (changed);
}

void printSet(char symbol, struct SymbolSet set) {
    printf("Follow(%c): { ", symbol);
    for (int i = 0; i < set.count; ++i) {
        printf("%c ", set.symbols[i]);
    }
    printf("}\n");
}

-------------------------------------------------------------
Enter the number of rules: 3
Enter the grammar rules in the format 'nonTerminal -> RHS':
Rule 1: S -> AB
Rule 2: A -> aB
Rule 3: B -> b
'''


'''
---INFIX TO POSTFIX---
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_SIZE 100

// Structure to represent a stack
struct Stack {
    int top;
    char items[MAX_SIZE];
};

// Function prototypes
void push(struct Stack *stack, char item);
char pop(struct Stack *stack);
int precedence(char op);
void infixToPostfix(char infix[], char postfix[]);

int main() {
    char infix[MAX_SIZE], postfix[MAX_SIZE];

    printf("Enter the infix expression: ");
    scanf("%s", infix);

    infixToPostfix(infix, postfix);

    printf("Postfix expression: %s\n", postfix);

    return 0;
}

// Function to push an item onto the stack
void push(struct Stack *stack, char item) {
    if (stack->top == MAX_SIZE - 1) {
        printf("Stack overflow\n");
        exit(1);
    }
    stack->items[++stack->top] = item;
}

// Function to pop an item from the stack
char pop(struct Stack *stack) {
    if (stack->top == -1) {
        printf("Stack underflow\n");
        exit(1);
    }
    return stack->items[stack->top--];
}

// Function to return the precedence of an operator
int precedence(char op) {
    if (op == '+' || op == '-') {
        return 1;
    } else if (op == '*' || op == '/') {
        return 2;
    }
    return 0;
}

// Function to convert infix expression to postfix expression
void infixToPostfix(char infix[], char postfix[]) {
    struct Stack stack;
    stack.top = -1;
    int i = 0, j = 0;

    while (infix[i] != '\0') {
        if (isdigit(infix[i])) {
            postfix[j++] = infix[i++];
        } else if (infix[i] == '(') {
            push(&stack, infix[i++]);
        } else if (infix[i] == ')') {
            while (stack.top != -1 && stack.items[stack.top] != '(') {
                postfix[j++] = pop(&stack);
            }
            if (stack.top == -1) {
                printf("Invalid infix expression\n");
                exit(1);
            }
            pop(&stack); // Pop '('
            i++;
        } else {
            while (stack.top != -1 && precedence(infix[i]) <= precedence(stack.items[stack.top])) {
                postfix[j++] = pop(&stack);
            }
            push(&stack, infix[i++]);
        }
    }

    while (stack.top != -1) {
        if (stack.items[stack.top] == '(') {
            printf("Invalid infix expression\n");
            exit(1);
        }
        postfix[j++] = pop(&stack);
    }

    postfix[j] = '\0';
}
'''