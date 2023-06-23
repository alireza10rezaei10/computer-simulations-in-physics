# beautiful custom print function --------

from IPython.display import display, HTML


def boxed_print(messages: list) -> None:
    '''
        Explanation:
            in this function we use css styles to print with beautiful styles.
        
        Important Note:
            note that because of html and css styles this function just work in jupyter (web browser).
        
        Parameters:
            messages:
                a list of messages to print each message in a single line.
    '''
    
    # css styles
    styles = '''
                <style>
                    .box {
                        padding: 5px 10px;
                        border: 1px solid black;
                    }
                    
                    .error {
                        color: green;
                    }
                </style>         
    '''
    
    # html content
    content = "<div class='box'>"
    
    for message in messages:
        if "Error" in message:
            content += f"<span class='error'> {message} </span> <br>"
        else:
            content += f"{message} <br>"
            
    content += "</div>"
    
    display(HTML(styles + content))
