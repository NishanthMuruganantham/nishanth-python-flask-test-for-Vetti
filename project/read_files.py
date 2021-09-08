import markdown



#* to read normal text files
def read_text_file(file_name):
    
    """
    [read_text_file]
        - Here we are reading the normal text file [file without MARKDOWN texts] and extracting the file content 
            for each lines in the file using a python dictionary
    Parameters:
        - file_name : the file path
    Returns:
        [type]: [dictionary]
        file_data : this dictionary contains the line numbers as KEY and the respective line content as VALUE
    """
    
    file_data = {}
    
    with open(file_name) as fp:
        lines = fp.readlines()
        for line in lines:
            lineno = line.strip().split(':')[0].strip()
            #here we are checking whether a particluar line in the file contains a valid data [i.e line number and content]
            try:
                content = line.strip().split(':')[1].strip()
                file_data[lineno] = content
            except IndexError:
                pass
    
    return file_data



#* to read text file containing MARKDOWNS
def read_markdown_text_file(file_name):
    
    """
    [read_markdown_text_file]
        - Here we are reading the MARKDOWN text file and extracting the file content as MRKDOWN strings
    Parameters:
        - file_name : the file path
    Returns:
        [type]: [string]
        htmlmarkdown : it contains the markdown data contained in the file
    """
    
    with open (file_name, 'r', encoding='utf-16') as fp:
        htmlmarkdown = markdown.markdown(fp.read())
        return htmlmarkdown