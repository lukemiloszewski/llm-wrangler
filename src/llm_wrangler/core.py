import re
from pathlib import Path
from typing import Dict, Any


class CodeSnippetOrganizer:
    START_MARKER = "<<FILE:"
    END_MARKER = "<<END>>"

    def __init__(self):
        """Initialize the organizer with the fixed template format."""
        self.pattern = (
            f"{re.escape(self.START_MARKER)}"
            r"(?P<filename>[^>]+)>>\n"
            r"(?P<content>[\s\S]*?)"
            f"\n{re.escape(self.END_MARKER)}"
        )

    def process_file(self, input_file: Path, output_dir: Path) -> Dict[str, Dict[str, Any]]:
        """
        Process the input file containing code snippets and create corresponding files.
        
        Args:
            input_file: Path to the input file containing code snippets
            output_dir: Directory where the files should be created
            
        Returns:
            Dict containing information about processed files
        """
        input_file = Path(input_file)
        output_dir = Path(output_dir)
        
        content = input_file.read_text(encoding='utf-8')
        matches = re.finditer(self.pattern, content)
        processed_files = {}

        for match in matches:
            filename = match.group('filename').strip()
            file_content = match.group('content').strip()
            
            full_path = output_dir / filename
            full_path.parent.mkdir(parents=True, exist_ok=True)
            
            full_path.write_text(file_content, encoding='utf-8')
            
            processed_files[filename] = {
                'path': str(full_path),
                'size': len(file_content)
            }

        return processed_files

    @staticmethod
    def prompt() -> str:
        return r'''
When providing code implementations, please format your response using the following structure:

```txt
<<FILE:filename.ext>>
// code content here
<<END>>
Each file should be wrapped with these exact markers. For example:
txtCopy<<FILE:main.py>>
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
<<END>>

<<FILE:utils/helper.py>>
def helper_function():
    return "Helper function called"
<<END>>

Use exactly these markers: <FILE:filename> to start and <<END>> to end each file
Include the full path if the file should be in a subdirectory (e.g., utils/helper.py)
Provide complete, working code in each file
Include all necessary imports
Maintain consistent import paths between files

Example
txtCopy<<FILE:src/calculator/__init__.py>>
from calculator.operations import Calculator

all = ["Calculator"]
<<END>>

<<FILE:src/calculator/operations.py>>
from typing import Optional

class Calculator:
    """Basic calculator with memory functionality."""

    def __init__(self) -> None:
        self.memory: Optional[float] = None

    def add(self, a: float, b: float) -> float:
        """Add two numbers and store result in memory."""
        self.memory = a + b
        return self.memory
<<END>>

<<FILE:tests/test_calculator.py>>
import pytest

from calculator import Calculator

def test_add() -> None:
    """Test basic addition and memory storage."""
    calc = Calculator()
    result = calc.add(2.0, 3.0)
    assert result == 5.0
    assert calc.memory == 5.0
<<END>>
```'''
