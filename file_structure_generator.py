#!/usr/bin/env python3
"""
University Schoolwork Repository Structure Generator
Creates the complete directory structure for organizing university coursework at WITS for Computer Science.
"""

import os
from pathlib import Path

def create_module_structure(base_path, module_name):
    """Create the standard folder structure for a module."""
    module_path = base_path / module_name
    
    folders = [
        "Lectures",
        "Labs", 
        "Assignments",
        "Past Tests/Exams",
        "Past Tests/Tests",
        "Extra"
    ]
    
    for folder in folders:
        folder_path = module_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Created: {folder_path}")

def create_year_structure(year_name, parent_modules):
    """Create the complete structure for a given year."""
    year_path = Path(year_name)
    year_path.mkdir(exist_ok=True)
    print(f"Created year directory: {year_path}")
    
    for parent_module, modules in parent_modules.items():
        parent_path = year_path / parent_module
        parent_path.mkdir(exist_ok=True)
        print(f"Created parent module: {parent_path}")
        
        for module in modules:
            create_module_structure(parent_path, module)

def main():
    """Generate the complete university coursework structure."""
    
    print("🎓 Generating University Schoolwork Repository Structure...")
    print("=" * 60)
    
    # First Year Structure
    first_year_modules = {
        "Computer Science I": [
            "Basic Computer Organisation",
            "Discrete Computational Structures", 
            "Introduction to Algorithms and Programming",
            "Introduction to Data Structures and Algorithms"
        ],
        "Mathematics I (Major)": [
            "Algebra I",
            "Calculus I"
        ],
        "Computational and Applied Mathematics I": [
            "Mathematical Methods and Modelling",
            "Mechanics",
            "Scientific Computing"
        ],
        "Other Level I Courses": [
            "Additional Course 1",
            "Additional Course 2"
        ]
    }
    
    # Second Year Structure
    second_year_modules = {
        "Computer Science II": [
            "Database Fundamentals",
            "Mobile Computing",
            "Computer Networks",
            "Analysis of Algorithms"
        ],
        "Mathematics II (Major)": [
            "Basic Analysis II",
            "Multivariable Calculus II",
            "Abstract Mathematics II",
            "Advanced Analysis II",
            "Linear Algebra II",
            "Introduction to Mathematical Statistics II"
        ],
        "Computational and Applied Mathematics II": [
            "Mathematical Methods and Modelling",
            "Mechanics", 
            "Scientific Computing"
        ]
    }
    
    # Third Year Structure
    third_year_modules = {
        "Computer Science III": [
            "Analysis of Advanced Algorithms",
            "Formal Languages and Automata",
            "Operating Systems and System Programming",
            "Software Design",
            "Software Engineering"
        ],
        "Computational Applications III": [
            "Computer Graphics and Visualisation",
            "Machine Learning",
            "Parallel Computing",
            "Software Design Project"
        ]
    }

    honours_year_modules = {
        "Honours Year": [
            # Compulsory courses
            "COMS4059A - Research Project Computer Science",
            "COMS4057A - Introduction to Research Methods",
            # Elective courses
            "COMS4030A - Adaptive Computation and Machine Learning",
            "COMS4032A - Applications of Algorithms",
            "COMS4033A - Artificial Intelligence",
            "COMS4036A - Computer Vision",
            "COMS4040A - High Performance Computing and Scientific Data Management",
            "COMS4043A - Multi-agent Systems",
            "COMS4045A - Robotics",
            "COMS4047A - Special Topics in Computer Science",
            "COMS4048A - Data Analysis and Exploration",
            "COMS4050A - Discrete Optimization",
            "COMS4054A - Natural Language Processing",
            "COMS4055A - Mathematical Foundations of Data Science",
            "COMS4060A - Introduction to Data Visualisation and Exploration",
            "COMS4061A - Reinforcement Learning",
            "APPM4058A - Digital Image Processing"
        ]
    }
    
    # Generate structures
    print("\n📁 Creating First Year structure...")
    create_year_structure("First-Year", first_year_modules)
    
    print("\n📁 Creating Second Year structure...")
    create_year_structure("Second-Year", second_year_modules)
    
    print("\n📁 Creating Third Year structure...")
    create_year_structure("Third-Year", third_year_modules)

    print("\n📁 Creating Honours Year structure...")
    create_year_structure("Honours-Year", honours_year_modules)
    
    print("\n✅ Repository structure generated successfully!")
    print("\n📝 Don't forget to:")
    print("   • Add a .gitignore file")
    print("   • Initialize git repository (git init)")
    print("   • Create your first commit")
    print("   • Add the README.md file")

if __name__ == "__main__":
    main()