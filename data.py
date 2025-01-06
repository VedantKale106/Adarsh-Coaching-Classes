from pymongo import MongoClient
from datetime import datetime, timedelta

# Connect to MongoDB
client = MongoClient('mongodb+srv://vedant:lulli@portfolio.e8ky0.mongodb.net/')
db = client['coaching_website']

# Clear existing data
db.courses.delete_many({})
db.faculty.delete_many({})
db.testimonials.delete_many({})
db.results.delete_many({})
db.messages.delete_many({})

# Sample Courses Data
courses = [
    {
        "name": "SSC (10th) Regular Batch",
        "grade": "10th",
        "description": "Comprehensive coaching for 10th standard board exams with focus on scoring high marks",
        "features": [
            "Daily practice sessions",
            "Weekly tests",
            "Doubt solving sessions",
            "Study material provided",
            "Parent-teacher meetings"
        ],
        "syllabus": [
            "Mathematics",
            "Science",
            "English",
            "Social Studies",
            "Hindi/Marathi"
        ],
        "timing": "7:00 AM - 9:00 AM",
        "duration": "11 months",
        "batch_size": 100,
        "created_at": datetime.now()
    },
    {
        "name": "HSC Science (12th)",
        "grade": "12th",
        "description": "Foundation course for HSC Science with focus on JEE/NEET preparation",
        "features": [
            "Specialized faculty for each subject",
            "Practical sessions",
            "Concept building",
            "Regular assessments",
            "Performance tracking"
        ],
        "syllabus": [
            "Physics",
            "Chemistry",
            "Mathematics/Biology"
        ],
        "timing": "2:00 PM - 5:00 PM",
        "duration": "12 months",
        "batch_size": 75,
        "created_at": datetime.now()
    },
    {
        "name": "CET Special Batch",
        "grade": "12th",
        "description": "Intensive coaching for MHT-CET entrance examination",
        "features": [
            "Daily mock tests",
            "Previous year paper solving",
            "Speed improvement techniques",
            "Personal mentoring",
            "Performance analysis"
        ],
        "syllabus": [
            "Physics",
            "Chemistry",
            "Mathematics/Biology",
            "CET Pattern Training"
        ],
        "timing": "6:00 PM - 8:30 PM",
        "duration": "3 months",
        "batch_size": 50,
        "created_at": datetime.now()
    }
]

# Insert courses
db.courses.insert_many(courses)

# Sample Faculty Data
from datetime import datetime

faculty = [
    {
        "name": "Mule Sir",
        "qualification": "M.Sc Mathematics",
        "experience": 20,
        "subjects": ["Algebra"],
        "image_url": "/static/images/faculty/mule_sir.jpg",
        "description": "Expert in Algebra with practical teaching methods",
        "achievements": [
            "Guided multiple Olympiad winners",
            "Developed Algebra teaching modules",
            "Achieved 95% student satisfaction"
        ],
        "specialization": "Algebra",
        "created_at": datetime.now()
    },
    {
        "name": "Malve Sir",
        "qualification": "M.Sc Mathematics",
        "experience": 22,
        "subjects": ["Geometry"],
        "image_url": "/static/images/faculty/malve_sir.jpg",
        "description": "Geometry specialist with an innovative teaching approach",
        "achievements": [
            "Developed advanced geometry problem sets",
            "Author of geometry textbooks",
            "Consistent 100% pass rate"
        ],
        "specialization": "Geometry",
        "created_at": datetime.now()
    },
    {
        "name": "Manoj Sir",
        "qualification": "M.Sc Mathematics and Biology",
        "experience": 12,
        "subjects": ["Mathematics", "Biology"],
        "image_url": "/static/images/faculty/manoj_sir.jpg",
        "description": "Expert in Mathematics and Biology with interdisciplinary teaching experience",
        "achievements": [
            "Created cross-discipline learning materials",
            "Produced numerous state toppers",
            "Pioneered STEM-based projects"
        ],
        "specialization": "Interdisciplinary Mathematics and Biology",
        "created_at": datetime.now()
    },
    {
        "name": "Saurabh Sir",
        "qualification": "M.Sc Physics",
        "experience": 20,
        "subjects": ["Physics"],
        "image_url": "/static/images/faculty/default.jpg",
        "description": "Physics expert specializing in Mechanics and Thermodynamics",
        "achievements": [
            "Conducted national-level physics workshops",
            "Published research papers in reputed journals",
            "Mentored students for competitive exams"
        ],
        "specialization": "Mechanics and Thermodynamics",
        "created_at": datetime.now()
    }]
    

# Insert faculty
db.faculty.insert_many(faculty)

# Sample Results Data
results = [
    {
        "year": 2023,
        "exam_type": "SSC",
        "highlights": [
            {"name": "Rahul Patil", "percentage": 98.6},
            {"name": "Priya Shah", "percentage": 97.8},
            {"name": "Amit Kumar", "percentage": 96.9}
        ],
        "class_average": 85.5,
        "total_students": 50,
        "distinctions": 35,
        "first_class": 12,
        "pass_percentage": 100,
        "created_at": datetime.now()
    },
    {
        "year": 2023,
        "exam_type": "HSC Science",
        "highlights": [
            {"name": "Sneha Joshi", "percentage": 95.2},
            {"name": "Rohan Sharma", "percentage": 94.8},
            {"name": "Neha Patel", "percentage": 93.7}
        ],
        "class_average": 82.3,
        "total_students": 45,
        "distinctions": 30,
        "first_class": 10,
        "pass_percentage": 98,
        "created_at": datetime.now()
    }
]

# Insert results
db.results.insert_many(results)

# Sample Testimonials
testimonials = [
    {
        "student_name": "Rahul Patil",
        "course": "SSC",
        "year": 2023,
        "content": "The teaching methodology and personal attention helped me score 98.6% in SSC board exams.",
        "rating": 5,
        "photo_url": "/static/images/testimonials/student1.jpg",
        "verified": True,
        "created_at": datetime.now()
    },
    {
        "student_name": "Sneha Joshi",
        "course": "HSC Science",
        "year": 2023,
        "content": "Excellent faculty and regular tests helped me maintain consistency throughout the year.",
        "rating": 5,
        "photo_url": "/static/images/testimonials/student2.jpg",
        "verified": True,
        "created_at": datetime.now()
    }
]

# Insert testimonials
db.testimonials.insert_many(testimonials)

# Sample Messages/Inquiries
messages = [
    {
        "name": "Rajesh Kumar",
        "email": "rajesh.k@gmail.com",
        "phone": "9876543210",
        "message": "Interested in SSC batch. Please share details.",
        "timestamp": datetime.now() - timedelta(days=2),
        "status": "responded"
    },
    {
        "name": "Priya Shah",
        "email": "priya.s@gmail.com",
        "phone": "9876543211",
        "message": "Want to know about CET batch timings and fees.",
        "timestamp": datetime.now() - timedelta(days=1),
        "status": "pending"
    }
]

# Insert messages
db.messages.insert_many(messages)

print("Sample data inserted successfully!")

# Print count of inserted records
print(f"Courses: {db.courses.count_documents({})}")
print(f"Faculty: {db.faculty.count_documents({})}")
print(f"Results: {db.results.count_documents({})}")
print(f"Testimonials: {db.testimonials.count_documents({})}")
print(f"Messages: {db.messages.count_documents({})}")