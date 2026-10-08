# Contributing to the Python Student Project

Thank you for your interest in contributing to this Python student project. This guide explains how beginners can report problems, suggest ideas, make changes, test them, and create a pull request.

## 1. How to Report an Issue

If you find a problem in the project:

1. Open the project's **Issues** section.
2. Create a new issue.
3. Give the issue a clear title.
4. Describe the problem clearly.
5. Include the steps needed to reproduce the problem.
6. Add any useful error messages.

Example:

```text
Title: Program shows an error when entering a number

Description:
The program gives an error when a number is entered.

Steps:
1. Run the program.
2. Enter a number.
3. Check the error message.
```

## 2. How to Suggest a Feature

If you have an idea for improving the project:

1. Open the project's **Issues** section.
2. Create a new issue.
3. Clearly describe your suggested feature.
4. Explain how the feature could improve the project.

Example:

```text
Title: Add a student search feature

Description:
Add a feature that allows users to search for a student by name.
```

## 3. How to Create a Branch

Before making changes, create a new branch.

Use:

```bash
git checkout -b feature-name
```

Replace `feature-name` with a short and meaningful name.

Example:

```bash
git checkout -b add-student-search
```

Work on your changes in this branch instead of directly changing the main branch.

## 4. How to Make Changes

Follow these steps:

1. Open the project.
2. Make the required changes.
3. Save your files.
4. Review your changes.
5. Make sure your changes are related to the issue or feature.

Keep changes small and easy to understand.

After making changes, check the files you changed:

```bash
git status
```

Add the changes:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Describe your changes"
```

Example:

```bash
git commit -m "Add student search feature"
```

## 5. How to Test Changes

Before submitting your changes:

1. Run the Python program.
2. Check that it works as expected.
3. Test the part of the project that you changed.
4. Check for errors.
5. Make sure existing features still work.

If the project contains Python test files, run the tests using the instructions provided by the project.

## 6. How to Create a Pull Request

After testing your changes:

1. Push your branch to the project repository.
2. Open the repository.
3. Create a **Pull Request**.
4. Select your branch as the source branch.
5. Add a clear title.
6. Describe what you changed.
7. Mention any related issue.
8. Submit the pull request for review.

Example pull request description:

```text
## Changes

- Added student search functionality.
- Updated the Python program.

## Testing

- Tested the search feature.
- Checked that the program runs correctly.
```

## 7. Basic Coding Guidelines

Follow these simple guidelines when writing Python code:

- Use clear and meaningful names for variables and functions.
- Keep the code simple and easy to understand.
- Use consistent indentation.
- Avoid unnecessary code.
- Add comments when they help explain difficult code.
- Keep functions focused on one task.
- Check your code for errors before submitting it.
- Do not change unrelated parts of the project.

Example:

```python
student_name = "Alan"

def display_student(name):
    print(name)

display_student(student_name)
```

## Conclusion

Thank you for contributing to the project. Every contribution, including small improvements and bug reports, can help make the project better.