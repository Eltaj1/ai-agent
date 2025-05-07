# Manim Installation and Usage Guide

## Overview
Manim is a powerful animation engine for creating mathematical animations, primarily used in educational contexts. This guide will cover the installation process, major changes in version 0.19.0, and useful tips for creating animations.

## Installation

### 1. Windows Installation
To install Manim on Windows, follow these steps:
- Install Python from the [official website](https://www.python.org/downloads/).
- Open command prompt and run:
  ```bash
  pip install manim
  ```
- Verify installation by running a sample command:
  ```bash
  manim -pql example.py ExampleScene
  ```

### 2. Mac Installation
For macOS, you can use Homebrew for installation. Execute the following commands:
```bash
brew install ffmpeg
pip install manim
```
For a smoother installation experience and environment consistency, it is recommended to use the **uv** tool:
```bash
uv install manim
```

### 3. Linux Installation
On Linux, Manim can be installed readily using:
```bash
sudo apt install ffmpeg
pip install manim
```

## Major Changes in Manim v0.19.0

### Enhanced Installation Process
- The external `ffmpeg` dependency has been replaced with the `pyav` library. This simplifies the installation as users now only need to run `pip install manim` without worrying about `ffmpeg`.

### New Features
- **HSV Color Class**: Manim now supports a new HSV color class, enabling more flexibility in color management.
- **Support for Python 3.13**: The latest version is compatible with Python versions ranging from 3.9 to 3.13.

### Breaking Changes
- Code Class Update: The `Code.styles_list` attribute has been replaced with a method `Code.get_styles_list()`.
- The `SurroundingRectangle` class now accepts multiple Mobjects.

### Performance Enhancements
- Significant improvements in rendering speeds and error messages have been optimized, making the user experience smoother.

## Creating Animations

### Basic Animation
Here's a simple example of creating an animation using Manim:
```python
from manim import *

class ExampleScene(Scene):
    def construct(self):
        square = Square()           # Create a square
        self.play(Create(square))  # Show the square being created
        self.play(square.animate.rotate(PI / 4))  # Rotate the square
        self.play(FadeOut(square))  # Fade out the square
```
To render this scene, save it in a file named `example.py` and run:
```bash
manim -pql example.py ExampleScene
```

### Advanced Animation Tips
- Utilize `AnimationGroups` for executing multiple animations simultaneously:
```python
self.play(AnimationGroup(
    Create(circle),
    Create(square),
    run_time=2
))
```

## Troubleshooting 

### Common Issues
- If installation fails, ensure that your Python version matches the requirements.
- Check for any conflicting installations of FFmpeg if using older versions of Manim.

### Community Support
For additional help, consider visiting the [Manim Community](https://docs.manim.community) or relevant forums for up-to-date discussions and solutions.

## Conclusion
Whether you're animating mathematical concepts or creating stunning educational content, this guide will assist you in maximizing your experience with Manim. Happy animating!