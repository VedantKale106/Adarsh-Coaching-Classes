from bson import ObjectId
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_pymongo import PyMongo
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configuration
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# Initialize MongoDB
mongo = PyMongo(app)


# Routes
@app.route('/')
def home():
    """Home page route"""
    courses = mongo.db.courses.find()
    faculty = mongo.db.faculty.find()
    results = mongo.db.results.find()
    return render_template('index.html', 
                         courses=courses, 
                         faculty=faculty,
                         results=results)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page route"""
    if request.method == 'POST':
        # Get form data
        message = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'message': request.form.get('message'),
            'timestamp': datetime.utcnow()
        }
        
        # Validate form data
        if not all([message['name'], message['email'], message['phone'], message['message']]):
            flash('Please fill in all fields', 'error')
            return redirect(url_for('contact'))
        
        try:
            # Save message to database
            mongo.db.messages.insert_one(message)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash('An error occurred. Please try again.', 'error')
            print(f"Error: {e}")  # For debugging
            
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

# Admin routes
@app.route('/admin/messages')
def admin_messages():
    """Admin route to view messages"""
    messages = mongo.db.messages.find().sort('timestamp', -1)
    return render_template('admin/messages.html', messages=messages)

@app.route('/admin/messages/delete/<message_id>', methods=['POST'])
def delete_message(message_id):
    """Delete a specific message by its ID."""
    try:
        result = mongo.db.messages.delete_one({"_id": ObjectId(message_id)})
        if result.deleted_count == 1:
            flash("Message deleted successfully.", "success")
        else:
            flash("Message not found.", "error")
    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error")
    return redirect(url_for('admin_messages'))

@app.route('/admin/add-course', methods=['GET', 'POST'])
def add_course():
    """Admin route to add new course"""
    if request.method == 'POST':
        course = {
            'name': request.form.get('name'),
            'grade': request.form.get('grade'),
            'description': request.form.get('description'),
            'features': request.form.get('features').split(','),
            'syllabus': request.form.get('syllabus').split(',')
        }
        
        try:
            mongo.db.courses.insert_one(course)
            flash('Course added successfully!', 'success')
        except Exception as e:
            flash('An error occurred. Please try again.', 'error')
            print(f"Error: {e}")  # For debugging
            
        return redirect(url_for('add_course'))
    
    return render_template('admin/add_course.html')

@app.route('/admin/add-faculty', methods=['GET', 'POST'])
def add_faculty():
    """Admin route to add new faculty"""
    if request.method == 'POST':
        faculty = {
            'name': request.form.get('name'),
            'qualification': request.form.get('qualification'),
            'experience': int(request.form.get('experience')),
            'subjects': request.form.get('subjects').split(','),
            'image_url': request.form.get('image_url'),
            'description': request.form.get('description')
        }
        
        try:
            mongo.db.faculty.insert_one(faculty)
            flash('Faculty added successfully!', 'success')
        except Exception as e:
            flash('An error occurred. Please try again.', 'error')
            print(f"Error: {e}")  # For debugging
            
        return redirect(url_for('add_faculty'))
    
    return render_template('admin/add_faculty.html')

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    """404 Page not found error handler"""
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(e):
    """500 Internal server error handler"""
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=os.getenv('FLASK_DEBUG', True))