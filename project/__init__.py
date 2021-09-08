from flask import Flask, render_template, request, abort
import os
from .read_files import read_text_file, read_markdown_text_file



#* initialising Flask app
app = Flask(__name__)


#* generating app secret Key
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


#* FIlepaths
basedir = os.path.abspath(os.path.dirname(__file__))

filepaths = {
    'file1': os.path.join(basedir,'source','file1.txt'),
    'file2': os.path.join(basedir,'source','file2.txt'),
    'file3': os.path.join(basedir,'source','file3.txt'),
    'file4': os.path.join(basedir,'source','file4.txt'),
}



#* THE ROUTE FUNCTION:

@app.route('/',defaults={'filename':'file1'})
@app.route("/<filename>")
def index(filename):
    
    """[index]
        - This function generates the views for the routes
        - It provides the views for Homepage and all other pages
        - It generates the views based on the file for which the content is asked for
        - By default, it provides the FILE-1 content as Homepage view.
    Parameters:
        filename - The name of the file for which the content is requested. By default it takes File1 if no filename is specified
        - based on the input file name, it will fetch the filepath from the filepaths dictionary
    Returns:
        generates the Flask view
    """
    
    #if file is file4.txt which contains MARKDOWN texts
    if filename == 'file4':
        note_file_content = read_markdown_text_file(filepaths[filename])
        return render_template(
            'index.html', note_file_content = note_file_content, table = False, page_title = filename
        )
    
    #for all other normal files which don't have MARKDOWN texts
    try:
        note_file_content = read_text_file(filepaths[filename])
        note_file_content_end_line = len(note_file_content)-1
        total_file_lines = len(note_file_content)
        
        start_line = request.args.get('start-line')
        end_line = request.args.get('end-line')
        
        #* if both start and end lines are specified
        if start_line and end_line:
            note_file_content = dict(list(note_file_content.items())[int(start_line):int(end_line)+1])
        
        #* if only startline is specified
        elif start_line and not end_line:
            note_file_content = dict(list(note_file_content.items())[int(start_line):])
            end_line = len(note_file_content)-1
        
        #* if only startline is specified
        elif not start_line and end_line:
            note_file_content = dict(list(note_file_content.items())[:int(end_line)+1])
            start_line = 0
        
        return render_template(
            'index.html',
            note_file_content = note_file_content,  # dictionary which contains notes contents
            table = True,                           # to check whether table to display or markdown DIV to display
            total_lines = total_file_lines,         # total lines present in the file
            note_file_content_end_line = note_file_content_end_line,    # end line of note content
            page_title = filename,                  # filename requested
            displaying_start_line = start_line,     # start line of displayed content
            displaying_end_line = end_line,         #end line of displayed content
        )
    
    except KeyError:
        # it will display 404 ERROR Page if any other file (other than the provided 4 files) is requested
        abort(404)



# 404 Error View
@app.errorhandler(404)
def page_not_found(e):
    """[summary]
        - 404 Error View
    Returns:
        generates the Flask view
    """
    return render_template("404.html", page_title = "404 Error")