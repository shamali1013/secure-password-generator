# Secure Password Generator (Tkinter)

A modern, customizable password generator with strength analysis, built in Python using Tkinter.  
Easily generate strong, secure passwords with control over length, number of digits, uppercase, lowercase, and special characters.  
Includes a visual strength meter and copy-to-clipboard functionality.

## Features
- Adjustable password length and character composition
- Real-time strength scoring with a color-coded progress bar
- Copy generated password to clipboard
- Show/Hide password toggle
- Clean, modern Tkinter interface with hover effects
- Responsive layout

## Screenshots
*(Add screenshots here once available)*

## Requirements
- Python **3.7+**
- Tkinter (comes pre-installed with most Python distributions)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/secure-password-generator.git
   cd secure-password-generator
```

2. Run the application:
    
    ```bash
    python password_generator.py
    ```
    

Usage
-----

1. Set the desired password length and character composition.
    
2. Click **Generate Password**.
    
3. View the strength indicator and copy the password if needed.
    

Building to EXE (Optional)
--------------------------

If you want to create a standalone executable:

```bash
pyinstaller --onefile --windowed --name SecurePasswordGenerator --icon=icon.ico password_generator.py
```

The executable will be located in the `dist/` folder.
