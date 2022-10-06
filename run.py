import os
from notes import note

if __name__ == "__main__":
    if __name__ == "__main__":
    aws_key_id = "AKIAIOSFODNN7EXAMPLE"
    aws_key_secret = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    
    port = int(os.environ.get("PORT", 5000))
    note.run(host='0.0.0.0', port=port, debug=True)
