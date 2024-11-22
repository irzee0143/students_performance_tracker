class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
    
    def calculate_average(self):
        return sum(self.scores) / len(self.scores)
    
    def is_passing(self, passing_score=40):
        return all(score >= passing_score for score in self.scores)

class PerformanceTracker:
    def __init__(self):
        self.students = {}
    
    def add_student(self, name, scores):
        self.students[name] = Student(name, scores)
    
    def calculate_class_average(self):
        if not self.students:
            return 0
        total_scores = [student.calculate_average() for student in self.students.values()]
        return sum(total_scores) / len(total_scores)
    
    def display_student_performance(self):
        print("\nStudent Performance Summary:")
        for name, student in self.students.items():
            avg = student.calculate_average()
            status = "Passing" if student.is_passing() else "Needs Improvement"
            print(f"{name}: Average Score = {avg:.2f}, Status = {status}")
        print(f"\nClass Average Score: {self.calculate_class_average():.2f}")

def main():
    tracker = PerformanceTracker()
    
    while True:
        try:
            name = input("Enter the student's name (or type 'done' to finish): ").strip()
            if name.lower() == 'done':
                break
            scores = []
            for subject in ["Math", "Science", "English"]:
                score = int(input(f"Enter {name}'s score in {subject}: "))
                if score < 0 or score > 100:
                    raise ValueError("Scores must be between 0 and 100.")
                scores.append(score)
            tracker.add_student(name, scores)
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    
    tracker.display_student_performance()

if __name__ == "__main__":
    main()
