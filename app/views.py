"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash
from .forms import PropertyForm
from app.models import PropertyObject
from werkzeug.utils import secure_filename
import os

###
# Routing for your application.
###


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/property', methods=['GET', 'POST'])
def property():
    """Display the form for adding a new property."""
    form = PropertyForm()
    if request.method == "POST":
        if form.validate_on_submit():
            propertyTitle = form.propertyTitle.data
            propertyDescription = form.propertyDescription.data
            propertyBathrooms = form.propertyBathrooms.data
            propertyBedrooms = form.propertyBedrooms.data
            propertyType = form.propertyType.data
            propertyPhoto = form.propertyPhoto.data
            propertyPrice = form.propertyPrice.data
            propertyLocation = form.propertyLocation.data
            filename = secure_filename(propertyPhoto.filename)
            propertyPhoto.save(os.path.join(
                app.config['UPLOAD_FOLDER'], filename))
            propertyObj = PropertyObject(propertyLocation=propertyLocation, propertyPrice=propertyPrice, propertyTitle=propertyTitle, propertyDescription=propertyDescription,
                                         propertyBathrooms=propertyBathrooms, propertyBedrooms=propertyBedrooms, propertyType=propertyType, propertyPhoto=filename)
            db.session.add(propertyObj)
            db.session.commit()
            flash('Property added successfully', 'success')
            return redirect(url_for("properties"))
        flash_errors(form)
    return render_template('propertyform.html',
                           form=form, data=[{'propertyType': 'Apartment'}, {'propertyType': 'House'}])


@app.route('/properties', methods=['GET'])
def properties():
    properties = db.session.query(PropertyObject).all()
    update_filepaths(properties=properties)

    return render_template('properties.html', properties=properties)


@app.route('/property/<propertyid>')
def view_property(propertyid):
    property = db.session.query(PropertyObject).get(propertyid)
    if property:
        update_filepaths(property)
        return render_template("property_info.html", property=property)
    else:
        return render_template('404.html')
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages


def update_filepaths(properties):
    """Add complete filepath to filenames from database"""
    if type(properties) != list:
        properties = [properties]
    for property in properties:
        property.propertyPhoto = 'uploads/' + property.propertyPhoto


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
