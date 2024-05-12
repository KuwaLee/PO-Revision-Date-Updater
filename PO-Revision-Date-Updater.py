import re
from datetime import datetime
import pytz

def update_po_revision_date(file_path, timezone='UTC'):
    # Read PO file.
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Get the current time stamp and convert it to the specified time zone.
    tz = pytz.timezone(timezone)
    now = datetime.now(tz)
    formatted_date = now.strftime('PO-Revision-Date: %Y-%m-%d %H:%M%z\\\\n')
    # Update "PO-Revision-Date" time stamp.
    new_content = re.sub(r'PO-Revision-Date:.+\\n', formatted_date, content)

    # Write back to file
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)


# Call the function with the provided arguments
update_po_revision_date(file_path, timezone)