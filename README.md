# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
      
   I've worked with OOP before, so inheritance and classes weren't new to me. However, I got more familiar with using __dict__ to inspect object attributes. The most interesting part was learning about shallow and deep copying, which I don't remember ever using in my previous programming experience.

2. What challenges did you encounter, and how did you overcome them?
   
   My biggest challenge was understanding why modifying the original object's inventory also changed the shallow copy. After printing both copies and comparing their inventories, I understood how shallow copies share references to nested objects.

3. Compare OOP to procedural programming.
   
   Procedural programming focuses on functions and instructions, while OOP organizes code around objects containing attributes and methods. I prefer OOP for larger projects because it keeps related functionality together and makes the code easier to manage.

4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.
   
   OOP makes maintaining and reusing code easier by reducing repetition. For example, my character system could be expanded to include warriors or archers without rewriting the parent class. While creating classes adds some initial overhead, I think the organization pays off as projects grow, especially when adding features or fixing bugs.